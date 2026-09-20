# Sistem Pengelolaan Pemesanan Album dan Merchandise K-pop

## 1. Penjelasan Program

Program ini dibuat menggunakan Python dengan konsep Pemrograman Berorientasi Objek (PBO). Tema yang digunakan adalah Sistem Pengelolaan Pemesanan Album dan Merchandise K-pop.
Program ini dibuat untuk mengelola data produk K-pop, seperti album dan merchandise, serta data pesanan. Di dalam program terdapat beberapa penerapan konsep PBO, seperti class, object, attribute, method, encapsulation, class method, static method, getter, dan setter.
Pada program ini, data stok dibuat sebagai private attribute dengan nama `__stok`. Untuk melihat atau mengubah stok, digunakan getter dan setter. Pada setter juga terdapat validasi, sehingga jika stok diisi dengan nilai 0 atau kurang, program akan menolak nilai tersebut.
Selain itu, program dapat digunakan untuk menampilkan data produk dan pesanan, mengubah harga produk, mengubah nama toko, melakukan validasi harga dan jumlah pesanan, serta menghitung total harga pesanan.

## 2. Struktur Class

Program ini memiliki 4 class utama, yaitu `ProdukKpop`, `Album`, `Merchandise`, dan `Pesanan`.

### ProdukKpop

Class `ProdukKpop` digunakan sebagai class dasar untuk menyimpan data produk K-pop.

Data yang disimpan antara lain ID produk, nama produk, harga, dan stok. Class ini juga memiliki beberapa method untuk menampilkan produk, mengubah harga, mengubah nama toko, dan melakukan validasi harga.

### Album

Class `Album` merupakan turunan dari class `ProdukKpop`. Class ini digunakan untuk menyimpan data album.

Selain data yang diwarisi dari `ProdukKpop`, class `Album` memiliki data tambahan berupa artis, versi album, dan jumlah lagu.

### Merchandise

Class `Merchandise` juga merupakan turunan dari class `ProdukKpop`. Class ini digunakan untuk menyimpan data merchandise.

Data tambahan yang dimiliki yaitu jenis merchandise, ukuran, dan bahan.

### Pesanan

Class `Pesanan` digunakan untuk menyimpan data pesanan.

Data yang disimpan meliputi ID pesanan, produk yang dipesan, jumlah, dan status pesanan. Class ini juga memiliki method untuk menghitung total harga, menampilkan data pesanan, mengubah status default, dan melakukan validasi jumlah pesanan.

## 3. Panduan Pengujian

Beberapa pengujian yang dilakukan dalam program yaitu:

1. Menampilkan data album dan merchandise.
2. Menampilkan data pesanan beserta total harga pesanan.
3. Mengubah nama toko menggunakan class method.
4. Mengubah status default pesanan menggunakan class method.
5. Menguji validasi harga menggunakan static method.
6. Menguji validasi jumlah pesanan menggunakan static method.
7. Menampilkan stok album menggunakan getter.
8. Mengubah stok album menggunakan setter.
9. Menguji setter dengan memasukkan stok `0`. Program akan menolak nilai tersebut dan menampilkan pesan error.
10. Mengubah harga album menggunakan instance method.
11. Menampilkan semua produk yang ada dalam daftar.
12. Menghapus salah satu produk dari daftar.
13. Menampilkan jumlah total produk dan total pesanan.