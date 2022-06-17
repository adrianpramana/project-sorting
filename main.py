# Nama Kelompok


# Jurusan : TI-MTI

# Program Sorting

from heapq import merge


class Sorting:
    # Selection Sort
    def selection_sort(self, angka):
        for pos_tujuan in range(len(angka)-1, 0, -1):
            pos_max = 0
            for x in range(1, pos_tujuan+1):
                max_sementara = angka[pos_max]
                if max_sementara < angka[x]:
                    pos_max = x
            angka[pos_max], angka[pos_tujuan] = angka[pos_tujuan], angka[pos_max]
        return angka

    # Bubble Sort
    def bubble_sort(self, angka):
        for pos_tujuan in range(len(angka)-1, 1, -1):
            for pos_sekarang in range(pos_tujuan):
                if angka[pos_sekarang] > angka[pos_sekarang+1]:
                    angka[pos_sekarang], angka[pos_sekarang +
                                               1] = angka[pos_sekarang+1], angka[pos_sekarang]

    # Merge Sort
    def merge_sort(self, list_bilangan):
        jumlah_bilangan = len(list_bilangan)
        if jumlah_bilangan > 1:
            posisi_tengah = len(list_bilangan)//2
            potongan_kiri = list_bilangan[:posisi_tengah]
            potongan_kanan = list_bilangan[posisi_tengah:]
            self.merge_sort(potongan_kiri)
            self.merge_sort(potongan_kanan)
            jumlah_bilangan_kiri = len(potongan_kiri)
            jumlah_bilangan_kanan = len(potongan_kanan)
            c_all, c_kiri, c_kanan = 0, 0, 0  # Pencacah / Counter
            while c_kiri < jumlah_bilangan_kiri or c_kanan < jumlah_bilangan_kanan:
                if c_kiri == jumlah_bilangan_kiri:  # Jika elemen di potongan kiri habis
                    list_bilangan[c_all] = potongan_kanan[c_kanan]
                    c_kanan = c_kanan + 1
                elif c_kanan == jumlah_bilangan_kanan:  # Jika elemen di potongan kanan habis
                    list_bilangan[c_all] = potongan_kiri[c_kiri]
                    c_kiri = c_kiri + 1
                # Nilai elemen di potongan kiri lebih kecil
                elif potongan_kiri[c_kiri] <= potongan_kanan[c_kanan]:
                    list_bilangan[c_all] = potongan_kiri[c_kiri]
                    c_kiri = c_kiri + 1
                else:  # Nilai  elemen di potongan kanan lebih besar
                    list_bilangan[c_all] = potongan_kanan[c_kanan]
                    c_kanan = c_kanan + 1
                c_all = c_all + 1
            print('Proses Merge:', list_bilangan)
            print()

    # Quick Sort
    def partition(self, l, bawah, atas):
        pivot = l[bawah]  # Bilangan pertama pada list sebagai pivot
        # Posisi yang akan menjadi batas partisi (di akhir fungsi akan menjadi posisi untuk pivot)
        pos_batas = bawah+1

        # Looping dari index ke 1 (Bilangan di kanan posisi awal pivot) ke seluruh elemen list.
        for j in range(bawah+1, atas):
            # Membandingkan nilai elemen yang diperiksa dengan pivot
            if l[j] < pivot:
                # Menukar nilai pada posisi pembatas nilai elemen yang diperiksa.
                l[pos_batas], l[j] = l[j], l[pos_batas]
                # Menggeser posisi pembatas (pivot value) naik setingkat ke kanan.
                pos_batas += 1
        l[pos_batas-1], l[bawah] = l[bawah], l[pos_batas-1]
        return pos_batas

        # Menggunakan konsep rekursif yang berfungsi untuk pemanggilan parttition atau untaian nilai secara terpisah dan ditetapkan sebagai pembatas (pivot).
    def quicksort(self, l, bawah, atas):
        # Jika seluruh elemen yang nilainya lebih kecil sama dengan dari pivot, maka pada sisi yang berlawanan dengan nilai lebih besar dari pivot akan mengeksekusi bilangan yang akan diurutkan.
        if atas <= bawah:
            return
        q = self.partition(l, bawah, atas)
        self.quicksort(l, bawah, q-1)
        self.quicksort(l, q, atas)
        return l

    # Menu dari Aplikasi Sorting
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            print("=========================")
            print("| Menu Aplikasi Sorting |")
            print("|_______________________|")
            print("| 1. Selection Sort     |")
            print("| 2. Bubble Sort        |")
            print("| 3. Merge Sort         |")
            print("| 4. Quick Sort         |")
            print("=========================")
            pilihan = str(input(("Silahkan masukan pilihan algoritma Anda: ")))
            if(pilihan == "1"):
                angka = [15, 16, 2, 97, 100, 78, 25, 10, 1, 17]
                print("**********Algortima Selection Sort********")
                print("Sebelum Sort: ", angka)
                self.selection_sort(angka)
                print("Setelah Sort: ", angka)
                x = input("")
            elif(pilihan == "2"):
                angka = [35, 24, 49, 30, 17, 37, 12, 22, 58, 36, 29, 23]
                print("**********Algortima Bubble Sort********")
                print("Sebelum Sort: ", angka)
                self.bubble_sort(angka)
                print("Setelah Sort: ", angka)
                x = input("")
            elif(pilihan == "3"):
                print("**********Algortima Merge Sort********")
                angka = [6, 5, 3, 1, 8, 7, 2, 4]
                print("Sebelum Sort: ", angka)
                print()
                self.merge_sort(angka)
                print("Setelah Sort Penuh: ", angka)
                x = input("")
            elif(pilihan == "4"):
                print("**********Algortima Quick Sort********")
                angka = [34, 21, 45, 32, 12, 31, 19, 23, 54, 31, 25, 27]
                print("Sebelum Sort: ", angka)
                self.quicksort(angka, 0, len(angka))
                print("Setelah Sort: ", angka)
                x = input("")
            else:
                pilih = "n"


if __name__ == "__main__":
    s = Sorting()
    s.mainmenu()
