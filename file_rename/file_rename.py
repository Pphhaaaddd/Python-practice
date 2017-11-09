import os


#function to rename files
def rename_files():
    # get file names from folder
    file_list = os.listdir(r"/home/phad/version-control/python-practice/file_rename/prank")
    print(file_list)

    # rename the files removing the numbers
    saved_path = os.getcwd()
    print("Current working directory is ", saved_path)
    #os.chdir("/home/phad/version-control/python-practice/file_rename/prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None, "0123456789"))

rename_files()
