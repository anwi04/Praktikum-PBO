class ProdukKpop:
    nama_toko = "K_pop Store"
    total_produk = 0
    kategori_produk = ["Album", "Merchandise"]

    def __init__(self, idProduk, namaProduk, harga, stok):
        self.idProduk = idProduk
        self.namaProduk = namaProduk
        self.harga = harga
        self.__stok = stok

        ProdukKpop.total_produk += 1

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru <= 0:
            raise ValueError("Stok tidak boleh 0.")
        self.__stok = stok_baru

    def tampilkan_produk(self):
        print("ID Produk :", self.idProduk)
        print("Nama      :", self.namaProduk)
        print("Harga     :", self.harga)
        print("Stok      :", self.stok)

    def ubah_harga(self, harga_baru):
        if harga_baru <= 0:
            print("Harga tidak valid.")
        else:
            self.harga = harga_baru
            print("Harga berhasil diubah.")

    @classmethod
    def ubah_nama_toko(cls, nama_baru):
        cls.nama_toko = nama_baru

    @staticmethod
    def validasi_harga(harga):
        return harga > 0


class Album(ProdukKpop):
    def __init__(self, idProduk, namaProduk, harga, stok, artis, versiAlbum, jumlahLagu):

        super().__init__(idProduk, namaProduk, harga, stok)

        self.artis = artis
        self.versiAlbum = versiAlbum
        self.jumlahLagu = jumlahLagu

    def tampilkan_produk(self):
        super().tampilkan_produk()
        print("Artis       :", self.artis)
        print("Versi       :", self.versiAlbum)
        print("Jumlah Lagu :", self.jumlahLagu)


class Merchandise(ProdukKpop):
    def __init__(self, idProduk, namaProduk, harga, stok, jenisMerch, ukuran, bahan):

        super().__init__(idProduk, namaProduk, harga, stok)

        self.jenisMerch = jenisMerch
        self.ukuran = ukuran
        self.bahan = bahan

    def tampilkan_produk(self):
        super().tampilkan_produk()
        print("Jenis  :", self.jenisMerch)
        print("Ukuran :", self.ukuran)
        print("Bahan  :", self.bahan)


class Pesanan:
    status_default = "Diproses"
    total_pesanan = 0
    nama_toko = "K-Pop Store"

    def __init__(self, idPesanan, produk, jumlah):
        self.idPesanan = idPesanan
        self.produk = produk
        self.jumlah = jumlah
        self.status = Pesanan.status_default

        Pesanan.total_pesanan += 1

    def hitung_total(self):
        return self.produk.harga * self.jumlah

    def tampilkan_pesanan(self):
        print("ID Pesanan :", self.idPesanan)
        print("Produk     :", self.produk.namaProduk)
        print("Jumlah     :", self.jumlah)
        print("Total      :", self.hitung_total())
        print("Status     :", self.status)

    @classmethod
    def ubah_status_default(cls, status_baru):
        cls.status_default = status_baru

    @staticmethod
    def validasi_jumlah(jumlah):
        return jumlah > 0

produk1 = ProdukKpop(
    "P001",
    "Photocard BTS",
    300000,
    10
)

produk2 = ProdukKpop(
    "P002",
    "Poster BTS",
    150000,
    15
)

album1 = Album(
    "A001",
    "Album BTS Arirang",
    350000,
    10,
    "BTS",
    "Standard",
    10
)

album2 = Album(
    "A002",
    "Album BTS Proof",
    400000,
    8,
    "BTS",
    "Compact",
    48
)

merch1 = Merchandise(
    "M001",
    "Hoodie BTS",
    900000,
    5,
    "Hoodie",
    "L",
    "Cotton"
)

merch2 = Merchandise(
    "M002",
    "T-Shirt BTS",
    200000,
    7,
    "T-Shirt",
    "M",
    "Cotton"
)

pesanan1 = Pesanan(
    "O001",
    album1,
    2
)

pesanan2 = Pesanan(
    "O002",
    merch1,
    1
)

print("=== DATA ALBUM ===")
album1.tampilkan_produk()
print()


print("=== DATA MERCHANDISE ===")
merch1.tampilkan_produk()
print()


print("=== DATA PESANAN ===")
pesanan1.tampilkan_pesanan()
print()

ProdukKpop.ubah_nama_toko("Weverse Store")

print("Nama toko:", ProdukKpop.nama_toko)

Pesanan.ubah_status_default("Diproses")

print("Status default:", Pesanan.status_default)
print()

print(
    "Validasi harga 350000:",
    ProdukKpop.validasi_harga(350000)
)

print(
    "Validasi jumlah 2:",
    Pesanan.validasi_jumlah(2)
)

print()

print("Stok album sebelum diubah:", album1.stok)

album1.stok = 15

print("Stok album setelah diubah:", album1.stok)

try:
    album1.stok = 0
except ValueError as e:
    print("Error:", e)

print()

album1.ubah_harga(375000)

print("Harga album setelah update:", album1.harga)

print()

print("=== SEMUA PRODUK ===")

daftar_produk = [
    produk1,
    produk2,
    album1,
    album2,
    merch1,
    merch2
]

for produk in daftar_produk:
    print(produk.namaProduk, "-", produk.harga)

print()

print("=== DELETE PRODUK ===")

daftar_produk.remove(produk2)

print("Produk setelah dihapus:")

for produk in daftar_produk:
    print(produk.namaProduk)

print()

print("Total produk :", ProdukKpop.total_produk)
print("Total pesanan:", Pesanan.total_pesanan)