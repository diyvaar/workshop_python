# Ringkasan Minggu Ke - 4
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## BAB. 6 Modules

Ketika pengguna keluar dari python, maka atribut yang didefinisikan akan hilang termasuk fungsi dan variables. Oleh karenanya, untuk program yang lebih lama, python memperkenalkan sebuah file yang dikenal dengan modul. Modul berisi definisi dan pernyataan dalam bahasa python dan disimpan dengan ekstensi .py. Nama dari modul tersedia sebagai value dari variable global ‘__name__’. Modul dapat dibuat dengan text editor dan disimpan dengan ekstensi .py pada direktori yang sedang / akan digunakan.
Untuk mengakses modul, dapat dengan membuka Python dan memasukan perintah import pada modul.

  * Import module

  Kemudian untuk menjalankan program pada modul, pastikan sesuai sintaks, seperti berikut :

  * module.atribut(parameter)

  Nama dan variable global dari modul dapat dengan perintah :

  * module._name__

6.1 More on Modules

  Variasi dalam meng-import module :

  * from <module> import <atribut1>, <atribut2>

  Oleh karena modul tidak diperkenalkan nama dan darimana impor diambil, maka merujuk pada contoh, modul ‘fibo’ tidak terdefinisi

  *	from <module> import *

  Dengan perintah ini, maka semua atribut pada modul akan di impor kecuali attribute yang diawali dengan underscore (_). Sebagai catatan, penggunaan ‘*’ haruslah dihindari karena meningkatkan potensi kesalahan dalam pemrograman.

  *	import <module> as <…>

  As pada perintah diatas dapat dikatakan hampir sama fungsinya dengan ‘alias’

6.2 Standard modules

  Python dilengkapi dengan standard modules dictionaries. Sys yang dibangun pada tiap penerjemah Python. sys.p1 dan sys.p2 menentukan string yang digunakan sebagai prompt utama dan sekunder. Library sys pada Python menyediakan akses ke beberapa variable yang digunakan oleh interpreter. 

6.3 The dir() function

  dir() digunakan untuk mengetahui nama – nama yang didefinisikan modul. It’ll be returns a sorted list dalam strings. dir() tanpa argument akan mengembalikan nama yang telah didefinisikan.

6.4 Packages

  Python dengan penamaan menggunakan nama modul titik. Penamaan tersebut sangat membantu dalam penulisan package multi model yang perlu ekstra hati – hati dengan nama modul satu sama lain.
