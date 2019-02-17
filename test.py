import dropbox 

ACCESS_TOKEN = "5a5bbxKLU_wAAAAAAACNDrmiKz-YfnPds9iy-N-DeY0QTJRdo9_GOYS17Qn1Fcx_"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

for entry in dbx.files_list_folder('/test').entries:
    print(entry.id)

 
