# Insta-Unfollow

This is used to check who has unfollowed you but left you as a follower on Instagram. 

Steps to use this: 
1. download followers and following html files through insta
    On computer go to Settings then Account Center
    Press Your information and permissions 
    Click Export your information and create export
    Select Export to device and choose a method to recieve the download progress notification
    Make sure Customize information only includes followers and following, Format is HTML, and Date range is All time
2. move the files into this folder with mv og_path . (current location)
3. run extract_username (so that the html are turned into csv)
4. run sqlite insta.db (opens up sqlite terminal for database)
    (optional) .quit to leave the sqlite terminal
5. run .import --skip 1 followers.csv followers (for followers and following) 
    .import imports the csv to the database
    --skip 1 skips the first line ("username")
    followers.csv is the original file and followers is the table 
6. run this sql file

Note: You can now use Meta's Muse agent to get you this information as well. This was just something fun I did in my free time.