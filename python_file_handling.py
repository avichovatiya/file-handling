# Organizing files extension wise:
import os
import shutil

path=input("Enter Path")
files= os.listdir(path)
for f in files:
    filename,ext=os.path.splitext(f)
    ext=ext[1:]
    
    if os.path.exists(path+ '/' + ext):
        shutil.move(path+'/'+f , path+'/'+ext+'/'+f)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+f ,path+'/'+ext)

print('Hurrayy !!....Your files are moved successfully')




# Organizing files category wise:
import os

mypath = input("Enter Path: ")
os.chdir(mypath)
filelist = ["Videos","Images","Files","Music","compressed_and_ececutables","Others"]

if not os.path.exists("Videos"):
    print("Creating Videos Folder...")
    os.mkdir("Videos")
if not os.path.exists("Music"):
    print("Creating Files Folder...")
    os.mkdir("Music")
if not os.path.exists("Files"):
    print("Creating Files Folder...")
    os.mkdir("Files")
if not os.path.exists("Images"):
    print("Creating Images Folder...")
    os.mkdir("Images")
if not os.path.exists("compressed_and_executables"):
    os.mkdir("compressed_and_executables")
if not os.path.exists("Others"):
    os.mkdir("Others")

def moveItems(mypath,path,fmt,folder):
    if os.path.basename(path) not in filelist:
        _ = os.system(rf'move "{path}\*.{fmt}" "{mypath}\{folder}"')
        print(rf'move "{path}\*.{fmt}" "{mypath}\{folder}"')

music_ext = ["mp3","wav"]
video_ext = ["mp4","avi","3gp","webm","flv","mov","mkv"]
image_ext = ["jpg","png","jpeg","tiff","gif","tif"]
files_ext = ["js","css","py","csv","html","txt","doc","docx","xml","pdf","xls","xlsx","ppt"]
exe_cmp_ext = ["exe","zip","rar","msi","tar","xz","7z","tgz","iso"]

for path,dirs,files in os.walk(os.getcwd()):
    extentions_present = []
    for item in image_ext:
        if item in str(files).lower():
            extentions_present.append((item,"Images"))

    for item in video_ext:
        if item in str(files).lower():
            extentions_present.append((item,"Videos"))

    for item in music_ext:
        if item in str(files).lower():
            extentions_present.append((item,"Music"))

    for item in files_ext:
        if item in str(files).lower():
            extentions_present.append((item,"Files"))

    for item in exe_cmp_ext:
        if item in str(files).lower():
            extentions_present.append((item,"compressed_and_executables"))

    for extention in extentions_present:
        moveItems(mypath,path,extention[0],extention[1])
    moveItems(mypath,path,"*","Others")

print('Hurrayy !!...Your files are moved successfully')
