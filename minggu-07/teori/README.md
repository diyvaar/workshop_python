# Ringkasan Minggu Ke - 8
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## Bab. 10 Brief Tour of the Standard Library

10.1 Operating System Interface

Modul os menyediakan banyak fungsi untuk dapat berinteraksi dengan sistem operasi. Pastikan menggunakannya dengan 'import os'. Fungsi dir() dan help() sangat bermanfaat sebagai alat bantu interaktif untuk bekerja dengan modul yang banyak. Untuk file dan direktori sehari - hari, 'shutil' menyediakan antar muka tertinggi sehingga lebih mudah digunakan.

10.2 File Wildcards 

Modul glob menyediakan sebuah fungsi yang digunakan untuk membuat daftar file dari sebuah pencarian wildcard direktori.

10.3 Command Line Arguments

Modul argparse menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. 

10.4 Error Output Redirection and Programming Termination

Modul sys memiliki atribut stdin, stdout, stderr. Stderr digunakan untuk memancarkan peringatan dan pesan kesalahan agar terlihat ketika stdout telah dialihkan.

10.5 String Pattern Machine

Modul re menyediakan tools ekspresi pada umumnya untuk pemrosesan string tingkat lanjut.

10.6 Mathematics

Modul math memberikan akses ke fungsi library C sebagai dasar untuk matematika floating point. Modul random menyediakan tools untuk membuat pilihan acak. Modul Statistik digunakan untuk menghitung properti statistik dasar (rata - rata, median, varians, dll) dari data numerik.

10.7 Internet Access

Umumnya terdapat beberapa modul yang digunakan untuk mengakses internet dan memproses protokol internet. Dua diantaranya yang paling sederhana ialah urlib.request untuk mengambil data dari URL dan smtplib untuk mengirim email.

10.8 Dates and Times

Modul datetime menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara sederhana dan kompleks. Dan mendukung date and time arithmetic. Fokus penerapannya ialah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi output. 

10.9 Data Compression

Beberapa format data pada umumnya yang didukung oleh modul untuk archive dan compress ialah zlib, gzip, bz2, lzma, zipfile dan tarfile.

10.10 Performance Measurement

Modul timeit akan dengan cepat menunjukkan keunggulan kinerja sederhana.

10.11 Quality Control 

Modul doctest menyediakan tool untuk scanning sebuah modul dan memvalidasi test untuk setiap fungsi yang dibangun dan dijalankan setiap proses development.

## BAB. 11 Brief Tour of the Standard Library 

11.1 Output Formatting
Bagian 11.1 dari tutorial modul standar library Python membahas pemformatan output. Modul "string" dan "reprlib" digunakan untuk mengontrol format tampilan objek dan teks yang dihasilkan.

Modul "string" menyediakan berbagai metode untuk memanipulasi dan memformat string, seperti "string.format()" untuk menggabungkan nilai ke dalam string format, dan "string.Template()" untuk penggantian string berbasis placeholder.

Modul "reprlib" digunakan untuk menghasilkan representasi terbatas dari objek kompleks, yang berguna untuk menghindari keluaran yang terlalu panjang atau berulang.

11.2 Templating

Modul "string" dan "template" digunakan untuk membuat dan mengelola templat string. Modul "string" menyediakan metode-metode untuk memanipulasi dan memformat string, sedangkan modul "template" menyediakan kelas "Template" yang memungkinkan pembuatan templat string dengan placeholder yang dapat digantikan.

Pemanfaatan templating memudahkan pembuatan teks yang dinamis, seperti pembuatan pesan atau email, penghasilan kode, atau pembuatan dokumen yang terstruktur.

11.3 Working with Binary Data Record Layouts

Modul "struct" digunakan untuk membaca, menulis, dan memanipulasi data dalam format biner. Modul "struct" menyediakan fungsi-fungsi untuk mengonversi data antara representasi biner dan representasi Python yang dapat dioperasikan.

Modul "struct" dapat membaca data dari file biner, memanipulasi data biner, dan menulis data ke file biner sesuai dengan format yang ditentukan.

11.4 Multi-threading

Modul "threading" digunakan untuk membuat dan mengelola thread dalam program Python.

Modul "threading" menyediakan kelas "Thread" yang memungkinkan pembuatan dan pengelolaan thread. Dengan membuat thread baru maka user dapat mengontrol eksekusi paralel, dan berkomunikasi antar thread menggunakan objek "Lock" atau "Condition".

Multi-threading dapat digunakan untuk menjalankan tugas-tugas secara paralel untuk meningkatkan kinerja dan responsivitas program. Sehingga berguna dalam situasi di mana tugas-tugas dapat dilakukan secara independen atau saat program perlu merespons input atau kejadian secara real-time.

11.5 Logging

Modul "logging" digunakan untuk mencatat pesan dan kejadian dalam program Python. Modul "logging" menyediakan kelas "Logger" yang memungkinkan pencatatan pesan dengan tingkat prioritas yang berbeda sehingga dapat membantu dalam pemantauan, pemecahan masalah, dan analisis program.

Modul "logging" memiliki fleksibilitas yang tinggi dan dapat diatur sesuai dengan kebutuhan yang di butuhkan. kita dapat mengarahkan output log ke berbagai target, seperti file, konsol, atau sistem log eksternal.

11.6 Weak References

Modul "weakref" digunakan untuk membuat referensi yang lemah (weak references) terhadap objek. Modul "weakref" menyediakan kelas "WeakRef" yang memungkinkan kita membuat referensi yang tidak mempengaruhi siklus referensi dan tidak mencegah penghapusan objek.

Modul "weakref" memungkinkan untuk mengikuti referensi terhadap objek yang terhapus secara otomatis dan mengatasi masalah dengan siklus referensi yang dapat menghambat penghapusan objek.

11.7 Tools for Working with Lists

Modul "array" menyediakan kelas "array" yang memungkinkan kita menyimpan dan memanipulasi data dalam bentuk array yang diketahui tipe datanya. Hal ini dapat menghemat ruang dan meningkatkan kinerja saat bekerja dengan data numerik.

Modul "collections" menyediakan kelas-kelas seperti "deque" (antrian ganda) dan "Counter" yang menyediakan fitur-fitur tambahan untuk memanipulasi daftar. Misalnya, "deque" memungkinkan operasi penghapusan dan penambahan elemen di kedua ujung antrian dengan kinerja yang baik. Serta memperluas fungsionalitas daftar dengan alat-alat yang lebih efisien dan khusus, tergantung pada kebutuhan program yang di inginkan.

11.8 Decimal Floating Point Arithmetic

Modul "decimal" digunakan untuk melakukan operasi matematika yang akurat dengan bilangan desimal. Dengan menggunakan modul "decimal" dapat menghindari kesalahan pembulatan yang umum terkait dengan aritmatika floating point biasa. 

Modul "decimal" memungkinkan kita untuk mengatur jumlah digit desimal yang diinginkan, mengendalikan pembulatan, dan menangani angka desimal dengan akurasi tinggi.
