# nomor 1
a = 3
print(type(a))
print("hallo python")

b = 3.5
print(type(b))

nama = "naufal"
print(type(nama))

angka = [1, 2, 3, 4, 5]
print(type(angka))
angka.append(6)
print(angka)


# nomor 2
belanja = ["beras", "minyak", "telur"]
print(type(belanja))
belanja.append("gula")
belanja.append("kopi")


# nomor 3
for sembako in belanja:
    print(sembako)
    
    harga = {
       "beras" : 15000, 
       "minyak" : 20000,
       "telur" : 12000,
       "gula" : 6000,
       "kopi" : 8000  
    }
    
    total = sum(harga.values())
print("TOTAL HARGA BELANJA", total)

# nomor 4
def hitung_lingkaran(r):
    luas = 3.14 * r * r
    keliling = 2 * 3.14 * r
    return luas, keliling   


r = int(input("Masukkan Jari Jari: "))
luas, keliling = hitung_lingkaran(7)

print("Luas:", luas)
print("Keliling:", keliling)

print("Luas dikali 2:", luas * 2)

# nomor 5
usia = int(input("Masukkan usia Anda: "))

if usia >= 0 and usia <= 13:
    print("Anak")
elif usia >= 14 and usia <= 24:
    print("Remaja")
elif usia >= 25 and usia <= 49:
    print("Dewasa")
elif usia >= 50:
    print("Lansia")
else:
    print("Usia tidak valid")




        
    
