Answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
Answer = Answer.strip().lower().replace("-"," ")
if Answer == "42" or Answer == "forty two":
    print("Yes")
else:
    print("No")
