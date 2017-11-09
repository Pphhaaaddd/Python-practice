import os


#function to rename files
def rename_files():
    # get file names from folder
    file_list = os.listdir(r"/home/phad/version-control/python-practice/file_rename/prank")
    print(file_list)
    # rename the files removing the numbers


rename_files()
