
def main(face):
    face = input("face? ")
    face = face.convert()
    print(face)

def convert(face):
    face = face.replace(":)","🙂").replace(":(","🙁")

print(main)


