# Ringkasan Minggu Ke - 9
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## Bab. 12 Virtual Environments and Packages

12.1 Introduction

Penggunaan python seringkali menggunakan paket dan modul yang tidak disertakan pada standard library. Tak jarang, aplikasi membutuhkan versi library tertentu untuk dapat dijalankan, hal ini karena aplikasi mungkin memerlukan bug tertentu yang telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi lama dari library's interface.

Hal ini berarti adanya kondisi yang tidak mungkin apabila dalam satu instalasi python dapat memenuhi setiap persyaratan aplikasi. Apabila aplikasi A membutuhkan versi 1.0, sedangkan B membutuhkan 2.0 maka hal ini bertentangan. Oleh karena itu timbul lah penyelesaian dengan adanya virtual environment.

12.2 Creating virtual environments

Modul yang digunakan dalam membuat dan mengelola virtual environments disebut venv. Venv akan menginstall sesuai dengan versi python yang dimiliki.

Adapun tahapan dalam membuat virtual environtments sebagai berikut :
* menentukan direktori - umumnya lokasi direktori terletak di .venv.
* mengaktifkan virtual environments
* menonaktifkan virtual environments - "deactive"

12.3 Managing packages with pip

Install, upgrade, remove package menggunakan program yaitu pip. By default, pip akan menginstall package dari Python Package Index. Adapun beberapa subcommands dari pip diantaranya 'install', 'uninstall', 'freeze', etc.
* Untuk menginstall package dengan versi tertentu dapat diikuti dengan '=='.

## Bagian Dokumentasi Conda

User Guide 

Bagian ini terdiri dari Home, Concepts, Getting Started, Installation, Configuration, Tasks, dan Additional Resources

Get Started

Bagian ini terdapat penjelasan lebih detail tentang apa saja yang ada pada conda

Dive Deeper

Bagian ini menjelaskan lebih detail tentang conda itu sendiri

Additional Resources

Bagian ini merupakan tambahan penjelasan terkait cheat sheet dan troubleshooting

## Conda - Getting Started

Bagian ini menjelaskan tentang Conda adalah pengelola paket dan pengelola lingkungan tangguh yang kita gunakan dengan perintah baris perintah di Anaconda Prompt untuk Windows, atau di jendela terminal untuk macOS atau Linux.

Panduan 20 menit untuk memulai conda ini memungkinkan kita untuk mencoba fitur-fitur utama conda. kita Harus memahami cara kerja conda saat kita menyelesaikan panduan ini.

Before you start

Bagian ini memastikan bahwa conda atau anaconda sudah di install sebelumnya

Contents

Bagian ini menjelaskan tentang contents yaitu:
* Memulai dengan Conda
* Mengelola conda
* Mengelola environment
* Mengelola python
* Mengelola paket

Starting conda

Bagian ini menjelaskan tentang langkah-langkah menginstal conda serta mengelola environment dan paket
