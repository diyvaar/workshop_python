# Ringkasan Minggu Ke - 6
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## Bab. 8 Errors and Exceptions

8.1 Syntax Errors

Syntax errors atau yang juga dikenal sebagai parsing errors merupakan bentuk complaint paling umum saat memulai menggunakan python. Ketika error terjadi, parser akan re-print statement yang bermasalah dan menampilkan panah kecil yang menunjukkan letak masalah. 

8.2 Exceptions

Bahkan jika suatu statement sudah benar secara sintaksis, akan muncul kesalahan ketika proses ekseskusi. Kesalahan pada proses eksekusi ini disebut dengan pengecualian atau exceptions. Exceptions terdiri dari berbagai jenis yang dapat dilihat pada pesan, seperti : ZeroDivissionError, NameError dan TypeError. Baris selanjutnya akan menjelaskan secara detail tentang sebab adanya kesalahan.

8.3 Handling Exceptions

Untuk mengatasi sebuah kesalahan pada proses eksekusi memungkinkan untuk menulis program untuk handle selected exceptions dengan menggunakan try clause. Dalam penggunaan try clause memungkinkan untuk menuliskan lebih dari satu exception.

8.4 Raising Exceptions

Raise statement memungkinkan programmer untuk memaksa exception tertentu terjadi. 
* "raise ValueError  # shorthand for 'raise ValueError()'"
Satu satunya argumen pada sintaks diatas akan dinaikkan untuk menunjukkan exception yang dimunculkan. Raise exceptions dapat digunakan untuk menentukan apakah ada exception namun tidak dapat di handle.

8.5 Exception Chaining

Exceptions yang tidak terhandle pada except section maka exceptions yang ter handle akan tampil padanya dan akan disertakan pula pada pesan kesalahan. 

8.6 User-defined exceptions

Program dapat menamai exception mereka sendiri dengan membuat kelas exception baru. Exceptions biasanya diturunkan dari kelas exception baik secara langsung maupun tidak.

Kelas exception dapat didefinisikan sebagai suatu yang dapat melakukan apa pun yang dapat dilakukan kelas lain. Sebagian besar exception didefinisikan dengan nama yang berakhir 'error' hampir serupa pada penamaan exception secara standar.

8.7 Defining clean-up actions

Try statement memiliki optional clause lainnya yang disisipkan untuk menentukan tindakan untuk pembersihan dengan 'finally' clause. Jika terdapat 'finally' clause, maka clause tersebut akan dieksekusi sebagai kerjaan terakhir sebelum try statement selesai.

Jika exceptions terjadi selama eksekusi clause, maka exception akan di hansle oleh except clause. Jika tidak, maka exceptions akan dimunculkan kembali setelah finally clause dieksekusi. Jika 'finally' clause mengeksekusi sebuah 'break', 'continue' atau 'return', maka exceptions tidak akan dimunculkan kembali.

8.8 Predefined clean-up actions

Beberapa objek berpengaruh pada penentuan tindakan pembersihan.
Contohnya, pada program yang membuka suatu file. Namun, masalah akan muncul dengan program tersebut jika membiarkan file terbuka untuk waktu yang tidak ditentukan setelah program dijalankan. Hal ini dapat menjadi sebuah masalah seiring dengan semakin besarnya data dfile yang dibuka. 'With' statement memungkinkan objek seperti file untuk digunakan dengan cara yang semestinya seperti dengan memastikan akan selalu dibersihkan dengan cepat dan benar. Dan setelah program dijalankan, file akan selalu ditutup.

8.9 Raising and Handling Multiple Unrelated Exceptions

Report multiple exceptions yang terjadi dalam situasi yang berbeda dengan menggunakan 'except*' daripada 'except'. Hal ini karena dapat menangani exceptions secara selektif dengan hanya menangani exceptions yang cocok dengan tipenya. 

8.10 Enriching Exceptions with notes

Ketika sebuah exception dibuat untuk di munculkan, umunya akan diinisialisasi dengan informasi yang menjelaskan kesalahan terjadi. Terdapat kasus dimana adanya manfaat dalam mencantumkan informasi. Untuk mengimplementasikannya adanya metode 'add_note' yang menerima string dan menambahkannya ke daftar catatan exceptions. 
