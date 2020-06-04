def urai(x): # fungsi urai untuk variabel x
    hasil = [] # storage berupa list untuk hasil iterasi 
    x = list(x) # menguraikan x per karakter dan dimasukkan dalam list
    for i in range(0,len(x)+1): # iterasi per karakter dalam x sebanyak panjang x+1
        hasil += x[:i] # slicing x sesuai kondisi soal [:i]
    hasil = "".join(hasil) # penggabungan semua karakter dalam list untuk membentuk kata sesuai output
    return hasil # return value   

def rajut(y): # fungsi urai untuk variabel y
    y = list(y) # menguraikan y per karakter dan dimasukkan dalam list
    hitung = y.count(y[0]) # menghitung berapa jumlah karakter pertama dalam y, hal ini akan menentukan panjang kalimat yang dicari (misal : CCoCodCode ada 4 huruf C maka panjang kata sebenarnya adalah 4 yaitu Code )
    y = y[(-1*(hitung)):] # slicing sebanyak hitung, namun dimulai dari paling belakang (-1)
    y = "".join(y) # penggabungan semua karakter dalam list membentuk kata sesuai output
    return y # return value
      
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))    

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

#Created by Tito Tamaro



