print(3*'=','tugas pertemuan 9','='*3)
print('| Nama: Diajeng triana\t|\n| NIM: 312110474\t|\n| Kelas: TI.21.C5\t|')
print(25*'=','\n')
print('program menambah data mahasiswa\n')
data={}
while True:
    c = input("\napakah ingin menambha data? y/t ")
    if (c.lower() == 'y'):
        print('\nTambah Data Mahasiswa Baru')
        nama= input("Masukkan Nama\t\t: ")
        nim= input("Masukkan NIM\t\t: ")
        nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))
        nilaiUts= int(input("masukkan Nilai UTS\t: "))
        nilaiUas= int(input("Masukkan Nilai UAS\t: "))
        nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        data[nama]= nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("\nData Berhasil Ditambahkan!")
    elif (c.lower() == 't'):
        if data.items():
            print("\n                          DAFTAR NILAI MAHASISWA                         ")
            print("===========================================================================")
            print("| NO |   Nama    |   NIM    |   Tugas   |   UTS    |    UAS    |   Akhir  |")
            print("===========================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:2} | {0:12s} |  {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                print("=======================================================================")
        else:
            print("\n                          DAFTAR NILAI MAHASISWA                         ")
            print("===========================================================================")
            print("| NO |   Nama    |   NIM    |   Tugas   |   UTS    |    UAS    |   Akhir  |")
            print("===========================================================================")
            print("|                               TIDAK ADA DATA!                           |")
            print("===========================================================================")
    else:
        break