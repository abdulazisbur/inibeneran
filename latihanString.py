nama = "abdul azis burhanudin"
alamat = "jalan cisaat,  desa baduwi selatan, kabupaten utara panjaitan, nomor 12"

print("nama saya:", nama)
print("alamat saya:", alamat)
print("huruf pertama nama saya:", nama[0])
print("huruf pertama nama saya:", nama[-1])
print("huruf pertama nama saya:", nama[-10:])
print("huruf pertama nama saya:", nama[:-14])


#split string
alamat_array = alamat.split(', ')
jalan = alamat_array[0]
kecamatan = alamat_array[1]
kabupaten = alamat_array[2]
nomor = alamat_array[3]
print("Alamat saya:", alamat_array)
print("Alamat jalan saya:", jalan)
print("Alamat kecamatan saya:", kecamatan)
print("Alamat desa saya:", kabupaten)
print("alamat tinggal saya", jalan, "Kecamatan", kecamatan, "Kabupaten", kabupaten)#join string
pemisah = " + "
print("Alamat join saya:", pemisah.join(alamat_array))
