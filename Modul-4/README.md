# SUBNETTING AND ROUTING

-   [A. PENGENALAN](#a-pengenalan)
    -   [Istilah](#istilah)
    -   [IP Address](#ip-address)
    -   [Subnet](#subnet)
    -   [Network ID, Broadcast Address, dan Available Hosts](#network-id-broadcast-address-dan-available-hosts)
        -   [Network ID](#network-id)
        -   [Broadcast Address](#broadcast-address)
        -   [Available Hosts](#available-hosts)
    -   [IP Publik dan IP Privat](#ip-publik-dan-ip-privat)
-   [B. SUBNETTING](#b-subnetting)
    -   [Pengertian](#pengertian)
    -   [Perhitungan Subnet](#perhitungan-subnet)
        -   [A. Classful](#a-classful)
        -   [B. Classless](#b-classless)
            -   [1. VLSM (Variable Length Subnet Masking)](#vlsm-(variable-length-subnet-masking))
            -   [2. CIDR (Classless Inter Domain Routing)](#2-cidr-(classless-inter-domain-routing))
-   [C. ROUTING](#c-routing)
    -   [Pengertian](#pengertian)
    -   [Praktik](#praktik)
        -   [1) Membuat Topologi](#1-membuat-topologi)
        -   [2) Subnetting](#2-subnetting)
        -   [3) Routing](#3-routing)
        -   [4) Testing](#4-testing)
-   [LATIHAN!](#-latihan!)

## A. Pengenalan



### Istilah

| Istilah | Penjelasan |
|--|--|
| iface | Disebut network interface, antarmuka yang menghubungkan 2 layer protokol. Setiap interface memiliki nama yang berbeda  |
| eth0 | Salah satu nama interface yang digunakan untuk berhubungan dengan subnet |
| address | Sebuah alamat IP unik bagi komputer dalam sebuah jaringan |
| netmask | Kombinasi angka sepanjang 32 bit yang berfungsi membagi IP ke dalam subnet-subnet dan menentukan rentang alamat IP pada subnet yang bisa digunakan |
| gateway | Alamat IP yang menjadi pintu keluar menuju subnet lain, biasanya diisi alamat IP router terdekat |

**Mengapa Perlu Subnetting?**

Sebagai permisalan, wilayah Indonesia perlu dibagi menjadi bagian-bagian kecil (provinsi, kota, dan seterusnya). Tujuannya untuk memudahkan pemerintah dalam mengatur kebijakan sesuai kondisi dari daerah masing-masing. Hal tersebut juga yang terjadi pada jaringan internet. Jaringan mencakup seluruh koneksi antar komputer yang terhubung ke internet. Manfaat subnetting :

-   Meningkatkan efisiensi routing
-   Dapat mengatur kebijakan sendiri untuk keamanan jaringan
-   Mengurangi ukuran broadcast domain

**Mengapa Perlu Routing?**

Sebagai permisalan, ketika Anda ingin mengantar paket, maka perlu mencantumkan alamat tujuan. Kemudian Anda kirim ke kantor pos, lalu kantor pos akan mengirimkan paket ke alamat yang dituju. Agar paket sampai ditujuan yang benar, Pak Pos yang mengirimkan paket perlu mengetahui rute untuk mencapai tujuan paket tersebut, proses tersebut yang dinamakan _**routing**_. Yaitu, memberitahukan rute perjalanan kepada Pak Pos untuk mencapai alamat tujuan paket yang diantarkannya.

### IP Address

IP Address (Versi 4)

-   Alamat IP adalah suatu alamat unik yang diberikan untuk menandai sebuah komputer yang terhubung dalam suatu jaringan.
-   Alamat IP terdiri dari 32 bit biner yang dalam penulisannya dikonversi menjadi bilangan desimal.
-   Alamat IP (yang panjangnya 32 bit itu) dibagi menjadi 4 oktet (masing-masing oktet berisi 8 bit) dipisahkan dengan tanda titik.

### Subnet

![Gambar](gambar/1.png)


### Network ID, Broadcast Address, dan Available Hosts

Jika suatu PC memiliki alamat 10.151.36.5/24, maka informasi yang dapat digali dari IP tersebut adalah:

1.  Alamat IP
2.  Netmask
3.  Network ID (NID) : Sebuah alamat IP yang menjadi identitas untuk suatu area jaringan/subnet
4.  Broadcast Address : Sebuah alamat IP yang berperan untuk pengiriman pesan broadcast dalam suatu jaringan/subnet
5.  Available Hosts: Rentang alamat IP yang bisa digunakan dalam suatu jaringan/subnet

Contoh skenario: Carilah Network ID (NID), Broadcast Address, dan rentang alamat IP dari sebuah alamat 10.151.36.5/24!

Penyelesaian : Informasi sementara yang didapat dari 10.151.36.5/24 adalah

```
    1. IP : 10.151.36.5
    2. Netmask : 255.255.255.0 (/24)
    3. Network ID?
    4. Broadcast Address?
    5. Available Host?
```

Berikut akan dijelaskan bagaimana mencari NID, Broadcast Address, dan Available Host:

#### Network ID

Mencari Network ID (NID)

![Gambar](gambar/2.PNG)

#### Broadcast Address

Mencari Broadcast Address

![Gambar](gambar/3.PNG)

#### Available Hosts

Mencari rentang alamat IP

![Gambar](gambar/4.PNG)

### IP Publik dan IP Privat

Alamat IP dibagi menjadi 2 jenis, yaitu :

-   IP Publik = alamat IP yang digunakan dalam jaringan global Internet, cirinya alamat IP dapat diakses melalui internet secara langsung.
-   IP Privat = alamat IP yang digunakan (dikenali) dan hanya dapat diakses oleh jaringan lokal.

Rentang IP Privat :

-   10.0.0.0/8 (Class A)
-   172.16.0.0/12, 172.31.0.0/12 (Class B)
-   192.168.0.0/16 (Class C)

Rentang IP Publik adalah selain rentang IP Privat di atas.

## B. SUBNETTING

### Pengertian

**Subnet** adalah suatu sub jaringan dari jaringan yang lebih besar. Dengan adanya subnet, kita dapat melakukan manajemen suatu jaringan dengan lebih baik.

**Tujuan** utama kita belajar subnetting adalah **pembagian alamat IP untuk kebutuhan tertentu**. Contohnya pada gedung Departemen Informatika dimana terdapat beberapa laboratorium, dan setiap laboratorium memiliki lebih dari 1 komputer yang harus dikonfigurasikan sedemikian rupa agar dapat saling berkomunikasi dan mengakses internet.

Dari contoh tersebut, muncullah salah satu konfigurasi paling dasar dalam penyelesaian permasalahan ini yaitu pembagian alamat IP untuk setiap laboratorium di gedung Departemen Informatika, seperti :

1.  Laboratorium LP memiliki jaringan dengan subnet **10.151.34.0/24**
2.  Laboratorium AJK memiliki jaringan dengan subnet **10.151.36.0/24**

### Perhitungan Subnet

Ada dua metode pembagian IP yang dikenal dalam jaringan, yaitu Classful

#### A. Classful

Pembagian IP dengan menggunakan metode ini didasarkan pada pembagian class pada alamat IP. Tiap subnet akan diberikan ukuran atau netmask yang dapat menampung jumlah komputer/ host yang terdapat dalam subnet tersebut. Tabel berikut menunjukkan Class yang terdapat pada metode _**Classful**_.

| Class | Netmask | Jumlah Host |
|--|--|--|
| Class A | /8 | 16777216 |
| Class B | /16 | 65536 |
| Class C | /24 | 256 |

Contoh penerapan pembagian alamat IP dengan metode _**Classful**_ sebagai berikut.

![Gambar](gambar/Gambar1.PNG)

Anggap kita memiliki topologi jaringan seperti gambar di atas. Lalu, tentukan jumlah subnet yang ada di dalam topologi tersebut.

![Gambar](gambar/Gambar2.PNG)

Terdapat 8 subnet di dalam topologi. Dengan menggunakan teknik classful setiap subnet akan memiliki netmask /24 karena semua subnet memiliki jumlah host di bawah 256. Sehingga pembagian IP yang memungkinkan untuk topologi di atas adalah sebagai berikut.

![Gambar](gambar/8.PNG)

#### B. Classless

##### 1. VLSM (Variable Length Subnet Masking)

Inti utama dari penggunaan teknik VLSM adalah untuk mengefisienkan pembagian IP di dalam jaringan. Besar netmask disesuaikan dengan banyaknya komputer/ host yang membutuhkan alamat IP.

> Jadi, pada teknik **VLSM**, subnet mask (netmask) akan diberikan sesuai dengan kebutuhan jumlah alamat IP dari subnet tersebut.

Contoh penerapannya, kita akan menggunakan topologi seperti contoh metode _**Classful**_.

**Langkah 1** - Tentukan jumlah alamat IP yang dibutuhkan oleh tiap subnet dan lakukan _labelling_ netmask berdasarkan jumlah IP yang dibutuhkan.

| Subnet | Jumlah IP | Netmask |
|--|--|--|
| A1 | 101 | /25 |
| A2 | 2 | /30 |
| A3 | 51 | /26 |
| A4 | 2 | /30 |
| A5 | 2 | /30 |
| A6 | 2 | /30 |
| A7 | 11 | /28 |
| A8 | 21 | /27 |
| **Total** | **192** | **/24** |


Berdasarkan total IP dan netmask yang dibutuhkan, maka kita dapat menggunakan netmask **/24** untuk memberikan pengalamatan IP pada subnet.

**Catatan**

> Penentuan subnet mask (netmask) _**root**_ dalam pembagian IP tidak hanya berdasarkan **jumlah** IP yang dibutuhkan, tetapi perlu diperhatikan juga berapa banyak netmask yang dibutuhkan oleh subnet yang ada dalam topologi tersebut. Seperti pada contoh yang kita gunakan, karena netmask terbesar yang dibutuhkan adalah **/25** dan hanya terdapat 1 subnet yang membutuhkan subnet tersebut, maka pembagian IP dapat dilakukan mulai dari netmask **/24**.

**Langkah 2** - Subnet besar yang dibentuk memiliki NID **192.168.1.0** dengan netmask **/24**. Hitung pembagian IP berdasarkan NID dan netmask tersebut menggunakan pohon seperti gambar di bawah.

![Gambar](gambar/9.png)

**Langkah 3** - Lakukan subnetting dengan menggunakan pohon tersebut untuk pembagian IP sesuai dengan kebutuhan masing-masing subnet yang ada.

![Gambar](gambar/10.png)

Dari pohon dari pohon tersebut akan mendapat pembagian IP sebagai berikut.

![Gambar](gambar/11.PNG)

##### 2. CIDR (Classless Inter Domain Routing)

Perhitungan pada teknik CIDR juga didasarkan pada jumlah komputer/ host yang ada di dalam subnet. Tetapi cara mendapatkan subnet besar tidak sama dengan VLSM. Penerapan teknik CIDR dapat dilakukan dengan langkah sebagai berikut.

**Langkah 1** - Tentukan subnet yang ada dalam topologi dan lakukan _labelling_ netmask terhadap masing-masing subnet. Contohnya dapat dilihat pada gambar berikut.

![Gambar](gambar/Gambar2.PNG)

Langkah 2 - Gabungkan subnet paling bawah di dalam topologi. Paling bawah berarti subnet yang paling jauh dari internet (gambar awan). Maka pada topologi yang digunakan kali ini, subnet yang dapat digabungkan adalah A1 dengan A2 dan subnet A7 dengan A8. Subnet yang digabung tersebut akan membentuk sebuah subnet lebih besar dari subnet-subnet kecil yang ada di dalamnya. 

![Gambar](gambar/Gambar3.PNG)

Subnet **B1** merupakan hasil penggabungan dari subnet **A1** dan **A2**, Subnet **B2** merupakan hasil penggabungan dari subnet **A7** dan **A8**.

> _**Mengapa subnet B1 memiliki netmask /24? Dan subnet B2 memiliki netmask /26?**_

Perhatikan subnet **A1** dan **A2**. Subnet **A1** memiliki netmask /25, dan subnet **A2** memiliki netmask /30. Pada teknik **CIDR** subnet gabungan akan memiliki netmask yang **1 tingkat di atas subnet terbesar yang digabungkan**. Berdasarkan contoh di atas A1 = /25 dan A2 = /30, maka jika dilakukan penggabungan akan menjadi subnet **B1** dengan netmask **/24**. Begitu pula dengan subnet B2.

Lalu ulangi langkah tersebut sampai menjadi sebuah subnet besar yang mencakup 1 topologi yang kita miliki.

![Gambar](gambar/Gambar4.PNG)
![Gambar](gambar/Gambar5.PNG)
![Gambar](gambar/Gambar6.PNG)

**Langkah 3** - Dari proses penggabungan yang telah dilakukan, didapatkan sebuah subnet besar dengan netmask **/21**. Kali ini dapat menggunakan NID **192.168.0.0**, netmask **255.255.248.0**.

**Langkah 4** - Hitung pembagian IP dengan pohon berdasarkan penggabungan subnet yang telah dilakukan.

![Gambar](gambar/17.PNG)

> **Catatan**

> **Perbedaan** antara pohon VLSM dengan pohon CIDR adalah ketika satu subnet diturunkan, netmask yang akan terbentuk **disesuaikan dengan penggabungan subnet** yang telah dilakukan sebelumnya. Sebagai contoh, dari netmask besar /21, pada teknik VLSM akan dibagi dua menjadi masing-masing /22. Namun pada penggabungan yang dilakukan sebelumnya, /21 dihasilkan dari penggabungan /22 dan /24 maka subnet yang terbentuk memiliki netmask /22 dan /24.

**Langkah 5** - Berdasarkan penghitungan, maka didapatkan pembagian IP sebagai berikut.

![Gambar](gambar/18.PNG)

Jika kalian menggunakan CIDR maka netmask yang terbentuk akan menjadi lebih besar dibandingkan dengan menggunakan VLSM. Tetapi salah satu **keunggulan** teknik **CIDR** adalah ketika terdapat subnet baru yang ditambahkan dalam topologi, **tidak perlu melakukan penghitungan kembali** karena kemungkinan besar masih ada interval (_range_) IP yang tidak terpakai. Selain itu, teknik CIDR juga mengefisienkan _routing_ karena umumnya tabel routing yang dimiliki lebih sederhana dibandingkan teknik VLSM.

## C. ROUTING

### Pengertian

Setelah mengetahui bagaimana cara _**Subnetting**_ suatu jaringan dan metode pembagian IP, terdapat satu hal lain yang perlu diketahui yaitu _**Routing**_.

Dalam perkembangan dunia jaringan muncul banyak protokol _routing_ yang dapat memudahkan administrator jaringan karena dapat memperbarui tabel routingnya secara otomatis, teknik tersebut dinamakan _**Dynamic Routing**_ (**Perutean Dinamis**). Beberapa protokol _routing_ dinamis terkenal antara lain RIP, RIP versi 2, EIGRP, dan OSPF. Protokol-protokol tersebut tidak dipelajari pada modul ini, namun dapat dipelajari lebih lanjut pada mata kuliah TAJ di semester 7 (gasal).

Routing yang dibahas yaitu _**Static Routing**_ (**Perutean Statis**), yang mengharuskan administrator jaringan untuk menambahkan/ memberitahukan rute (_route_) baru ke dalam tabel routing ketika terdapat subnet tambahan dalam jaringannya.

Konsep _static routing_ sederhana, daftarkan NID dan netmask yang ada serta tentukan gateway untuk menuju ke subnet tersebut. Untuk mencoba teknik _routing static_, kita akan menggunakan aplikasi **Cisco Packet Tracer**.

### Praktik

Buka aplikasi Cisco Packet Tracer, kita akan membuat topologi baru.

#### 1) Membuat Topologi

![Gambar](gambar/Gambar1.PNG)

Silakan buat topologi menggunakan **Cisco Packet Tracer**. Untuk menambahkan Router, Switch, dan PC dapat dilakukan dengan _drag and drop_ yang ada pada menu. Pada praktik kali ini, sesuaikan _device_ dengan pilihan dengan kotak merah pada gambar di bawah

-   untuk menambahkan Cloud

![Gambar](gambar/20.png)

-   untuk menambahkan Router

![Gambar](gambar/21.png)

-   untuk menambahkan Switch

![Gambar](gambar/22.png)

-   untuk menambahkan PC

![Gambar](gambar/23.png)

-   untuk menambahkan Cable

![Gambar](gambar/24.png)

-   jika terdapat peringatan (_alert_) ketika menyambungkan kabel antar device, tambahkan port pada router terlebih dahulu.

![Gambar](gambar/Venusaur4.PNG)

Pada UML, buatlah topologi tersebut seperti yang telah diajarkan pada [modul pengenalan UML](https://github.com/afrchmdi/Jarkom-Modul-Pengenalan-UML) dengan **catatan** setiap _device_ yang akan terhubung **harus** dihubungkan menggunakan _**switch**_.


#### 2) Subnetting

Praktik kali ini akan menerapkan cara routing untuk teknik _subnetting_ **VLSM** yang telah kita lakukan sebelumnya.

![Gambar](gambar/Gambar2.PNG)

![Gambar](gambar/27.png)

Atur IP untuk masing-masing **interface** yang ada di setiap _device_ sesuai dengan pembagian subnet pada pohon **VLSM**.

Pada UML, buka /etc/network/interfaces untuk mengatur interface pada setiap perangkat.

Pada CPT, interface dapat diatur pada menu **Config** > **INTERFACE** > **“nama interface”** (contoh: FastEthernet0/0). Isi alamat IP dan subnet mask dari subnet interface tersebut. Berikut contoh untuk mengatur IP pada subnet **A4**.

Atur IP pada interface PIKACHU yang mengarah ke VENUSAUR dengan **192.168.1.5**.

![Gambar](gambar/Pikachu.PNG)

Atur IP pada interface VENUSAUR yang mengarah ke PIKACHU dengan **192.168.1.6**.

![Gambar](gambar/Venusaur.PNG)

Selanjutnya atur IP pada subnet A3. Atur IP pada interface VENUSAUR yang mengarah ke _client_ dengan **192.168.1.65**.

![Gambar](gambar/Venusaur2.PNG)

Atur IP pada _client_ (nama UML nya) dengan cara :

-   Masuk ke _client_
-   Pilih tab Desktop
-   Pilih IP Configuration

![Gambar](gambar/Klien1.png)

![Gambar](gambar/Klien2.png)

Lakukan hal yang sama untuk mengatur alamat IP setiap _**interface**_ pada device yang ada dalam topologi. Setelah selesai, lakukan langkah selanjutnya yaitu _**Routing**_ agar topologi dapat berfungsi dengan semestinya.

#### 3) Routing

Pada CPT, _**Routing**_ dapat dilakukan pada menu **Config** > **Routing** > **Static** pada device **Router**. Lalu isi **Static Routes** seperti gambar dibawah pada PIKACHU dan tekan tombol **Add**

![Gambar](gambar/Pikachu2.PNG)

Pada _static routing_ juga dibutuhkan _**default routing**_ agar router dapat mengirimkan paket sesuai dengan tujuan. Default routing dibutuhkan untuk router yang berada di bawah router utama (router yang terhubung internet), contohnya VENUSAUR

![Gambar](gambar/Venusaur3.PNG)

_**Keterangan**_ :

1.  Network 192.168.1.64 adalah Network ID yang akan dihubungkan
2.  Mask 255.255.255.192 adalah netmask dari subnet A3
3.  Next Hop 192.168.1.65 (disebut **gateway**), adalah IP yang dituju ketika ingin menuju subnet poin 1, yaitu interface pada VENUSAUR yang mengarah ke PIKACHU

Pada **UML**, _routing_ dilakukan pada device _**router**_ dengan perintah :

```
route add -net <NID subnet> netmask <netmask> gw <IP gateway>

```

Lalu lihat hasil _routing_ dengan perintah :

```
route -n

```

Maka sekarang, (nama UML nya) dan _host_ pada (nama UML nya) sudah saling terhubung. Agar semua subnet dapat saling terhubung, tambahkan _static routing_ berikut :

1.  Pada PIKACHU
    
    ```
     Network 192.168.1.128 Netmask 255.255.255.128 Next Hop 192.168.1.6
     Network 192.168.1.0 Netmask 255.255.255.252 Next Hop 192.168.1.6
     Network 192.168.1.12 Netmask 255.255.255.252 Next Hop 192.168.1.10
     Network 192.168.1.16 Netmask 255.255.255.240 Next Hop 192.168.1.10
     Network 192.168.1.32 Netmask 255.255.255.224 Next Hop 192.168.1.10
    
    ```
    
2.  Pada VENUSAUR
    
    ```
     Network 192.168.1.128 Netmask 255.255.255.128 Next Hop 192.168.1.2
    
    ```
    
3.  Pada CHARIZAD
    
    ```
     Network 0.0.0.0 Netmask 0.0.0.0 Next Hop 192.168.1.1
    
    ```
    
4.  Pada BLASTOISE
    
    ```
     Network 0.0.0.0 Netmask 0.0.0.0 Next Hop 192.168.1.9
     Network 192.168.1.16 Netmask 255.255.255.240 Next Hop 192.168.1.14
     Network 192.168.1.32 Netmask 255.255.255.224 Next Hop 192.168.1.14
    
    ```
    
5.  Pada ARCEUS
    
    ```
     Network 0.0.0.0 Netmask 0.0.0.0 Next Hop 192.168.1.13
    
    ```
    

**Kesimpulannya**, untuk melakukan _static routing_ disesuaikan dengan daftar NID yang ada. Semakin banyak NID dalam suatu topologi, semakin banyak pula rute yang perlu ditambahkan ke router, maka diperlukan teknik pengelompokkan (_**Subnetting**_) yang tepat untuk menyederhanakan _**Routing**_.

#### 4) Testing

Untuk mengetesnya dapat dilakukan dengan cara ping dari client ke IP tujuan atau menggunakan tombol dengan ikon surat pada _toolbar_.

![Gambar](gambar/35.PNG)

### Latihan!

![Gambar](gambar/Latihan.PNG)

Implementasikan subnetting dan routing topologi di atas pada Cisco Packet Tracer dan UML menggunakan teknik subnetting yang berbeda! Contoh pada Cisco Packet Tracer menggunakan CIDR, pada UML menggunakan VLSM atau sebaliknya. (Untuk UML, tiap subnet diwakili satu client/komputer saja)
