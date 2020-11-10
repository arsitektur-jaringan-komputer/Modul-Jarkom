# 2. Proxy Server
## Outline
- 2. Proxy Server
	- Outline
	- 2.1 Pengertian, Fungsi, dan Manfaat
		- 2.1.1 Pengertian 
		- 2.1.2 Fungsi 
		- 2.1.3 Manfaat
		- 2.1.4 Software Proxy Server
		- 2.1.5 Cara Kerja Squid
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
