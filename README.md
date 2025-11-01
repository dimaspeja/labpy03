# labpy03
# Latihan 1: Menampilkan bilangan acak lebih kecil dari 0.5
tulis fungsi random agar angka dapat diacak dari 0.0 dan 1.0

input nilai N (ingin ada berapa jumlah bilangan random yang di tampilkan)

i = 0 untuk menghitung jumlah bilangan acak yang sudah ditampilkan

while i < n selama i masih kurang dari n, maka program akan terus berjalan

for _ range(1) loop for berjalan 1 kali setiap iterasi while

random.random() agar menghasilkan bilangan acak antara 0.0 dan 1.0

if bilangan < 0.5: agar hanya angka yang dibawah 0.5 yang akan di tampilkan

i += 1 i dinaikkan 1 agar angka yang pertama ditampilkan adalah angka 1

print(f"data ke-{i} => {bilangan}") memunculkan data ke (i) dan hasih bilangan dibawah 0.5

selesai

# Latihan 2: Hitung total keuntungan
modal di isi dengan modal awal Rp.100.000.000

total laba diset ke 0 untung menyimpan akumulasi laba selama 8 bulan.

for bulan in range(1, 9): program menjalankan blok kode didalamnya sebanyak 8 kali (1-8). setiap iterasi mewakili 1 bulan

bulan 1 dan 2 persentasenya 0% karena belum ada keuntungan

bulan 3 dan 4 keuntungan 1% dari modal awal

bulan 5, 6 dan 7 keuntungan 5% dari modal awal

bulan 8 keuntungan 3% dari modal awal

total laba += laba  setiap laba bulan tertentu dihitung, nilainya ditambahkan ke total_laba

print(f"Laba bulan ke-{bulan} sebesar:Rp.{laba:,.2f}") menampilkan hasil laba untuk bulan itu dengan format :,.2f untuk menambahkan tanda koma sebagai pemisah ribuan dan 2 angka di belakang koma

print(f"Total laba adalah:Rp.{total_laba:,.2f}") setelah semua selesai dihitung, program menampilkan total laba selama 8 bulan.

# Latihan 3: Mesin ATM Sederhana
nilai awal saldo ditetapkan sebesar Rp 1.000.000

while True agar perulangan terus menerus sampai ada perintah break

program menampilkan saldo saat ini dan pilihan 1. tarik uang dan 2. keluar

pengguna memilih antara menu 1 atau 2

jika pengguna memilih menu 1 maka diminta memasukkan jumlah uang yang ingin ditarik

jika jumlah penarikan dibawah awal saldo, maka saldo dikurang jumlah penarikan

jika selesai tampilkan Penarikan Berhasil!

saldo yang baru akan otomatis tersimpan dan akan ditampilkan lagi pada perulangan berikutnya.

jika jumlah penarikan lebih besar dari saldo maka

tampilakan pesan "Saldo tidak mencukupi!" dan tampilkan perulangan dari awal

jika pengguna memilih menu 2 maka muncul tampilan Terima Kasih telah menggunakan ATM!

program lalu dihentikan.

jika pengguna menginput selain 1 dan 2, maka muncul tampilan Pilihan tidak valid, silakan coba lagi

tampilkan perulangan dari awal.

Selesai
