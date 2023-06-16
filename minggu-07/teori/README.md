# Ringkasan Minggu Ke - 7
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## Bab. 9 Classes

kelas (classes) dalam Python:

* Kelas adalah struktur dasar untuk membuat objek dalam Python.
* Kelas memiliki atribut (variabel) dan metode (fungsi) yang terkait dengan objek.
* Atribut adalah variabel dalam kelas yang menyimpan informasi tentang objek.
* Metode adalah fungsi dalam kelas yang digunakan untuk memanipulasi atribut atau melakukan operasi lain pada objek. 
* Metode kelas adalah metode yang terikat dengan kelas itu sendiri, sedangkan metode statis adalah metode terkait dengan kelas secara umum.
* Pewarisan memungkinkan kelas baru untuk menggunakan dan memperluas fungsionalitas kelas yang sudah ada.
* Overriding memungkinkan kelas turunan untuk mengganti metode yang diwarisi dari kelas induk.
* Multiple inheritance memungkinkan kelas untuk diturunkan dari beberapa kelas.
* Polymorphism memungkinkan objek untuk memiliki banyak bentuk yang berbeda.

9.1 A Word About Names and Objects

Dalam Python, variabel merupakan nama yang digunakan untuk merujuk pada objek di dalam memori. Ketika kita membuat variabel, sebenarnya kita membuat referensi ke objek tersebut. Objek dalam Python dapat memiliki banyak nama yang merujuk pada mereka. Perubahan nilai objek yang dilakukan melalui satu variabel akan mempengaruhi semua variabel lain yang merujuk pada objek yang sama. 

9.2 Python Scopes and Namespaces

Namespaces adalah tempat di mana nama-nama unik disimpan untuk menghindari konflik. Setiap cakupan memiliki ruang nama terkait. Python akan mencari nama di dalam cakupan lokal terlebih dahulu, kemudian di dalam cakupan global jika tidak ditemukan.

9.2.1 Scopes and Namespaces Example

Contohnya ialah terdapat dua buah fungsi: "outer_function" dan "inner_function". Setiap fungsi memiliki variabel "x" yang didefinisikan di dalam cakupan lokalnya. Ketika "inner_function" mencoba mengakses variabel "x", Python akan mencari nilainya terlebih dahulu di dalam cakupan lokal fungsi tersebut. Jika tidak ditemukan, Python akan mencari di dalam cakupan lokal fungsi yang mengelilingi. Jika tetap tidak ditemukan, Python akan mencari di dalam cakupan global.

Dalam contoh ini, karena variabel "x" tidak ditemukan di dalam cakupan lokal "inner_function", Python mencari di dalam cakupan lokal "outer_function" dan menemukan variabel "x" yang telah didefinisikan di sana. Oleh karena itu, nilai variabel "x" yang diakses di dalam "inner_function" berasal dari cakupan lokal "outer_function".

Contoh ini memberikan pemahaman praktis tentang bagaimana Python mengorganisir cakupan dan ruang nama, serta bagaimana akses ke variabel ditentukan berdasarkan urutan pencarian dalam berbagai cakupan.

9.3 A First Look at Classes

9.3.1 Class Definition Syntax

Kelas didefinisikan dengan menggunakan kata kunci "class" diikuti dengan nama kelas yang diawali dengan huruf kapital. Setelah deklarasi kelas, blok kode yang mengikuti akan menjadi tubuh kelas. Tubuh kelas berisi atribut dan metode yang mendefinisikan perilaku dan karakteristik dari objek yang dibuat dari kelas tersebut. Atribut adalah variabel yang terkait dengan kelas dan menyimpan informasi tentang objek. Metode adalah fungsi yang terkait dengan kelas dan digunakan untuk melakukan operasi pada objek.

9.3.2 Class Objects 

Objek kelas adalah instansi dari sebuah kelas dan memiliki atribut serta metode yang terkait. Atribut adalah variabel yang terkait dengan objek kelas, sedangkan metode adalah fungsi yang terkait dengan objek tersebut. Atribut dan metode dapat diakses melalui objek kelas menggunakan notasi titik.

Setiap objek kelas memiliki ruang nama yang terpisah, tetapi mereka berbagi struktur dan perilaku yang ditentukan oleh kelas yang sama. Objek kelas dapat dibuat menggunakan sintaksis "nama_kelas()" dan konstruktor kelas, yang merupakan metode khusus, dipanggil saat objek kelas dibuat.

