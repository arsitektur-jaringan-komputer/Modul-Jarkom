# 2. Proxy Server
## Outline
- [2. Proxy Server](#2-proxy-server)
	- [Outline](#outline)
	- [2.1 Pengertian, Fungsi, dan Manfaat](#21-pengertian-fungsi-dan-manfaat)
		- [2.1.1 Pengertian](#211-pengertian) 
		- [2.1.2 Fungsi](#212-fungsi) 
		- [2.1.3 Manfaat](#213-manfaat)
		- [2.1.4 Software Proxy Server](#214-software-proxy-server)
		- [2.1.5 Cara Kerja](#215-cara-kerja)
	- [2.2 Implementasi](#22-implementasi)
		- [2.2.1 Instalasi Squid](#221-instalasi-squid)
		- [2.2.2 Konfigurasi Dasar Squid](#222-konfigurasi-dasar-squid)
		- [2.2.3 Membuat User Login](#223-membuat-user-login)
		- [2.2.4 Pembatasan Waktu Akses](#224-pembatasan-waktu-akses)
		- [2.2.5 Pembatasan Waktu Akses ke Website Tertentu](#225-pembatasan-waktu-akses-ke-website-tertentu)
		- [2.2.6 Pembatasan Bandwith](#226-pembatasan-bandwidth)
	- [2.3 Soal Latihan](#23-soal-latihan)
	

##  2.1 Pengertian, Fungsi, dan Manfaat
### 2.1.1 Pengertian
Proxy server adalah sebuah server atau program komputer yang berperan sebagai penghubung antara suatu komputer dengan jaringan internet. Atau dalam kata lain, proxy server adalah suatu jaringan yang menjadi perantara antara jaringan lokal dan jaringan internet. Program Internet seperti browser, download manager dan lain-lain berhubungan dengan proxy server, dan proxy server tersebut yang akan berkomunikasi dengan server lain di Internet.
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/proxy%20server.png)
Proxy server dapat berupa suatu sistem komputer ataupun sebuah aplikasi yang bertugas menjadi gateway atau pintu masuk yang menghubungan komputer kita dengan jaringan luar.

### 2.1.2 Fungsi
1.  _**Connection sharing**_  : Proxy bertindak sebagai gateway yang menjadi pembatas antara jaringan lokal dengan jaringan luar. Gateway bertindak juga sebagai sebuah titik dimana sejumlah koneksi dari pengguna lokal dan koneksi jaringan luar juga terhubung kepadanya. Oleh sebab itu, koneksi dari jaringan lokal ke internet akan menggunakan sambungan yang dimiliki oleh gateway secara bersama-sama (connection sharing).
    
2.  _**Filtering**_  : Proxy bisa difungsikan untuk bekerja pada layar aplikasi dengan demikian maka dia bisa berfungsi sebagai firewalll paket filtering yang dapat digunakan untuk melindungi jaringan lokal terhadap gangguan maupun ancaman serangan dari jaringan luar. Fungsi filtering ini juga dapat diatur atau dikonfigurasi untuk menolak akses terhadap situs web tertentu dan pada waktu- waktu tertentu juga.
    
3.  _**Caching**_  : Sebuah proxy server mempunyai mekanisme penyimpanan obyek-obyek yang telah diminta dari server-server yang ada di internet. Dengan mekanisme caching ini maka akan menyimpan objek-objek yang merupakan berbagai permintaan/request dari para pengguna yang di peroleh dari internet.

### 2.1.3 Manfaat
Proxy server memiliki manfaat-manfaat berikut ini:

-   Membagi koneksi
-   Menyembunyikan IP
-   Memblokir situs yang tidak diinginkan
-   Mengakses situs yang telah diblokir
-   Mengatur bandwith

### 2.1.4 Software Proxy Server
Beberapa contoh software proxy server yang sering digunakan adalah sebagai berikut:

1.  CCProxy
2.  WinGate
3.  Squid
4.  Nginx

### 2.1.5 Cara Kerja
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/cara-kerja-proxy.JPG)

## 2.2 Implementasi
Untuk praktikum jarkom kali ini, software proxy server yang digunakan adalah **Squid** dan UML yang digunakan sebagai proxy server adalah **MOJOKERTO**

### 2.2.1 Instalasi Squid
**Step 1** - Install squid3 pada UML  **MOJOKERTO**
```
apt-get install squid3
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/instalasi-squid.PNG)

**Step 2** - Cek status squid untuk memastikan bahwa Squid telah berjalan dengan baik
```
service squid status
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/squid-status.PNG)

Jika muncul status **ok** maka instalasi telah berhasil.

### 2.2.2 Konfigurasi Dasar Squid
**Step 1** - Backup terlebih dahulu file konfigurasi default yang disediakan Squid. 
```
mv /etc/squid/squid.conf /etc/squid/squid.conf.bak
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/backup-squid-config.PNG)

**Step 2** - Buat konfigurasi baru dengan mengetikkan 
```
nano /etc/squid/squid.conf
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/buat-config-squid.PNG)

**Step 3** - Kemudian, pada file config yang baru, ketikkan script :
```
http_port 8080
visible_hostname mojokerto
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/conf-squid-new.PNG)

**Keterangan:**

-   `http_port 8080`  : Port yang digunakan untuk mengakses proxy, dalam kasus ini adalah  **8080**. (Sintaks:  `http_port 'PORT_YANG_DIINGINKAN'`)
-   `visible_hostname mojokerto`  : Nama proxy yang akan terlihat oleh user (Sintaks:  `visible_hostname 'NAMA_YANG_DIINGINKAN'`)

**STEP 4**  - Restart squid dengan cara mengetikkan perintah:
```
service squid restart
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/restart-squid-1.PNG)

**STEP 5** - Ubah pengaturan proxy browser. Gunakan **MOJOKERTO** sebagai host dan isikan port **8080**. Pada OS Windows :
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/setting-proxy-system.PNG)

Kemudian cobalah untuk mengakses web **[http://its.ac.id](http://its.ac.id/)** (usahakan menggunakan mode **incognito/private**). Maka akan muncul halaman seperti berikut:
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/its-ac-id-error.PNG)

**Step 6** - Supaya bisa mengakses web **[http://its.ac.id](http://its.ac.id/)**, maka kalian harus menambah sebaris script pada konfigurasi squid. Buka kembali file konfigurasi tadi dan tambahkan baris berikut:
```
http_access allow all
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/allow-all-conf.PNG)

**Keterangan:**

-   `http_access allow all`  : Memperbolehkan semuanya untuk mengakses proxy via http. Pengaturan ini perlu ditambahkan karena pengaturan default squid adalah  **deny**  (Sintaks:  `http_access allow 'TARGET'`)
-   Untuk menolak koneksi, maka  **allow**  diganti dengan  **deny**.
- 
**Step 7** - **Simpan**  file konfigurasi tersebut, lalu  **restart**  squid. Refresh halaman web  **[http://its.ac.id](http://its.ac.id/)**.

Seharusnya halaman yang ditampilkan kembali normal.

### 2.2.3 Membuat User Login

**STEP 1**  - Install  `apache2-utils`  pada UML  **MOJOKERTO**. Sebelumnya kalian sudah harus melakukan  `apt-get update`. Ketikkan:
```
apt-get install apache2-utils
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/install-apache-utils.PNG)

**STEP 2**  - Buat user dan password baru. Ketikkan:
```
htpasswd -c /etc/squid3/passwd jarkom203
```
Ketikkan password yang diinginkan. Jika sudah maka akan muncul notifikasi:
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/add-userpass.PNG)

**STEP 3** - Edit konfigurasi squid menjadi:
```
http_port 8080
visible_hostname mojokerto

auth_param basic program /usr/lib/squid3/basic_ncsa_auth /etc/squid3/passwd
auth_param basic children 5
auth_param basic realm Proxy
auth_param basic credentialsttl 2 hours
auth_param basic casesensitive on
acl USERS proxy_auth REQUIRED
http_access allow USERS
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/conf-userpass.PNG)

**Keterangan:**

-   `auth_param`  digunakan untuk mengatur autentikasi (Sintaks:  `auth_param 'SCHEME' 'PARAMETER' 'SETTING'`. Lebih lengkapnya di  [http://www.squid-cache.org/Doc/config/auth_param/](http://www.squid-cache.org/Doc/config/auth_param/)).
-   `program`  : Perintah untuk mendefiniskan autentikator eksternal.
-   `children`  : Mendefinisikan jumlah maksimal autentikator muncul.
-   `realm`  : Teks yang akan muncul pada pop-up autentikasi.
-   `credentialsttl`  : Mengatur masa aktif suatu autentikasi berlaku.
-   `casesensitive`  : Mengatur apakah  **username**  bersifat case sensitive atau tidak.
-   `acl`  digunakan untuk mendefinisikan pengaturan akses tertentu. (Sintaks umum:  **acl ACL_NAME ACL_TYPE ARGUMENT**  . Lebih lengkapnya di  [http://www.squid-cache.org/Doc/config/acl/](http://www.squid-cache.org/Doc/config/acl/))
-   Untuk melihat daftar apa saja yang bisa diatur dengan acl bisa diakses di:  [https://wiki.squid-cache.org/SquidFaq/SquidAcl](https://wiki.squid-cache.org/SquidFaq/SquidAcl))

**STEP 4**  - Restart squid

**STEP 5**  - Ubah pengaturan proxy browser. Gunakan  **IP MOJOKERTO**  sebagai host, dan isikan port  **8080**. 
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/setting-proxy-system.PNG)

Kemudian cobalah untuk mengakses web  **elearning.if.its.ac.id**  (usahakan menggunakan mode  **incognito/private**), akan muncul pop-up untuk login.
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/user-pass-its.PNG)

**STEP 6**  - Isikan username dan password.

**STEP 7**  - E-learning berhasil dibuka.

### 2.2.4 Pembatasan Waktu Akses
Kita akan mencoba membatasi akses proxy pada hari dan jam tertentu. Asumsikan proxy dapat digunakan hanya pada hari Senin sampai Jumat pada jam 08.00-17.00.

**STEP 1**  - Buat file baru bernama acl.conf di folder squid
```
nano /etc/squid/acl.conf
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_1.PNG)

**STEP 2**  - Tambahkan baris berikut
```
acl AVAILABLE_WORKING time MTWHF 08:00-17:00
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_2.PNG)

**STEP 3**  - Simpan file acl.conf.

**STEP 4**  - Buka file squid.conf.
```
nano /etc/squid/squid.conf
```

**STEP 5**  - Ubah konfigurasinya menjadi:
```
include /etc/squid/acl.conf

http_port 8080
http_access allow AVAILABLE_WORKING
http_access deny all
visible_hostname mojokerto
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_3.PNG)

**STEP 6**  - Simpan file tersebut. Kemudian restart squid.

**STEP 7** - Cobalah untuk mengakses web http://its.ac.id (usahakan menggunakan mode incognito/private). Akan muncul halaman error jika mengakses diluar waktu yang telah ditentukan.
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_4.PNG)

**Keterangan:**
-   **MTWHF** adalah hari-hari dimana user diperbolehkan menggunakan proxy. (S: Sunday, M: Monday, T: Tuesday, W: Wednesday, H: Thursday, F: Friday, A: Saturday)
-   Penulisan jam menggunakan format: **h1:m1-h2:m2**. Dengan syarat **h1<h2** dan **m1<m2**

### 2.2.5 Pembatasan Akses ke Website Tertentu
Kita akan mencoba membatasi akses ke beberapa website. Untuk contoh disini, kita akan memblokir website **monta.if.its.ac.id** dan **elearning.if.its.ac.id**

**STEP 1**  - Buat file bernama restrict-sites.acl di folder squid dengan mengetikkan:
```
nano /etc/squid/restrict-sites.acl
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_5.PNG)

**STEP 2**  - Tambahkan alamat url yang akan diblock seperti baris berikut:
```
monta.if.its.ac.id
elearning.if.its.ac.id
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_6.PNG)

**STEP 3**  - Ubah file konfigurasi squid menjadi seperti berikut ini.
```
http_port 8080
visible_hostname mojokerto

acl BLACKLISTS dstdomain "/etc/squid/restrict-sites.acl"
http_access deny BLACKLISTS
http_access allow all
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_7.PNG)

**STEP 4**  - Restart squid. Kemudian cobalah untuk mengakses web **monta.if.its.ac.id** , **elearning.if.its.ac.id** , dan **google.com** (usahakan menggunakan mode incognito/private). Seharusnya halaman yang diakses menampilkan tampilan seperti gambar di bawah ini.
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_8.PNG)

**Keterangan:**
-   dstdomain artinya destination domain/domain tujuan. Sintaksnya bisa diikuti dengan nama domain tujuan atau file yang menampung list-list alamat website.

### 2.2.6 Pembatasan Bandwidth
Kita akan mencoba untuk membatasi bandwidth yang akan diberikan kepada user proxy. Untuk contoh disini kita akan membatasi penggunaannya maksimal 512 kbps.

**STEP 1** - Buat file bernama acl-bandwidth.conf di folder squid
```
nano /etc/squid/acl-bandwidth.conf
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_9.PNG)

**STEP 2**  - Ketikkan baris berikut
```
delay_pools 1
delay_class 1 1
delay_access 1 allow all
delay_parameters 1 16000/64000
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_10.PNG)

**STEP 3**  - Ubah konfigurasi pada file squid.conf menjadi:
```
include /etc/squid/acl-bandwidth.conf
http_port 8080
visible_hostname mojokerto

http_access allow all
```
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_11.PNG)

**STEP 4**  - Restart Squid

**STEP 5**  - Cobalah untuk melakukan speed test. Berikut perbedaan sebelum dan sesudah adanya pembatasan bandwidth saat melakukan speed test
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/acl_12.PNG)

**Keterangan:**
-   **delay_pools** digunakan untuk menentukan berapa bagian/pool yang akan dibuat. (Sintaks: **delay_pools JUMLAH_YANG_DIINGINKAN**. Lebih lengkap lihat di [http://www.squid-cache.org/Doc/config/delay_pools/](http://www.squid-cache.org/Doc/config/delay_class/)).
-   **delay_class** digunakan untuk menentukan tipe/class pembagian bandwith dari setiap pool. (Sintaks: **delay_class POOL_KE_BERAPA KELAS**.) Lebih lengkap lihat di [http://www.squid-cache.org/Doc/config/delay_class/](http://www.squid-cache.org/Doc/config/delay_class/).
-   **delay_access** mirip seperti http_access, tetapi digunakan untuk mengakses pool yang telah dibuat (Sintaks: **delay_access POOL_KE_BERAPA allow/deny TARGET**. Lebih lengkap lihat di [http://www.squid-cache.org/Doc/config/delay_access/](http://www.squid-cache.org/Doc/config/delay_access/).
-   **delay_parameters** digunakan untuk mengatur parameter dari pool yang telah dibuat. Sintaks berbeda-beda sesuai dengan tipe/kelas dari pool yang dibuat. Lebih lengkap lihat di [http://www.squid-cache.org/Doc/config/delay_parameters/](http://www.squid-cache.org/Doc/config/delay_parameters/)

## 2.3 Soal Latihan
Reli adalah seorang pendaki gunung. Dia ingin mendaki gunung Puncak Jaya untuk menguji keterampilan mendakinya. Salah satu ritual yang dilakukan Reli sebelum mendaki gunung adalah membuat proxynya sendiri. Proxy yang akan dibuat nantinya harus bisa diakses dengan nama puncakjaya.xxx.id dengan port yang digunakan adalah 8080. 	Untuk bisa mengakses proxynya perlu dilakukan login terlebih dahulu. Untuk akun milik Reli, username yang digunakan adalah reli dan password loveToHike-07. Proxy ini hanya bisa diakses pada hari Senin, Kamis, Jumat, dan Sabtu mulai jam 10 malam sampai jam 4 pagi. Karena Reli ingin fokus mendaki, Reli memutuskan untuk memblokir website korindo.co.id dan website if.its.ac.id beserta subdomainnya, ajk.if.its.ac.id. Reli juga mengatur di proxynya agar user mendapatkan bandwith 512 kbps. Bantu Reli melakukan persiapan agar Reli bisa mendaki gunung Puncak Jaya dan menyelesaikan ritualnya!
