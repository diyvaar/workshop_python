# Ringkasan Minggu Ke - 1
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## Bab 1 
Python lebih mudah digunakan dan tersedia di banyak sistem operasi, seperti Windows, macOS, dan Unix sehingga mampu menyelesaikan pekerjaan lebih cepat. Walaupun lebih mudah digunakan, python memberikan banyak penawaran seperti penyediaan struktur dan dukungan pada program besar, error-checking, high-level data types built in seperti flexible arrays dan dictionaries. Python is an interpreted language yang artinya dapat menghemat waktu pengguna karena tidak memerlukan kompilasi dan penautan. Penerjemah ini bersifat interaktif yang membuatnya mudah untuk digunakan terutama untuk bereksperimen melalui fitur bahasanya.

Kelebihan python dari bahasa pemrograman lainnya ialah penulisan program yang relatif lebih singkat, hal ini disebabkan karena high-level data types, pengelompokkan statement yang hanya melalui lekukan dan tidak diperlukannya deklarasi variable atau argument.

## Bab 2
Saat memulai program, tampilan prompt akan menyatakan versi dari python yang digunakan dan keterangan waktu. Ketika perintah dibaca oleh tty, penerjemah python berada pada mode interaktif. Mode ini ditandai dengan adanya three greater-than signs (>>>). Jika perintah terdiri dari lebih dari satu baris maka by default akan ditandai dengan awalan tanda tiga titik (…) atau continuation lines. Untuk mengakhiri program python pada prompt dapat dengan Ctrl + z atau menuliskan perintah quit().

By default, python source files are encoded in UTF-8. Walaupun kebanyakan karakter pada bahasa yang ada di dunia menggunakan pengkodean UTF-8, secara standar hanya menggunakan ASCII karakter untuk pengidentifikasi maka diperlukan konvensi yang harus diikuti untuk dapat menampilkan karakter. Hal tersebut tentu berdampak pada editor yang harus mampu mengenali suatu file apabila file tersebut encoded as UTF-8 dan mampu menggunakan font yang mendukung suma karakter dalam file.

## Bab 3
Numbers 

Penerjemah Python dapat berfungsi sebagai kalkulator sederhana yang mampu menyelesaikan operasi matematika sederhana. Sama halnya dengan bahasa pemrograman lainnya dimana operator terdiri dari +, -, * , / dan %. Operator pembagi atau division (/) akan mengembalikan nilai dengan tipe data float. Sedangkan, floor division akan mengembalikan nilai dengan tipe data integer. Operasi matematika dengan penggunaan jenis operator yang bermacam – macam akan secara otomatis mengembalikan nilai dengan tipe data float. Selain integer dan float, python juga supports tipe data lainnya, seperti decimal dan pecahan serta memiliki dukungan bawaan untuk bilangan kompleks. Contohnya, penggunaan akhiran j atau J pada suatu angka untuk menunjukkan bagian imajiner. Operator ** digunakan untuk menghitung pangkat, sedangkan '='  (equal sign) digunakan untuk menetapkan nilai pada variable.

Pada mode interaktif, last printed expression by default akan di set pada variable ‘_’. Hal ini dapat memudahkan pengguna khususnya yang menggunakan python as calculator.

Strings

Penggunaan tanda kutip satu dan tanda kutip ganda pada strings akan menghasilkan keluaran yang sama. Namun, jika pada suatu teks (string) menggunakan tanda kutip ganda maka perlu menggunakan tanda kutip satu pada awalan teks yang ada di dalam fungsi print(). 
- Tanda \n digunakan untuk membuat baris baru pada suatu string.
Untuk menghindari suatu string dengan tulisan yang sama dengan ‘\n’ sign maka dapat dengan menyisipkan ‘r’ sebelum kutipan string.
- Menggabungkan string dengan operator dengan operator ‘+’ dan ‘*’. Operator ‘+’ dapat digunakan untuk menggabungkan dua string terpisah, sedangkan ‘*’ dapat digunakan as repeated.
- Dua atau lebih string yang terpisah dengan tanda kutip masing – masing dan terletak bersampingan satu sama lain, secara otomatis akan digabungkan.
- Menggabungkan antara variable dan string dapat menggunakan operator ‘+’
- String dapat menjadi suatu index. Index dengan bilangan positif maka dimulai dari huruf yang berada di kiri, sedangkan index dengan bilangan ganjil dimulai dari huruf kanan.
- Fungsi len() akan mengembalikan jumlah huruf dari suatu string.

Lists

List berisi beberapa item dari tipe data yang berbeda, namun kebanyakan list berisi dengan tipe data yang sama. Sama halnya dengan string yang dapat indexed, begitu pula halnya dengan lists yang juga dapat indexed and sliced.
