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
    print("Komposisi pakan yang sebaiknya anda berikan:\n"+
          "Jagung: {:.2f} gram\n".format(53.6/100*120*banyak)+
          "Bungkil kedelai: {:.2f} gram\n".format(35.64/100*120*banyak)+
          "Tepung tulang: {:.2f} gram\n".format(5/100*120*banyak)+
          "Bubuk lemak: {:.2f} gram\n".format(3.1/100*120*banyak)+
          "Fosfor dan kalsium: {:.2f} gram\n".format(0.44/100*120*banyak)+
          "Asam amino: {:.2f} gram\n".format(1.6/100*120*banyak)+
          "Tepung Batu: {:.2f} gram".format(0.62/100*120*banyak)
    )
  elif fase == "2":
    print("Komposisi pakan yang sebaiknya anda berikan:\n"+
          "Jagung: {:.2f} gram\n".format(62.5/100*120*banyak)+
          "Bungkil kedelai: {:.2f} gram\n".format(29.2/100*120*banyak)+
          "Tepung tulang: {:.2f} gram\n".format(5/100*120*banyak)+
          "Bubuk lemak: {:.2f} gram\n".format(1.2/100*120*banyak)+
          "Fosfor dan kalsium: {:.2f} gram\n".format(0.5/100*120*banyak)+
          "Asam amino: {:.2f} gram\n".format(1.3/100*120*banyak)+
          "Tepung Batu: {:.2f} gram".format(0.4/100*120*banyak)
    )
  else:
    print("Masukkan anda harus berupa angka 1, 2, atau 3 pada kolom 'Fase Ternak'.")