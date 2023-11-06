filetype = input("file name: ")
filetype = filetype.lower()
if filetype.endswith(".gif") == True:
    print("image/gif")
elif filetype.endswith(".jpg") == True or filetype.endswith(".jpeg") == True:
     print("image/jpeg")
#.png .pdf.txt.zip
elif filetype.endswith(".png") == True:
    print("image/png")
elif filetype.endswith(".pdf") == True:
    print("application/pdf")
elif filetype.endswith(".txt") == True:
    print("plain.text")
elif filetype.endswith(".zip") == True:
    print("application/zip")
else:
    print
