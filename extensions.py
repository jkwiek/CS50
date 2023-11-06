filetype = input("file name: ")
filetype = filetype.lower().strip().partition(".")[2]
if filetype == "gif":
    print("image/gif")
elif filetype == "jpg" or filetype == "jpeg":
    print("image/jpeg")
elif filetype == "png":
    print("image/png")
elif filetype == "pdf":
    print("application/pdf")
elif filetype.endswith(".txt") == True:
    print("text/plain")
elif filetype.endswith(".zip") == True:
    print("application/zip")
else:
    print("application/octet-stream")
