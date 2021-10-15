import os

input("This will take one letter off the start of the filename in the following directory: ")

a = input("What is the full file path? ")

os.chdir(a)

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title = f_name.strip()[1:] 
    new_Name = '{}{}'.format(f_title, f_ext)
    os.rename(f, new_Name)
    
'''
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name)
# So far this prints the file and fileextension in separate lists

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('-'))
# this will separate the item whatever you put in the split function.
# In this case it will split on '-'

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    print(f_num)

# this will give you a choice of what to print. You are essentially dividing
# filename split into 3 catagories title, course and num that are divided by the '-'.

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip() 
    f_course = f_course.strip()
    f_num = f_num.strip()
    print('{}{}{}{}'.format(f_num, f_course, f_title, f_ext))

# What we have done so far is rearranged the filename in the way we wanted.

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title = f_name.strip()[1:] 
    print('{}{}'.format(f_title, f_ext))

# this will take the first letter off the file name. Using [1:].

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title = f_name.strip()[1:].zfill(2)
    print('{}{}'.format(f_title, f_ext))

# this has added a zero to all single digits at the front of a filename.01 instead of 1

powershell commands
go to location of files
dir | Where-Object -FilterScript {($_.Extension -like '.jpg')} | Rename-Item -NewName {('Test'+$_.Name)}
This adds the word test on to our filename

dir | Where-Object -FilterScript {($_.Extension -like '.jpg')} | Rename-Item -NewName {($_.Name -replace " ", "-")}
replaces spaces in filenames with dashes

dir | Where-Object -FilterScript {($_.Extension -like '.jpg')} |Rename-Item -NewName {($_.basename + "-Example" + $_.extension)}
This adds "-Example" to the end of a filename without confusing it with a file extension.

dir | Rename-Item -NewName {($_.Name.substring(1))}
This removes the first digit in the current working directory

'''



