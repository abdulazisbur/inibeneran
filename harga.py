# aplikasi menghitung harga jual berdasar persen
hargaSuplier = int(input("Silahkan masukan harga supplier"))
persen = int(input("Silahkan masukan persentase harga"))
hargaPersen = hargaSuplier * (persen / 100)
hargaJual = hargaSuplier +  hargaPersen

print("harga suplier:Rp. ", hargaSuplier)
print("harga suplier:Rp. {}".format(hargaSuplier))
print("persentase ", persen)
print("Untung dari Persentase:Rp {}".format(hargaPersen))
print("harga jual :Rp. {}".format (hargaJual))