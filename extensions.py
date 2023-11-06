filetype = input("file name: ")
filetype = filetype.lower().strip().split(".",[2])
if filetype == gif:
    print("image/gif")
elif filetype.endswith(".jpg") == True or filetype.endswith(".jpeg") == True:
    print("image/jpeg")
elif filetype.endswith(".png") == True:
    print("image/png")
elif filetype.endswith(".pdf") == True:
    print("application/pdf")
elif filetype.endswith(".txt") == True:
    print("text/plain")
elif filetype.endswith(".zip") == True:
    print("application/zip")
else:
    print("application/octet-stream")
