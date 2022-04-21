print("------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("------------------------")
angka = []
sum = 0
total = 0
while True: 
        data = str(input("Masukkan bilangan bulat : "))
        isInt=True
        try:
            int(data)
            
        except:
            print('Nilai bukan bilangan bulat')        
            
        else:
            angka.append(data)
            cont = input("Lagi (y/n)? : ")
            while cont.lower() not in ("y","n"):
                    cont = input("Masukan anda salah, masukan hanya n atau y : ")
            if cont == "n":
                    break
            
       
for datas in angka:
        sum = sum + int(datas)
        
hasil = sum / len(angka)
print("------------------------")
print("Total data  : " +str(len(angka)))
print("Jumlah data : " +str(sum))
print("Nilai Rata-ratanya adalah : "+ str(hasil))
print("------------------------")

