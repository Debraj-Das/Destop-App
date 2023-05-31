import os
import glob
#* add the staged files to the commit and commit the changes with a message
#* push the changes to the remote repository

# / message for the commit
commit_message = "Completed the Web Scraping the codeforces"


# commit and push the changes to the remote repository

# add the staged files to the commit
os.system("git add .")
# commit the changes with a message
os.system(f"git commit -m \"{commit_message}\"")
# push the changes to the remote repository
os.system("git push origin master")

print("All changes are commit and pushed to the remote repository\n\n")
