# Ringkasan Minggu Ke - 3
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## Bab. 5 Data Structure
5.1 More and Lists

* list.append(x) ; menambahkan sebuah item dalam sebuah list dan diletakkan pada urutan akhir
* list.extend(iterable) ; memperpanjang list dengan menambahkan semua item dari iterable
* list.insert(i, x) ; digunakan untuk menyisipkan item pada posisi tertentu. Argument pertama digunakan untuk mendefinisikan letak untuk item disisipkan. Sedangkan, argument kedua ialah value yang akan disisipkan
*	list.remove(x) ; remove item pertama dari list
*	list.pop([i]) ; remove item pada posisi tertentu pada list
*	list.clear() ; remove seluruh item pada list
*	list.index() ; return index of x
*	list.count() ; digunakan untuk menghitung jumlah x dari suatu list
*	list.sort() ; mengurutkan item – item pada list
*	list.reverse() ; digunakan untuk membalikkan urutan item pada list

5.1.1 Using Lists as Stacks

Menggunakan metode list dapat lebih mudah apabila menggunakan list as a stack, dimana item / element yang ditambahkan pada urutan terakhir maka akan diambil / dihapus pertama.

5.1.2 Using List as Queues

Metode list juga dapat diimplementasikan sebagai list as queue, dimana element pertama yang ditambahkan akan menjadi elemen pertama pula apabila diambil / dihapus.

5.1.3 List Comprehensions

List comprehensions menyediakan cara ringkas untuk membuat list. Aplikasi pada umumnya membuat sebuah list baru ketika setiap elemen akan memiliki hasil dari suatu operasi dan diterapkan pada setiap anggota elemen lainnya atau iterable.

5.1.4 Nested List Comprehensions

Nested List Comprehensions secara konsep hampir serupa seperti list comprehensions perbedaanya terletak pada implementasinya yang digunakan lebih besar dan luas.

5.2 The del statement

Del statement digunakan untuk menghapus items / element yang ada pada list by index, slice, atau keseluruhan list. Hal ini berkebalikan dari pop() yang menggunakan value sebagai parameter.

5.3 Tuple and Sequnce

Python memiliki tipe data urutan yakni lists dan tuples. Perbedaan keduanya adalah list bersifat dapat berubah dan homogen, sedangkan tuples tidak dapat berubah dan hetergoen. Tuple memiliki syntax khusus untuk membuat tuple kosong atau sebuah item tunggal. 

5.4 Sets

Set adalah kumpulan elemen yang yang tidak berurutan dan tidak memiliki elemen duplikat. Set juga didukung dengan operasi matematika seperti union, intersect, difference dan symmetric difference. Fungsi set() dapat digunakan untuk membuat set itu sendiri. 

5.5 Dictionary

Python memiliki data type dictionary. Tidak seperti sequence yang index nya berupa angka, dictionaries memiliki index by keys. Keys dapat berupa string, number atau tuple. Khusus tuple, tuple dapat menjadi keys apabila didalamnya hanya terdapat string, number atau tuple. List tidak dapat dijadikan sebagai keys.  Dapat dikatakan bahwa dictionary merupakan kumpulan dari key : value pairs, dengan syarat bahwa keys bersifat unique. 

5.6 Looping Techniques

*	looping melalui dictionaries, key and value dapat dikembalikan (ditampilkan) dalam waktu yang sama menggunakan metode items(). Metode items rerurn view object berupa pasangan key-value.
*	looping melalui sequence, position index and value can be return at the same time dengan metode enumerate(). Metode ini akan mengembalikan value beserta index posisinya .
*	looping lebih dari 2 sequence dapat menggunakan metode zip().
*	looping sequence secara terbalik dapat dengan menggunakan metode reversed()
*	looping sequence secara berurut dapat dengan menggunakan metode sorted(). Adapun untuk menghapus duplikat elements dapat dengan diiringi penggunaan metode set().

5.7 More on Conditions

Dalam penggunaan while dan if statements dapat dengan menyisipkan operator. Operator yang digunakan tidak hanya operator perbandingan. Operator ‘in’ dan ‘not in’ membandingkan dua objek yang keduanya objek yang sama. Semua operator perbandingan memiliki prioritas yang sama. Operator perbandingan dapat dikombinasikan dengan operator Boolean seperti ‘and’ dan ‘or’. Operator ‘and’ dan ‘or’ dapat juga berupa negative dengan tambahan operator ‘not’. Dalam hal ini, terdapat perbedaan prioritas penyelesaian. Operator ‘not’ memiliki priotitas tertinggi dan ‘or’ prioritas terbawah. Sehingga apabila dalam suatu operasi dengan penggunaan operator Boolean maka selesaikan operasi pada ‘not’. 

5.8 Comparing Sequence and Other Types

Sequence object dapat dibandingkan dengan object lainnya dengan tipe sequence yang sama. Sequence object will be compare using lexicographical ordering. Perbandingan akan dilakukan elemen demi elemen, dan akan dilakukan secara rekursif jika diperlukan hingga selisih atau perbedaan ditemukan atau sequence lainnya kehilangan elemen. 

