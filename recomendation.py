def ayam_petelur(fase, banyak):
  i = 0
  if fase == "1":
    while i < banyak:
      print("ini anak ayam petelur")
      i+=1
  elif fase == "2":
    while i < banyak:
      print("ini ayam remaja petelur")
      i+=1
  elif fase == "3":
    while i < banyak:
      print("ini ayam finisher petelur")
      i+=1
  else:
    print("Masukkan anda harus berupa angka 1, 2, atau 3 pada kolom 'Fase Ternak'.")

def ayam_pedaging(fase, banyak):
  i = 0
  if fase == "1":
    while i < banyak:
      print("ini anak ayam pedaging")
      i+=1
  elif fase == "2":
    while i < banyak:
      print("ini ayam remaja pedaging")
      i+=1
  elif fase == "3":
    while i < banyak:
      print("ini ayam finisher pedaging")
      i+=1
  else:
    print("Masukkan anda harus berupa angka 1, 2, atau 3 pada kolom 'Fase Ternak'.")

print("Peruntukan Ternak\n"+
      "1. Petelur\n"+
      "2. Pedaging")
peruntukan = str(input("Masukkan angka yang sesuai: "))
print("Fase Ternak\n"+
      "1. Starter\n"+
      "2. Grower\n"+
      "3. Adult")
fase = str(input("Masukkan angka yang sesuai: "))
banyak = int(input("Jumlah ternak anda: "))

if peruntukan == "1":
  ayam_petelur(fase, banyak)
elif peruntukan == "2":
  ayam_pedaging(fase, banyak)
else:
  print("Masukan anda harus berupa angka 1 atau 2 pada kolom 'Peruntukan Ternak'.")