SELECT username
   FROM following
EXCEPT
SELECT username
   FROM followers;

/*Steps to do again in future
1. download followers and following html files through insta
2. move the files into this folder with mv og_path to . (current location)
3. run extract_username (so that the html are turned into csv)
4. run sqlite insta.db (opens up sqlite terminal for database)
    (optional) .quit to leave the sqlite terminal
5. run .import --skip 1 followers.csv followers (for followers and following) 
    .import imports the csv to the database
    --skip 1 skips the first line ("username")
    followers.csv is the original file and followers is the table 
6. run this sql file
*/