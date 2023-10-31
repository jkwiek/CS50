# ask for name, remove whitespace, capitalize
name = input("what's your name? ").strip().title()
#split to first and last
first,last = name.split(" ")
#print output
print(f"hello,{first}")
