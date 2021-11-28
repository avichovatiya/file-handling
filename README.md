# file-handling
We use to work on lots of different type of files in everyday life and we felt it so challenging about maintaing all that files in our system. It is also very boring to separate all that files in diiferent directories according to their category. 
For that we will use python programming to make our work easy and this will organize/separate all our files in different directories. This can be done in many ways and here I had did it in 2 different ways 1) extension of file & 2) category of file.

# extension wise file organizing:
In this we will check the extension of the file and then check if the folder for that extension exists or not. If its already there we will move that file to its respective folder. And if the folder does not exists for any extension then we will create a new folder for that extension and move the file with that extension in the created folder. We will use os and shutil modules which are built-in. OS - to check or create the new directories and SHUTIL - to move the files to the different directories.

# category wise file organizing:
In this firstly we will create different folders for different categories (i.e. images, videos, music, files, etc). Then we will check the extension of the file and check in the lists of extensions, if the file is of recognized extension then it will be categorized and moved to respective folder otherwise it will be moved to the folder named 'Others'. We will use OS module to locate to files in system and make changes in it
