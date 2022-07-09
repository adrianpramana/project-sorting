# <++++++++++++++++++++++++++++++++++++++++++++>
# *Nama Kelompok:
# *1. I Komang Hari Sulaksana Putra (20101171)
# *2. I Made Adrian Astalina Pramana (20101282)
# *3. I Made Agus Ari Subawa (21101108)
# *Kelas: AC
# <++++++++++++++++++++++++++++++++++++++++++++>
# * Source: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
# <|================>
# <|Program Sorting|>
# <|================>


class Sorting:
    # * Selection Sort
    # * Def mendefenisikan sebuah fungsi atau method.
    # ** Algoritma selection sort, sesuai dengan namanya (select = pilih), merupakan teknik pengurutan yang dilakukan dengan memilih nilai terbesar/terkecil dari sekumpulan nilai kemudian meletakkannya pada posisi ujung kumpulan nilai tersebut.
    # Membuat Constructor berupa parameternya untuk menampung pos berupa connector.
    def selection_sort(self, angka):
        # Melakukan perulangan dengan panjang dan jangkauan (scope) yang ditampung melalui variabel angka, yang mana nilai maksimum di set 0 sebagai nilai default dalam indeks.
        for pos_tujuan in range(len(angka)-1, 0, -1):
            pos_max = 0
            for x in range(1, pos_tujuan+1):
                max_sementara = angka[pos_max]
                if max_sementara < angka[x]:
                    pos_max = x
            angka[pos_max], angka[pos_tujuan] = angka[pos_tujuan], angka[pos_max]
            print("Proses Selection", angka)
            print()
        # Mengembalikan nilai berupa hasil block event list yang telah didefinisikan dan akan ditampilkan dalam console log seperti terminal / command prompt.
        return angka

    # *Bubble Sort
    # ** Algoritma bubble sort merupakan salah satu teknik pengurutan sederhana, yang dilakukan dengan menelusuri sebuah list, membandingkan elemen yang berdekatan, kemudian menukarnya apabila posisinya tidak tepat.
    # Membuat Constructor metode bubble sort, yang terdiri dari 2 parameter.
    def bubble_sort(self, angka):
        # Melakukan perulangan dengan fungsi range dan menghitung lenght dari variabel angka dengan valuenya.
        for pos_tujuan in range(len(angka)-1, 1, -1):
            for pos_sekarang in range(pos_tujuan):
                # Pengkondisian jika statement pos > angka, maka akan menghasilkan increment (syntatix sugar) berupa value yang telah diinisialisasikan.
                if angka[pos_sekarang] > angka[pos_sekarang+1]:
                    angka[pos_sekarang], angka[pos_sekarang +
                                               1] = angka[pos_sekarang+1], angka[pos_sekarang]
            print("Proses Bubble", angka)
            print()

    # *Merge Sort
    # ** Algoritma Merge sort merupakan pengurutan dengan cara menggabungkan. Sesuai dengan namanya, algoritma pengurutan merge sort melibatkan penggabungan secara berulang-ulang hingga membentuk rangkaian nilai yang terurut.
    # Membuat Constructor merge sort yang terdiri dari 2 parameter
    def merge_sort(self, list_bilangan):
        # Mendeklarasikan variabel kemudian di assign ke fungsi len untuk menampilkan panjang dari variabel yang diberikan expression.
        jumlah_bilangan = len(list_bilangan)
        # Melakukan pengkondsian terhadap variabel jumlah bilangan, kemudian dilakukan fungsi operator assignment dalam conditional statement
        if jumlah_bilangan > 1:
            posisi_tengah = len(list_bilangan)//2
            potongan_kiri = list_bilangan[:posisi_tengah]
            potongan_kanan = list_bilangan[posisi_tengah:]
            # Melakukan penggabungan di sisi kiri
            self.merge_sort(potongan_kiri)
            # Melakukan penggabungan di sisi kanan.
            self.merge_sort(potongan_kanan)
            # Hasil definisi dari object self.mergesort()
            jumlah_bilangan_kiri = len(potongan_kiri)
            jumlah_bilangan_kanan = len(potongan_kanan)
            c_all, c_kiri, c_kanan = 0, 0, 0  # Pencacah / Counter
            # Melakukan perulangan dengan membandingkan counter sebelah kiri dengan sebelah kanan lebih besar / kecil dari jumlah bilangan.
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

    # *Quick Sort
    # ** Algoritma quick sort adalah algoritma pengurutan yang menggunakan proses pemisahan (partitioning) berdasarkan suatu nilai pembatas (pivot) secara berulang-ulang hingga suatu untaian nilai menjadi terurut.
    # Membuat Constructor partition untuk menampung 4 parameter yang berfungsi sebagai blueprint (prototype dalam fungsi quick sort)
    def partition(self, l, bawah, atas):
        pivot = l[bawah]  # Bilangan pertama pada list sebagai pivot
        print("Bilangan Pivot: ", pivot)
        # Posisi yang akan menjadi batas partisi (di akhir fungsi akan menjadi posisi untuk pivot)
        pos_batas = bawah+1

        # Looping dari index ke 1 (Bilangan di kanan posisi awal pivot) ke seluruh elemen list.
        for j in range(bawah+1, atas):
            print()
            print("List Saat Ini: ", l)
            print("Periksa elemen pada indeks {} dengan posisi indeks pembatas {}".format(
                j, pos_batas))
            # Membandingkan nilai elemen yang diperiksa dengan pivot
            if l[j] < pivot:
                print(
                    "Elemen yang diperiksa lebih kecil dari pivot, lakukan pertukaran nilai dan naikan indeks pembatas")
                # Menukar nilai pada posisi pembatas nilai elemen yang diperiksa.
                l[pos_batas], l[j] = l[j], l[pos_batas]
                # Menggeser posisi pembatas (pivot value) naik setingkat ke kanan.
                pos_batas += 1
                print("List Setelah Pertukaran: ", l)
            else:
                print(
                    "Elemen yang diperiksa lebih besar atau sama dengan pivot, lanjutkan ke indeks berikutnya")
        l[pos_batas-1], l[bawah] = l[bawah], l[pos_batas-1]
        return pos_batas
        # * Quick Sort menerapkan kategori divide & conquer secara rekursif.
        # *+ Partitioning dengan pivot yang dipilih dari awal elemen (angka n). Perlu diperhatikan bahwa setelah partitioning, seluruh angka yang lebih kecil dari m berpindah ke sisi kiri dan sebaliknya. Pada proses ini, tidak ada jaminan bahwa elemen di kanan maupun kiri pivot terurut (sorted).

    # * Child Class Quick Sort dari fungsi Partition dengan mewariskan parameter dari parent classnya. Konsep ini disebut pewarisan(Inheritance).
    # ** Menggunakan konsep rekursif yang berfungsi untuk pemanggilan partition atau untaian nilai secara terpisah dan ditetapkan sebagai pembatas (pivot).
    def quicksort(self, l, bawah, atas):
        # Jika seluruh elemen yang nilainya lebih kecil sama dengan dari pivot, maka pada sisi yang berlawanan dengan nilai lebih besar dari pivot akan mengeksekusi bilangan yang akan diurutkan.
        # Pengkondisian ini dilakukan berulang-ulang hingga hanya tersisa satu elemen untuk partition (pemisahan), yang tentunya sudah tidak diperlukan lagi
        if atas <= bawah:
            return
        # Proses Eksekusi bilangan yang diurutkan.
        q = self.partition(l, bawah, atas)
        self.quicksort(l, bawah, q-1)  # Untaian nilai sebelah kanan
        self.quicksort(l, q, atas)  # Untaian nilai sebelah kiri
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
                angka = [3, 2, 4, 1, 10, 9, 6]
                print("<+++++++++++++Algortima Selection Sort+++++++++++++>")
                print("Sebelum Sort: ", angka)
                self.selection_sort(angka)
                print("Setelah Sort: ", angka)
                x = input("")
            elif(pilihan == "2"):
                angka = [3, 2, 4, 1, 10, 9, 6]
                print("<+++++++++++++Algortima Bubble Sort+++++++++++++>")
                print("Sebelum Sort: ", angka)
                self.bubble_sort(angka)
                print("Setelah Sort: ", angka)
                x = input("")
            elif(pilihan == "3"):
                print("<+++++++++++++Algortima Merge Sort+++++++++++++>")
                angka = [6, 5, 3, 1, 8, 7, 2, 4]
                print("Sebelum Sort: ", angka)
                print()
                self.merge_sort(angka)
                print("Setelah Sort Penuh: ", angka)
                x = input("")
            elif(pilihan == "4"):
                print("<+++++++++++++Algortima Quick Sort+++++++++++++>")
                angka = [25, 42, 17, 34, 20, 10, 8, 39]
                print("Sebelum Sort: ", angka)
                self.quicksort(angka, 0, len(angka))
                print("Setelah Sort: ", angka)
                x = input("")
            else:
                # Jika pointer / navigator yang dicari tidak terdapat dalam console (terminal / CLI), maka akan dikeluarkan dalam program, yang merujuk pada path/directory komputer masing-masing.
                pilih = "n"
                print("<!---------List Menu Tidak Tersedia!---------!>")


# Melakukan operator assigement == , yang mana merupakan operator untuk mendefinisikan sama persis dari parameter yang digunakan, agar dapat menampilkan fungsi mainmenu dengan  struktur fungsi Sorting yang relevan.
if __name__ == "__main__":
    s = Sorting()
    s.mainmenu()
