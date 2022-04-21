print("===========================================================")
print("Program sederhana membuka, membaca dan menampilkan file txt")
print("===========================================================")

nm_file = str(input("Masukkan path lokasi dan nama file : "))

try:  
    file = open(nm_file,"r")

except: 
    print ( "Lokasi file tidak tersedia / file tidak ditemukan !" ) 

else:
    print("Isi file "+nm_file+" adalah:")
    print(file.read())



print("===========================================================")


