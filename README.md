# proton-data-base-report
This is my first my project analysing data from the [protondb-data](https://github.com/bdefore/protondb-data)github repo.The purpose of this project is to help Linux users who have a lot of games in the wishlist to be able to read user reviews for the game output by the program instead of having to go to the [protondb](https://www.protondb.com/) website to read each user review of the game manually(For a person like me who have 208 games in the wishlist).
## What to do
1. Clone this repo in your machine
2. Download Data: Download the data from the [protondb-data](https://github.com/bdefore/protondb-data) repository. Ensure that you have extracted the JSON files from the tar archive.
3. Update JSON File Names: Append the upload date and year of the json file(see the date modified) to the end of each JSON file extracted. For example, rename reports_piiremoved.json to reports_piiremoved(apr 2019).json.
4. Put all the renamed json files in a folder
5. Copy the full folder path and paste it in the directory_path = r''
6. Login into steam account on steam website, click onto your wishlist and copy the whole link and paste it in the webUrl = urllib.request.urlopen('')
7. If you want to specify what reviews you want the program to output that matches your Linux OS name, CPU and GPU brand name(all case-sensitive). You can do so in the criteria section of the code
8. Run and wait for the code to finish
9. After the code finishes, you will see the program will list the number of games corresponding to the title
10. Input the number correlating to the game title and the code will output relevant user reviews of the game
11. Update the folder when you see new file uploaded in the protondb-data repo and repeat
### Notice
- I have encountered a problem in trying to access steam it says "This site can’t be reached" with a line below saying "DNS_PROBE_FINISHED_NXDOMAIN". This problem only occurs on my Windows laptop and when i try to to login into steam on desktop(soon to be replaced) I have no problem whatsoever.

- I have figured a way to fix this issue by changing the DNS server but my code won't run on my machine even after i have modified the dns server. So if this problem happends to you, don't clone this repo
## Weakness
- Can't analyse the json files uploaded in 2019 from the repo due to different json structure for the json files at the time

- Can't display the proton version of user review(at least not consistently)

That is all I have to say about this project. I'm very proud of it and i hope this project will Linux users who have a lot of Steam games in the wishlist and don't have the time to read users reviews for fixes to your games from the protondb website 
