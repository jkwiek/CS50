filetype = input("file name: ")
filetype = filetype.lower().strip().split(".",-1)[2]
if filetype == "gif":
    print("image/gif")
elif filetype == "jpg" or filetype == "jpeg":
    print("image/jpeg")
elif filetype == "png":
    print("image/png")
elif filetype == "pdf":
    print("application/pdf")
elif filetype == "txt":
    print("text/plain")
elif filetype == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
