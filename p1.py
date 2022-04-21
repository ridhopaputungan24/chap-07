try:
    file = open("f:/myfile.txt","r")
except FileNotFoundError:
    print("file tidak ada / belum dibuat")
else:
    print(file.read())
