# Web Server

## Daftar Isi
+ A. [Persyaratan Tambahan untuk Mengikuti Sesi Lab ](#a-persyaratan-tambahan-untuk-mengikuti-sesi-lab)
+ B. [Penting Untuk Dibaca](#b-penting-untuk-dibaca)
+ C. [Dasar Teori](#c-dasar-teori)
  + 1.[ Web Server](#1-web-server)
  + 2.[ Load Balancing](#2-load-balancing)
  + 3.[ Apache2 Web Server](#3-apache-web-server)
+ D. [Instalasi Lynx](#d-instalasi-lynx)
+ E. [Instalasi Apache](#e-instalasi-apache)
+ F. [Instalasi PHP](#f-instalasi-php)
+ G. [Mengenal Apache](#g-mengenal-apache)
+ H. [Konfigurasi Apache Sederhana](#h-konfigurasi-apache-sederhana)
  + A. [Penggunaan Sederhana](#a-penggunaan-sederhana)
  + B. [Membuat Konfigurasi Website Menggunakan Port 8080](#b-membuat-konfigurasi-website-menggunakan-port-8080)
+ I. [Mari Berimajinasi](#i-mari-berimajinasi)
  + A. [Setting Domain pada Apache](#a-setting-domain-pada-apache)
  + B. [Directory Listing](#b-directory-listing)
  + C. [Directory Alias](#c-directory-alias)
  + D. [Module Rewrite](#d-module-rewrite)
+ J. [Nginx Web Server](#4-nginx-web-server)
  + A. [Instalasi Nginx](#a-instalasi-nginx)
  + B. [Nginx Load Balancing](#b-load-balancing-pada-nginx)
  + C. [Nginx Upstream](#c-upstream)
  + D. [Reverse Proxy](#d-reverse-proxy)
  + E. [Setup Load Balancing di Nginx](#e-setup-load-balancing-di-nginx)

## A. Persyaratan Tambahan untuk Mengikuti Sesi Lab
Record A dan PTR pada jarkom2022.com sudah harus mengarah ke IP Water7

<img src="images/1.png" width="700">
<br/>
<img src="images/2.png" width="700">

## B. Penting Untuk Dibaca

1. Pastikan semua Node dapat terhubung ke internet, baik dapat melakukan koneksi ke luar maupun dapat ping dari luar
2. Jangan mencoba untuk mendahului arahan asisten. Kelalaian ditanggung praktikan.
3. Ketika mengalami kendala/error __cek syntax dan samakan seperti modul__ terlebih dahulu. Besar kemungkinan masalah yang terjadi dikarenakan adanya kesalahan dalam pengetikan.

## C. Dasar Teori

### 1. Web Server

Terdapat dua pengertian dari web server. Secara _hardware_, web server berarti sebuah storage yang digunakan untuk menyimpan semua data dari aplikasi web (file HTML, CSS, JavaScript, dll.). Sedangkan secara _software_,  web server adalah sebuah perangkat yang bertugas untuk menyediakan layanan akses menggunakan protokol HTTP atau HTTPS melalui aplikasi web.

### 2. Load Balancing

___Load balancing___ adalah suatu mekanisme penyeimbangan beban yang bekerja dengan cara membagi beban pekerjaan. ___Load balancer___ adalah aplikasi atau alat yang bertugas untuk melakukan _load balancing_. _Load balancer_ dapat meggunakan berbagai macam algoritma _load balancing_ yang bertujuan untuk membagi beban pekerjaan seadil-adilnya. Arsitektur minimal untuk _load balancing_ adalah sebagai berikut

<img src="images/Load Balancer.jpg">

#### Kenapa dibutuhkan load balancing?
Untuk menangani banyaknya pengguna yang mengakses layanan pada satu waktu dan menjaga layanan tetap tersedia setiap saat, dibutuhkan lebih dari satu komputer untuk memasang layanannya. Dengan layanan yang tersedia di banyak server, dibutuhkan mekanisme pembagian beban untuk memberikan beban yang seimbang pada setiap server. Dengan meletakkan layanan pada beberapa server dan pembagian beban yang optimal, setiap permintaan pengguna bisa ditangani dengan efisien.

### 3. Apache2 Web Server

Apache HTTP Server atau biasa disebut Apache adalah sebuah software web server cross-platform dan open source yang banyak digunakan. Dalam sesi lab ini, kita akan menggunakan Apache sebagai software web server kita.

## D. Instalasi Lynx

__Lynx__ adalah salah satu web browser yang dapat digunakan pada command-line. Lynx dapat menampilkan _hypertext document_ dan menavigasi _link_ yang ada pada suatu halaman web dengan hanya menggunakan keyboard.
#### 1. Buka Node _Loguetown_

Lalu jalankan perintah
```
apt-get update
apt-get install lynx
```
jika muncul tulisan _"Do you want to continue? [Y/n]"_  input `Y` lalu tekan ___enter___.
#### 2. Buka halaman google.com menggunakan lynx
Jalankan perintah
```
lynx google.com
```
Kalau ada pilihan seperti gambar di bawah ini, pilihlah sesuai keinginan.
<img src="images/lynx-confirm.png" width="700">
<br/>
Kalau sudah terinstall dengan benar, akan muncul tampilan seperti di bawah ini.
<br/>
<img src="images/google.png" width="700">


## E. Instalasi Apache
#### 1. Buka Node _Water7_
Lalu jalankan perintah
```
apt-get install apache2
```
jika muncul tulisan _"Do you want to continue? [Y/n]"_  input `Y` lalu tekan ___enter___.

<img src="images/3.png" width="700">

Apabila telah selesai melakukan instalasi Apache2, silakan jalankan perintah
```
service apache2 start
```

#### 2. Gunakan `lynx` untuk mengakses web.
Buka web __IP Water7 Masing-Masing Kelompok__ dengan `lynx` sampai muncul halaman Apache seperti di bawah ini.

<img src="images/5.png">

## F. Instalasi PHP
#### 1. Buka Node Water7
Lalu jalankan perintah
```
apt-get install php
```
jika muncul tulisan _"Do you want to continue? [Y/n]"_  input `Y` lalu tekan ___enter___.

#### 2. Test apakah php sudah ter-install
Jalankan perintah di bawah ini untuk memeriksa versi dari __php__ kalian.
```
php -v
```
Bila _output_-nya mirip dengan yang di bawah ini, maka __php__ kalian telah ter-_install_.

<img src="images/6.png" width="700">

## G. Mengenal Apache
Web server Apache memiliki _directory_ berisi berbagai konfigurasi yang terletak di `/etc/apache2/`

<img src="images/7.png" width="700">

Berikut beberapa hal yang penting untuk diketahui:
+ File Konfigurasi di `/etc/apache2`

|__Nama File__ | __Kegunaan__ |
| --- | --- |
| __apache2.conf__ | File konfigurasi utama apache2 |
| __ports.conf__ | File konfigurasi port yang digunakan untuk web server |
| __sites-available__ | _Directory_ tempat konfigurasi website (virtual host) yang tersedia |
| __sites-enabled__ | _Directory_ tempat konfigurasi website (virtual host) yang tersedia dan sudah aktif |
| __mods-available__ | _Directory_ tempat modul-moadul apache2 yang tersedia |
| __mods-enabled__ | _Directory_ tempat modul-moadul apache2 yang tersedia dan sudah aktif |

+ _Command_ yang sering digunakan

|__Command__ | __Kegunaan__ |
| --- | --- |
| __a2ensite__ | Untuk mengaktifkan (_ENABLE_) konfigurasi website yang telah dibuat |
| __a2dissite__ | Untuk menonaktifkan (_DISABLE_) konfigurasi website yang sedang aktif |
| __a2enmod__ | Untuk mengaktifkan (_ENABLE_) sebuah modul tertentu ke dalam konfigurasi apache2 |
| __a2dismod__ | Untuk menonaktifkan (_DISABLE_) sebuah modul tertentu dalam konfigurasi apache2 |

## H. Konfigurasi Apache Sederhana
### A. Penggunaan Sederhana
#### A.1. Pindah ke _directory_ `/etc/apache2/sites-available`
Gunakan perintah `cd /etc/apache2/sites-available`

<img src="images/8.png" width="700">

Dapat dilihat di sana terdapat dua buah file:
+ file __000-default.conf__, file konfigurasi website default apache untuk http.
+ file __default-ssl.conf__, file konfigurasi website default apache untuk https.

__Catatan tambahan__ :

Cek versi apache2 yang telah kalian install dengan menggunakan command : `apache2 -v`. Jika versi apache2 yang telah kalian install versi 2.4.x maka mengikuti sesuai modul. Jika versi apache yang telah kalian install versi 2.2.x maka mengikuti sesuai modul dengan catatan tambahan tertentu.

#### A.2. Buka file ___default___
Untuk versi 2.4.x gunakan perintah `nano /etc/apache2/sites-available/000-default.conf`. Sedangkan untuk versi 2.2.x gunakan perintah `nano /etc/apache2/sites-available/default`

Untuk versi 2.4.x setiap configurasi file yang berada di directory `/etc/apache2/sites-available` nama file-nya ditambahi dengan `.conf`. Contoh : `/etc/apache2/sites-available/default.conf`. Karena jika tidak ditambahi dengan `.conf` maka akan error.

<img src="images/9.png" width="700">

#### A.3.  Pada file _default_ terdapat konfigurasi standar apache
Beberapa diantaranya adalah:
##### __Port__ yang digunakan
```
<VirtualHost *:80>
```
Konfigurasi di atas menunjukkan bahwa port yang digunakan adalah port 80

##### ___Directory___ tempat file website kita berada
```
DocumentRoot /var/www/html
```
+ Untuk sesi lab JarKom ini silahkan mengubah _DocumentRoot_-nya menjadi `/var/www/html`
+ Jangan lupa lakukan `service apache2 restart` setelah melakukan perubahan konfigurasi agar perubahan yang telah dilakukan teraplikasikan

#### A.4. Pindah ke _directory_ yang ditunjuk oleh _DocumentRoot_ pada file _default_
Gunakan perintah `cd /var/www/`

+ Karena tadi kita mengubah _DocumentRoot_ di file _default_ menjadi `/var/www/html`, maka sekarang buatlah _directory_ bernama "html" dengan perintah `mkdir /var/www/html` apabila belum ada directorynya

#### A.5. Pindah ke _directory_ `/var/www/html` dan buat file _index.php_
Gunakan perintah `nano /var/www/html/index.php` dan isi file  tersebut dengan
```
<?php
	phpinfo();
?>
```

<img src="images/10.png" width="700">

#### A.6. Buka browser laptop/komputer masing-masing
Akses alamat menggunakan lynx __http://[IP Water7]/index.php__

<img src="images/11.png">

+ __Catatan__:
	Apabila tampilan web tidak muncul seperti gambar di atas dan hanya muncul plain text isi file index.php, silahkan install **libapache2-mod-php7.0** dengan menjalankan perintah
	```
	apt-get install libapache2-mod-php7.0
	```
	lalu restart apache dengan perintah
	```
	service apache2 restart
	```

### B. Membuat Konfigurasi Website Menggunakan Port 8080
#### B.1 Pindah ke _directory_ `/etc/apache2/sites-available`
Pindah ke _directory_ `/etc/apache2/sites-available` menggunakan perintah
```
cd /etc/apache2/sites-available
```
Copy file _000-default.conf_ menjadi file _000-default-8080.conf_ dengan perintah
```
cp 000-default.conf default-8080.conf
```
Jangan lupa untuk tidak menggunakan `.conf` jika apache2 versi 2.2.x. Jika sudah kalian bisa rename file tersebut menggunakan perintah

#### B.2 Buka file _default-8080.conf_
Buka file yang telah kalian buat pada sebelumnya. Gunakan perintah `nano /etc/apache2/sites-available/default-8080.conf`. Jangan lupa untuk tidak menambahkan `.conf` jika apache2 versi 2.2.x.
+ Kemudian ubah port yang digunakan. Dimana awalnya port `80` menjadi port `8080`.
+ Ubah juga _DocumentRoot_ yang awalnya `/var/www/html` menjadi `/var/www/web-8080`.

<img src="images/12.png" width="700">

#### B.3 Tambahkan _port 8080_ pada file `ports.conf`
File __ports.conf__ berada pada _directory_ `/etc/apache2`

Cara menambahkan port yang perlu didengar adalah dengan menuliskan
```
Listen 8080
```

<img src="images/13.png" width="700">

#### B.4 Aktifkan konfigurasi _default-8080.conf_
Untuk mengaktifkan suatu konfigurasi, kita menggunakan perintah `a2ensite` diikuti dengan __nama file konfigurasi__ yang telah dibuat.
Dalam kasus ini perintah yang dijalankan adalah
```
a2ensite default-8080.conf
```

<img src="images/14.png" width="700">

#### B.5 Restart apache
Gunakan perintah `service apache2 restart`

<img src="images/15.png" width="700">

#### B.6 Pindah ke _directory_ `/var/www`
Buatlah sebuah _directory_ baru di dalam `var/www` dengan nama __web-8080__

<img src="images/16.png" width="700">

#### B.7 Masuk ke _directory_ `/var/www/web-8080` dan buat file _index.php_
Isi file __index.php__ tersebut dengan
```
<?php
    echo "Halo, saya berlari di port 8080";
?>
```

<img src="images/17.png" width="700">

#### B.8 Buka browser laptop/komputer masing-masing
Akses alamat __http://[IP Water7]:8080__

<img src="images/18.png">

## I. Mari Berimajinasi
### A. Setting Domain pada Apache
Fulan dan Poyoyo adalah satu kelompok dalam mata kuliah Jaringan Komputer. Mereka diperintahkan oleh asisten untuk membuat website dengan domain __jarkom2022.com__, dan diberikan akses ke server yang bisa digunakan sebagai tempat host untuk websitenya. Tapi karena sesuatu dan lain hal, Poyoyo tidak bisa membantumu mengerjakan perintah dari asisten. Beruntungnya, Poyoyo meninggalkan catatan untuk Fulan ikuti agar Fulan dapat menyelesaikan perintah dari asisten.

Ayo bantu Fulan dengan mengonfigurasi server sesuai petunjuk yang diberikan Poyoyo:

#### A.1 Pindah ke _directory_ `/etc/apache2/sites-available`
Copy file __000-default.conf__ menjadi file __jarkom2022.com__. Jangan lupa untuk tidak menambahkan `.conf` jika apache2 versi 2.2.x

<img src="images/19.png" width="700">

#### A.2 Buka file _jarkom2022.com_
+ Tambahkan
	```
	ServerName jarkom2022.com
	ServerAlias www.jarkom2022.com
	```
	Menurut [dokumentasi apache2.4](https://httpd.apache.org/docs/2.2/mod/core.html):
	+ `ServerName` adalah "_Hostname and port that the server uses to identify itself_"
	+ `ServerAlias` adalah "_Alternate names for a host used when matching requests to name-virtual host_"
+ Ubah _DocumentRoot_ menjadi `/var/www/jarkom2022.com`

<img src="images/20.png" width="700">

#### A.3 Aktifkan konfigurasi _jarkom2022.com_
Gunakan perintah `a2ensite jarkom2022.com`

#### A.4 Restart apache
Gunakan perintah `service apache2 restart`

<img src="images/21.png" width="700">

#### A.5 Pindah ke _directory_ `/var/www`
Kemudian buatlah sebuah _directory_ baru di dalam `/var/www` dengan nama __jarkom2022.com__

<img src="images/22.png" width="700">

#### A.6 Masuk ke _directory_ `/var/www/jarkom2022.com` dan buat file _index.php_
Isi file __index.php__ tersebut dengan
```
<?php
    echo "Water7 adalah kota di One Piece...";
?>
```

<img src="images/23.png" width="700">

#### A.7 Buka _jarkom2022.com_ menggunakan _lynx_

<img src="images/24.png">

### B. Directory Listing
Di dalam _directory_ `/var/www/jarkom2022.com` diberikan struktur _directory_ sebagai berikut.
```
/var/www/jarkom2022.com/
├── assets/
│   └── javascript/
├── data/
└── download/
    └── img/
```
Perintah berikutnya dari asisten adalah untuk membuat beberapa direktori, __/assets__, __/data__, dan __/download__. Direktori __/download__ harus dapat menampilkan daftar file yang ada dalam direktori tersebut, sedangkan direktori __/assets__ tidak boleh menampilkan isi direktori tersebut.

Ayo bantu Fulan yang kebingunan membaca penjelasan dari Poyoyo agar dapat mengerjakan perintah asisten.

#### B.1 Buat _directory-directory_ yang diperlukan oleh website jarkom2022.com milik Waffle
Gunakan perintah-perintah berikut ini:
```
mkdir /var/www/jarkom2022.com/data
mkdir /var/www/jarkom2022.com/download
mkdir /var/www/jarkom2022.com/download/img
mkdir /var/www/jarkom2022.com/assets
mkdir /var/www/jarkom2022.com/assets/javascript
```

<img src="images/25.png" width="700">

#### B.2 Aktifkan Directory Listing untuk /download
+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com/download>
	    Options +Indexes
	</Directory>
	```
	jangan lupa untuk menyimpan perubahan tersebut agar _directory_  ___download___ menampilkan isi _directory_-nya.

	<img src="images/26.png" width="700">


+ Restart apache dengan perintah `service apache2 restart`
+ Buka browser dan akses http://jarkom2022.com/download

<img src="images/27.png">

__Keterangan__:
Untuk mengatur _directory_ pada sebuah web, menggunakan
```
<Directory /x> ... </Directory>
```
Contoh untuk mengatur `/var/www/jarkom2022.com/download`
```
<Directory /var/www/jarkom2022.com/download>

</Directory>
```

#### B.3 Matikan Directory Listing untuk /assets
+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com/assets>
	    Options -Indexes
	</Directory>
	```
	jangan lupa untuk menyimpan perubahan tersebut agar _directory_  ___assets___ tidak menampilkan isi _directory_-nya.

	<img src="images/28.png" width="700">

+ Restart apache dengan perintah `service apache2 restart`
+ Buka browser dan akses http://jarkom2022.com/assets

<img src="images/29.png">

### C. Directory Alias
Karena URL __http://[IP Water7]/assets/javascript__ dirasa terlalu panjang, maka Fulan mencoba membuat _directory alias_ menjadi __http://[IP Water7]/assets/js__ agar lebih terlihat _simple_.

Berikut adalah langkah-langkah pengerjaan yang diberikan Poyoyo:

+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com/assets/javascript>
	    Options +Indexes
	</Directory>

	Alias "/assets/js" "/var/www/jarkom2022.com/assets/javascript"
	```

	jangan lupa untuk menyimpan perubahan tersebut agar _directory_  ___assets/javascript___ dapat menampilkan isi _directory_-nya saat pengguna mengakses __http://[IP Water7]/assets/js__.

	<img src="images/30.png" width="700">

+ Restart apache dengan perintah `service apache2 restart`
+ Pindah ke folder __/var/www/jarkom2022.com/assets/javascript__ dan buat file __app.js__ dengan perintah `touch app.js`
+ Buka browser dan akses http://jarkom2022.com/assets/js

<img src="images/31.png">

### D. Module Rewrite
#### D.1 Aktifkan Module Rewrite
Perintah asisten berikutnya adalah menyalakan _module rewrite_ agar penulisan URL menjadi lebih rapi dan tanpa perlu menuliskan ekstensi _.php_ ketika mengakses laman.

+ Jalankan perintah `a2enmod rewrite` untuk mengaktifkan _module rewrite_.

+ Restart apache dengan perintah `service apache2 restart`

	<img src="images/32.png" width="700">

Biasanya semua konfigurasi terhadap sebuah website diatur pada file di _directory_ __/etc/apache2/sites-available__. Namun terkadang ada sebuah kasus bahwa   hak akses root untuk mengedit file konfigurasi yang berada di folder __/etc/apache2/sites-available__ tidak dimiliki, atau kita tidak ingin user lain untuk mengedit file konfigurasi yang berada di _directory_ __/etc/apache2/sites-available__.

Untuk mengatasi masalah tersebut, buat file __.htaccess__ pada _directory_ yang akan diatur.

Contohnya adalah seperti kasus di atas, dimana kita ingin mengatur _mod rewrite_ dari __[http://jarkom2022.com](http://jarkom2022.com)__ agar saat mengakses file php kita tidak perlu menuliskan ekstensinya. Maka yang yang perlu kita lakukan adalah
+ Pindah ke _directory_ `/var/www/jarkom2022.com` dan buat file __.htaccess__ dengan isi file
	```
	RewriteEngine On
	RewriteCond %{REQUEST_FILENAME} !-d
	RewriteRule ^([^\.]+)$ $1.php [NC,L]
	```

	<img src="images/33.png" width="700">

	__Keterangan__:
	+ `RewriteEngine On` = untuk flag bahwa menggunakan module rewrite
	+ `RewriteCond %{REQUEST_FILENAME} !-d` = aturan tidak akan jalan ketika yang diakses adalah _directory_ (d)
	+ `RewriteRule ^([^\.]+)$ $1.php [NC,L]` = $1 adalah parameter input yang akan dicari oleh webserver
	* Lebih detailnya [klik disini](https://httpd.apache.org/docs/2.4/rewrite/flags.html)
+ Buat file _about.php_ di dalam _directory_ `/var/www/jarkom2022.com/` dengan isi
	```
	<?php
		echo "Ini adalah halaman About";
	?>
	```
+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com>
	    Options +FollowSymLinks -Multiviews
	    AllowOverride All
	</Directory>
	```
	dan jangan lupa untuk menyimpan perubahan tersebut.

	<img src="images/34.png" width="700">

	__Keterangan__:
	+ `AllowOverride All` ditambahkan agar  konfigurasi __.htaccess__ dapat berjalan.
	+ `+FollowSymLinks` ditambahkan agar konfigurasi __mod_rewrite__ dapat berjalan.
	+ `-Multiviews` ditambahkan agar konfigurasi __mod_negotiation__ tidak dapat berjalan. __mod_negotiation__ bisa '_rewrite_' _requests_ sehingga menimpa dan mengganggu __mod_rewrite__.

+ Restart apache dengan perintah `service apache2 restart`
+ Buka browser dan akses __http://jarkom2022.com/about__

	<img src="images/35.png">

### 4. Nginx Web Server
__Nginx__ (baca: engine-x) adalah perangkat lunak (software) yang bersifat open source yang memiliki banyak fungsi. Web server yang satu ini dikenal dengan performanya yang powerful dan memiliki banyak fitur canggih. Beberapa fungsi dari Nginx di antaranya adalah:

- Web server
- Load Balancing
- Reverse Proxy

#### A. Instalasi Nginx

##### 1. Buka Node Foosha

Lalu jalankan perintah

```bash
apt-get update
apt-get install nginx
```

jika muncul tulisan _"Do you want to continue? [Y/n]"_  input `Y` lalu tekan ___enter___.

Apabila instalasi Nginx telah selesai, jangan lupa jalankan perintah berikut

```bash
service nginx start
```

Untuk mengecek status dari Nginx, bisa menggunakan perintah

```bash
service nginx status
```

##### 2. Gunakan `lynx` untuk mengakses web.

Buka web __IP Water7 Masing-Masing Kelompok__ dengan `lynx` sampai muncul halaman Nginx seperti di bawah ini.

<img src="images/lynx-nginx-1.png">


#### B. Load Balancing pada Nginx

Arsitektur load balancing pada umumnya yang digunakan di Nginx (default):

<img src="images/nginx-lb-default.png">

Namun kita juga bisa menggunakan jenis arsitektur lain, yaitu __Weighted load balancing__, dengan menambahkan parameter `weight` pada konfigurasi Nginx sehingga ada satu node yang memiliki weight atau beban lebih.

<img src="images/nginx-lb-weight.png">


Nginx  juga menawarkan beberapa metode atau algoritma load balancing yang dapat disesuaikan dengan kebutuhan pengguna, berikut ini beberapa metode yang sering digunakan:

- Round robin

	Jika kita memilih metode ini maka distribusi beban akan didistribusikan sesuai dengan urutan nomer dari server atau master. Jika kita memiliki 3 buah node, maka urutannya adalah dari node pertama, kemudian node kedua, dan ketiga. Setelah node ketiga menerima beban, maka akan diulang kembali dari node ke satu. Round robin sendiri merupakan metode default yang ada di Nginx.

	```bash
	upstream mynode {
		server srv1.example.com;
		server srv2.example.com;
		server srv3.example.com;
	}
	```
- Least-connection

	 Jika Round robin akan mendistribusikan berdasarkan nomer dan urutan server, maka least-connection akan melakukan prioritas pembagian dari beban kinerja yang paling rendah. Node master akan mencatat semua beban dan kinerja dari semua node, dan akan melakukan prioritas dari beban yang paling rendah. Sehingga diharapkan tidak ada server dengan beban yang rendah.

	 ```bash
	upstream mynode {
        least_conn;
        server srv1.example.com;
        server srv2.example.com;
        server srv3.example.com;
    }
	 ```

- IP Hash

	Agak berbeda dengan kedua algoritma di atas, algoritma ini akan melakukan hash berdasarkan request dari pengguna (menggunakan alamat IP dari pengguna). Sehingga server akan selalu menerima request dari alamat IP yang berbeda. Ketika server ini tidak tersedia, permintaan dari klien ini akan dilayani oleh server lain.

	```bash
	upstream mynode {
		ip_hash;
		server srv1.example.com;
		server srv2.example.com;
		server srv3.example.com;
	}
	```

- Generic Hash

	Metode Load Balancer Hash ini memetakan beban ke masing-masing node dengan cara membuat hashing berdasarkan text dan atau `Nginx Variables` yang ditentukan dalam hash config.

	```bash
	upstream mynode {
    	hash $request_uri consistent;
    	server srv1.example.com;
		server srv2.example.com;
		server srv3.example.com;
	}
	```

#### C. Upstream
Upstream pada Nginx merujuk pada kelompok atau cluster nodes yang ingin kita gunakan sebagai web server.

```bash
http {
    upstream nama_upstream {
        nama_method;
        server 192.168.1.2;
        server 192.168.1.3;
	server 192.168.1.4 weight=5;
        server ....;
    }
}

server {
    location / {
        proxy_pass http://nama_upstream;
    }
}

```

#### D. Reverse Proxy

Reverse Proxy adalah sistem proxy yang digunakan untuk meneruskan/bypass permintaan client. Reverse proxy sebagai jembatan diantara server frontend dan backend, dan bertugas untuk menjamin pertukaran data dan request berjalan secara lancar.

Selain pertukaran data, Reverse Proxy juga memberikan keamanan dan kompresi, sehingga server menjadi lebih ringan dalam memenuhi banyak permintaan sekaligus. Berikut script sederhana menggunakan reverse proxy

```bash
server {
    listen 80;
    server_name www.jarkom.site jarkom.site;

    location /blog {
       proxy_pass http://blog.jarkom.site:8000/posts/;
    }
}
```

Jika pengunjung mengakses http://jarkom.site/blog/my-post, Nginx akan mem-proxy permintaan ini ke server lain dengan alamat http://blog.jarkom.site:8000/posts. Meski begitu, tetap server utama yang menerima dan melayani koneksi. Singkatnya hanya sebagai perantara.

Ketika alamat server proxy berisi URI, /blog/, permintaan URI yang diteruskan ke server proxy digantikan oleh URI yang ditentukan dalam directive. Jika alamat server proxy ditentukan tanpa URI, maka permintaan koneksi ke URI diteruskan ke server proxy.

#### E. Setup Load Balancing di Nginx

Buatlah topologi sederhana seperti gambar dibawah

<img src="images/lb.png">

Setup IP Address di masing-masing nodes, pastikan setiap nodes terhubung ke  internet

- Foosha

	```bash
	auto eth0
	iface eth0 inet dhcp

	auto eth1
	iface eth1 inet static
		address [Prefix IP].1.1
		netmask 255.255.255.0

	auto eth2
	iface eth2 inet static
		address [Prefix IP].2.1
		netmask 255.255.255.0
	```

- Loguetown

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].1.2
		netmask 255.255.255.0
		gateway [Prefix IP].1.1
	```

- Alabasta

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].1.3
		netmask 255.255.255.0
		gateway [Prefix IP].1.1
	```

- Dressrosa

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].2.2
		netmask 255.255.255.0
		gateway [Prefix IP].2.1
	```

- Enieslobby

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].2.3
		netmask 255.255.255.0
		gateway [Prefix IP].2.1
	```

- Water7

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].2.4
		netmask 255.255.255.0
		gateway [Prefix IP].2.1
	```

#### Dressrosa (DNS Server)

- instal Bind9 dan Nginx di Dressrosa:

	```bash
	apt-get update
	apt-get install bind9 nginx
	```

- kemudian buat domain sederhana seperti contoh di modul sebelumnya, pada topologi kali ini kita akan menggunakan `jarkom.site` sebagai domain utama.

- isi dari file __named.conf.local__

	```bash
	//
	// Do any local configuration here
	//

	// Consider adding the 1918 zones here, if they are not used in your
	// organization
	//include "/etc/bind/zones.rfc1918";


	zone "jarkom.site" {
			type master;
			file "/etc/bind/jarkom/jarkom.site";
	};

	zone "2.168.192.in-addr.arpa" {
		type master;
		file "/etc/bind/jarkom/2.168.192.in-addr.arpa";
	};
	```

- isi dari file __jarkom.site__

	```bash
	;
	; BIND data file for local loopback interface
	;
	$TTL    604800
	@       IN      SOA     jarkom.site. root.jarkom.site. (
					2         ; Serial
					604800    ; Refresh
					86400     ; Retry
					2419200   ; Expire
					604800 )  ; Negative Cache TTL
	;
	@       IN      NS      jarkom.site.
	@       IN      A       192.168.2.2
	```

- isi dari file __2.168.192.in-addr.arpa__

	```bash
	;
	; BIND data file for local loopback interface
	;
	$TTL    604800
	@       IN      SOA     jarkom.site. root.jarkom.site. (
					2         ; Serial
					604800    ; Refresh
					86400     ; Retry
					2419200   ; Expire
					604800 )  ; Negative Cache TTL
	;
	2.168.192.in-addr.arpa.         IN      NS      jarkom.site.
	2                               IN      PTR     jarkom.site.
	```

- lakukan pengujian untuk domain yang telah dibuat, dari `Alabasta`

	<img src="images/lb-setup-1.png">

#### EniesLobby (Nginx worker)

- install lalu setup Nginx dan PHP

	```bash
	apt-get update && apt install nginx php php-fpm -y
	```

- cek versi dari PHP

	```bash
	php -v
	```

	<img src="images/lb-setup-2.png">

- buat direktori baru di `/var/www`, dengan nama `jarkom`

	```bash
	mkdir /var/www/jarkom
	```

- masuk direktori `jarkom` lalu buat file `index.php`

	```php
	<?php
	echo "Halo, Kamu berada di EniesLobby";
	?>
	```

- selanjutnya kita akan melakukan konfigurasi pada Nginx, pertama masuk ke direktori `/etc/nginx/sites-available` lalu buat file baru dengan nama `jarkom`

	```
	nano jarkom

	atau

	touch jarkom
	```

- kemudian isi dengan konfigurasi server block ini:

	```bash
	server {

		listen 80;

		root /var/www/jarkom;

		index index.php index.html index.htm;
		server_name _;

		location / {
				try_files $uri $uri/ /index.php?$query_string;
		}

		# pass PHP scripts to FastCGI server
		location ~ \.php$ {
		include snippets/fastcgi-php.conf;
		fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
		}

	location ~ /\.ht {
				deny all;
		}

		error_log /var/log/nginx/jarkom_error.log;
		access_log /var/log/nginx/jarkom_access.log;
	}
	```

- lalu simpan, kemudian buat `symlink`

	```bash
	ln -s /etc/nginx/sites-available/jarkom /etc/nginx/sites-enabled
	```

- terakhir restart Nginx

	```bash
	service nginx restart

	atau

	nginx -s reload
	```

- jika mengecek apakah konfigurasi yang dibuat sudah benar atau belum, bisa mengunakan perintah berikut

	```bash
	nginx -t
	```

	<img src="images/lb-setup-3.png">


#### Water7 (Nginx worker)

- lakukan hal yang sama seperti di node EniesLobby, namun bedakan pada konfigurasi `index.php` nya agar memudahkan pada saat pengujian

	```php
	<?php
	echo "Halo, Kamu berada di Water7";
	?>
	```
#### Penjelasan

##### Server Block:

 - `listen` mendefinisikan di port berapa nantinya Nginx berjalan.

 - `root` menjunjukan letak direktori dari file web yang digunakan.

- `index` menentukan urutan file indeks yang akan dicoba oleh server ketika ada permintaan masuk.

- `server_name` menentukan nama server. Tanda garis bawah _ adalah penanda bahwa server akan menanggapi permintaan untuk semua nama server yang tidak cocok dengan nama server lain. Nama server bisa diganti dengan IP Address, nama domain, localhost, dll.

- `location { ... }` Konfigurasi untuk menangani permintaan ke akar situs. __try_files__ mencoba mencari file yang sesuai dengan __$uri__, kemudian __$uri/__, dan jika itu juga tidak ditemukan, akan mengarahkan ke index.php dengan menggunakan __data query string__.

- `location ~ \.php$` konfigurasi untuk menangani file PHP. Lokasi ini akan mencocokkan ekstensi .php pada URL dan akan memprosesnya dengan menggunakan FastCGI dan mengarahkannya ke socket FastCGI PHP. Untuk  penggunaan PHP Socket perlu disesuaikan dengan versi PHP yang diinstall, dalam case ini kita menggunakan PHP7.2.

- `location ~ /\.ht` mengatur bahwa akses ke file .ht (seperti .htaccess) akan ditolak. Ini adalah langkah keamanan yang umum digunakan untuk mencegah akses ke file sensitif.

- `error_log` mengarahkan log error ke file tertentu.

- `access_log` mengarahkan log akses ke file tertenu.

- `ln -s /etc/nginx/sites-available/jarkom /etc/nginx/sites-enabled` adalah perintah untuk membuat symlink (link simbolik) dari file konfigurasi Nginx yang berada di direktori /etc/nginx/sites-available ke direktori /etc/nginx/sites-enabled.


#### Dressrosa (Load Balancer)

- kembali lagi ke node Dressrosa, kemudian buat file baru di direktori `/etc/nginx/sites-available` dengan nama `lb-jarkom`

	```bash
	# Default menggunakan Round Robin
	upstream myweb  {
		server 192.168.2.3; #IP EniesLobby
		server 192.168.2.4; #IP Water7
	}

	server {
		listen 80;
		server_name jarkom.site;

		location / {
		proxy_pass http://myweb;
		}
	}
	```
- lalu simpan lalu buat `symlink`

	```bash
	ln -s /etc/nginx/sites-available/lb-jarkom /etc/nginx/sites-enabled
	```

#### Penjelasan

- `upstream` - mendefinisikan grup atau kelompok server yang akan menerima lalu lintas atau beban dengan __myweb__ sebagai nama upstream. Dalam kasus ini, ada dua server dengan  alamat IP masing-masing 192.168.2.3 dan 192.168.2.4. Dengan metode Round Robin, lalu lintas akan dibagi secara setara antara kedua server ini.

- `listen` - mendefinisikan bahwa web server ini akan berjalan dan mendengarkan permintaan (request) pada port 80.

- `location / { ... }` mengatur cara server Nginx menangani permintaan. Dalam hal ini, semua permintaan akan diteruskan ke grup server yang telah didefinisikan di bagian __upstream__.

#### Pengujian
Masuk ke Loguetwon atau Alabasta lalu jalankan perintah __lynx http://jarkom.site__.

```bash
lynx http://jarkom.site
```
<img src="images/lb-testing-1.gif">


Coba untuk stop service Nginx di salah satu worker, lalu lakukan pengujian lagi.

<img src="images/lb-testing-2.gif">

#### Troubleshoting

- `502 Bad Gateway` - Pastikan socket PHP yang digunakan pada server block sudah sesuai dengan versi PHP yang diinstal.

- `404 Not Found` - Pastikan kembali lokasi dari file PHP di __root__ sudah benar atau belum.

- `403 Forbidden` - Pastikan nama file yang ingin dipanggil dibagian __index__ sudah benar.

- `service php7.2-fpm restart` - Tapi statusnya masih fail, coba dijalankan dulu dengan perintah `service php7.2-fpm start`.

- `Default page Nginx` - Jika ingin menghilangkan default page dari Nginx, jalan perintah `sudo rm /etc/nginx/sites-enabled/default` atau menjalankan command unlink: `unlink /etc/nginx/sites-enabled/default` lalu restart Nginx. Sering terjadi ketika ingin menampilkan halaman dari PHP, tapi yang muncul masih default page Nginx.

- Jangan lupa melakukan restart service, ketika ada perubahan pada konfigurasi.


<!-- ### E. Otorisasi
Pada web http:jarkom2022.com terdapat path __/data__ yang tidak boleh dibuka sembarang orang. Rachma ingin __/data__ hanya boleh diakses oleh pengguna yang memiliki IP 10.151.252.0/255.255.252.0

Maka yang diinstruksikan Ifin agar _directory_ __/data__ milik Rachma tetap aman adalah
+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com/data>
	    Options +Indexes
	    Order deny,allow
	    Deny from all
	    Allow from 10.151.252.0/255.255.252.0
	</Directory>
	```
	jangan lupa untuk menyimpan perubahan tersebut.

	__Keterangan__:
	+ `Order deny, allow` merupakan urutan hak akses. Terdapat dua jenis tipe order yaitu:
		+ `deny,allow`: Bagian _Deny_ harus di-_declare_ terlebih dahulu sebelum _Allow_
		+ `allow,deny`: Bagian _Allow_ harus di-_declare_ terlebih dahulu sebelum _Deny_
	+ `Deny from all`  berarti semua pengguna ditolak
	+ `Allow from 10.151.252.0/255.255.252.0` berarti apabila pengguna memiliki IP NID 10.151.252.0./22, ia diperbolehkan untuk mengakses halaman.
	+ Info lebih lanjut [klik disini](https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html)	+ Restart apache dengan perintah `service apache2 restart`
+ Buka browser dan akses __http://jarkom2022.com/data__
Saat pengguna tidak memiliki __IP NID 10.151.252.0/22__ maka akan muncul halaman seperti di bawah ini

	IMG HERE

Sedangkan saat pengguna  memiliki __IP NID 10.151.252.0/22__ maka halaman yang muncul adalah seperti di bawah ini

	IMG HERE

-->

## I. Latihan
<!-- #### TBA -->
1. Download halaman soal latihan di https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/raw/master/Modul-2/Web%20server/page.zip (Gunakan wget)
2. Buat domain baru dengan nama __jarkom.yyy.id__ untuk membuka halaman tersebut.
3. Edit kata `yyy` yang ada di index.php dengan nama kelompok kalian.
4. Atur agar jika kalian mengetikkan __jarkom.yyy.id__, Web latihan dapat terbuka dengan lynx.
5. Cobalah menggunakan algoritma load balancing selain Roundrobin (Least-Conn, IP Hash & Generic Hash)
6. Cobalah untuk menggunakan web server Apache2 di node selain LB.

### Catatan
+ Kemudian unzip file tersebut. Jika muncul error seperti `unzip: command not found` maka install unzip terlebih dahulu menggunakan command `apt-get install unzip`.
+ Buat directory hasil unzip file tersebut menjadi _DocumentRoot_ web
+ Untuk nomor 2, 3, dan 4, '__yyy__' diisi dengan nama kelompok. Contoh: __jarkom.E01.id__


## Jangan ragu bertanya kalau ada yang masih bingung!
<p align="center">
	<img src="images/bingung.jpg" width="50%">
</p>

<!--
	<img src="images/36.png" width="700">
	<img src="images/37.png">
	<img src="images/38.png" width="700">
	<img src="images/39.png" width="700">
	<img src="images/40.png" width="700">
	<img src="images/41.png">
	<img src="images/42.png" width="700">
	<img src="images/43.png">
	<img src="images/44.png">
 -->
=======
# Web Server

## Daftar Isi
+ A. [Persyaratan Tambahan untuk Mengikuti Sesi Lab ](#a-persyaratan-tambahan-untuk-mengikuti-sesi-lab)
+ B. [Penting Untuk Dibaca](#b-penting-untuk-dibaca)
+ C. [Dasar Teori](#c-dasar-teori)
  + 1.[ Web Server](#1-web-server)
  + 2.[ Load Balancing](#2-load-balancing)
  + 3.[ Apache2 Web Server](#3-apache-web-server)
+ D. [Instalasi Lynx](#d-instalasi-lynx)
+ E. [Instalasi Apache](#e-instalasi-apache)
+ F. [Instalasi PHP](#f-instalasi-php)
+ G. [Mengenal Apache](#g-mengenal-apache)
+ H. [Konfigurasi Apache Sederhana](#h-konfigurasi-apache-sederhana)
  + A. [Penggunaan Sederhana](#a-penggunaan-sederhana)
  + B. [Membuat Konfigurasi Website Menggunakan Port 8080](#b-membuat-konfigurasi-website-menggunakan-port-8080)
+ I. [Mari Berimajinasi](#i-mari-berimajinasi)
  + A. [Setting Domain pada Apache](#a-setting-domain-pada-apache)
  + B. [Directory Listing](#b-directory-listing)
  + C. [Directory Alias](#c-directory-alias)
  + D. [Module Rewrite](#d-module-rewrite)
+ J. [Nginx Web Server](#4-nginx-web-server)
  + A. [Instalasi Nginx](#a-instalasi-nginx)
  + B. [Nginx Load Balancing](#b-load-balancing-pada-nginx)
  + C. [Nginx Upstream](#c-upstream)
  + D. [Reverse Proxy](#d-reverse-proxy)
  + E. [Setup Load Balancing di Nginx](#e-setup-load-balancing-di-nginx)

## A. Persyaratan Tambahan untuk Mengikuti Sesi Lab
Record A dan PTR pada jarkom2022.com sudah harus mengarah ke IP Water7

<img src="images/1.png" width="700">
<br/>
<img src="images/2.png" width="700">

## B. Penting Untuk Dibaca

1. Pastikan semua Node dapat terhubung ke internet, baik dapat melakukan koneksi ke luar maupun dapat ping dari luar
2. Jangan mencoba untuk mendahului arahan asisten. Kelalaian ditanggung praktikan.
3. Ketika mengalami kendala/error __cek syntax dan samakan seperti modul__ terlebih dahulu. Besar kemungkinan masalah yang terjadi dikarenakan adanya kesalahan dalam pengetikan.

## C. Dasar Teori

### 1. Web Server

Terdapat dua pengertian dari web server. Secara _hardware_, web server berarti sebuah storage yang digunakan untuk menyimpan semua data dari aplikasi web (file HTML, CSS, JavaScript, dll.). Sedangkan secara _software_,  web server adalah sebuah perangkat yang bertugas untuk menyediakan layanan akses menggunakan protokol HTTP atau HTTPS melalui aplikasi web.

### 2. Load Balancing

___Load balancing___ adalah suatu mekanisme penyeimbangan beban yang bekerja dengan cara membagi beban pekerjaan. ___Load balancer___ adalah aplikasi atau alat yang bertugas untuk melakukan _load balancing_. _Load balancer_ dapat meggunakan berbagai macam algoritma _load balancing_ yang bertujuan untuk membagi beban pekerjaan seadil-adilnya. Arsitektur minimal untuk _load balancing_ adalah sebagai berikut

<img src="images/Load Balancer.jpg">

#### Kenapa dibutuhkan load balancing?
Untuk menangani banyaknya pengguna yang mengakses layanan pada satu waktu dan menjaga layanan tetap tersedia setiap saat, dibutuhkan lebih dari satu komputer untuk memasang layanannya. Dengan layanan yang tersedia di banyak server, dibutuhkan mekanisme pembagian beban untuk memberikan beban yang seimbang pada setiap server. Dengan meletakkan layanan pada beberapa server dan pembagian beban yang optimal, setiap permintaan pengguna bisa ditangani dengan efisien.

### 3. Apache2 Web Server

Apache HTTP Server atau biasa disebut Apache adalah sebuah software web server cross-platform dan open source yang banyak digunakan. Dalam sesi lab ini, kita akan menggunakan Apache sebagai software web server kita.

## D. Instalasi Lynx

__Lynx__ adalah salah satu web browser yang dapat digunakan pada command-line. Lynx dapat menampilkan _hypertext document_ dan menavigasi _link_ yang ada pada suatu halaman web dengan hanya menggunakan keyboard.
#### 1. Buka Node _Loguetown_

Lalu jalankan perintah
```
apt-get update
apt-get install lynx
```
jika muncul tulisan _"Do you want to continue? [Y/n]"_  input `Y` lalu tekan ___enter___.
#### 2. Buka halaman google.com menggunakan lynx
Jalankan perintah
```
lynx google.com
```
Kalau ada pilihan seperti gambar di bawah ini, pilihlah sesuai keinginan.
<img src="images/lynx-confirm.png" width="700">
<br/>
Kalau sudah terinstall dengan benar, akan muncul tampilan seperti di bawah ini.
<br/>
<img src="images/google.png" width="700">


## E. Instalasi Apache
#### 1. Buka Node _Water7_
Lalu jalankan perintah
```
apt-get install apache2
```
jika muncul tulisan _"Do you want to continue? [Y/n]"_  input `Y` lalu tekan ___enter___.

<img src="images/3.png" width="700">

Apabila telah selesai melakukan instalasi Apache2, silakan jalankan perintah
```
service apache2 start
```

#### 2. Gunakan `lynx` untuk mengakses web.
Buka web __IP Water7 Masing-Masing Kelompok__ dengan `lynx` sampai muncul halaman Apache seperti di bawah ini.

<img src="images/5.png">

## F. Instalasi PHP
#### 1. Buka Node Water7
Lalu jalankan perintah
```
apt-get install php
```
jika muncul tulisan _"Do you want to continue? [Y/n]"_  input `Y` lalu tekan ___enter___.

#### 2. Test apakah php sudah ter-install
Jalankan perintah di bawah ini untuk memeriksa versi dari __php__ kalian.
```
php -v
```
Bila _output_-nya mirip dengan yang di bawah ini, maka __php__ kalian telah ter-_install_.

<img src="images/6.png" width="700">

## G. Mengenal Apache
Web server Apache memiliki _directory_ berisi berbagai konfigurasi yang terletak di `/etc/apache2/`

<img src="images/7.png" width="700">

Berikut beberapa hal yang penting untuk diketahui:
+ File Konfigurasi di `/etc/apache2`

|__Nama File__ | __Kegunaan__ |
| --- | --- |
| __apache2.conf__ | File konfigurasi utama apache2 |
| __ports.conf__ | File konfigurasi port yang digunakan untuk web server |
| __sites-available__ | _Directory_ tempat konfigurasi website (virtual host) yang tersedia |
| __sites-enabled__ | _Directory_ tempat konfigurasi website (virtual host) yang tersedia dan sudah aktif |
| __mods-available__ | _Directory_ tempat modul-moadul apache2 yang tersedia |
| __mods-enabled__ | _Directory_ tempat modul-moadul apache2 yang tersedia dan sudah aktif |

+ _Command_ yang sering digunakan

|__Command__ | __Kegunaan__ |
| --- | --- |
| __a2ensite__ | Untuk mengaktifkan (_ENABLE_) konfigurasi website yang telah dibuat |
| __a2dissite__ | Untuk menonaktifkan (_DISABLE_) konfigurasi website yang sedang aktif |
| __a2enmod__ | Untuk mengaktifkan (_ENABLE_) sebuah modul tertentu ke dalam konfigurasi apache2 |
| __a2dismod__ | Untuk menonaktifkan (_DISABLE_) sebuah modul tertentu dalam konfigurasi apache2 |

## H. Konfigurasi Apache Sederhana
### A. Penggunaan Sederhana
#### A.1. Pindah ke _directory_ `/etc/apache2/sites-available`
Gunakan perintah `cd /etc/apache2/sites-available`

<img src="images/8.png" width="700">

Dapat dilihat di sana terdapat dua buah file:
+ file __000-default.conf__, file konfigurasi website default apache untuk http.
+ file __default-ssl.conf__, file konfigurasi website default apache untuk https.

__Catatan tambahan__ :

Cek versi apache2 yang telah kalian install dengan menggunakan command : `apache2 -v`. Jika versi apache2 yang telah kalian install versi 2.4.x maka mengikuti sesuai modul. Jika versi apache yang telah kalian install versi 2.2.x maka mengikuti sesuai modul dengan catatan tambahan tertentu.

#### A.2. Buka file ___default___
Untuk versi 2.4.x gunakan perintah `nano /etc/apache2/sites-available/000-default.conf`. Sedangkan untuk versi 2.2.x gunakan perintah `nano /etc/apache2/sites-available/default`

Untuk versi 2.4.x setiap configurasi file yang berada di directory `/etc/apache2/sites-available` nama file-nya ditambahi dengan `.conf`. Contoh : `/etc/apache2/sites-available/default.conf`. Karena jika tidak ditambahi dengan `.conf` maka akan error.

<img src="images/9.png" width="700">

#### A.3.  Pada file _default_ terdapat konfigurasi standar apache
Beberapa diantaranya adalah:
##### __Port__ yang digunakan
```
<VirtualHost *:80>
```
Konfigurasi di atas menunjukkan bahwa port yang digunakan adalah port 80

##### ___Directory___ tempat file website kita berada
```
DocumentRoot /var/www/html
```
+ Untuk sesi lab JarKom ini silahkan mengubah _DocumentRoot_-nya menjadi `/var/www/html`
+ Jangan lupa lakukan `service apache2 restart` setelah melakukan perubahan konfigurasi agar perubahan yang telah dilakukan teraplikasikan

#### A.4. Pindah ke _directory_ yang ditunjuk oleh _DocumentRoot_ pada file _default_
Gunakan perintah `cd /var/www/`

+ Karena tadi kita mengubah _DocumentRoot_ di file _default_ menjadi `/var/www/html`, maka sekarang buatlah _directory_ bernama "html" dengan perintah `mkdir /var/www/html` apabila belum ada directorynya

#### A.5. Pindah ke _directory_ `/var/www/html` dan buat file _index.php_
Gunakan perintah `nano /var/www/html/index.php` dan isi file  tersebut dengan
```
<?php
	phpinfo();
?>
```

<img src="images/10.png" width="700">

#### A.6. Buka browser laptop/komputer masing-masing
Akses alamat menggunakan lynx __http://[IP Water7]/index.php__

<img src="images/11.png">

+ __Catatan__:
	Apabila tampilan web tidak muncul seperti gambar di atas dan hanya muncul plain text isi file index.php, silahkan install **libapache2-mod-php7.0** dengan menjalankan perintah
	```
	apt-get install libapache2-mod-php7.0
	```
	lalu restart apache dengan perintah
	```
	service apache2 restart
	```

### B. Membuat Konfigurasi Website Menggunakan Port 8080
#### B.1 Pindah ke _directory_ `/etc/apache2/sites-available`
Pindah ke _directory_ `/etc/apache2/sites-available` menggunakan perintah
```
cd /etc/apache2/sites-available
```
Copy file _000-default.conf_ menjadi file _000-default-8080.conf_ dengan perintah
```
cp 000-default.conf default-8080.conf
```
Jangan lupa untuk tidak menggunakan `.conf` jika apache2 versi 2.2.x. Jika sudah kalian bisa rename file tersebut menggunakan perintah

#### B.2 Buka file _default-8080.conf_
Buka file yang telah kalian buat pada sebelumnya. Gunakan perintah `nano /etc/apache2/sites-available/default-8080.conf`. Jangan lupa untuk tidak menambahkan `.conf` jika apache2 versi 2.2.x.
+ Kemudian ubah port yang digunakan. Dimana awalnya port `80` menjadi port `8080`.
+ Ubah juga _DocumentRoot_ yang awalnya `/var/www/html` menjadi `/var/www/web-8080`.

<img src="images/12.png" width="700">

#### B.3 Tambahkan _port 8080_ pada file `ports.conf`
File __ports.conf__ berada pada _directory_ `/etc/apache2`

Cara menambahkan port yang perlu didengar adalah dengan menuliskan
```
Listen 8080
```

<img src="images/13.png" width="700">

#### B.4 Aktifkan konfigurasi _default-8080.conf_
Untuk mengaktifkan suatu konfigurasi, kita menggunakan perintah `a2ensite` diikuti dengan __nama file konfigurasi__ yang telah dibuat.
Dalam kasus ini perintah yang dijalankan adalah
```
a2ensite default-8080.conf
```

<img src="images/14.png" width="700">

#### B.5 Restart apache
Gunakan perintah `service apache2 restart`

<img src="images/15.png" width="700">

#### B.6 Pindah ke _directory_ `/var/www`
Buatlah sebuah _directory_ baru di dalam `var/www` dengan nama __web-8080__

<img src="images/16.png" width="700">

#### B.7 Masuk ke _directory_ `/var/www/web-8080` dan buat file _index.php_
Isi file __index.php__ tersebut dengan
```
<?php
    echo "Halo, saya berlari di port 8080";
?>
```

<img src="images/17.png" width="700">

#### B.8 Buka browser laptop/komputer masing-masing
Akses alamat __http://[IP Water7]:8080__

<img src="images/18.png">

## I. Mari Berimajinasi
### A. Setting Domain pada Apache
Fulan dan Poyoyo adalah satu kelompok dalam mata kuliah Jaringan Komputer. Mereka diperintahkan oleh asisten untuk membuat website dengan domain __jarkom2022.com__, dan diberikan akses ke server yang bisa digunakan sebagai tempat host untuk websitenya. Tapi karena sesuatu dan lain hal, Poyoyo tidak bisa membantumu mengerjakan perintah dari asisten. Beruntungnya, Poyoyo meninggalkan catatan untuk Fulan ikuti agar Fulan dapat menyelesaikan perintah dari asisten.

Ayo bantu Fulan dengan mengonfigurasi server sesuai petunjuk yang diberikan Poyoyo:

#### A.1 Pindah ke _directory_ `/etc/apache2/sites-available`
Copy file __000-default.conf__ menjadi file __jarkom2022.com__. Jangan lupa untuk tidak menambahkan `.conf` jika apache2 versi 2.2.x

<img src="images/19.png" width="700">

#### A.2 Buka file _jarkom2022.com_
+ Tambahkan
	```
	ServerName jarkom2022.com
	ServerAlias www.jarkom2022.com
	```
	Menurut [dokumentasi apache2.4](https://httpd.apache.org/docs/2.2/mod/core.html):
	+ `ServerName` adalah "_Hostname and port that the server uses to identify itself_"
	+ `ServerAlias` adalah "_Alternate names for a host used when matching requests to name-virtual host_"
+ Ubah _DocumentRoot_ menjadi `/var/www/jarkom2022.com`

<img src="images/20.png" width="700">

#### A.3 Aktifkan konfigurasi _jarkom2022.com_
Gunakan perintah `a2ensite jarkom2022.com`

#### A.4 Restart apache
Gunakan perintah `service apache2 restart`

<img src="images/21.png" width="700">

#### A.5 Pindah ke _directory_ `/var/www`
Kemudian buatlah sebuah _directory_ baru di dalam `/var/www` dengan nama __jarkom2022.com__

<img src="images/22.png" width="700">

#### A.6 Masuk ke _directory_ `/var/www/jarkom2022.com` dan buat file _index.php_
Isi file __index.php__ tersebut dengan
```
<?php
    echo "Water7 adalah kota di One Piece...";
?>
```

<img src="images/23.png" width="700">

#### A.7 Buka _jarkom2022.com_ menggunakan _lynx_

<img src="images/24.png">

### B. Directory Listing
Di dalam _directory_ `/var/www/jarkom2022.com` diberikan struktur _directory_ sebagai berikut.
```
/var/www/jarkom2022.com/
├── assets/
│   └── javascript/
├── data/
└── download/
    └── img/
```
Perintah berikutnya dari asisten adalah untuk membuat beberapa direktori, __/assets__, __/data__, dan __/download__. Direktori __/download__ harus dapat menampilkan daftar file yang ada dalam direktori tersebut, sedangkan direktori __/assets__ tidak boleh menampilkan isi direktori tersebut.

Ayo bantu Fulan yang kebingunan membaca penjelasan dari Poyoyo agar dapat mengerjakan perintah asisten.

#### B.1 Buat _directory-directory_ yang diperlukan oleh website jarkom2022.com milik Waffle
Gunakan perintah-perintah berikut ini:
```
mkdir /var/www/jarkom2022.com/data
mkdir /var/www/jarkom2022.com/download
mkdir /var/www/jarkom2022.com/download/img
mkdir /var/www/jarkom2022.com/assets
mkdir /var/www/jarkom2022.com/assets/javascript
```

<img src="images/25.png" width="700">

#### B.2 Aktifkan Directory Listing untuk /download
+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com/download>
	    Options +Indexes
	</Directory>
	```
	jangan lupa untuk menyimpan perubahan tersebut agar _directory_  ___download___ menampilkan isi _directory_-nya.

	<img src="images/26.png" width="700">


+ Restart apache dengan perintah `service apache2 restart`
+ Buka browser dan akses http://jarkom2022.com/download

<img src="images/27.png">

__Keterangan__:
Untuk mengatur _directory_ pada sebuah web, menggunakan
```
<Directory /x> ... </Directory>
```
Contoh untuk mengatur `/var/www/jarkom2022.com/download`
```
<Directory /var/www/jarkom2022.com/download>

</Directory>
```

#### B.3 Matikan Directory Listing untuk /assets
+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com/assets>
	    Options -Indexes
	</Directory>
	```
	jangan lupa untuk menyimpan perubahan tersebut agar _directory_  ___assets___ tidak menampilkan isi _directory_-nya.

	<img src="images/28.png" width="700">

+ Restart apache dengan perintah `service apache2 restart`
+ Buka browser dan akses http://jarkom2022.com/assets

<img src="images/29.png">

### C. Directory Alias
Karena URL __http://[IP Water7]/assets/javascript__ dirasa terlalu panjang, maka Fulan mencoba membuat _directory alias_ menjadi __http://[IP Water7]/assets/js__ agar lebih terlihat _simple_.

Berikut adalah langkah-langkah pengerjaan yang diberikan Poyoyo:

+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com/assets/javascript>
	    Options +Indexes
	</Directory>

	Alias "/assets/js" "/var/www/jarkom2022.com/assets/javascript"
	```

	jangan lupa untuk menyimpan perubahan tersebut agar _directory_  ___assets/javascript___ dapat menampilkan isi _directory_-nya saat pengguna mengakses __http://[IP Water7]/assets/js__.

	<img src="images/30.png" width="700">

+ Restart apache dengan perintah `service apache2 restart`
+ Pindah ke folder __/var/www/jarkom2022.com/assets/javascript__ dan buat file __app.js__ dengan perintah `touch app.js`
+ Buka browser dan akses http://jarkom2022.com/assets/js

<img src="images/31.png">

### D. Module Rewrite
#### D.1 Aktifkan Module Rewrite
Perintah asisten berikutnya adalah menyalakan _module rewrite_ agar penulisan URL menjadi lebih rapi dan tanpa perlu menuliskan ekstensi _.php_ ketika mengakses laman.

+ Jalankan perintah `a2enmod rewrite` untuk mengaktifkan _module rewrite_.

+ Restart apache dengan perintah `service apache2 restart`

	<img src="images/32.png" width="700">

Biasanya semua konfigurasi terhadap sebuah website diatur pada file di _directory_ __/etc/apache2/sites-available__. Namun terkadang ada sebuah kasus bahwa   hak akses root untuk mengedit file konfigurasi yang berada di folder __/etc/apache2/sites-available__ tidak dimiliki, atau kita tidak ingin user lain untuk mengedit file konfigurasi yang berada di _directory_ __/etc/apache2/sites-available__.

Untuk mengatasi masalah tersebut, buat file __.htaccess__ pada _directory_ yang akan diatur.

Contohnya adalah seperti kasus di atas, dimana kita ingin mengatur _mod rewrite_ dari __[http://jarkom2022.com](http://jarkom2022.com)__ agar saat mengakses file php kita tidak perlu menuliskan ekstensinya. Maka yang yang perlu kita lakukan adalah
+ Pindah ke _directory_ `/var/www/jarkom2022.com` dan buat file __.htaccess__ dengan isi file
	```
	RewriteEngine On
	RewriteCond %{REQUEST_FILENAME} !-d
	RewriteRule ^([^\.]+)$ $1.php [NC,L]
	```

	<img src="images/33.png" width="700">

	__Keterangan__:
	+ `RewriteEngine On` = untuk flag bahwa menggunakan module rewrite
	+ `RewriteCond %{REQUEST_FILENAME} !-d` = aturan tidak akan jalan ketika yang diakses adalah _directory_ (d)
	+ `RewriteRule ^([^\.]+)$ $1.php [NC,L]` = $1 adalah parameter input yang akan dicari oleh webserver
	* Lebih detailnya [klik disini](https://httpd.apache.org/docs/2.4/rewrite/flags.html)
+ Buat file _about.php_ di dalam _directory_ `/var/www/jarkom2022.com/` dengan isi
	```
	<?php
		echo "Ini adalah halaman About";
	?>
	```
+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com>
	    Options +FollowSymLinks -Multiviews
	    AllowOverride All
	</Directory>
	```
	dan jangan lupa untuk menyimpan perubahan tersebut.

	<img src="images/34.png" width="700">

	__Keterangan__:
	+ `AllowOverride All` ditambahkan agar  konfigurasi __.htaccess__ dapat berjalan.
	+ `+FollowSymLinks` ditambahkan agar konfigurasi __mod_rewrite__ dapat berjalan.
	+ `-Multiviews` ditambahkan agar konfigurasi __mod_negotiation__ tidak dapat berjalan. __mod_negotiation__ bisa '_rewrite_' _requests_ sehingga menimpa dan mengganggu __mod_rewrite__.

+ Restart apache dengan perintah `service apache2 restart`
+ Buka browser dan akses __http://jarkom2022.com/about__

	<img src="images/35.png">

### 4. Nginx Web Server
__Nginx__ (baca: engine-x) adalah perangkat lunak (software) yang bersifat open source yang memiliki banyak fungsi. Web server yang satu ini dikenal dengan performanya yang powerful dan memiliki banyak fitur canggih. Beberapa fungsi dari Nginx di antaranya adalah:

- Web server
- Load Balancing
- Reverse Proxy

#### A. Instalasi Nginx

##### 1. Buka Node Foosha

Lalu jalankan perintah

```bash
apt-get update
apt-get install nginx
```

jika muncul tulisan _"Do you want to continue? [Y/n]"_  input `Y` lalu tekan ___enter___.

Apabila instalasi Nginx telah selesai, jangan lupa jalankan perintah berikut

```bash
service nginx start
```

Untuk mengecek status dari Nginx, bisa menggunakan perintah

```bash
service nginx status
```

##### 2. Gunakan `lynx` untuk mengakses web.

Buka web __IP Water7 Masing-Masing Kelompok__ dengan `lynx` sampai muncul halaman Nginx seperti di bawah ini.

<img src="images/lynx-nginx-1.png">


#### B. Load Balancing pada Nginx

Arsitektur load balancing pada umumnya yang digunakan di Nginx (default):

<img src="images/nginx-lb-default.png">

Namun kita juga bisa menggunakan jenis arsitektur lain, yaitu __Weighted load balancing__, dengan menambahkan parameter `weight` pada konfigurasi Nginx sehingga ada satu node yang memiliki weight atau beban lebih.

<img src="images/nginx-lb-weight.png">


Nginx  juga menawarkan beberapa metode atau algoritma load balancing yang dapat disesuaikan dengan kebutuhan pengguna, berikut ini beberapa metode yang sering digunakan:

- Round robin

	Jika kita memilih metode ini maka distribusi beban akan didistribusikan sesuai dengan urutan nomer dari server atau master. Jika kita memiliki 3 buah node, maka urutannya adalah dari node pertama, kemudian node kedua, dan ketiga. Setelah node ketiga menerima beban, maka akan diulang kembali dari node ke satu. Round robin sendiri merupakan metode default yang ada di Nginx.

	```bash
	upstream mynode {
		server srv1.example.com;
		server srv2.example.com;
		server srv3.example.com;
	}
	```
- Least-connection

	 Jika Round robin akan mendistribusikan berdasarkan nomer dan urutan server, maka least-connection akan melakukan prioritas pembagian dari beban kinerja yang paling rendah. Node master akan mencatat semua beban dan kinerja dari semua node, dan akan melakukan prioritas dari beban yang paling rendah. Sehingga diharapkan tidak ada server dengan beban yang rendah.

	 ```bash
	upstream mynode {
        least_conn;
        server srv1.example.com;
        server srv2.example.com;
        server srv3.example.com;
    }
	 ```

- IP Hash

	Agak berbeda dengan kedua algoritma di atas, algoritma ini akan melakukan hash berdasarkan request dari pengguna (menggunakan alamat IP dari pengguna). Sehingga server akan selalu menerima request dari alamat IP yang berbeda. Ketika server ini tidak tersedia, permintaan dari klien ini akan dilayani oleh server lain.

	```bash
	upstream mynode {
		ip_hash;
		server srv1.example.com;
		server srv2.example.com;
		server srv3.example.com;
	}
	```

- Generic Hash

	Metode Load Balancer Hash ini memetakan beban ke masing-masing node dengan cara membuat hashing berdasarkan text dan atau `Nginx Variables` yang ditentukan dalam hash config.

	```bash
	upstream mynode {
    	hash $request_uri consistent;
    	server srv1.example.com;
		server srv2.example.com;
		server srv3.example.com;
	}
	```

#### C. Upstream
Upstream pada Nginx merujuk pada kelompok atau cluster nodes yang ingin kita gunakan sebagai web server.

```bash
http {
    upstream nama_upstream {
        nama_method;
        server 192.168.1.2;
        server 192.168.1.3;
	server 192.168.1.4 weight=5;
        server ....;
    }
}

server {
    location / {
        proxy_pass http://nama_upstream;
    }
}

```

#### D. Reverse Proxy

Reverse Proxy adalah sistem proxy yang digunakan untuk meneruskan/bypass permintaan client. Reverse proxy sebagai jembatan diantara server frontend dan backend, dan bertugas untuk menjamin pertukaran data dan request berjalan secara lancar.

Selain pertukaran data, Reverse Proxy juga memberikan keamanan dan kompresi, sehingga server menjadi lebih ringan dalam memenuhi banyak permintaan sekaligus. Berikut script sederhana menggunakan reverse proxy

```bash
server {
    listen 80;
    server_name www.jarkom.site jarkom.site;

    location /blog {
       proxy_pass http://blog.jarkom.site:8000/posts/;
    }
}
```

Jika pengunjung mengakses http://jarkom.site/blog/my-post, Nginx akan mem-proxy permintaan ini ke server lain dengan alamat http://blog.jarkom.site:8000/posts. Meski begitu, tetap server utama yang menerima dan melayani koneksi. Singkatnya hanya sebagai perantara.

Ketika alamat server proxy berisi URI, /blog/, permintaan URI yang diteruskan ke server proxy digantikan oleh URI yang ditentukan dalam directive. Jika alamat server proxy ditentukan tanpa URI, maka permintaan koneksi ke URI diteruskan ke server proxy.

#### E. Setup Load Balancing di Nginx

Buatlah topologi sederhana seperti gambar dibawah

<img src="images/lb.png">

Setup IP Address di masing-masing nodes, pastikan setiap nodes terhubung ke  internet

- Foosha

	```bash
	auto eth0
	iface eth0 inet dhcp

	auto eth1
	iface eth1 inet static
		address [Prefix IP].1.1
		netmask 255.255.255.0

	auto eth2
	iface eth2 inet static
		address [Prefix IP].2.1
		netmask 255.255.255.0
	```

- Loguetown

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].1.2
		netmask 255.255.255.0
		gateway [Prefix IP].1.1
	```

- Alabasta

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].1.3
		netmask 255.255.255.0
		gateway [Prefix IP].1.1
	```

- Dressrosa

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].2.2
		netmask 255.255.255.0
		gateway [Prefix IP].2.1
	```

- Enieslobby

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].2.3
		netmask 255.255.255.0
		gateway [Prefix IP].2.1
	```

- Water7

	```bash
	auto eth0
	iface eth0 inet static
		address [Prefix IP].2.4
		netmask 255.255.255.0
		gateway [Prefix IP].2.1
	```

#### Dressrosa (DNS Server)

- instal Bind9 dan Nginx di Dressrosa:

	```bash
	apt-get update
	apt-get install bind9 nginx
	```

- kemudian buat domain sederhana seperti contoh di modul sebelumnya, pada topologi kali ini kita akan menggunakan `jarkom.site` sebagai domain utama.

- isi dari file __named.conf.local__

	```bash
	//
	// Do any local configuration here
	//

	// Consider adding the 1918 zones here, if they are not used in your
	// organization
	//include "/etc/bind/zones.rfc1918";


	zone "jarkom.site" {
			type master;
			file "/etc/bind/jarkom/jarkom.site";
	};

	zone "2.168.192.in-addr.arpa" {
		type master;
		file "/etc/bind/jarkom/2.168.192.in-addr.arpa";
	};
	```

- isi dari file __jarkom.site__

	```bash
	;
	; BIND data file for local loopback interface
	;
	$TTL    604800
	@       IN      SOA     jarkom.site. root.jarkom.site. (
					2         ; Serial
					604800    ; Refresh
					86400     ; Retry
					2419200   ; Expire
					604800 )  ; Negative Cache TTL
	;
	@       IN      NS      jarkom.site.
	@       IN      A       192.168.2.2
	```

- isi dari file __2.168.192.in-addr.arpa__

	```bash
	;
	; BIND data file for local loopback interface
	;
	$TTL    604800
	@       IN      SOA     jarkom.site. root.jarkom.site. (
					2         ; Serial
					604800    ; Refresh
					86400     ; Retry
					2419200   ; Expire
					604800 )  ; Negative Cache TTL
	;
	2.168.192.in-addr.arpa.         IN      NS      jarkom.site.
	2                               IN      PTR     jarkom.site.
	```

- lakukan pengujian untuk domain yang telah dibuat, dari `Alabasta`

	<img src="images/lb-setup-1.png">

#### EniesLobby (Nginx worker)

- install lalu setup Nginx dan PHP

	```bash
	apt-get update && apt install nginx php php-fpm -y
	```

- cek versi dari PHP

	```bash
	php -v
	```

	<img src="images/lb-setup-2.png">

- buat direktori baru di `/var/www`, dengan nama `jarkom`

	```bash
	mkdir /var/www/jarkom
	```

- masuk direktori `jarkom` lalu buat file `index.php`

	```php
	<?php
	echo "Halo, Kamu berada di EniesLobby";
	?>
	```

- selanjutnya kita akan melakukan konfigurasi pada Nginx, pertama masuk ke direktori `/etc/nginx/sites-available` lalu buat file baru dengan nama `jarkom`

	```
	nano jarkom

	atau

	touch jarkom
	```

- kemudian isi dengan konfigurasi server block ini:

	```bash
	server {

		listen 80;

		root /var/www/jarkom;

		index index.php index.html index.htm;
		server_name _;

		location / {
				try_files $uri $uri/ /index.php?$query_string;
		}

		# pass PHP scripts to FastCGI server
		location ~ \.php$ {
		include snippets/fastcgi-php.conf;
		fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
		}

	location ~ /\.ht {
				deny all;
		}

		error_log /var/log/nginx/jarkom_error.log;
		access_log /var/log/nginx/jarkom_access.log;
	}
	```

- lalu simpan, kemudian buat `symlink`

	```bash
	ln -s /etc/nginx/sites-available/jarkom /etc/nginx/sites-enabled
	```

- terakhir restart Nginx

	```bash
	service nginx restart

	atau

	nginx -s reload
	```

- jika mengecek apakah konfigurasi yang dibuat sudah benar atau belum, bisa mengunakan perintah berikut

	```bash
	nginx -t
	```

	<img src="images/lb-setup-3.png">


#### Water7 (Nginx worker)

- lakukan hal yang sama seperti di node EniesLobby, namun bedakan pada konfigurasi `index.php` nya agar memudahkan pada saat pengujian

	```php
	<?php
	echo "Halo, Kamu berada di Water7";
	?>
	```
#### Penjelasan

##### Server Block:

 - `listen` mendefinisikan di port berapa nantinya Nginx berjalan.

 - `root` menjunjukan letak direktori dari file web yang digunakan.

- `index` menentukan urutan file indeks yang akan dicoba oleh server ketika ada permintaan masuk.

- `server_name` menentukan nama server. Tanda garis bawah _ adalah penanda bahwa server akan menanggapi permintaan untuk semua nama server yang tidak cocok dengan nama server lain. Nama server bisa diganti dengan IP Address, nama domain, localhost, dll.

- `location { ... }` Konfigurasi untuk menangani permintaan ke akar situs. __try_files__ mencoba mencari file yang sesuai dengan __$uri__, kemudian __$uri/__, dan jika itu juga tidak ditemukan, akan mengarahkan ke index.php dengan menggunakan __data query string__.

- `location ~ \.php$` konfigurasi untuk menangani file PHP. Lokasi ini akan mencocokkan ekstensi .php pada URL dan akan memprosesnya dengan menggunakan FastCGI dan mengarahkannya ke socket FastCGI PHP. Untuk  penggunaan PHP Socket perlu disesuaikan dengan versi PHP yang diinstall, dalam case ini kita menggunakan PHP7.2.

- `location ~ /\.ht` mengatur bahwa akses ke file .ht (seperti .htaccess) akan ditolak. Ini adalah langkah keamanan yang umum digunakan untuk mencegah akses ke file sensitif.

- `error_log` mengarahkan log error ke file tertentu.

- `access_log` mengarahkan log akses ke file tertenu.

- `ln -s /etc/nginx/sites-available/jarkom /etc/nginx/sites-enabled` adalah perintah untuk membuat symlink (link simbolik) dari file konfigurasi Nginx yang berada di direktori /etc/nginx/sites-available ke direktori /etc/nginx/sites-enabled.


#### Dressrosa (Load Balancer)

- kembali lagi ke node Dressrosa, kemudian buat file baru di direktori `/etc/nginx/sites-available` dengan nama `lb-jarkom`

	```bash
	# Default menggunakan Round Robin
	upstream myweb  {
		server 192.168.2.3; #IP EniesLobby
		server 192.168.2.4; #IP Water7
	}

	server {
		listen 80;
		server_name jarkom.site;

		location / {
		proxy_pass http://myweb;
		}
	}
	```
- lalu simpan lalu buat `symlink`

	```bash
	ln -s /etc/nginx/sites-available/lb-jarkom /etc/nginx/sites-enabled
	```

#### Penjelasan

- `upstream` - mendefinisikan grup atau kelompok server yang akan menerima lalu lintas atau beban dengan __myweb__ sebagai nama upstream. Dalam kasus ini, ada dua server dengan  alamat IP masing-masing 192.168.2.3 dan 192.168.2.4. Dengan metode Round Robin, lalu lintas akan dibagi secara setara antara kedua server ini.

- `listen` - mendefinisikan bahwa web server ini akan berjalan dan mendengarkan permintaan (request) pada port 80.

- `location / { ... }` mengatur cara server Nginx menangani permintaan. Dalam hal ini, semua permintaan akan diteruskan ke grup server yang telah didefinisikan di bagian __upstream__.

#### Pengujian
Masuk ke Loguetwon atau Alabasta lalu jalankan perintah __lynx http://jarkom.site__.

```bash
lynx http://jarkom.site
```
<img src="images/lb-testing-1.gif">


Coba untuk stop service Nginx di salah satu worker, lalu lakukan pengujian lagi.

<img src="images/lb-testing-2.gif">

#### Troubleshoting

- `502 Bad Gateway` - Pastikan socket PHP yang digunakan pada server block sudah sesuai dengan versi PHP yang diinstal.

- `404 Not Found` - Pastikan kembali lokasi dari file PHP di __root__ sudah benar atau belum.

- `403 Forbidden` - Pastikan nama file yang ingin dipanggil dibagian __index__ sudah benar.

- `service php7.2-fpm restart` - Tapi statusnya masih fail, coba dijalankan dulu dengan perintah `service php7.2-fpm start`.

- `Default page Nginx` - Jika ingin menghilangkan default page dari Nginx, jalan perintah `sudo rm -rf /etc/nginx/sites-enabled/default` lalu restart Nginx. Sering terjadi ketika ingin menampilkan halaman dari PHP, tapi yang muncul masih default page Nginx.

- Jangan lupa melakukan restart, ketika ada perubahan pada konfigurasi.


<!-- ### E. Otorisasi
Pada web http:jarkom2022.com terdapat path __/data__ yang tidak boleh dibuka sembarang orang. Rachma ingin __/data__ hanya boleh diakses oleh pengguna yang memiliki IP 10.151.252.0/255.255.252.0

Maka yang diinstruksikan Ifin agar _directory_ __/data__ milik Rachma tetap aman adalah
+ Pindah ke _directory_ `/etc/apache2/sites-available` kemudian buka file ___jarkom2022.com___ dan tambahkan
	```
	<Directory /var/www/jarkom2022.com/data>
	    Options +Indexes
	    Order deny,allow
	    Deny from all
	    Allow from 10.151.252.0/255.255.252.0
	</Directory>
	```
	jangan lupa untuk menyimpan perubahan tersebut.

	__Keterangan__:
	+ `Order deny, allow` merupakan urutan hak akses. Terdapat dua jenis tipe order yaitu:
		+ `deny,allow`: Bagian _Deny_ harus di-_declare_ terlebih dahulu sebelum _Allow_
		+ `allow,deny`: Bagian _Allow_ harus di-_declare_ terlebih dahulu sebelum _Deny_
	+ `Deny from all`  berarti semua pengguna ditolak
	+ `Allow from 10.151.252.0/255.255.252.0` berarti apabila pengguna memiliki IP NID 10.151.252.0./22, ia diperbolehkan untuk mengakses halaman.
	+ Info lebih lanjut [klik disini](https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html)	+ Restart apache dengan perintah `service apache2 restart`
+ Buka browser dan akses __http://jarkom2022.com/data__
Saat pengguna tidak memiliki __IP NID 10.151.252.0/22__ maka akan muncul halaman seperti di bawah ini

	IMG HERE

Sedangkan saat pengguna  memiliki __IP NID 10.151.252.0/22__ maka halaman yang muncul adalah seperti di bawah ini

	IMG HERE

-->

## I. Latihan
<!-- #### TBA -->
1. Download halaman soal latihan di https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/raw/master/Modul-2/Web%20server/page.zip (Gunakan wget)
2. Buat domain baru dengan nama __jarkom.yyy.id__ untuk membuka halaman tersebut.
3. Edit kata `yyy` yang ada di index.php dengan nama kelompok kalian.
4. Atur agar jika kalian mengetikkan __jarkom.yyy.id__, Web latihan dapat terbuka dengan lynx.
5. Cobalah menggunakan algoritma load balancing selain Roundrobin (Least-Conn, IP Hash & Generic Hash)
6. Cobalah untuk menggunakan web server Apache2 di node selain LB.

### Catatan
+ Kemudian unzip file tersebut. Jika muncul error seperti `unzip: command not found` maka install unzip terlebih dahulu menggunakan command `apt-get install unzip`.
+ Buat directory hasil unzip file tersebut menjadi _DocumentRoot_ web
+ Untuk nomor 2, 3, dan 4, '__yyy__' diisi dengan nama kelompok. Contoh: __jarkom.E01.id__


## Jangan ragu bertanya kalau ada yang masih bingung!
<p align="center">
	<img src="images/bingung.jpg" width="50%">
</p>

<!--
	<img src="images/36.png" width="700">
	<img src="images/37.png">
	<img src="images/38.png" width="700">
	<img src="images/39.png" width="700">
	<img src="images/40.png" width="700">
	<img src="images/41.png">
	<img src="images/42.png" width="700">
	<img src="images/43.png">
	<img src="images/44.png">
 -->
