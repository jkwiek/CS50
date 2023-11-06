filetype = input("file name: ")
filetype = filetype.lower()
if filetype.endswith(".gif") == True:
    print("image/gif")
if filetype.endswith(".jpg" or ".jpeg") == True:
     print("image/jpeg")
#.png .pdf.txt.zip
