def convert(face):
    face = face.replace(':)','🙂')
    face = face.replace(':(','🙁')
    return face
def main():
    text = input("Text: ")
    print(convert(text))

main()