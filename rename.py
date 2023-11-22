import os

STARTS_WITH = "How"

REPLACE_TEXT = ""
REPLACE_WITH = ""


for file in os.listdir("./"):
    base_name = os.path.basename(file)
    file_name, file_ext = os.path.splitext(base_name)
    if file_ext == '.mkv' or file_ext == '.avi' or file_ext == '.mp4' or file_ext == '.m4v':
        # Add a dash into the file_name string
        # new_file_name = file_name[:30] + " -" + file_name[30:]
        new_file_name = file_name.replace(REPLACE_TEXT,REPLACE_WITH)
        os.rename(base_name,new_file_name+file_ext)
        print(file_name)


