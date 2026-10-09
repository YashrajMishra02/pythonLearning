import os
from datetime import datetime

print(dir(os))

# to know your current directory
print(os.getcwd())

# navigate to new location 
os.chdir("D:/pythonLearning/chapter11/")

print(os.getcwd())

# To see files and folders on the desktop 
print(os.listdir()) # bydefault it will list the files from the current directory 

# Creating Directory 2 way mkdir() and makedirs()

os.mkdir("OS-demo/sub-dir") # won't create sub directory untill parent folder is created 
os.makedirs("OS-demo/sub-dir") # Create a sub dirctory

os.rmdir("OS-demo/sub-dir")
os.removedirs("OS-demo/sub-dir") # remove the sub folder along with the parent directory

os.rename('test.txt','Demo.txt') # Use to rename the folder/file

mod_time = os.stat('Demo.txt').st_mtime

print(datetime.fromtimestamp(mod_time))

os.walk() # represent the directories in tree format with returning three tuple i.e. dirpath, dirnames, filenames

for dirpath, dirnames, filenames in os.walk("D:/pythonLearning/chapter11/"):
    print("Current Path: ", dirpath)
    print("Directoreis: ",dirnames)
    print("Files: ",filenames)
    print() 
print(os.environ.get('windir'))

# we cannot directly concatinate the path and the sub folder as there me be / or // at the end hence this cannot be done like this
full_path = os.environ.get('windir') + 'test.txt'

full_path = os.path.join(os.environ.get('windir'), 'text.txt')
print(full_path)




