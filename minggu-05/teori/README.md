# Ringkasan Minggu Ke - 5
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## Bab. 7 Input and Output 

7.1 Fancier Output Formatting

Sejauh ini, kita telah mengetahui cara bagaimana _writing values_ : _expressions statements_ dan melalui fungsi print(). Cara Ketiga ialah dengan menggunakan write() methods. 

* menggunakan f atau F sebelum string dan menggunakan _expressions_ { dan } untuk menuliskan variable yang akan digunakan sebagai rujukan dari string. Dengan mendefinisikan suatu variable nama dan value nya. Kemudian membuat string dan akan menampilkan nama yang ada pada variable tersebut, maka dapat menggunakan ekspresi {} yang didalamnya tertulis variable nama. Maka secara otomatis ketika di run, maka akan menampilkan string tersebut beserta value dari variable nama.
* str.format() ; penggunaan metode ini tetap mengharuskan penulis untuk menggunakan {} sebagai penanda dimana variable akan di subtitusi.
* str() ; fungsi yang dimaksudkan untuk _return representations_ dari sebuah nilai dari suatu variable yang sederhana untuk dibaca
* repr() ; fungsi yang dimaksudkan untuk _generate representations_ yang bisa dibaca oleh penerjemah
* % _used for string formatting_ ; % digunakan untuk mengatur formatting pada string terkhusus apabila mengarah pada penyisipan numeric seperti penggunaan package math. contoh "'... %5.3f.'% math.pi" artinya akan menyisipkan sebuah nilai numerik pi pada string dengan format nilai pi terdiri dari 5 angka dengan 3 buah angka desimal.

7.2 Reading and Writing Files

Penggunaan open() yang digunakan untuk membuka sebuah file object. Pada umumnya penggunaan fungsi open() diiringi dengan dua buah argumen lainnya yaitu 'mode' dan 'encoding'. Contoh : **open('workfile', 'w', encoding="utf-8")**

Argumen pertama ialah nama file yang akan dibuka. Argumen kedua, ialah mode yang value nya merupakan karakter yang mendeskripsikan alasan mengapa menggunakan file tersebut. Mode yang tersedia di antaranya ialah 'r' = only read, 'w' = only writing, 'a' = opens, r++ = 'reading and writing'. Argumen ketiga, ialah text mode. Secara umum file akan berada pada text mode dengan encoding 'UTF-8', namun apabila file merupakan binary mode maka tambahkan kata kunci'b'. Binary mode ialah data yang dibaca dan ditulis dengan _bytes objects_.
