saldo = 1000000

while True:
    print(f"\nSaldo saat ini: Rp {saldo:,.2f}")
    print("1. Tarik Uang")
    print("2. Keluar")

    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah penarikan: "))
        if jumlah <= saldo:
            saldo -= jumlah
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi!")
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
