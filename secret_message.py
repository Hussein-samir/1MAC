import os

def rename_files():
    #1 get file name from a folder
    file_list = os.listdir(r"C:\Users\alityan\Desktop\prank")
    #2 for each file rename filename
    os.chdir(r"C:\Users\alityan\Desktop\prank")
    for file_name in file_list:
        new_name = file_name.translate(None,"0123456789")
        os.rename(file_name,new_name)
rename_files()