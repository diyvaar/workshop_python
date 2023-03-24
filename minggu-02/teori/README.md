# Ringkasan Minggu Ke - 2
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## Bab 4. More Control Flow Tools
4.1 if statements

If merupakan satu diantara statement yang paling banyak dikenal. Pada if statement, terdapat pula elif dan else sebagai other optional Elif merupakan singkatan dari ‘else if’ dan digunakan serupa dengan if. Umumnya, urutan dari penggunaan if statements ialah, if… elif…else.

4.2 for statements

For statements dimiliki oleh bahasa pemrograman lainnya seperti C atau Pascal, namun pada python, for statements digunakan dengan lebih mudah. 

4.3 range() function

Fungsi range() yang merupakan fungsi bawaan dari python berguna untuk memudahkan user khususnya dalam mengulangi urutan angka. Fungsi range() dapat berisi beberapa argument dan argument tersebut berupa angka dan dimulai dari 0. Contoh range(5) maka urutan angkanya ialah 0, 1, 2, 3, 4. Range() dengan 2 argumen, artinya argument 1 merupakan start num dan argument 2 merupakan end num. Sedangkan, range() dengan 3 argumen, artinya argument 1 start num, argument 2 end num, dan argument 3 adalah jarak dari urutan angka. Tidak jarang fungsi range() digunakan secara bersamaan dengan fungsi len(). Fungsi len() digunakan untuk menghitung jumlah dari suatu variable.
Umumnya, return value dari range() seperti list, namun sebenarnya return value dari range() adalah item yang dikembalikan secara terurut dari urutan yang diinginkan.

4.4 break dan continue statement, dan else clauses on loops

Break statement umumnya digunakan pada kasus looping bersarang, dimana break statement digunakan pada looping terdalam. Sama halnya, dengan break statement, else clause juga umumnya digunakan pada kasus looping for bersarang. Else clauses dieksekusi ketika loop berada pada kondisi salah (false) looping. Pada kasus looping, ketika program dijalankan dan mengeksekusi break statement maka berada pada kondisi true, sedangkan else, dieksekusi ketika berada pada kondisi false. 
Sedangkan, continue statement, jika pada kasus looping bersarang, apabila program pada suatu seleksi baik if / switch, dan menggunakan continue statements, maka program akan terus berlanjut. Hal ini berbanding terbalik dengan break statement.

4.5 pass statement

Pas statement tidak menghasilkan apa – apa. Statement ini digunakan ketika suatu pernyataan membutuhkan sintaksis namun pada program tidak memerlukan aksi apapun.

4.6 match statement

Match statement memiliki cara kerja dengan mengambil ekspresi dan membandingkannya kepada beberapa pola secara berurutan. Match statement umumnya mirip dengan pernyataan switch pada bahasa pemrograman C atau Java. Pada contoh program, case ‘-‘, akan bertindak apabila tidak ada ekspresi yang cocok pada pola – pola sebelumnya. ‘or’ ( | ) berperan sebagai ‘atau’ dan dapat digunakan apabila mengkombinasikan beberapa pola.
Match statement dapat digunakan :
-	Dengan class struktur data. Class diikuti dengan argument yang menyerupai konsttuktor namun dengan kemampuan untuk menangkap atribut ke dalam suatu variable.
-	Dengan parameter posisi dengan kelas bawaan yang menyediakan pengurutan untuk atributnya. 
-	Dengan menambahkan if clause pada pola yang dikenal sebagai ‘guard’ (penjaga). Apabila ‘guard’ bernilai salah, maka baris ekspresi match akan bergerak pada blok case pola selanjutnya.

4.7 defining functions

Kata kunci ‘def’ digunakan untuk mendefinisikan suatu fungsi. ‘def’ harus diikuti dengan nama fungsi dan parameternya yang dikurung. Pernyataan yang merupakan isi dari suatu fungsi, ditulis pada baris selanjutnya dan diber identasi. Statement pertama dari fungsi itu sendiri dapat secara optional berisi function’s document string atau docstring. Eksekusi pada fungsi akan memperkenalkan tabel symbol baru yang digunakan untuk variable local dari fungsi tersebut. 
-	Semua penugasan variable dalam suatu fungsi menyimpan nilai dalam tabel symbol local
-	Variable global dan variable fungsi terlampir tidak dapat secara langsung diberi nilai dalam suatu fungsi. Terkecuali apabila, variable global disebutkan pada pernyataan global, dan variable fungsi disebutkan dalam pernyataan local.
Parameter actual (argument) digunakan untuk pemanggilan fungsi diperkenalkan di tabel symbol local. Argument diteruskan menggunakan panggilan berdasarkan nilai. Ketika suatu fungsi memanggil fungsi lain / dirinya sendiri secara rekursif, tabel symbol local baru akan dibuat untuk panggilan. 
Return statement akan mengembalikan sebuah nilai dari sutau fungsi. Return tanpa sebuah argument ekspresi akan mengembalikan ‘none’.

4.8 More on defining functions

4.8.1 Default argument values

Bentuk yang paling sering digunakan pada fungsi ialah penentuan nilai default untuk satu atau beberapa argument.

4.8.2 Keyword Arguments

Suatu fungsi juga dapat dipanggil dengan menggunakan keyword arguments dari suatu bentuk fungsi. Dalam hal ini, suatu fungsi dapat dipanggil dengan required argument dan optional argument.

4.8.3 Special parameters

