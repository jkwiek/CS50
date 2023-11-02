
def main():
    face = input("face? ")
    face = convert(face)
    print(face)

def convert(face):
    face = face.replace(":)","🙂")
    face = face.replace(":(","🙁")

main()