Konstruktor kelas dapat menginisialisasi atribut objek menggunakan argumen yang diteruskan saat pembuatan objek. Objek kelas juga dapat dihapus dari memori menggunakan pernyataan "del" atau ketika tidak lagi direferensikan oleh objek lain.

9.3.3 Instance Objects

Objek instansi adalah objek yang dibuat dari kelas dan mewakili kasus individu atau instansi khusus dari kelas tersebut. Setiap objek instansi memiliki atribut yang membedakannya dari objek instansi lain yang dibuat dari kelas yang sama.

Atribut objek instansi adalah variabel yang terkait dengan objek tersebut. Atribut dapat diakses dan dimodifikasi melalui objek instansi menggunakan notasi titik. Setiap objek instansi memiliki ruang nama terpisah yang menyimpan nilai unik untuk atributnya.

Ketika objek instansi dibuat, konstruktor kelas dipanggil untuk melakukan inisialisasi awal. Konstruktor kelas adalah metode khusus yang didefinisikan dalam kelas dengan nama "init". Dalam konstruktor, kita dapat menginisialisasi atribut objek instansi dengan nilai-nilai awal yang diberikan.

9.3.4 Method Objects 

Objek metode adalah objek yang mewakili metode yang terkait dengan sebuah kelas. Metode adalah fungsi yang didefinisikan dalam kelas dan digunakan untuk melakukan operasi pada objek yang dibuat dari kelas tersebut.

Ketika sebuah metode dipanggil, objek metode yang terkait dengan metode tersebut dibuat secara otomatis. Objek metode ini menyimpan referensi ke metode asli bersama dengan objek instansi yang memanggil metode.

Objek metode dapat disimpan dalam variabel dan digunakan untuk memanggil metode yang terkait. Ketika objek metode dipanggil, metode yang terkait dijalankan pada objek instansi yang telah ditentukan sebelumnya.

Objek metode juga dapat diteruskan sebagai argumen ke metode lain atau digunakan dalam ekspresi lambda. Dalam kasus ini, objek metode berfungsi sebagai objek fungsi yang dapat dipanggil.

9.3.5 Class and Instance Variables

ariabel kelas adalah variabel yang terkait dengan kelas itu sendiri, bukan dengan objek instansi yang dibuat dari kelas. Variabel kelas dapat diakses melalui kelas atau objek instansi dan berlaku untuk semua objek instansi yang dibuat dari kelas tersebut.

Variabel instansi adalah variabel yang terkait dengan objek instansi tertentu. Setiap objek instansi memiliki salinan terpisah dari variabel instansi, dan perubahan pada variabel instansi tidak mempengaruhi objek instansi lain.

Variabel kelas didefinisikan di dalam tubuh kelas, di luar metode kelas. Mereka dapat diakses melalui notasi titik menggunakan nama kelas atau objek instansi. Variabel kelas juga dapat diakses melalui metode kelas dan metode instansi.

Variabel instansi biasanya didefinisikan di dalam metode kelas, terutama dalam konstruktor kelas "init". Setiap objek instansi memiliki salinan terpisah dari variabel instansi tersebut.

9.4 Random Remarks

Metode dan atribut dalam kelas dapat diwarisi dan diubah oleh kelas turunan.

Keyword "super" digunakan untuk mengakses metode yang diwarisi dari kelas dasar saat mendefinisikan metode yang sama di kelas turunan.

Polimorfisme adalah kemampuan objek untuk memiliki banyak bentuk. Dalam Python, polimorfisme dapat dicapai melalui metode yang sama dengan perilaku yang berbeda pada kelas-kelas yang berbeda.

Metode "isinstance()" dan "issubclass()" digunakan untuk memeriksa hubungan antara objek dan kelas dalam hierarki pewarisan.

Encapsulation adalah konsep untuk menyembunyikan implementasi internal objek dan hanya memungkinkan akses melalui antarmuka publik.

Duck typing adalah prinsip dalam Python yang berfokus pada perilaku objek daripada tipe kelasnya. Jika objek bertindak seperti bebek dan berbunyi seperti bebek, maka dianggap sebagai bebek.

9.5 Inheritance

Warisan adalah konsep yang memungkinkan kelas untuk mewarisi atribut dan metode dari kelas lain yang disebut kelas dasar atau superclass. Kelas yang mewarisi atribut dan metode disebut kelas turunan atau subclass.

Dalam warisan, kelas turunan dapat menggunakan atribut dan metode yang sudah ada dalam kelas dasar tanpa perlu mendefinisikannya ulang. Ini memungkinkan untuk mengorganisir dan mengelompokkan kode secara hierarkis.

