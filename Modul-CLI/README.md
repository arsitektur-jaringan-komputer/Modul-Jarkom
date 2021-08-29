# Modul Pengenalan CLI

## Deskripsi

Command Line Interface (CLI) adalah sebuah text-based interface pada system operasi dimana pengguna dapat meng-input-kan sebuah command lalu mendapat respon dari system. Tiap system operasi memiliki nama yang berbeda-beda untuk CLI-nya. Pada Unix disebut bash, ash, dsb. Pada MS-DOS dinamakan Command Prompt. Pada Apple namanya adalah commandshell. Pada Microsoft dinamakan PowerShell sedangkan pengguna Linux menyebutnya terminal. Pada modul ini kita akan mempelajari tentang CLI pada Linux.


## Macam - macam Command

1. **ls**

    Perintah ls  berfungsi untuk menampilkan seluruh file yang terdapat pada direktori tersebut

    ![Alt text](images/ls.png)

    Perintah-perintah ls sendiri ada beberapa macam. Contohnya ls -a dan ls -l.  Perintah dari ls -a sendiri berfungsi untuk menampilkan hidden file dari direktori tersebut.

    ![Alt text](images/ls-a.png)

    Sedangkan perintah dari ls -l berfungsi untuk menampilkan permission dari file yang ada di dalam direktori tersebut.

    ![Alt text](images/ls-l.png)
    
    ###
2. **pwd**

    Perintah pwd berfungsi untuk menampilkan lokasi direktori Anda saat itu.

    ![Alt text](images/pwd.png)
    
    ###
3. **cd [nama folder]**

    Perintah cd berfungsi untuk pindah dari suatu direktori ke direktori lain.

    ![Alt text](images/cd.png)
    
    Sedangkan perintah *"cd .."* berfungsi untuk kembali ke direktori atasnya *(bukan direktori sebelumnya)*.

    ![Alt text](images/cdtitik2.png)
    
    ###
4. **mkdir [nama folder]**

    Perintah mkdir berfungsi untuk membuat direktori baru.

    ![Alt text](images/mkdir.png)
    
    ###

5. **touch [nama file]**

    Perintah touch berfungsi untuk membuat file kosong baru.

    ![Alt text](images/touch.png)
    
    ###
6. **cp [nama file1] [nama folder tujuan]**

    Perintah cp berfungsi untuk menyalin file dari suatu direktori ke direktori tertentu. Pada gambar di bawah terlihat bahwa di dalam direktori Videos hanya terdapat file kosong.txt.

    ![Alt text](images/cp1.png)
    
    lalu kita mencoba mengcopy file yang bernama contohfile.txt ke direktori Videos.

    ![Alt text](images/cp2.png)
    
    Pada gambar di atas dapat terlihat jika file yang bernama contohfile.txt sudah tercopy di direktori Videos.
    ###

7. **mv**

    * **mv [nama file/folder] [nama folder tujuan]**


      Perintah mv tersebut berfungsi untuk memindahkan file/folder ke direktori tertentu. Pada gambar di bawah terlihat bahwa folder Videos hanya terdapat file kosong.txt.

      ![Alt text](images/mvpindah1.png)
      
      Lalu kita pindah file contohfile2.txt ke folder Videos

      ![Alt text](images/mvpindah2.png)
      
      Maka file contohfile2.txt akan dipindah ke foler Videos.
    ######
    * **mv [nama file/folder] [nama file/folder baru]**

        Perintah mv tersebut berfungsi untuk mengganti nama sebuah file atau folder

        ![Alt text](images/mvgantinama1.png)
    
    ###
8. **rm [nama_file/folder]**

    Perintah rm berfungsi untuk menghapus satu atau lebih file pada direktori tersebut. Pada gambar di bawah ada file yang bernama contohfile.txt. Kita akan mencoba untuk menghapusnya.

    ![Alt text](images/rm1.png)

###
9. **chmod [kode permission] [nama file/folder]**

    Perintah chmod berfungsi untuk mengganti permission dari sebuah file atau direktori. Perintah chmod mempunyai 3 rute utama:

    ![Alt text](images/chmod1.png)
    
    * R (Read)
    * W (Write)
    * X (Execute)

    Yang disediakan untuk 3 macam user:
    * O (Owner)	-> Pemilik suatu file atau direktori
    * G (Group)	-> Sekelompok user
    * P (Public)	-> Selain dari owner dan group

    Lalu untuk aturannya adalah:
    * 4	-> Read
    * 2	-> Write
    * 1	-> Execute

    Pada gambar di atas ada perintah chmod 777. Maksud dari perintah pada gambar di atas adalah:

    * Mode 7 (angka pertama) untuk owner, yang didapat dari 4+2+1. Jadi owner dapat membaca file (read), menulis file (write), dan mengeksekusi fle (exeute) tersebut.
    * Mode 7 (angka kedua) untuk group, yang didapat dari 4+2+1. Jadi group dapat membaca file (read), menulis file (write), dan mengeksekusi fle (exeute) tersebut.
    * Mode 7 (angka ketiga) untuk publik, yang didapat dari 4+2+1. Jadi publik dapat membaca file (read), menulis file (write), dan mengeksekusi fle (exeute) tersebut.
###
10. **chown [user]:[group] [nama file]**

    Perintah chown berfungsi untuk mengubah kepemilikan. Perintah pada gambar di bawah akan mengubah kepemilikan file “contohfile.txt”ke root.

    ![Alt text](images/chown1.png)

###

11. **nano [nama file]**

    Perintah nano berfungsi untuk mengedit sebuah file dan membuat file baru jika file tersebut belum ada. Nano sendiri merupakan salah satu dari sekian editor di terminal UNIX.

    ![Alt text](images/nano1.png)
    
    Maka terminal akan berubah menjadi editor untuk mengedit file tersebut

    ![Alt text](images/nano2.png)

###

12. **export**

    Perintah export berfungsi untuk mengatur variable yang ada di linux. Biasanya kita menggunakan export untuk mem-bypass proxy melalui terminal. Contoh sintaksnya adalah
    ####
    ```
    export http_proxy=”http://[username-vpn]:[password]@proxy.its.ac.id:8080”
    export https_proxy=”http://[username-vpn]:[password]@proxy.its.ac.id:8080”
    export ftp_proxy=”http://[username-vpn]:[password]@proxy.its.ac.id:8080”
    ```
###
13. **man [command]**

    Suatu saat jika Anda butuh penjelasan/dokumentasi mengenai command line tertentu, Anda bisa bertanya kepada google atau gunakan perintah man. Misalkan ketikkan "*man ls*". Maka terminal akan berubah menjadi manual akan command tersebut seperti gambar dibawah
    
    ![Alt text](images/manls.png)

###
14. **apt-get [perintah] [nama paket]**

    Untuk menginstall aplikasi di linux kita cukup mengetikkan perintah di atas. 
    Misal kita hendak menginstall suatu perintah 'sl' yang perlu kita lakukan adalah 
    1. *apt-get update* (lakukan terlebih dulu untuk menginstall sesuatu, supaya list - list package terupdate)

    ![Alt text](images/apt-get-update.png)

    2. *apt-get install sl* (menginstall sl)

    ![Alt text](images/apt-get-install.png)


Sekian :)