By default¸argumen dapat diteruskan ke fungsi python baik dengan posisi maupun secara eksplisit dengan keyword. Untuk keterbacaan dan kinerja, maka pengembang membatasi cara argument untuk dapat diteruskan ke fungsi dengan melihat definisi dari fungsi untuk menentukan apakah argument diteruskan by keyword or position.

4.8.3.1 Positional-or-keyword arguments

Symbol / dan * digunakan secara optional. Jika digunakan, symbol tersebut akan mengindikasikan jenis dari parameter dengan mengetahui argument apa yang akan diteruskan kepada fungsi. Symbol tersebut dapat dikatakan semacam penanda, bagiaman suatu argument dapat diteruskan apakah melalui posisi, posisi atau kata kunci, atau kata kunci. Jika kedua symbol tersebut tidak digunakan, maka argument akan diteruskan melalui posisi atau katakunci.

4.8.3.2 Positional-only-parameters

Jika dilihat lebih rinci, memungkinkan untuk melabeli suatu parameter dengan ‘positional only’. Jika ‘position only’ maka urutan parameter sanagt penting dan parameter tidak dapat diteruskan by keyword. Positional only parameter diletakkan sebelum garis miring (/) dan (/) garis miring digunakan sebagai penanda parameter positional-only.

4.8.3.3 Keyword only arguments

Untuk mengindikasikan suatu parameter ‘keyword only’ dapat dengan menempatkan symbol * pada parameter.

4.8.3.4 function examples

Parameter tanpa symbol yang mengindikasikan metode penerusan ke fungsi maka dapat diteruskan dengan posisi atau kata kunci. 

argument :'standard_arg⁡(2)' atau

argument : 'standard_arg⁡(arg=2)'

Parameter dengan symbol ‘/’ maka argument diteruskan dengan posisi. Contoh :

argument : 'pos_only_arg⁡(1)'

Parameter dengan symbol ‘*’ maka argument diteruskan dengan keyword

argument : 'kwd_only_arg⁡(arg=3)'

4.8.3.5

Use case will determina which parameters to use in the function definition :

- Gunakan positional-only jika nama dari parameter tidak tersedia ke pengguna. Hal ini membantu ketika nama parameter tidak memiliki makna.

- Gunakan keyword-only ketika nama parameter memiliki makna atau peranan dan ketika dapat mempermudah mendefinisikan fungsi 

- Untuk API, gunakan positional-only untuk mencegah kerusakan pada API apabila nama dari parameter berubah di masa mendatang

4.8.4 Arbitary argument lists

Suatu fungsi dapat dipanggil dengan jumlah argument yang berubah – ubah. Argument ini dibungkus dalam sebuah tuple. Argument setelah symbol ‘*’ adalah keyword only argument.

4.8.5 Unpacking argument lists

Sebaliknya dari arbitrary argument list, jenis unpacking arguments list tidak dibungkus oleh tuple sehingga perlu dibongkar untuk pemanggilan fungsi dan memerlukan argument pemisah. Jika argument tidak tersedia secara terpisah, maka perlunya pemanggilan fungsi dengan menambahkan symbol ‘*’ pada argument untuk membongkar agumen dari tuple.

4.8.6 Lambda expressions

Lambda expressions dapat digunakan untuk sebuah fungsi kecil, dimana lambda akan mengembalikan jumlah dari 2 arguments. Lambda dapat digunakan dimanapun objek fungsi diperlukan.

4.8.7 Documentation Strings

Berikut adalah beberapa konvensi tentang konten dan format dari documentation strings.

Baris pertama berupa ringkasan singkat, ringkas dari tujuan objek dan tidak boleh secara eksplisit menyatakan nama atau jenis objek. Penulisan harus dimulai dengan huruf kapital dan diakhiri titik.

Jika > 1 baris, baris kedua harus kosong, untuk memisahkan ringkasan dari deskripsi lainnta. Baris setelahnya, harus berupa 1 atau lebih paragraph dan menjelaskan konvensi pemanggilan objek, efek samping, dll.

4.8.8 Function annotations

Annotations function adalah informasi metadata yang sepenuhnya opsional, seperti mengenai jenis yang digunakan oleh fungsi. Annotations disimpan dalam atribut __annotations__ dari fungsi sebagai kamus dan tidak mempengaruhi bagian lain dari fungsi tersebut. Parameter  ditentukan oleh tanda titik dua setelah nama parameter dan diikuti dengan ekspresi.

4.9.9 Intermezzo: coding style

Python PEP 8 telah merilis penduan style yang diikuti oleh kebanyakan project dengan klaimnya yang mudah dibaca dan lebih menyenangkan mata.

- Menggunakan 4 spasi tanpa tab

- Membungkus baris tanpa melibih 79 karakter. Hal ini membantu pengguna denga tampilan kecil dan membantu membuat tampilan lebih besar dengan kode yang berdampingan

- Baris kosong untuk memisahkan fungsi dan kelas, dan blok kode yang lebih besar pada fungsi

- Menyantumkan komentar pada baris

- Menggunakan docstring
- Menggunakan spasi di sekitar operator dan setelah koma, terkecuali pada tanda kurung
- Memberi nama kelas dan fungsi secara konsisten. Huruf kapital untuk kelas dan huruf kecil serta garis bawah untuk fungsi
- Jangan menggunakan fancy encodings jika kode dimaksudkan untuk digunakan di lingkungan yang luas, eg internasional. Gunakan UTF-8 atau ASCII lebih baik.
- Hindari penggunaan karakter non-ASCII dalam pengidentifikasi jika hanya sedikit kemungkinan orang dengan bahasa berbeda akan membaca
