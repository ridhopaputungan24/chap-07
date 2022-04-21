print("======================================================")
print("Program sederhana membuka dan menambahkan isi file txt")
print("======================================================")

nm_file = str(input("Masukkan path lokasi dan nama file : "))

try:
    open(nm_file,"r")
    
except: 
    print("lokasi file tidak tersedia / file tidak ditemukan !")   

else:
    while True: 
        data = str(input("Data yang mau ditambahkan : "))
        file = open(nm_file,"a")
        file.write("\n"+data)
        file.close()
            
        cont = input("Mau menambahkan lagi (y/n) : ")
        while cont.lower() not in ("y","n"):
            cont = input("masukan anda salah, masukan hanya n atau y : ")
        if cont == "n":
            break
