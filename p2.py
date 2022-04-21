# membuka dan mau membaca file f:/data.txt
try:
    file = open("f:/data.txt","r")
except FileNotFoundError:
    print("file tidak ada / belum dibuat")
else:
    #baca baris pertama dari file
    #simpan ke dalam variabel bil1 sbg integer
    bil1 = int(file.readline())

    #baca baris pertama dari file
    #simpan ke dalam variabel bil2 sbg integer       
    bil2 = int(file.readline())

    #hitung dan tampilkan hasil bagi
    try:  
        hasil = bil1/bil2
    except: 
        print ( "Tidak boleh pembagian dengan nol !" ) 

    else: 
        print(str(bil1)+' dibagi '+str(bil2)+' sama dengan ' +str(hasil))

