file_name = input("Name of file: ").split(".")
name = file_name[1]
if file_name[1] == "jpg":
    name = "jpeg"
match name:
    case "gif"|"jpeg"|"png"|"pdf"|"txt"|"zip":
        print(f"image/{name}")
    case _:
        print("application/octet-stream")





