import json
import os
import re
import urllib.request

# Define the directory path where JSON files are located
directory_path = r'' # Directory path for the folder installed in my repo

# Define the base filename for the reports
base_filename = 'reports_piiremoved'

# Define the starting and ending months
start_month = 'jan'
end_month = 'dec'

# Searching labeling year for each json files in order of dates of the report
start_year = 2019
end_year = 2024

criteria = {
    'os': '',  # Write your Linux OS name here (case-sensitive)
    'cpu': '',  # Write your CPU brand name here (case-sensitive)
    'gpu': ''  # Write your GPU brand name here (case-sensitive)
}

# Define a list of month names formatted in the json files
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# Fetch app IDs from the link provided(specifically
webUrl = urllib.request.urlopen('')
#provide your steam profile wishlist link in this format https://store.steampowered.com/wishlist/profiles/XXXXXXXXXXXXXXXXX#sort=order
html_content = webUrl.read().decode('utf-8')
pattern = re.compile(r'var g_rgWishlistData = (.*?);', re.DOTALL)

if match := pattern.search(html_content):
    javascript_data = match.group(1)
    wishlist_data = json.loads(javascript_data)

    app_ids_from_link = []
    for item in wishlist_data:
        app_id = str(item.get("appid", ''))
        app_title = item.get("app", {}).get("title", '')  # Try to get title in json files that matches the fetched appid
        if app_id:
            app_ids_from_link.append(app_id)
else:
    print("JavaScript object not found in HTML content.")

# Set to keep track of matched app IDs and their filtered system info
matched_app_info = {}
matched_app_notes = {}  # Initialize matched_app_notes here

for year in range(start_year, end_year + 1):
    for month in months:
        # Construct the filename
        filename = f"{base_filename}({month} {year}).json"
        file_path = os.path.join(directory_path, filename)

        # Check if the file exists
        if os.path.exists(file_path):
            try:
                # Open the JSON file and load its content
                with open(file_path, 'rb') as file:
                    report_data = json.load(file)

                    # Process the report data
                    print(f"Processing report data for {month} {year}:")
                    for report in report_data:
                        app_info = report.get('app', {})
                        app_title = app_info.get('title', '')

                        # Check if the app ID matches the fetched app ID
                        app_id = app_info.get('steam', {}).get('appId', '')

                        if str(app_id) in app_ids_from_link:
                            if app_id not in matched_app_info:
                                matched_app_info[app_id] = {'title': app_title}
                            system_info = report.get('systemInfo', {})
                            os_info = system_info.get('os', '')  # Assign the OS information to os_info
                            cpu_info = system_info.get('cpu', '')
                            gpu_info = system_info.get('gpu', '')
                            if re.search(criteria['os'], os_info):  # Use os_info for regular expression search
                                # Check if systemInfo matches the criteria
                                if cpu_info.startswith(criteria['cpu']) and gpu_info.startswith(criteria['gpu']):
                                    if app_id not in matched_app_notes:
                                        matched_app_notes[app_id] = {'title': app_title, 'proton_version': '','notes': []}

                                    # Extract proton version
                                    proton_version = report.get('protonVersion', {}).get('protonVersion', 'Not Found')

                                    # Check if the notes section is a duplicate
                                    notes_section = report.get('responses', {}).get('notes', {})
                                    if notes_section not in matched_app_notes[app_id]['notes']:
                                        matched_app_notes[app_id]['proton_version'] = proton_version
                                        matched_app_notes[app_id]['notes'].append(notes_section)

                                    # Check for launchOptions in the responses section
                                    launch_options = report.get('responses', {}).get('launchOptions', '')
                                    if launch_options:
                                        matched_app_notes[app_id]['launch_options'] = launch_options
                                    # Check for concludingNotes in the responses section(You can add more to specify what you want to see in the code structure below this)
                                    concluding_notes = report.get('responses', {}).get('concludingNotes', '')
                                    if concluding_notes:
                                        matched_app_notes[app_id]['concluding_notes'] = concluding_notes

            except json.JSONDecodeError:
                print(f"Error: Unable to decode JSON data in file {file_path}")
        else:
            print(f"File {filename} does not exist.")

# Print app ID, title, and filtered system info for each matched app ID
count = 0
for app_id in app_ids_from_link:
    count += 1
    if app_id in matched_app_info:
        app_info = matched_app_info[app_id]
        print(f"{count}. App ID: {app_id}, Title: {app_info['title']}")

# Find the selected app ID based on the selected number
selected_number = int(input("Enter the number corresponding to the title you want to select: "))

# Find the selected app ID based on the selected number
if 1 <= selected_number <= len(app_ids_from_link):
    selected_app_id = app_ids_from_link[selected_number - 1]

    # Display the information related to the selected app ID
    if selected_app_id in matched_app_info:
        app_info = matched_app_info[selected_app_id]
        print(f"App ID: {selected_app_id}, Title: {app_info['title']}")
        # Iterate through matched_app_notes and print relevant information for the selected title
        for app_id, app_data in matched_app_notes.items():
            if app_data['title'].lower() == app_info['title'].lower():  # Case-insensitive comparison
                proton_version = app_data['proton_version']
                if proton_version == '':
                    proton_version_str = 'Default'
                    variant_str = ''
                else:
                    proton_version_str = f'{proton_version}'
                    variant_str = app_data.get('variant', '')

                print("Notes:")
                for note in app_data['notes']:
                    # Check if the note contains 'protonVersion'
                    if 'protonVersion' in note:
                        note_proton_version = note['protonVersion']
                        proton_note_str = f"(Proton: {note_proton_version})"
                    else:
                        proton_note_str = f"(Proton: {proton_version_str})"
                    if variant_str:
                        proton_note_str += f" ({variant_str})"

                    note_str = json.dumps(note, indent=2)
                    note_str = note_str[:-1] + f' {proton_note_str}"'
                    print(f"- {note_str}")

                    # Search for specific sections in the notes
                    if 'customizationsUsed' in note or 'audioFaults' in note or 'inputFaults' in note or 'extra' in note:
                        print("Interactions found in the notes section:")
                        if 'customizationsUsed' in note:
                            print("\n\t- Customizations Used:")
                            print(f"    {note['customizationsUsed']}")
                        if 'audioFaults' in note:
                            print("- Audio Faults:")
                            print(f"    {note['audioFaults']}")
                        if 'inputFaults' in note:
                            print("\n\t- Input Faults:")
                            print(f"    {note['inputFaults']}")
                        if 'extra' in note:
                            print("\n\t- Extra:")
                            print(f"    {note['extra']}")
                        if 'performanceFaults' in note:
                            print("\n\t- Performance Faults:")
                            print(f"    {note['performanceFaults']}")
                    elif 'verdict' not in note:
                        if 'windowingFaults' in note or 'launchFlagsUsed' in note:
                            print("No verdict found, checking for windowingFaults and launchFlagsUsed")
                            if 'windowingFaults' in note:
                                print("\n\t- Windowing Faults:")
                                print(f"    {note['windowingFaults']}")
                            if 'launchFlagsUsed' in note:
                                print("\n\t- Launch Flags Used:")
                                print(f"    {note['launchFlagsUsed']}")
                # Print launchOptions if available
                if 'launch_options' in app_data:
                    print("Launch Options:")
                    print(app_data['launch_options'])
                if 'concluding_notes' in app_data:
                    print("Concluding Notes:")
                    print(app_data['concluding_notes'])
                print()
else:
    print("Invalid number. Please select a number within the range.")














































