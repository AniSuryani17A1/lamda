NAMA  = raw_input("\tMasukan Nama      :")
UTS   = input    ("\tNilai UTS         :")
UAS   = input    ("\tNilai UAS         :")
TUGAS = input    ("\tNilai TUGAS       :")


print "\tNama              : ", NAMA
print "\tNilai UTS         : ", UTS
print "\tNilai UAS         : ", UAS
print "\tNilai TUGAS       : ", TUGAS
akhir =(UTS+UAS+TUGAS)/3
print  "Nilai Akhir        : ", akhir

if akhir >80:
    print "\tNilai Huruf        : A"
    print "\tketerangan         : Lulus"
elif akhir >=70 and akhir <=80:
    print "\tNilai Huruf        : B"
    print "\tketerangan         : Lulus"
elif akhir >=60 and akhir <=70:
    print "\tNilai Huruf        : C"
    print "\tketerangan         : Tidak lulus"
elif akhir >=40 and akhir <=50:
    print "\tNilai Huruf        : D"
    print "\keterangan          : Tidak lulus"
elif akhir >=0 and akhir <=30:
    print "\tNilai Huruf        : E"
    print "\keterangan          : Tidak lulus"
    
