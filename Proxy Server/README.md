# 2. Proxy Server
## Outline
- 2. Proxy Server
	- Outline
	- 2.1 Pengertian, Fungsi, dan Manfaat
		- 2.1.1 Pengertian 
		- 2.1.2 Fungsi 
		- 2.1.3 Manfaat
		- 2.1.4 Software Proxy Server
		- 2.1.5 Cara Kerja
	- 2.2 Implementasi
		- 2.2.1 Instalasi Squid
		-  2.2.2 Konfigurasi Dasar Squid
		- 2.2.3 Membuat User Login
		- 2.2.4 Pembatasan Waktu Akses
		- 2.2.5 Pembatasan Waktu Akses ke Website Tertentu
		- 2.2.6 Pembatasan Bandwith
	- 2.3 Soal Latihan
	
	- 2.4 Referensi

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
