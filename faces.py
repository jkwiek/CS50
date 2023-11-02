
def convert(face):
    face = face.replace(":)","🙂").replace(":(","🙁")

def main(face):
    face = input("face? ")
    face = face.convert()
    print(face)

main(face)
