# Tugas pertemuan 9
# Nama  : Diajeng triana k.
# NIM   : 312110474
pertama adalah membuat list dengan 5 elemen saya membuat list

a = [6, 7, 8, 9, 10]

kedua pada akses list saya diberi 3 soalan

menampilkan elemen ke 3\

ambil nilai elemen ke 2 sampai elemen ke 4

ambil elemen terakhir\

dari soal diatas saya mengerjakan dengan cara sebagai berikut:

1. a[2]
2. del a[1:4]
    print(a)
3. del a[1] 
    print(a)

ketiga pada ubah element list saya diberikan 2 soalan

ubah elemen ke 4 dengan nilai lainnya

ubah elemen ke 4 sampai dengan elemen terakhir

dari soalan diatas saya menjawab dengan cara sebagai berikut:

a [3] = 5
print (a)
a [3:5] = 3, 4
print(a)

terakhir pada tambah elemen list saya diberi soalan sebagai berikut

ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)

tambah list B dengan nilai string

tambah list B dengan 3 nilai

gabungkan list B dengan list A

dari soal diatas saya menjawab dengan cara sebagai berikut

b = []
b.extend (a[0:2])
print(b)
b.append ('delapan')
print(b)
b.extend([9, 10, 11])
print(b)
c=a+b
print(c)

# berikut ini adalah screenshot hasil output :

<img width="727" alt="outputss1" src="https://user-images.githubusercontent.com/92905452/144408158-cb9005ba-390c-4935-88fa-c21608f59dc9.png">

# flowchart

pertama sebelum membuat program saya membuat flowchart terlebih dahulu
berikut flowchart yang telah dibuat

<img width="579" alt="flowchart" src="https://user-images.githubusercontent.com/92905452/144409096-99dccfe8-3bdb-4747-9270-ee89c9a3874b.png">

pertama saya membuat inputan dan looping agar program terus berjalan

while true:
    c = input("apakah ingin menambah data? y/t ")

lalu saya membuat fungsi if apabila menginput 'y'

if (c.lower() == 'y'):                                               
        print('\nTambah Data Mahasiswa Baru')
        nama= input("Masukkan Nama\t\t: ")                                        
        nim= input("Masukkan NIM\t\t: ")                                         
        nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                              
        nilaiUts= int(input("Masukkan Nilai UTS\t: "))                                   
        nilaiUas= int(input("Masukkan Nilai UAS\t: "))                                    
        nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)              
        data[nama]= nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                         
        print("\nData Berhasil Ditambahkan!")

saya juga membuat percabangan if untuk apabila menginput 't'

elif (c.lower() == 't'):                                                                    
        if data.items():                                                                     
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  
            print("==================================================================")
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================")

dan saya menambahan else untuk menyetop loopingan tadi

else:
    break

# berikut ini adalah screenshot hasil output :