Konsep warisan juga mendukung konsep polimorfisme, di mana objek kelas turunan dapat digunakan sebagai objek kelas dasar. Hal ini memungkinkan fleksibilitas dalam penggunaan objek dan memungkinkan penggunaan pola desain seperti polimorfisme dan substitusi Liskov.

9.5.1 Multiple Inheritance

Multiple inheritance adalah konsep di mana sebuah kelas dapat mewarisi atribut dan metode dari lebih dari satu kelas dasar. Dalam hal ini, kelas turunan memiliki beberapa kelas dasar. Dalam Python, untuk menggunakan multiple inheritance, kita dapat menyebutkan beberapa kelas dasar dipisahkan oleh tanda koma setelah kata kunci "class". Kelas turunan akan mewarisi atribut dan metode dari semua kelas dasar yang diberikan.

9.6 Private Variables

Variabel pribadi adalah variabel yang dianggap bersifat pribadi dan seharusnya tidak diakses atau dimodifikasi langsung dari luar kelas. Variabel pribadi dimulai dengan garis bawah ganda (underscore) di awal namanya, seperti "_namaVariabel".

Variabel pribadi diimplementasikan menggunakan konvensi dan aturan tertentu, tetapi secara teknis masih dapat diakses dan dimodifikasi dari luar kelas. Namun, penggunaan garis bawah ganda menandakan bahwa variabel tersebut seharusnya digunakan secara pribadi dan tidak dianggap sebagai bagian publik antarmuka kelas.

9.7 Odds and Ends 

Menggunakan fungsi built-in "getattr()" untuk mengakses atribut atau metode dari objek secara dinamis.

Dalam Python, semua tipe data adalah objek, termasuk tipe data dasar seperti angka dan string.

Konstruktor kelas, "init()", dapat digunakan untuk melakukan inisialisasi saat objek instansi dibuat.

"self" digunakan dalam definisi metode kelas untuk mengacu pada objek instansi yang sedang dikerjakan.

Penerusan metode ("method delegation") adalah konsep yang memungkinkan objek delegasi untuk memanggil metode pada objek lain.

Konsep "getter" dan "setter" digunakan untuk mengakses dan memodifikasi atribut dengan cara yang terkontrol.

9.8 Iterators 

Iterator adalah objek yang digunakan untuk mengiterasi atau mengulang secara berurutan melalui elemen-elemen dari suatu koleksi atau struktur data. Iterasi adalah proses melalui elemen-elemen satu per satu.

Untuk mendukung iterasi, suatu objek harus mengimplementasikan dua metode khusus: "iter()" dan "next()". Metode "iter()" mengembalikan objek iterator itu sendiri, sementara metode "next()" mengembalikan elemen berikutnya dalam iterasi. Jika tidak ada elemen berikutnya, metode "next()" harus menghasilkan pengecualian StopIteration untuk menghentikan iterasi.

Iterasi dapat dilakukan menggunakan pernyataan "for" yang umum digunakan dalam Python. Pernyataan "for" akan secara otomatis memanggil metode "iter()" untuk mendapatkan iterator dan menggunakan metode "next()" untuk mendapatkan elemen-elemen selama iterasi.

9.9 Generators 

Generator adalah fungsi khusus yang menghasilkan serangkaian nilai secara bertahap, satu nilai pada satu waktu, tanpa harus menyimpan seluruh rangkaian nilai dalam memori. Generator memungkinkan kita untuk menghasilkan nilai-nilai secara efisien dalam situasi di mana menghasilkan seluruh rangkaian nilai sekaligus akan memakan banyak memori.

Untuk membuat generator, kita menggunakan kata kunci "yield" dalam fungsi. Ketika "yield" dieksekusi, generator akan menghasilkan nilai tersebut dan menyimpan keadaan internalnya. Pada pemanggilan berikutnya, generator akan melanjutkan dari keadaan terakhirnya dan menghasilkan nilai berikutnya.

9.10 Generator Expressions

Generator expression mirip dengan list comprehension, tetapi menggunakan tanda kurung () daripada tanda kurung siku []. Mereka memungkinkan kita untuk membuat generator secara langsung dalam satu baris kode, tanpa perlu mendefinisikan fungsi terpisah.

Dalam generator expression, kita menuliskan ekspresi yang menghasilkan nilai untuk setiap elemen dalam rangkaian yang diinginkan. Generator expression akan secara otomatis menghasilkan nilai-nilai ini satu per satu saat diminta, tanpa perlu menyimpan semua nilai dalam memori.


