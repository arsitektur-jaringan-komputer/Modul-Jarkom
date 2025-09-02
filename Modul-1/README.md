# Crimping dan Wireshark

## Daftar Isi
+ 0.[Basic Command Line Tools untuk Koneksi pada Jaringan](#0-basic-command-line-tools-untuk-koneksi-pada-jaringan)
  + [telnet](#01-telnet)
  + [ssh](#02-ssh-secure-shell)
  + [nc](#03-netcat-nc)
  + [ping](#04-ping)
+ 1.[Konsep IP dan Port](#1-konsep-ip-dan-port)
  + [Konsep IP](#11-konsep-ip)
  + [Alokasi Port](#12-alokasi-port)
+ 2.[Wire Crimping](#2-wire-crimping)
   + 2.1 [Peralatan yang dibutuhkan](#21-peralatan-yang-dibutuhkan)
   + 2.2 [Jenis-jenis Konfigurasi Kabel UTP](#22-konfigurasi-kabel)
   + 2.3 [Langkah-langkah](#23-langkah---langkah)
+ 3.[Wireshark](#3-wireshark)
  + 3.1 [Instalasi](#31-instalasi)
  + 3.2 [Filters](#32-filters)
  + 3.3 [Export data hasil packet capture](#33-export-data-hasil-paket-capture)
  + 3.4 [Penggunaan Wireshark pada FTP Server](#34-penggunaan-wireshark-pada-ftp-server)
+ 4.[Termshark](#4-termshark)
  + 4.1 [Instalasi](#41-instalasi-termshark)
  + 4.2 [Penggunaan](#42-penggunaan-termshark)

## 0. Basic Command Line Tools untuk Koneksi pada Jaringan

### 0.1 Telnet

Bayangkan Anda ingin memastikan bahwa sebuah situs web dapat diakses melalui port 80 (yang biasanya digunakan untuk HTTP). Dengan Telnet, Anda bisa mengetik perintah:

```
telnet google.com 80
```
Jika Telnet terhubung, artinya situs tersebut aktif dan port 80 terbuka, memungkinkan komunikasi. Ini adalah cara sederhana untuk memeriksa apakah suatu layanan di server (seperti web) dapat dijangkau dari komputer Anda.

#### Jadi, apa itu Telnet?

Telnet (Telecommunication Network) adalah protokol jaringan yang memungkinkan kita terhubung dan berinteraksi dengan komputer lain dari jarak jauh melalui jaringan, seperti internet atau LAN (Local Area Network). Dengan Telnet, kita bisa mengakses file dan data di komputer lain, seolah-olah kita sedang duduk langsung di depan komputer tersebut.

Fungsi utama Telnet adalah untuk login ke komputer lain (host/server) dari jarak jauh dan mengelolanya. Ini bisa sangat berguna, misalnya untuk administrasi sistem atau perbaikan jarak jauh.

Namun, Telnet memiliki kelemahan serius dalam hal keamanan. Informasi seperti nama pengguna dan password dikirim dalam bentuk teks biasa (unencrypted) seperti pada gambar di bawah, yang membuatnya mudah disadap oleh pihak lain di jaringan. Karena itu, penggunaan Telnet sudah mulai digantikan oleh protokol yang lebih aman seperti SSH.
![Telnet](../Modul-1/images/telnet2.png)

### 0.2 SSH (Secure Shell)

Bayangkan Anda seorang pengembang yang bekerja dari rumah dan perlu memperbarui kode di server perusahaan. Dengan SSH, Anda bisa masuk ke server dari komputer Anda di rumah, mengedit atau mengupload file kode, dan menjalankan program untuk memastikan semuanya bekerja dengan baik, seolah-olah Anda berada di depan server tersebut secara langsung.

![remote-worker](../Modul-1/images/remote-worker.jpg)

#### Jadi, apa itu SSH?

SSH adalah sebuah protokol yang memungkinkan Anda mengakses dan mengelola komputer atau server dari jarak jauh dengan aman. Anda bisa melakukan berbagai tugas, seperti menjalankan program, membuat atau menghapus file, dan mentransfer file ke server lain. SSH memastikan bahwa semua data yang dikirim dan diterima terlindungi dengan enkripsi, sehingga lebih aman daripada metode lama seperti Telnet.

Cara kerja protokol SSH adalah dengan menerapkan model client-server. Koneksi yang terjadi adalah SSH client (komputer yang digunakan pengguna) melakukan koneksi ke SSH server (server remote yang dituju).

SSH saat ini versi terbarunya yaitu [SSH v2](https://www.synopsys.com/software-integrity/security-testing/fuzz-testing/defensics/protocols/ssh2-server.html). SSH bisa dikatan lebih secure dibandingan Telnet.

Cara melakukan koneksi dengan SSH adalah sebagai berikut:
```
ssh username@host or
ssh username@host -p 2224
```

### 0.3 Netcat (nc)

Bayangkan Anda ingin menguji apakah sebuah server dapat menerima data dari komputer Anda. Dengan Netcat, Anda bisa mengirim pesan ke server dan melihat apakah server merespons. Ini berguna untuk memeriksa koneksi jaringan atau debug aplikasi.

```
echo "Hello, Server!" | nc example.com 1234
```
Ini akan mengirimkan pesan "Hello, Server!" ke server di example.com pada port 1234.

#### Jadi, apa itu Netcat?

Netcat (atau nc) adalah utilitas baris perintah yang membaca dan menulis data melalui koneksi jaringan, menggunakan protokol TCP atau UDP. Perintah ini adalah salah satu alat yang paling kuat dalam jaringan dan persenjataan administrator sistem dan dianggap sebagai alat multi fungsi.

Sintaks dari netcat sendiri adalah sebagai berikut:
```
nc [options] host port
```
Secara default, Netcat akan mencoba untuk memulai koneksi TCP ke host dan port yang ditentukan. Jika Anda ingin membuat koneksi UDP, gunakan opsi -u.

### 0.4 Ping

Bayangkan Anda mengirimkan pesan singkat ke komputer atau server dan menunggu balasan. Jika balasan datang dengan cepat, berarti koneksi jaringan baik dan perangkat tersebut dapat dijangkau. Jika tidak ada balasan atau lambat, mungkin ada masalah dengan koneksi atau perangkat tersebut. Ping membantu Anda mengetahui apakah jaringan berfungsi dengan baik.

#### Jadi, apa itu Ping?

Ping merupakan singkatan dari Packet Internet Network Groper. Secara sederhana, ping adalah perintah untuk mengecek status dan keberadaan host dalam sebuah jaringan internet.

Prinsip utama ping adalah seperti penggunaan sonar untuk mengukur kedalaman laut. Jadi, sebuah sinyal dikirimkan ke dasar, lalu lamanya waktu kembali ke atas menjadi dasar perhitungannya.

![ping](https://niagaspace.sgp1.digitaloceanspaces.com/blog/wp-content/uploads/2021/12/14203814/cara-kerja-ping-2-1024x546.jpg)

source: [https://www.niagahoster.co.id/blog/apa-itu-ping/](https://www.niagahoster.co.id/blog/apa-itu-ping/)

Berikut merupakan cara melakukan ping:

![ping](images/ping.png)

Dengan perintah di atas, Anda akan mendapatkan informasi sebagai berikut:
+ Reply adalah balasan dari host yang diikuti oleh informasi alamat IP. Perintah default di atas, idealnya akan memberikan empat balasan (reply). Namun, bisa saja muncul Request Timed Out (RTO) yang artinya tidak ada balasan sesuai waktu tunggu dari ping tersebut.
+ Bytes adalah jumlah data yang dikirimkan. Untuk Windows, umumnya adalah 32 bytes.
+ Time adalah lamanya waktu respon dari host, yang dihitung dengan satuan ms, atau millisecond. Waktu ping yang bagus adalah di bawah 100ms, terutama kalau penggunaannya untuk game online yang menuntut ping yang rendah.
+ TTL (Time To Live) merupakan durasi sebuah paket data dapat berada di jaringan, yang dicatat dalam hitungan detik. Umumnya, TTL diatur pada kisaran ideal 64 detik.


## 1. Konsep IP dan Port

### 1.1 Konsep IP

Apakah Anda pernah bertanya-tanya bagaimana internet tahu bahwa saat Anda mengetik google.com, Anda akan dibawa ke situs web Google dan bukan ke situs lain? Sebenarnya, internet tidak memahami nama google.com secara langsung. Sebaliknya, internet menggunakan alamat IP untuk mengetahui ke mana harus mengirimkan data. Misalnya, google.com sebenarnya terhubung ke alamat IP 8.8.8.8.

#### Apa itu IP?
Bayangkan Anda mempunyai tetangga, cara Anda membedakan rumah Anda dengan rumah tetangga adalah dengan menggunakan alamat. Alamat IP seperti alamat rumah. Setiap perangkat, seperti komputer atau ponsel, memiliki alamat rumahnya sendiri di jaringan. Saat Anda mengirimkan sesuatu, seperti surat atau data, Anda perlu alamat rumah penerima agar kiriman Anda sampai ke tempat yang benar. Begitu juga dengan alamat IP: saat Anda mengirim data melalui internet, alamat IP memastikan data tersebut sampai ke perangkat yang tepat.

![ip-alamat-rumah](../Modul-1/images/ip-alamat-rumah.jpg)

IP adalah singkatan dari Internet Protocol, atau dalam bahasa Indonesia berarti Protokol Internet. Jadi, IP address atau internet protocol address adalah alamat protokol internet (alamat IP) yang mengidentifikasi segala perangkat yang terhubung ke jaringan, baik jaringan internet pada umumnya maupun lokal.

Jenis-jenis alamat IP:
#### a. IPv4

IPv4 adalah alamat IP yang paling umum digunakan, dengan panjang 32-bit dan empat bagian (oktet) yang dipisahkan oleh titik. Nilai setiap oktet berkisar dari 0 – 255. Kepanjangan IPv4 yaitu Internet Protocol version 4.

Dengan kemungkinan ini, bisa disimpulkan bahwa saat ini ada sekitar 4,3 miliar alamat IPv4 yang berbeda di seluruh dunia.

Contoh IPv4 adalah seperti berikut:

+ 169.89.131.246
+ 192.0. 2.146
+ 01.102.103.104

Karena merupakan yang paling banyak digunakan, saat ini hampir semua sistem pasti bisa menangani routing IPv4 tanpa masalah. Selain itu, alamat IPv4 mendukung mayoritas topologi jaringan karena prefiksnya yang sederhana. Data dalam address packet IPv4 juga dienkripsi dengan baik untuk memastikan komunikasi yang aman antar jaringan.

#### b. IPv6

IPv6 adalah versi IP address yang lebih baru dari IPv4, dimaksudkan untuk menggantikan IPv4 karena variasi IPv4 yang kini mulai terbatas.

Kalau IPv4 memiliki panjang 32 bit, panjang IPv6 mencapai 128 bit. Artinya, ada sekitar 340 undecillion (angka di belakang digit pertamanya ada 66!) alamat IPv6 yang berbeda.

IPv6 ditulis dalam rangkaian digit heksadesimal 16 bit dan huruf, dipisahkan oleh titik dua. Jadi, pada jenis IP address ini, Anda akan menjumpai huruf dari A sampai F.

Berikut adalah contoh IPv6:

+ 2001:3FFE:9D38:FE75:A95A:1C48:50DF:6AB8
+ 2001:0db8:85a3:0000:0000:8a2e:0370:7334
+ 2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF
Dengan IPv6, routing akan menjadi lebih efisien karena memungkinkan penyedia layanan internet meminimalkan ukuran tabel routing. IPv6 juga menggunakan Internet Protocol Security (IPsec), jadi Anda tidak perlu cemas dengan autentikasi, kerahasiaan, dan integritas data.

Terlebih lagi, IPv6 tidak memiliki IP checksum sehingga pemrosesan packet menjadi lebih efisien, dan mendukung multicast. Hasilnya, transmisi data pun bisa dikirim ke beberapa tujuan sekaligus sehingga akan menghemat bandwidth jaringan.

### 1.2 Alokasi Port

Saat Anda mengunjungi gedung, Anda memberi tahu nomor apartemen yang ingin Anda tuju agar resepsionis bisa mengarahkan Anda ke tempat yang tepat. Begitu juga dengan port dalam jaringan: saat Anda mengirimkan data, Anda perlu menyebutkan nomor port agar data sampai ke aplikasi atau layanan yang tepat di komputer atau server.

![port-apartemen](../Modul-1/images/port-apartemen.jpg)

#### Jadi, apa itu Port?

Port adalah cara yang memungkinkan komputer untuk menangani beberapa koneksi dan program secara bersamaan di jaringan. Setiap port terhubung dengan aplikasi atau layanan tertentu. Misalnya, port membantu komputer membedakan antara email dan halaman web yang masuk, karena mereka menggunakan port yang berbeda.

Untuk meningkatkan kompatibilitas, port sudah memiliki sistem standardisasi di semua perangkat yang terhubung ke jaringan. Setiap port memiliki identitas dalam bentuk angka 16-bit (dua byte) yang disebut sebagai Port Number.

**Logical Port**

Logical port adalah jalur yang digunakan oleh aplikasi untuk menghubungkan dengan komputer lain melalui jaringan TCP/IP. Salah satu contohnya adalah mengkoneksikan komputer dengan internet. Port ini berperan penting dalam jaringan komputer.

Dilihat dari penomorannya, logical port terbagi menjadi tiga jenis. Ada jenis port yang terdaftar di Internet Assigned Numbers Authority (IANA), dan ada yang tidak, berikut pembagiannya:

+ Well-known port: berkisar dari 0 – 1023. Ini merupakan port yang dikenali atau port sistem. Port ini selalu merepresentasikan layanan jaringan yang sama dan ditetapkan oleh IANA.
+ Registered port: berkisar dari 1024 – 49151. Port ini diketahui dan terdaftar di IANA tetapi tidak dialokasikan secara permanen, sehingga dapat menggunakan port number yang sama.
+ Dynamically assigned port: berkisar dari 49152 – 65535. Port ini ditetapkan oleh sistem operasi atau aplikasi yang digunakan untuk melayani request dari pengguna sesuai dengan kebutuhan.

Berikut ini beberapa contoh logical port yang sering digunakan beserta fungsinya:
+ Port 20 & 21 (FTP), adalah protokol yang berguna dalam mentransfer data di dalam suatu jaringan.
+ Port 22 (SSH), berfungsi mengirimkan data melalui jaringan dalam bentuk terenkripsi. Dapat digunakan untuk menjalankan fungsi atau tugas yang bisa diakses dari jarak jauh, misalnya menghubungkan ke host atau server.
+ Port 23 (TELNET), port untuk menghubungkan komputer dan server jarak jauh. Fungsinya mirip dengan SSH, hanya saja port 23 TELNET tidak menggunakan enkripsi pada koneksinya.
+ Port 25 (SMTP), berfungsi memastikan pengiriman email melalui jaringan dikomunikasikan dengan aman antara sesama SMTP server.
+ Port 53 (DNS), berfungsi sebagai penerjemah alamat IP pada setiap host.
+ Port 67 & 68 (DHCP), atau Dynamic Host Configuration Protocol berfungsi untuk menetapkan informasi terkait alamat IP.
+ Port 80 (HTTP/ Web Server), memungkinkan browser terhubung ke halaman web.
+ Port 443 (HTTPS),  berguna untuk menghubungkan klien ke internet, namun dengan fitur keamanan tambahan yang tidak dimiliki port HTTP 80. Port 443 mengenkripsi paket jaringan sebelum mentransfernya.
+ Port 143 (IMAP), Internet Message Access Protocol atau IMAP adalah protokol untuk mengakses email dari server.

## 2. Wire Crimping
Dalam jaringan komputer, terjadi komunikasi antara satu perangkat dengan perangkat lainnya. Komunikasi itu tentu membutuhkan suatu media. Walaupun sudah ada teknologi komunikasi nirkabel, peran kabel dalam jaringan masih penting dan belum tergantikan. Oleh karena itu dalam modul kali ini, kita akan belajar cara melakukan _crimping_ pada salah satu jenis kabel jaringan yang bernama kabel UTP (_Unshielded Twisted Pair_).

### 2.1 Peralatan yang dibutuhkan
Untuk melakukan _wire crimping_ kita membutuhkan peralatan di bawah ini:
#### a. Kabel UTP
![Kabel UTP](images/kabelutp.jpg)

Bahan utama dari proses ini.
#### b. RJ45
![Kabel UTP](images/rj45.jpg)

RJ45 adalah konektor yang akan menghubungkan kabel UTP dengan perangkat.
#### c. Tang Crimping
![Kabel UTP](images/tang_crimping.jpg)

Tang ini digunakan untuk memasangkan kabel pada RJ45.
#### d. LAN Tester
![Kabel UTP](images/lan_tester.jpg)

Seperti namanya, alat ini digunakan untuk memeriksa apakah kabel yang kita buat berfungsi dengan baik atau tidak.
### 1.2 Konfigurasi Kabel
Ada beberapa macam konfigurasi kabel. Dari urutan warnanya yang sesuai standar internasional dapat dibagi menjadi __T568A__ dan __T568B__.

![Perbedaan urutan warna T568A dan T568B](images/urutan_warna.png)

Sedangkan dari pemasangannya dibagi menjadi
#### a. __Kabel Straight-Through__
  Jenis pengkabelan ini digunakan untuk menyambungkan dua tipe perangkat berbeda yang tersambung ke jaringan, yakni perangkat DTE (data terminal equipment) ke DCE (data circuit-terminating equipment) atau sebaliknya. Perangkat DTE adalah perangkat yang melakukan generate data digital dan bertindak sebagai source dan destination untuk data digital, contohnya adalah komputer, mikrokomputer, terminal, printer. DCE adalah perangkat yang menerima dan mengkonversi data ke link telekomunikasi yang sesuai, umumnya DCE adalah perangkat jaringan seperti router, switch, modem.

![Kabel Straight-Through](images/straight_through.png)

  Aturan pemasangannya adalah bahwa tiap ujung kabel harus memiliki urutan warna yang sama. Misal ujung yang satu menggunakan susunan warna berdasarkan aturan T568A maka begitu juga ujung lainnya.

#### b. __Kabel Crossover__
Berkebalikan dengan kabel Straight-through, pengkabelan ini digunakan untuk menyambungkan dua tipe perangkat yang sama yang tersambung ke jaringan, yakni perangkat DTE ke DTE atau DCE ke DCE. Misalnya antara komputer dengan komputer, router dengan router, router dengan switch, komputer dengan printer.

  ![Kabel Crossover](images/crossover.png)

  Aturan pemasangannya pun berbeda dengan kabel jenis straight-trough, kabel jenis Crossover memiliki urutan warna yang berbeda dikedua ujungnya. Tapi, perbedaan warna ini tidak boleh sembarangan, karena kedua ujung ini juga memiliki aturan urutan warna. Pada kabel jenis Crossover standar, jika salah satu ujung Pin memiliki susunan warna berdasarkan aturan T568A, maka ujung Pin yang lain harus memiliki urutan warna berdasarkan standar T568B.

### 2.3 Langkah - Langkah
1. Siapkan keperluan crimping (kabel UTP, RJ45, tang crimping, LAN tester)
2. Kupas pelindung kabel UTP
3. Urutkan kabel sesuai konfigurasi yang diinginkan (Straight/Cross/yang lainnya).
4. Potong ujung kabel untuk meratakannya.
5. Masukkan ujung kabel tersebut ke RJ45 dan pastikan menyentuh ujung RJ45.
6. Gunakan tang crimping untuk mengunci kabel UTP dalam RJ45 (pastikan ujung kabel masih menempel dengan ujung RJ45 saat penguncian dilakukan)
7. Terakhir, gunakan LAN tester untuk memastikan kabel yang anda buat bekerja dengan baik.

### Video crimping Straight

[![video-straight](https://i.ytimg.com/vi/JDiybTG9dGY/maxresdefault.jpg)](https://youtu.be/NL0F8bP8k7I)

## 3. Wireshark
Wireshark adalah sebuah aplikasi penganalisa paket jaringan. Penganalisa paket jaringan akan mencoba menangkap paket jaringan dan mencoba untuk menampilkan data paket sedetail mungkin.
Sebuah jaringan komputer dibangun dengan tujuan mengirimkan atau menerima data antara satu end-point dengan end-point lainnya. Data dikirim dalam bentuk paket-paket. Struktur sebuah paket terdiri dari :

***1. Header***
Bagian header berisi alamat dan data lainnya yang dibawa oleh paket. Struktur dari header meliputi :

| Intruksi | Keterangan |
|--  |---|
| Panjang paket | Beberapa jaringan sudah memiliki panjang paket yang baku (*fixed-length*), sementara yang lain bergantung pada header untuk memuat informasi ini |
| Sinkronisasi | Beberapa bit yang membantu paket mencocokkan jaringan yang dimaksud |
| Nomor paket | Menunjukkan urutan dari total paket yang ada |
| Protokol | Pada jaringan yang membawa lebih dari satu macam informasi, protokol ini menunjukkan jenis paket yang ditransmiskan: e-mail, halaman web, atau yang lain |
| Alamat tujuan | Ke mana paket dikirimkan |
| Alamat asal | Dari mana paket dikirimkan |

***2. Payload***
Payload juga disebut sebagai ***body*** dari paket. Pada bagian inilah data yang akan dikirimkan lewat paket berada

***3. Trailer***
trailer, kadang-kadang disebut ***footer***, biasanya memuat sepasang bit yang memberi sinyal pada perangkat penerima bahwa paket sudah mencapai ujungnya. trailer juga bisa memuat semacam *error checking*.

### 3.1 Instalasi
Instalasi untuk OS WIndows atau macOS bisa mengunduh installer pada [ laman ini](https://www.wireshark.org/download.html). Untuk OS linux dapat melihat tutorialnya [di sini](https://linuxtechlab.com/install-wireshark-linux-centosubuntu/).
Setelah melakukan instalasi , jalankan Wireshark sebagai **administrator** (WIndows) atau **root** (linux)
Berikut tampilan awalnya :
![wireshark](images/wireshark.png)

### 3.2 Filters
Dalam Wireshark terdapat 2 jenis filter yaitu ***Capture Filter*** dan ***Display Filter***

#### 3.2.1 Capture Filter
![Capture](images/capture.png)

 - Definisi : Memilah paket yang akan ditangkap (captured). Paket yang tidak memenuhi kriteria dibiarkan lewat tanpa ditangkap
 - Sintaks filter dapat terdiri dari 1 atau lebih **primitive**. primitive sendiri biasanya terdiri dari sebuah **id** (bilangan atau nama) yang didahului oleh 1 atau lebih jenis qualifier. Perlu diingat bahwa dalam 1 primitive tidak boleh ada 2 atau lebih qualifier sejenis
 - Jenis qualifier :

| Qualifier | Keterangan | Contoh |
|--|--|--|
| type | Menentukan jenis id atau nama yang menjadi nilai filter | host, net, port, portrange |
| dir | Menentukan direction atau arah dari id | src, dst, dan lain-lain |
| proto | Menentukan protokol dari id | tcp, udp, dan lain-lain |

 - Sintaks filter dapat memuat operator, tanda kurung, negasi ( `!` / `not` ), dan kongjungsi ( `&&` / `and` atau `||` / `or` ). Kongjungsi digunakan untuk menghubungkan 2 primitive dalam satu sintaks
 - Contoh sintaks capture filter :

| Filter expression / Primitive(s) | Keterangan |
|--|--|
| `host 10.151.36.1` | Menangkap semua paket yang spesifik menuju ke atau berasal dari alamat 10.151.36.1 |
| `src host 10.151.36.1` | Menangkap semua paket yang spesifik berasal dari alamat 10.151.36.1 |
| `net 192.168.0.0/24` atau `net 192.168.0.0 mask 255.255.255.0` | Menangkap semua paket yang berasal dari atau menuju ke subnet 192.168.0.0/24 |
| `dst net 192.168.0.0/24` | Menangkap semua paket yang menuju ke subnet 192.168.0.0/24 |
| `udp port 80` | Menangkap semua paket dengan protokol UDP yang menuju ke atau berasal dari port 80 |
| `tcp src port 22 or host 10.151.36.30` | Menangkap semua paket dengan protokol TCP yang berasal dari port 22 atau semua paket yang berasal dari atau menuju ke alamat 10.151.36.30 |

 - Contoh capture filter `host 10.151.36.1`
![Contoh-capture](images/capture-filter.png)

#### 3.2.2 Display Filter
![Display](images/display.png)
 - Definisi : Memilah paket yang akan ditampilkan dari kumpulan paket yang sudah ditangkap
 - Secara umum sintaks display filter terdiri dari `[protokol] [field] [comparison operator] [value]`. Berikut ini daftar ***comparison operator*** yang tersedia :

| English | Comparison Operator (C-like) | Indonesia |
|---|---|---|
| equal | == | Sama dengan |
| inequality | != | Tidak sama dengan |
| greater than | > | Lebih besar dari |
| less than | < | Lebih kecil dari |
| greater than or equal than | >= | Lebih besar dari atau sama dengan |
| less than or equal to | <= | Lebih kecil dari atau sama dengan |
| contains |  | Protokol atau field mengandung nilai tertentu |
| matches | ~ | Protokol atau field cocok dengan *regular expression* |
| bitwise_and | & | Membandingkan nilai bit sebuah field |

 - Pada display filter bisa menggabungkan 2 filter expression dengan ***logical operator***

| Logical Operator | Keterangan |
|---|---|
| `and` atau `&&` | logical AND |
| `or` | logical OR |
| `xor` atau `^^` | logical XOR |
| `not` atau `!` | logical NOT |
| `[...]` | substring operator |
| `in` | membership operator |

 - Contoh penggunaan display filter :

| Filter expression | Keterangan |
|---|---|
| `tcp.port == 443` | Menampilkan semua paket dengan protokol TCP yang menuju ke atau berasal dari port 443 |
| `ip.src == 192.168.0.1 or ip.dst == 192.168.0.1` | Menampilkan semua paket yang berasal dari alamat 192.168.0.1 atau menuju ke alamat 192.168.0.1 |
| `http.request.uri constains "login"` | Menampilkan semua paket dengan protokol HTTP yang URI nya mengandung string "login" |

 - Contoh display filter `tcp.port == 80`, berikut hasilnya :
![Contoh-display](images/display-filter.png)

### 3.3 Export data hasil paket capture

 1. Setelah memiliki packet, pilih pada menu bar File -> Export Objects -> (protokol yang diinginkan). Pada contoh ini dipilih protokol HTTP
![export](images/export.PNG)
 2. Pilih paket yang akan di-export. Pada contoh ini dipilih paket yang memuat gambar dari situs tertentu tertentu. lalu klik Save dan berikan nama file, path, beserta ekstensinya jika diperlukan.
![Pilih-paket](images/pilih-paket.png)
 3. File berhasil di-export
![logo](images/logo.png)

### 3.4 Penggunaan Wireshark pada FTP Server
Jalankan aplikasi wireshark sebelum *connect* ke server FTP yang dituju.
#### 3.4.1 Connect ke Server
##### a. Windows
Untuk pengguna windows kita akan menggunakan bantuan **FileZilla**. Untuk percobaan di server, di sini menggunakan Filezilla Server dan untuk client menggunakan Filezilla Client. Nantinya server dan clientnya bisa komputer yang sama atau berbeda (asal terhubung ke jaringan komputer).

###### Pembuatan Server FTP di Filezilla Server
1. Buka Filezilla Server (bisa melalui aplikasi Filezilla Server desktop atau XAMPP dengan start module Filezilla dan klik tombol Admin). Jika muncul pop up "Connect to Server" langsung saja klik Ok. Muncul tampilan berikut.

![Home FileZilla Server](images/fz_server_home.png)

2. Klik menu Edit->Users. Di kolom Users paling kanan, tambahkan user baru dengan cara klik Add dan isikan nama user FTP nya. Berikut hasil setelah menambah user (di sini ditambah user "coba"). Jika ingin menggunakan password, centang "Password" dan masukkan password yang diinginkan.

![Add User FileZilla Server](images/fz_server_add_user.png)

3. Setelah user terbuat, berikutnya masuk ke setting shared folder untuk menentukan folder yang akan dishare atau diremote dengan FTP. Pada kolom Users, pilih user, dan pada kolom Shared folders, klik tombol "Add" untuk menambah direktori. Berikutnya bisa diatur akses yang akan dimiliki oleh user tersebut terhadap shared folder yang dipilih pada kotak-kotak centang pada kolom Files dan Directories.

![Add Shared Folder FileZilla Server](images/fz_server_add_shared_folder.png)

Server untuk FTP berhasil dibuat.

#### 3.4.2 Koneksi dari Client

##### a. Menggunakan Filezilla client
Buka FileZilla dan masukkan *Host*, *Username*, *Password*, dan *Port* dari server yang akan disambungkan. Bila sudah yakin, klik *Quickconnect* untuk menyambungkan.

![Login FileZilla](images/filezilla_connect.JPG)

##### b. Menggunakan command Linux
`$ ftp [Host ip]`
Masukkan username dan password, kemudian jalankan seperti CLI

Saat hasil capture dari Wireshark dilihat, akan muncul data di bawah ini:

![Login FileZilla](images/fz_login_wireshark.JPG)

| Perintah | Keterangan |
|---|---|
| USER | Username yang digunakan untuk login ke FTP server |
| PWD | Password yang digunakan untuk login ke FTP server |)

#### 3.4.3 Upload File
##### a. Menggunakan Filezilla client
Untuk FileZilla drag file dari Local site lalu drop di Remote site

| Perintah | Keterangan |
|---|---|
| STOR | Meng-upload file ke FTP server |

##### b. Menggunakan command Linux
Command upload untuk linux
```
$ put [full path file]
```

Saat hasil capture dilihat akan muncul data dibawah ini :

![STOR](images/stor.JPG)

#### 3.4.4 Download File
##### a. Menggunakan Filezilla client
Untuk Filezilla drag file dari Remote site ke Local site

| Perintah | Keterangan |
|---|---|
| RETR | Men-download suatu file dari FTP server |

##### b. Menggunakan command Linux
Command download untuk linux
```
$ get [nama file]
```

Saat hasil capture dilihat akan muncul data dibawah ini :

![STOR](images/retr.JPG)

## 4. Termshark
Jika sebelumnya kita sudah menggunakan Wireshark, sekarang kita akan menggunakan tools bernama **Termshark**. Pada dasarnya, Termshark merupakan wrapper dari tshark yang memungkinkan kita untuk menganalisis lalu lintas jaringan melalui terminal tanpa memerlukan GUI. Fitur-fitur pada Termshark mirip dengan Wireshark. Banyak command-command Wireshark yang juga bisa digunakan pada Termshark.

### 4.1 Instalasi Termshark
Termshark merupakan binary standalone yang dapat di download langsung pada GitHub [Termshark Releases](https://github.com/gcla/termshark/releases). Pada saat penulisan modul ini, versi paling terbaru dari Termshark merupakan versi *v2.4.0*, atau menggunakan package manager seperti `apt`:
```sh
sudo apt install termshark
```

### 4.2 Penggunaan Termshark
Untuk menggunakan Termshark, kita dapat menjalankan perintah berikut di terminal:
```sh
$ termshark
```
Maka akan muncul tampilan seperti berikut:

![termshark-init](images/termshark-init.png)

Secara default, Termshark akan melakukan packet capture pada interface eth0.

Termshark juga dapat melakukan packet capture pada interface lain dengan menggunakan opsi `-i` diikuti dengan nama interface yang diinginkan.
```sh
$ termshark -i [nama_interface]
```
![termshark-interface](images/termshark-interface.png)

Termshark juga dapat melakukan inspeksi file pcap/pcapng dengan menggunakan opsi `-r` diikuti dengan nama file yang ingin dianalisis.
```sh
$ termshark -r [nama_file.pcap]
```
Kita juga dapat melakukan filtering packet seperti pada Wireshark, command-command yang digunakan sangat mirip dengan Wireshark. Kalian bisa refer command-command yang ada pada section [3.2 Filters](#32-filters) di atas.

Disini kita akan mencoba untuk melakukan request ke http://example.com dan hanya filter traffic http:

```sh
#!/bin/bash
while true; do
  curl -s http://example.com >/dev/null 2>&1
  sleep 10
done &
```
Jalankan script diatas lalu buka **Termshark** dan filter dengan `http`.

Maka akan terlihat traffic http ke http://example.com

![termshark-http](images/termshark-http.png)

Untuk petunjuk penggunaan lebih lengkap, kita bisa merujuk ke [dokumentasi Termshark](https://github.com/gcla/termshark/blob/master/docs/UserGuide.md).

## Latihan
1. Apakah perbedaan capture filter dan display filter pada wireshark berdasarkan paket yang ditangkap?
2. Apa perbedaan filter `ip.dst` dengan `ip.dst_host`
3. Lakukan `ping` pada `1.1.1.1` (server dns cloudflare), terapkan display filter yang menampilkan paket-paket yang bersangkutan, lalu carilah apa protokol yang digunakan!
4. Buka halaman `http://example.com/index.html` dan dapatkan source file `index.html` nya mengunakan wireshark!


## Referensi
+ https://nyengnyeng.com/macam-macam-kabel-jaringan-komputer/
+ http://haidirhmc.blogspot.com/2011/12/urutan-warna-kabel-lan-atau-kabel-t568a.html
+ https://www.nesabamedia.com/pengertian-dan-fungsi-kabel-utp/
+ https://www.berguruit.com/2017/09/cara-crimping-kabel-lan-rj45-yang-baik.html
+ https://www.wireshark.org/docs/wsug_html_chunked/ChapterIntroduction.html
+ https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html
+ https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html
+ https://computer.howstuffworks.com/question5251.htm]
+ https://www.comparitech.com/net-admin/difference-between-straight-through-crossover-rollover-cables/
+ https://www.indowebsite.co.id/kb/cara-mengaktifkan-ftp-pada-localhost-atau-xammp/
+ https://github.com/gcla/termshark