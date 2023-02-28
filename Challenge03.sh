#First step, ask the user for the folder and save to variable "directory"
echo "Choose a Directory"
read directory

#Second step, ask the user which permissions he wants and save to variable "permissions"
echo "Which permissions you want?"
read permissions

#Third step, change the permissions of all the files on the directory choosed by the user
chmod -R $permissions $directory

#Fourth step, show changed permissions to user
ls -l $directory