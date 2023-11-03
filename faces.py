
def main():
    response = input("")
    response = convert(response)
    print(response)

def convert(text):
    text = text.replace(":)","🙂").replace(":(","🙁")
    return(text)
main()


