with open("myfile.txt",'w') as file:
    file.write("Hello file world")

with open ("myfile.txt") as file:
    try:
        print(file.readline())
    except FileNotFoundError:
        print("No such directory")


