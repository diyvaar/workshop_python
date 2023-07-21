# Ringkasan Minggu Ke - 12
NIM     :  **205410155**<br>
Nama    :  **Renina Diva Pindho Linangkung**<br>
Kelas   :  **IF - 3**
___
## Pertemuan 12 - Python untuk Data Analytics

5 Perintah Yang Ada Pada Pandas :
* DataFrame - perintah ini digunakan untuk membuat sebuah dataframe. Penggunaan 'DataFrame' diawali dengan library pandas sehingga secara sintaksis sebagai berikut : pandas.DataFrame(...) / pd.DataFrame(...)
*  .head() - perintah ini digunakan untuk menampilkan records teratas dari sebuah dataframe. Penggunaan '.head()' harus diawali dengan nama dataframe dan menyertakan parameter pada tanda kurungnya. Secara sintaksis antara lain : 'df.head()' atau 'df.head(10)'. Perintah head() tanpa menyertakan parameter secara default akan menampilkan 5 record teratas dari dataframe. 
* .tail() -  perintah ini digunakan untuk menampilkan records terbawah / terakhir dari sebuah dataframe. Penggunaan '.tail()' harus diawali dengan nama dataframe dan menyertakan parameter pada tanda kurungnya. Secara sintaksis antara lain : 'df.tail()' atau 'df.tail(10)'. Perintah tail() tanpa menyertakan parameter secara default akan menampilkan 5 record terakhir dari dataframe.
* .describe() - perintah ini digunakan untuk mengetahui gambaran secara umum atau dasar dari suatu dataset. Output dari perintah ini akan menampilkan sebaran data dari dataset berdasarkan tiap kolom, seperti mean, standar deviasi, minimum dan maximum, serta kuartil dari tiap - tiap kolom.
* .info() - perintah ini digunakan untuk mengetahui informasi dari value tiap - tiap kolom. Apabila .describe() mengarah pada sebaran data tiap kolom, maka .info() akan menampilkan informasi umum mengenai value dari tiap kolom, seperti data types, jumlah records non-null, serta nama kolom
