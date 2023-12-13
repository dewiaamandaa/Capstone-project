import recomendation as rc

print("Peruntukan Ternak\n"+
      "1. Petelur\n"+
      "2. Pedaging")
peruntukan = str(input("Masukkan angka yang sesuai: "))


if peruntukan == "1":
    banyak = int(input("Jumlah ternak anda: "))
    print("Fase Ternak\n"+
          "1. Starter\n"+
          "2. Grower\n"+
          "3. Finisher"
    )
    fase = str(
       input("Masukkan angka yang sesuai: ")
    )
    rc.ayam_petelur(fase, banyak)
elif peruntukan == "2":
    banyak = int(input("Jumlah ternak anda: "))
    print("Fase Ternak\n"+
          "1. Starter\n"+
          "2. Finisher"
    )
    fase = str(
       input("Masukkan angka yang sesuai: ")
    )
    rc.ayam_pedaging(fase, banyak)
else:
  print("Masukan anda harus berupa angka 1 atau 2 pada kolom 'Peruntukan Ternak'.")