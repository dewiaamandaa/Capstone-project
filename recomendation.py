def ayam_petelur(fase, banyak):
  #https://www.youtube.com/watch?v=5wGz_9Xn33o
  if fase == "1": #fase starter
    print("Ternak anda berada pada fase starter, komposisi pakan yang sebaiknya anda berikan:\n"+
          "Jagung: {:.2f} gram\n".format(72.4/100*40*banyak)+
          "Tepung ikan: {:.2f} gram\n".format(18.4/100*40*banyak)+
          "Kedelai/ampas tahu: {:.2f} gram".format(9.2/100*40*banyak)
    )
  elif fase == "2": #fase grower
    print("Ternak anda berada pada fase grower, komposisi pakan yang sebaiknya anda berikan:\n"+
          "Jagung: {:.2f} gram\n".format(76.9/100*80*banyak)+
          "Tepung ikan: {:.2f} gram\n".format(15.4/100*80*banyak)+
          "Kedelai/ampas tahu: {:.2f} gram".format(7.7/100*80*banyak)
    )
  elif fase == "3": #fase layers
    print("Ternak anda berada pada fase layers, komposisi pakan yang sebaiknya anda berikan:\n"+
          "Jagung: {:.2f} gram\n".format(81.5/100*120*banyak)+
          "Tepung ikan: {:.2f} gram\n".format(12.3/100*120*banyak)+
          "Kedelai/ampas tahu: {:.2f} gram".format(6.2/100*120*banyak)
    )
  else:
    print("Masukkan anda harus berupa angka 1, 2, atau 3 pada kolom 'Fase Ternak'.")

def ayam_pedaging(fase, banyak):
  #https://www.medion.co.id/manajemen-pakan-broiler/
  i = 0
  if fase == "1": #fase starter
    print("Ternak anda berada pada fase starter, komposisi pakan yang sebaiknya anda berikan:\n"+
          "Jagung: {:.2f} gram\n".format(53.6/100*50*banyak)+
          "Bungkil kedelai: {:.2f} gram\n".format(35.64/100*50*banyak)+
          "Tepung tulang: {:.2f} gram\n".format(5/100*50*banyak)+
          "Bubuk lemak: {:.2f} gram\n".format(3.1/100*50*banyak)+
          "Fosfor dan kalsium: {:.2f} gram\n".format(0.44/100*50*banyak)+
          "Asam amino: {:.2f} gram\n".format(1.6/100*50*banyak)+
          "Tepung Batu: {:.2f} gram".format(0.62/100*50*banyak)
    )
  elif fase == "2": #fase finisher
    print("Ternak anda berada pada fase finisher, komposisi pakan yang sebaiknya anda berikan:\n"+
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