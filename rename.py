import os

STARTS_WITH = "Rick.and.Morty."
FORMATTED_NAME = "rick_and_morty_"

for file in os.listdir("./"):
    print(file)
    # if file.startswith(STARTS_WITH):
    #     old_name = os.path.join("./", file)
    #     new_name = old_name.replace(STARTS_WITH,FORMATTED_NAME).replace(".HDTV.x264","")
    #     os.rename(old_name,new_name)
    #     print(file)
    

