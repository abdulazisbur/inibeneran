while True:
    print("Pilih opsi:")
    print("1. Hitung luas segitiga")
    print("2. Hitung luas persegi panjang")
    print("3. Menentukan angka ganjil/genap")
    print("4. Keluar")

    opsi = int(input("Masukkan pilihan Anda (1-4): "))

    if opsi == 1:
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print(f"Luas segitiga adalah {luas}")
    elif opsi == 2:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = panjang * lebar
        print(f"Luas persegi panjang adalah {luas}")
    elif opsi == 3:
        angka = int(input("Masukkan bilangan: "))
        if angka % 2 == 0:
            print(f"Bilangan {angka} adalah genap")
        else:
            print(f"Bilangan {angka} adalah ganjil")
    elif opsi == 4:
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")