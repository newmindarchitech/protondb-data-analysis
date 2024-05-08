# proton-data-base-report
This is my first my project analysing data from the [protondb-data](https://github.com/bdefore/protondb-data)github repo.The purpose of this project is to use the data from the repo along with my code to analyse and return user reviews that matches their Linux OS,CPU and GPU specifications
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
-There is a problem i have encountered and i don't know if you have the same but in my country(Viet Nam). Whenever i try to login into the steam store using Chrome, it always returns an error saying that "This site can’t be reached" with line below saying "DNS_PROBE_FINISHED_NXDOMAIN". 

-I have figured a way to fix this issue by changing the DNS server but my code just won't run on my machine even if i have modified the dns server. So that's something to keep in mind before you clone this repo

 That is all i have to say about this project. I'm very proud of it and i hope this project will help Linux users who
doesn't have time to read through numerous reviews if you have alot of games in the wishlist
