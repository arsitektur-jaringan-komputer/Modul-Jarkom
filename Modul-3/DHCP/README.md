# 1. Dynamic Host Configuration Protocol (DHCP)

## Outline

- [1. Dynamic Host Configuration Protocol (DHCP)](#1-dynamic-host-configuration-protocol-dhcp)
  - [Outline](#outline)
  - [1.1 Konsep](#11-konsep)
    - [1.1.1 Pendahuluan](#111-pendahuluan)
    - [1.1.2 Apa itu DHCP?](#112-apa-itu-dhcp)
    - [1.1.3 Bootstrap Protocol dan DHCP](#113-bootstrap-protocol-dan-dhcp)
    - [1.1.4 DHCP Message Header](#114-dhcp-message-header)
    - [1.1.5 Cara Kerja DHCP](#115-cara-kerja-dhcp)
  - [1.2 Implementasi](#12-implementasi)
    - [1.2.1 Instalasi ISC-DHCP-Server](#121-instalasi-isc-dhcp-server)
    - [1.2.2 Konfigurasi DHCP Server](#122-konfigurasi-dhcp-server)
    - [1.2.3 Konfigurasi DHCP Client](#123-konfigurasi-dhcp-client)
    - [1.2.4 Fixed Address](#124-fixed-address)
    - [1.2.5 Testing](#125-testing)
  - [Soal Latihan](#soal-latihan)
  - [Referensi](#referensi)

## 1.1 Konsep

### 1.1.1 Pendahuluan

Pada modul-modul sebelumnya, kita telah mempelajari cara mengonfigurasi IP, nameserver, gateway, dan subnetmask pada UML secara manual. Metode manual ini oke-oke saja saat diimplementasikan pada jaringan yang memiliki sedikit host. Tapi bagaimana jika jaringan tersebut memiliki banyak host? Jaringan WiFi umum misalnya. Apakah Administrator Jaringannya harus mengonfigurasi setiap host-nya satu per satu? Membayangkannya saja mengerikan, ya.

Di sinilah peran DHCP sangat dibutuhkan.

### 1.1.2 Apa itu DHCP?

**Dynamic Host Configuration Protocol (DHCP)** adalah protokol berbasis arsitektur _client-server_ yang dipakai untuk memudahkan pengalokasian alamat IP dalam satu jaringan. DHCP secara otomatis akan meminjamkan alamat IP kepada host yang memintanya.

![cara kerja DHCP](images/cara-kerja.png)

Tanpa DHCP, administrator jaringan harus memasukkan alamat IP masing-masing komputer dalam suatu jaringan secara manual. Namun jika DHCP dipasang di jaringan, maka semua komputer yang tersambung ke jaringan akan mendapatkan alamat IP secara otomatis dari DHCP server.

### 1.1.3 Bootstrap Protocol dan Dynamic Host Configuration Protocol

Selain DHCP, terdapat protokol lain yang juga memudahkan pengalokasian alamat IP dalam suatu jaringan, yaitu Bootstrap Protocol (BOOTP). Perbedaan BOOTP dan DHCP terletak pada proses konfigurasinya.

| BOOTP                                                                                       | DHCP                                                                                                                                               |
| ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrator jaringan melakukan konfigurasi mapping MAC Address client dengan IP tertentu. | Server akan melakukan peminjaman IP Address dan konfigurasi lainnya dalam rentang waktu tertentu. Protokol ini dibuat berdasarkan cara kerja BOOTP |

### 1.1.4 DHCP Message Header

![DHCP header](images/DHCP-message-header.png)

![DHCP header legend](images/DHCP-message-header-keterangan.png)

### 1.1.5 Cara Kerja DHCP

DHCP bekerja dengan melibatkan dua pihak yakni **Server** dan **Client**:

1. **DHCP Server** memberikan suatu layanan yang dapat memberikan alamat IP dan parameter lainnya kepada semua client yang memintanya.
2. **DHCP Client** adalah mesin client yang menjalankan perangkat lunak client yang memungkinkan mereka untuk dapat berkomunikasi dengan DHCP server.
   DHCP Server umumnya memiliki sekumpulan alamat IP yang didistribusikan yang disebut DHCP Pool. Setiap client akan meminjamnya untuk rentan waktu yang ditentukan oleh DHCP sendiri (dalam konfigurasi). Jika masa waktu habis, maka client akan meminta alamat IP yang baru atau memperpanjangnya. Itulah sebabnya alamat IP client menjadi dinamis.

![Cara kerja DHCP](images/DHCP.gif)

Terdapat 5 tahapan yang dilakukan dalam proses peminjaman alamat IP pada DHCP:

1. **DHCPDISCOVER**: Client menyebarkan request secara broadcast untuk mencari DHCP Server yang aktif. DHCP Server menggunakan UDP port 67 untuk menerima broadcast dari client melalui port 68.
2. **DHCPOFFER**: DHCP server menawarkan alamat IP (dan konfigurasi lainnya apabila ada) kepada client. Alamat IP yang ditawarkan adalah salah satu alamat yang tersedia dalam DHCP Pool pada DHCP Server yang bersangkutan.
3. **DHCPREQUEST**: Client menerima tawaran dan menyetujui peminjaman alamat IP tersebut kepada DHCP Server.
4. **DHCPACK**: DHCP server menyetujui permintaan alamat IP dari client dengan mengirimkan paket ACKnoledgment berupa konfirmasi alamat IP dan informasi lain. Kemudian client melakukan inisialisasi dengan mengikat (binding) alamat IP tersebut dan client dapat bekerja pada jaringan tersebut. DHCP Server akan mencatat peminjaman yang terjadi.
5. **DHCPRELEASE**: Client menghentikan peminjaman alamat IP (apabila waktu peminjaman habis atau menerima DHCPNAK).

![Flowchart cara kerja DHCP](images/cara-kerja-2.png)

Lebih lanjut: [https://www.nada.kth.se/kurser/kth/2D1392/05/lectures/lecture_9.pdf](https://www.nada.kth.se/kurser/kth/2D1392/05/lectures/lecture_9.pdf)
Video: [https://youtu.be/S43CFcpOZSI](https://youtu.be/S43CFcpOZSI)

## 1.2 Implementasi

### 1.2.1 Instalasi ISC-DHCP-Server

Pada topologi ini, kita akan menjadikan router **Foosha** sebagai DHCP Server. Oleh sebab itu, kita harus meng-_install_ **isc-dhcp-server** di **Foosha** dengan melakukan langkah-langkah berikut:

1. Update _package lists_ di router **Foosha** dengan perintah

```
apt-get update
```

2. Install **isc-dhcp-server** di router **Foosha**

```
apt-get install isc-dhcp-server
```

3. Pastikan **isc-dhcp-server** telah terinstall dengan perintah

```
dhcpd --version
```

![image](https://user-images.githubusercontent.com/61197343/139392770-655e93b6-70f9-4cd9-8d67-8323b9cd25dc.png)


### 1.2.2 Konfigurasi DHCP Server

Langkah-langkah yang harus dilakukan setelah instalasi adalah:

#### A. Menentukan interface mana yang akan diberi layanan DHCP

##### A.1. Buka file konfigurasi interface

Silakan edit file konfigurasi isc-dhcp-server pada `/etc/default/isc-dhcp-server`

##### A.2. Tentukan interface

Coba perhatikan topologi yang telah kalian buat. Contoh dari topologi yang dibuat adalah interface dari router **Foosha** yang menuju ke switch kiri adalah `eth1`, maka kita akan memilih interface `eth1` untuk diberikan layanan DHCP.

![image](https://user-images.githubusercontent.com/61197343/139393762-9f2f6df2-489d-42bc-84bf-e2270b74f71f.png)

#### B. Melakukan konfigurasi pada isc-dhcp-server

Ada banyak hal yang dapat dikonfigurasi, antara lain:

- Range IP
- DNS Server
- Informasi Netmask
- Default Gateway
- dll.

##### B.1. Buka file konfigurasi DHCP dengan perintah

Edit file konfigurasi isc-dhcp-server pada `/etc/dhcp/dhcpd.conf`

##### B.2. Tambahkan script berikut

```conf
subnet 'NID' netmask 'Netmask' {
    range 'IP_Awal' 'IP_Akhir';
    option routers 'iP_Gateway';
    option broadcast-address 'IP_Broadcast';
    option domain-name-servers 'DNS_yang_diinginkan';
    default-lease-time 'Waktu';
    max-lease-time 'Waktu';
}
```

Script tersebut mengatur parameter jaringan yang dapat didistribusikan oleh DHCP, seperti informasi netmask, default gateway dan DNS server. Berikut ini beberapa parameter jaringan dasar yang biasanya digunakan:

| **No** | **Parameter Jaringan**                             | **Keterangan**                                                                                                                                                                                                                                                                                         |
| ------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1      | `subnet 'NID'`                                     | Network ID pada subnet interface. Sederhananya pada kasus pembelajaran praktikum kita, nilai NID merupakan 3 bytes dari IP interface tujuan (sesuai dengan langkah [A2](#a2-tentukan-interface)) **pada router** (dalam kasus ini adalah Foosha) dengan byte terakhirnya adalah 0. Contoh, jika interface yang kamu pilih adalah `eth1` dengan IP 10.9.0.1, maka NID subnetnya adalah 10.9.0.0. **NB: Cara menentukan NID yang proper akan dijelaskan pada modul berikutnya**                                                                                                                                                                                                                                                                                   |
| 2      | `netmask 'Netmask`                                 | Netmask pada subnet. Dapat dilihat pada konfigurasi network router dengan cara: Ke topologi (GNS3) → klik kanan router → Configure → Edit Network Configuration → Lihat nilai netmask pada interface yang diinginkan                                                                                                                                                                                                                                                                                    |
| 3      | `range 'IP_Awal' 'IP_Akhir'`                       | Rentang alamat IP yang akan didistribusikan dan digunakan secara dinamis                                                                                                                                                                                                                               |
| 4      | `option routers 'Gateway'`                         | IP gateway dari router menuju client sesuai konfigurasi subnet                                                                                                                                                                                                                                         |
| 5      | `option broadcast-address 'IP_Broadcast'`          | IP broadcast pada subnet                                                                                                                                                                                                                                                                               |
| 6      | `option domain-name-servers 'DNS_yang_diinginkan'` | DNS yang ingin kita berikan pada client                                                                                                                                                                                                                                                                |
| 7      | Lease time                                         | Waktu yang dialokasikan ketika sebuah IP dipinjamkan kepada komputer client. Setelah waktu pinjam ini selesai, maka IP tersebut dapat dipinjam lagi oleh komputer yang sama atau komputer tersebut mendapatkan alamat IP lain jika alamat IP yang sebelumnya dipinjam, dipergunakan oleh komputer lain |
| 8      | `default-lease-time 'Waktu'`                       | Lama waktu DHCP server meminjamkan alamat IP kepada client, dalam satuan detik. Default 600 detik                                                                                                                                                                                                      |
| 9      | `max-lease-time 'Waktu'`                           | Waktu maksimal yang di alokasikan untuk peminjaman IP oleh DHCP server ke client dalam satuan detik. Default 7200 detik                                                                                                                                                                                |

Pada contoh berikut, kita akan menggunakan DNS 202.46.129.2. Maka konfigurasinya menjadi:

![image](https://user-images.githubusercontent.com/61197343/139402619-96aaa7ee-896e-4632-b80c-621d0a8781b8.png)

##### A.3. Restart service `isc-dhcp-server` dengan perintah

```
service isc-dhcp-server restart
```

Jika terjadi **failed!**, maka service harus dihentikan dulu (stop), kemudian jalankan kembali (start)

Untuk memastikan isc-dhcp-server berjalan, silakan gunakan perintah


```
service isc-dhcp-server status
```

Selamat 🎉
Konfigurasi DHCP Server selesai!

---

### 1.2.3 Konfigurasi DHCP Client

Setelah mengonfigurasi server, kita juga perlu mengonfigurasi interface client supaya bisa mendapatkan layanan dari DHCP server. Di dalam topologi ini, clientnya adalah **Alabasta**, **Loguetown**, dan **Jipangu**.

#### A. Mengonfigurasi Client

##### A.1. Periksa IP Alabasta dengan `ip a`

![image](https://user-images.githubusercontent.com/61197343/139403919-e197fc94-8146-4b2b-812e-b2d4cbc70dda.png)

Dari konfigurasi sebelumnya, **Alabasta** telah diberikan IP statis 192.168.1.3

##### A.2. Buka `/etc/network/interfaces` untuk mengonfigurasi interface **Alabasta**

Silakan edit file `/etc/network/interfaces`


##### A.3. Comment atau hapus konfigurasi yang lama (konfigurasi IP statis)

Lalu tambahkan:

```
auto eth0
iface eth0 inet dhcp
```

![image](https://user-images.githubusercontent.com/61197343/139404262-352673c1-c1f7-4d51-8ba0-b5c2d8919cda.png)

**Keterangan**:

- **eth0** adalah interface yang digunakan client
- `iface eth0 inet dhcp`: memberikan konfigurasi DHCP pada interface eth0, bukan konfigurasi statis

##### A.4. Restart Alabasta

Untuk melakukan restart Alabasta, silakan menuju GNS3 → klik kanan Alabasta → klik Stop → klik kanan kembali Alabasta → klik Start.


#### B. Testing

Cek kembali IP **Alabasta** dengan menjalankan `ip a`

![image](https://user-images.githubusercontent.com/61197343/139404826-8740d662-c2e8-44cd-901b-1398ad328fce.png)

Periksa juga apakah **Alabasta** sudah mendapatkan DNS server sesuai konfigurasi di DHCP Server. Periksa `/etc/resolv.conf` dengan menggunakan perintah

![image](https://user-images.githubusercontent.com/61197343/139404948-a7c6aea2-4557-4c41-997d-732c893b487e.png)

Bila IP dan nameserver **Alabasta** telah berubah sesuai dengan konfigurasi yang diberikan oleh DHCP, maka selamat 🎉🎉
Kalian telah berhasil!

**Keterangan**:

- Jika IP **Alabasta** masih belum berubah, jangan panik. Silakan restart kembali node melalui halaman GNS3
- Jika masih belum berubah juga, jangan buru-buru bertanya. Coba periksa lagi semua konfigurasi yang telah kalian lakukan, mungkin terdapat kesalahan penulisan.

#### C. Lakukan kembali langkah - langkah di atas pada client Loguetown dan Jipangu

- Client **Loguetown** dan **Jipangu**

![image](https://user-images.githubusercontent.com/61197343/139405760-ff97af44-1e02-4dde-b67c-4816e8a0c786.png)


Setelah IP dipinjamkan ke sebuah client, maka IP tersebut tidak akan diberikan ke client lain. Buktinya, tidak ada client yang mendapatkan IP yang sama.

---

### 1.2.4 Fixed Address

![](https://thumbs.gfycat.com/FalseNiftyCrab-max-1mb.gif)

> **Studi Kasus**:
>
> Ternyata kapal milik Franky yang diparkir di **Jipangu** selain menjadi client, juga akan digunakan sebagai server suatu aplikasi jual beli kapal, sehingga akan menyulitkan jika alamat IPnya berganti-ganti setiap **Jipangu** terhubung ke jaringan internet. Oleh karena itu, **Jipangu** membutuhkan IP yang tetap dan tidak berganti-ganti.

Masalah yang dihadapi oleh Franky adalah IP address dari Jipangu yang berganti-ganti. Sehingga, requirementnya adalah IP address yang tetap. Oleh karena itu, solusi yang dapat ditawarkan adalah dengan fitur dari DHCP Server, yaitu layanan untuk "menyewakan" alamat IP secara tetap pada suatu host, yakni **Fixed Address**. Dalam kasus ini, **Jipangu** akan mendapatkan IP tetap 192.168.1.13

#### A. Konfigurasi DHCP Server di router Foosha

##### A.1. Buka file konfigurasi isc-dhcp-server

Buka dan edit file `/etc/dhcp/dhcpd.conf`

##### A.2. Tambahkan script berikut

```
host Jipangu {
    hardware ethernet 'hwaddress_milik_Jipangu';
    fixed-address 192.168.0.13;
}
```

![image](https://user-images.githubusercontent.com/61197343/139408258-00413d72-cd37-4a6f-8df8-8af62ac81dc2.png)

**Penjelasan**:

- Untuk mencari `hwaddress_milik_Jipangu` (hardware address milik Jipangu), kamu bisa mengeksekusi perintah `ip a` di Jipangu, kemudian lihat interface yang berhubungan dengan router, dalam kasus ini adalah `eth0`, dan lihat pada bagian `link/ether`. Silakan copy address tersebut dan masukkan pada konfigurasi isc-dhcp-server di Foosha.

![image](https://user-images.githubusercontent.com/61197343/139408469-54699b15-3ce3-43e0-828a-5a1fdef434e5.png)

- **fixed-address** adalah alamat IP yang "disewa" tetap oleh **Jipangu**

##### A.3. Restart service `isc-dhcp-server` pada **Foosha**


#### B. Konfigurasi DHCP Client

##### B.1. Konfigurasi network interface **Jipangu**

Network interface dapat diakses pada `/etc/network/interfaces`


##### B.2. Tambah konfigurasi berikut

```
hwaddress ether 'hwaddress_milik_Jipangu'
```

![image](https://user-images.githubusercontent.com/61197343/139409129-4ced81d2-2248-4582-ade5-bbba00aaf434.png)

**Keterangan**:
Hardware addresss perlu di-_setting_ juga di `/etc/network/interfaces` untuk mencegah bergantinya hwaddress saat project GNS3 dimatikan atau diexport.

#### B.3. Restart node Jipangu

Silakan restart node Jipangu di halaman GNS3

#### C. Testing

Periksa IP **Jipangu** dengan melakukan `ip a`

![image](https://user-images.githubusercontent.com/61197343/139409496-78bc3496-a836-4ec9-9aa6-c4dfa778d32d.png)

IP **Jipangu** telah berubah menjadi 192.168.0.13 sesuai dengan Fixed Address yang diberikan oleh DHCP Server.

👋👋👋

---

### 1.2.5 Menguji Konfigurasi DHCP pada Topologi

Setelah melakukan berbagai konfigurasi di atas, kalian bisa memastikan apakah DHCP Server kalian berhasil dengan cara:

1. Matikan semua node melalui halaman GNS3
2. Menyalakan kembali semua node
3. Lakukan perintah `ip a` pada setiap node

Jika node client berganti alamat IP sesuai dengan range yang telah dikonfigurasi pada DHCP Server dan **Jipangu** tetap mendapatkan IP 192.168.0.13, maka konfigurasi DHCP server kalian berhasil.

## Soal Latihan

1. Buatlah konfigurasi DHCP agar Loguetown dan Alabasta mendapatkan IP dengan range [Prefix IP].0.100 - [Prefix IP].0.169 dan [Prefix IP].0.200 - [Prefix IP].0.202 dengan syarat:
Setiap 1 menit, IP pada client berubah dan juga DNS diarahkan ke DNS server kalian sendiri tetapi client tetap bisa digunakan untuk mengakses internet.

## Referensi
- [https://www.isc.org/dhcp/](https://www.isc.org/dhcp/)
- [http://www.tcpipguide.com/free/t_DHCPGeneralOperationandClientFiniteStateMachine.htm](http://www.tcpipguide.com/free/t_DHCPGeneralOperationandClientFiniteStateMachine.htm)


# Salam dari Foosha

<img src="https://c.tenor.com/6GdFsIPn71cAAAAS/faiz.gif" width="833" height="833">
