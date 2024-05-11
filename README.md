# 1.Protondb-data Analysis
This is my first my project analysing data from the [protondb-data](https://github.com/bdefore/protondb-data) github repo.The purpose of this project is to help Linux users who have a lot of games in the wishlist to be able to read user reviews for the game output by the program instead of having to go to [protondb](https://www.protondb.com/) website to read each user review of the game manually(For a person like me who have 208 games in the wishlist).
## 2.What to do
1. Clone this repo in your machine
2. Download the data from the [protondb-data](https://github.com/bdefore/protondb-data) repository. Ensure that you have extracted the JSON files from the tar archive.
3. Append the upload date and year of the json file(see the date modified for Windows) at the end of each JSON file extracted. For example, rename reports_piiremoved.json to reports_piiremoved(apr 2019).json.
4. For Linux users, use tar xvf command then use ls -l command to see the modified date of the extracted json file and append the modified date to the end of the json file using the mv command and change to the new name of the json file under apostrophe ('').
5. Put all the renamed json files in a folder
6. Copy the full folder path and paste it in the directory_path = r''
7. Login into your steam account on the steam website, click onto your wishlist and copy the whole link and paste it in the webUrl = urllib.request.urlopen('')
8. If you want to specify what reviews you want the program to output that matches your Linux OS name, CPU and GPU brand name(all case-sensitive). You can do so in the criteria section of the code
9. Run and wait for the code to finish
10. After the code finishes, the program will list the number of games corresponding to the title
11. Input the number that matches the game title and the code will output user reviews
12. Update the folder when a new file is uploaded in the protondb-data repo and repeat
### 3.Notice
For Vietnamese users who are currently affected by the sudden incapability to enter the steam store website. You can follow [this video](https://www.youtube.com/watch?v=uq2LwahDhTM&t=479s) to resolve the issue.For future events when this problem no longer exists, please ignore this notice.

That is all I have to say about this project. I'm very proud of it and i hope this project will help Linux users who have a lot of Steam games in the wishlist and don't have the time to read users reviews for fixes to your games from the protondb website 
