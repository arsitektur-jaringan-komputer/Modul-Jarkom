# **PENTING UNTUK DIBACA**
1. Pastikan UML *MALANG* dan *MOJOKERTO* Memory yang sebelumnya **96 diganti 256** pada file topologi.sh.

2. Jalankan **iptables** agar client *GRESIK* dan *SIDOARJO* bisa terhubung ke internet.

3. Ketika ingin mengakses internet pastikan sudah mengexport proxy terlebih dahulu. **syntaxnya cek modul pengenalan UML** .

4. Jangan melakukan apapun sebelum asisten memberikan perintah.

5. Ikuti apa yang asisten arahkan.

6. Ketika point 4 dan 5 tidak ditaati **resiko tanggung sendiri!!!**


# 1. DNS (Domain Name System)

## 1.1 Teori

### 1.1.A Pengertian

DNS (_Domain Name System_) adalah sistem penamaan untuk semua device (smartphone, computer, atau
network) yang terhubung dengan internet. DNS Server berfungsi menerjemahkan nama domain menjadi alamat IP. DNS dibuat guna untuk menggantikan sistem penggunaan file host yang dirasa tidak efisien.

### 1.1.B Cara Kerja

![DNS](gambar/1.jpg)

Client akan meminta alamt IP dari suatu domain ke DNS server. Jika pada DNS server data alamat IP dari DNS server tersebut ada maka akan di return alamat IP nya kembali menuju client. Jika DNS server tersebut tidak memiliki alamat IP dari domain tersebut maka dia akan bertanya kepada DNS server yang lain sampai alamat domain itu ditemukan.

### 1.1.C Aplikasi DNS Server

Untuk praktikum jarkom kita menggunakan aplikasi BIND9 sebagai DNS server, karena BIND(Berkley Internet Naming Daemon) adalah DNS server yang paling banyak digunakan dan juga memiliki fitur-fitur yang cukup lengkap.

### 1.1.D List DNS Record
| Tipe          | Deskripsi                     |
| ------------- |:-----------------------------|
| A             | Memetakan nama domain ke alamat IP (IPv4) dari komputer hosting domain|
| AAAA          | AAAA record hampir mirip A record, tapi mengarahkan domain ke alamat Ipv6|
| CNAME         | Alias ​​dari satu nama ke nama lain: pencarian DNS akan dilanjutkan dengan mencoba lagi pencarian dengan nama baru|
| NS            | Delegasikan zona DNS untuk menggunakan authoritative name servers yang diberikan|
| PTR           | Digunakan untuk Reverse DNS (Domain Name System) lookup|
| SOA           | Mengacu server DNS yang mengediakan otorisasi informasi tentang sebuah domain Internet|
| TXT           | Mengijinkan administrator untuk memasukan data acak ke dalam catatan DNS, catatan ini juga digunakan di spesifikasi Sender Policy Framework|

### 1.1.E SOA (Start of Authority)

Adalah informasi yang dimiliki oleh suatu DNS zone.

| Nama          | Deskripsi                     |
| ------------- |:-----------------------------|
| Serial        | Jumlah revisi dari file zona ini. Kenaikan nomor ini setiap kali file zone diubah sehingga perubahannya akan didistribusikan ke server DNS sekunder manapun|
| Refresh       | Jumlah waktu dalam detik bahwa nameserver sekunder harus menunggu untuk memeriksa salinan baru dari zona DNS dari nameserver utama domain. Jika file zona telah berubah maka server DNS sekunder akan memperbarui salinan zona tersebut agar sesuai dengan zona server DNS utama|
| Retry         | Jumlah waktu dalam hitungan detik bahwa nameserver utama domain (atau server) harus menunggu jika upaya refresh oleh nameserver sekunder gagal sebelum mencoba refresh zona domain dengan nameserver sekunder itu lagi|
| Expire        | Jumlah waktu dalam hitungan detik bahwa nameserver sekunder (atau server) akan menahan zona sebelum tidak lagi mempunyai otoritas|
| Minimum       | Jumlah waktu dalam hitungan detik bahwa catatan sumber daya domain valid. Ini juga dikenal sebagai TTL minimum, dan dapat diganti oleh TTL catatan sumber daya individu|
| TTL           | (waktu untuk tinggal) - Jumlah detik nama domain di-cache secara lokal sebelum kadaluarsa dan kembali ke nameserver otoritatif untuk informasi terbaru|



------





## 1.2 Praktik

### 1.2.A Buat Topologi Berikut

![Topologi](gambar/topologi.png)

Seperti pada modul pengenalan UML kemaren

### 1.2.A Instalasi bind

- Buka *MALANG* dan update package lists dengan menjalankan command:

	```
	apt-get update
	```

- Setalah melakukan update silahkan install aplikasi bind9 pada *MALANG* dengan perintah:

	```
	apt-get install bind9 -y
	```

![instal bind9](gambar/1.png)

### 1.2.B Pembuatan Domain
Pada sesilab ini kita akan membuat domain **jarkom2020.com**.

- Lakukan perintah pada *MALANG*. Isikan seperti berikut:

  ```
   nano /etc/bind/named.conf.local
  ```

- Isikan configurasi domain **jarkom2020.com** sesuai dengan syntax berikut:

  ```
  zone "jarkom2020.com" {
  	type master;
  	file "/etc/bind/jarkom/jarkom2020.com";
  };
  ```

![config jarkom2020.com](gambar/2.png)

- Buat folder **jarkom** di dalam **/etc/bind**

  ```
  mkdir /etc/bind/jarkom
  ```

- Copykan file **db.local** pada path **/etc/bind** ke dalam folder **jarkom** yang baru saja dibuat dan ubah namanya menjadi **jarkom2020.com**

  ```
  cp /etc/bind/db.local /etc/bind/jarkom/jarkom2020.com
  ```

- Kemudian buka file **jarkom2020.com** dan edit seperti gambar berikut dengan IP *MALANG* masing-masing kelompok:

  ```
  nano /etc/bind/jarkom/jarkom2020.com
  ```

![konfig jarkom2020](gambar/3.png)

- Restart bind9 dengan perintah 

  ```
  service bind9 restart
  
  ATAU
  
  named -g //Bisa digunakan untuk restart sekaligus debugging
  ```



### 1.2.C Setting nameserver pada client

Domain yang kita buat tidak akan langsung dikenali oleh client oleh sebab itu kita harus merubah settingan nameserver yang ada pada client kita.

- Pada client *GRESIK* dan *SIDOARJO* arahkan nameserver menuju IP *MALANG* dengan mengedit file _resolv.conf_ dengan mengetikkan perintah 

	```
	nano /etc/resolv.conf
	```

![ping](gambar/4.png)

- Untuk mencoba koneksi DNS, lakukan ping domain **jarkom2020.com** dengan melakukan  perintah berikut pada client *GRESIK* dan *SIDOARJO*

  ```
  ping jarkom2020.com
  ```

![ping](gambar/5.png)



### 1.2.D Reverse DNS (Record PTR)

Jika pada pembuatan domain sebelumnya DNS server kita bekerja menerjemahkan string domain **jarkom2020.com** kedalam alamat IP agar dapat dibuka, maka Reverse DNS atau Record PTR digunakan untuk menerjemahkan alamat IP ke alamat domain yang sudah diterjemahkan sebelumnya.

- Edit file **/etc/bind/named.conf.local** pada *MALANG*

  ```
  nano /etc/bind/named.conf.local
  ```

- Lalu tambahkan konfigurasi berikut ke dalam file **named.conf.local**

  ```
  zone "71.151.10.in-addr.arpa" {
      type master;
      file "/etc/bind/jarkom/71.151.10.in-addr.arpa";
  };
  ```

![](gambar/6.png)

- Copykan file **db.local** pada path **/etc/bind** ke dalam folder **jarkom** yang baru saja dibuat dan ubah namanya menjadi **71.151.10.in-addr.arpa**

  ```
  cp /etc/bind/db.local /etc/bind/jarkom/71.151.10.in-addr.arpa
  ```

  *Keterangan 71.151.10 adalah 3 byte pertama IP MALANG yang dibalik urutan penulisannya*

- Edit file **71.151.10.in-addr.arpa** menjadi seperti gambar di bawah ini


![konfig](gambar/7.png)

- Kemudian restart bind9 dengan perintah 

  ```
  service bind9 restart
  ```

- Untuk mengecek apakah konfigurasi sudah benar atau belum, lakukan perintah berikut pada client *GRESIK* 

  ```
  // Install package dnsutils
  // Pastikan nameserver telah dikembalikan ke settingan awal
  apt-get update
  apt-get install dnsutils
  
  //Kembalikan nameserver agar tersambung dengan MALANG
  host -t PTR "IP MALANG"
  ```

![host](gambar/8.png)



### 1.2.E Record CNAME
Record CNAME adalah sebuah record yang membuat alias name dan mengarahkan domain ke alamat/domain yang lain.

Langkah-langkah membuat record CNAME:

- Buka file **jarkom2020.com** pada server *MALANG* dan tambahkan konfigurasi seperti pada gambar berikut:


![DNS](gambar/9.png)



- Kemudian restart bind9 dengan perintah

  ```
  service bind9 restart
  ```

- Lalu cek dengan melakukan **host -t CNAME www.jarkom2020.com** atau **ping www.jarkom2020.com**. Hasilnya harus mengarah ke host dengan IP *MALANG*.


![DNS](gambar/10.png)



### 1.2.F Membuat DNS Slave

DNS Slave adalah DNS cadangan yang akan diakses jika server DNS utama mengalami kegagalan. Kita akan menjadikan server *MOJOKERTO* sebagai DNS slave dan server *MALANG* sebagai DNS masternya.

#### I. Konfigurasi Pada Server MALANG

- Edit file **/etc/bind/named.conf.local** dan sesuaikan dengan syntax berikut

  ```
  zone "jarkom2020.com" {
      type master;
      notify yes;
      also-notify { "IP MOJOKERTO"; }; // Masukan IP MOJOKERTO tanpa tanda petik
      allow-transfer { "IP MOJOKERTO"; }; // Masukan IP MOJOKERTO tanpa tanda petik
      file "/etc/bind/jarkom/jarkom2020.com";
  };
  ```

  ![DNS](gambar/11.png)



- Lakukan restart bind9

  ```
  service bind9 restart
  ```



#### II. Konfigurasi Pada Server MOJOKERTO

- Buka *MOJOKERTO* dan update package lists dengan menjalankan command:

  ```
  apt-get update
  ```

- Setalah melakukan update silahkan install aplikasi bind9 pada *MOJOKERTO* dengan perintah:

  ```
  apt-get install bind9 -y
  ```

- Kemudian buka file **/etc/bind/named.conf.local** pada MOJOKERTO dan tambahkan syntax berikut:

  ```
  zone "jarkom2020.com" {
      type slave;
      masters { "IP MALANG"; }; // Masukan IP MALANG tanpa tanda petik
      file "/var/lib/bind/jarkom2020.com";
  };
  ```

![DNS](gambar/12.png)

- Lakukan restart bind9

  ```
  service bind9 restart
  ```



#### III. Testing

- Pada server *MALANG* silahkan matikan service bind9

  ```
  service bind9 stop
  ```

- Pada client *GRESIK* pastikan pengaturan nameserver mengarah ke IP *MALANG* dan IP *MOJOKERTO*

  ![DNS](gambar/13.png)

- Lakukan ping ke jarkom2020.com pada client *GRESIK*. Jika ping berhasil maka konfigurasi DNS slave telah berhasil


![DNS](gambar/14.png)



### 1.2.G Membuat Subdomain

Subdomain adalah bagian dari sebuah nama domain induk. Subdomain umumnya mengacu ke suatu alamat fisik di sebuah situs contohnya: **jarkom2020.com** merupakan sebuah domain induk. Sedangkan **neko.jarkom2020.com** merupakan sebuah subdomain.

- Edit file **/etc/bind/jarkom/jarkom2020.com** lalu tambahkan subdomain untuk **jarkom2020.com** yang mengarah ke IP *MALANG*.

  ```
  nano /etc/bind/jarkom/jarkom2020.com
  ```

- Tambahkan konfigurasi seperti pada gambar ke dalam file **jarkom2020.com**.

![DNS](gambar/15.png)

- Restart service bind  

  ```
  service bind9 restart
  ```

- Coba ping ke subdomain dengan perintah berikut dari client *GRESIK*

  ```
  ping neko.jarkom2020.com
  
  ATAU
  
  host -t A neko.jarkom2020.com
  ```

  ![DNS](gambar/16.png)



### 1.2.H Delegasi Subdomain

Delegasi subdomain adalah pemberian wewenang atas sebuah subdomain kepada DNS baru.

#### I. Konfigurasi Pada Server *MALANG*

- Pada *MALANG*, edit file **/etc/bind/jarkom/jarkom2020.com** dan ubah menjadi seperti di bawah ini sesuai dengan pembagian IP *MALANG* kelompok masing-masing.

  ```
  nano /etc/bind/jarkom/jarkom2020.com
  ```

![DNS](gambar/17.png)

- Kemudian edit file **/etc/bind/named.conf.options** pada *MALANG*.

  ```
  nano /etc/bind/named.conf.options
  ```

- Kemudian comment **dnssec-validation auto;** dan tambahkan baris berikut pada **/etc/bind/named.conf.options**

  ```
  allow-query{any;};
  ```


![DNS](gambar/18.png)

- Kemudian edit file **/etc/bind/named.conf.local** menjadi seperti gambar di bawah:

  ```
  zone "jarkom2020.com" {
      type master;
      file "/etc/bind/jarkom/jarkom2020.com";
      allow-transfer { "IP MOJOKERTO"; }; // Masukan IP MOJOKERTO tanpa tanda petik
  };
  ```


![DNS](gambar/19.png)

- Setelah itu restart bind9

  ```
  service bind9 restart
  ```

#### II. Konfigurasi Pada Server *MOJOKERTO*

- Pada *MOJOKERTO* edit file **/etc/bind/named.conf.options**

  ```
  nano /etc/bind/named.conf.options
  ```

- Kemudian comment **dnssec-validation auto;** dan tambahkan baris berikut pada **/etc/bind/named.conf.options**

  ```
  allow-query{any;};
  ```

![DNS](gambar/20.png)

- Lalu edit file **/etc/bind/named.conf.local** menjadi seperti gambar di bawah:

![DNS](gambar/21.png)

- Kemudian buat direktori dengan nama **delegasi** 

- Copy **db.local** ke direktori pucang dan edit namanya menjadi **its.jarkom2020.com** 

  ```
  mkdir /etc/bind/delegasi
  cp /etc/bind/db.local /etc/bind/delegasi/its.jarkom2020.com
  ```

- Kemudian edit file **its.jarkom2020.com** menjadi seperti dibawah ini

![DNS](gambar/22.png)

- Restart bind9

  ```
  service bind9 restart
  ```

#### III. Testing

- Lakukan ping ke domain **its.jarkom2020.com** dan **integra.its.jarkom2020.com** dari client *GRESIK*

![DNS](gambar/23.png)



### 1.2.I DNS Forwarder

DNS Forwarder digunakan untuk mengarahkan DNS Server ke IP yang ingin dituju.

- Edit file **/etc/bind/named.conf.options** pada server *MALANG*
- Uncomment pada bagian ini

```
forwarders {
    8.8.8.8;
};
```
- Comment pada bagian ini

```
// dnssec-validation auto;
```
- Dan tambahkan

```
allow-query{any;};
```

![DNS](gambar/24.png)

- Harusnya jika nameserver pada file **/etc/resolv.conf** di client diubah menjadi IP MALANG maka akan di forward ke IP DNS google yaitu 8.8.8.8 dan bisa mendapatkan koneksi.
- Coba ping google.com pada GRESIK, kalau benar maka tetap bisa mendapatkan respon dari google

![DNS](gambar/25.png)



### 1.3 Keterangan Configurasi Zone file

1. #### Penulisan Serial

   Ditulis dengan format YYYYMMDDXX. Serial di increment setiap melakukan perubahan pada file zone.

   ```
   YYYY adalah tahun
   MM adalah bulan
   DD adalah tanggal
   XX adalah counter
   ```

   Contoh:

   ![DNS](gambar/7.png)

2. #### Penggunaan Titik

   ![DNS](gambar/17.png)

   Pada salah satu contoh di atas, dapat kita amati pada kolom keempat terdapat record yang menggunakan titik pada akhir kata dan ada yang tidak. Penggunaan titik berfungsi sebagai penentu FQDN (Fully-Qualified Domain Name) suatu domain.

   Contohnya jika "**jarkom2020.com.**" di akhiri dengan titik maka akan dianggap sebagai FQDN dan akan dibaca sebagai "**jarkom2020.com**" , sedangkan ns1 di atas tidak menggunakan titik sehingga dia tidak terbaca sebagai FQDN. Maka ns1 akan di tambahkan di depan terhadap nilai $ORIGIN sehinga ns1 akan terbaca sebagai "**ns1.jarkom2020.com**" . Nilai $ORIGIN diambil dari penamaan zone yang terdapat pada  */etc/bind/named.conf.local*.

3. #### Penulisan Name Server (NS) record

   Salah satu aturan penulisan NS record adalah dia harus menuju A record., bukan CNAME. 



## Latihan

1. Buatlah agar bila kita mengecek *IP MALANG* menggunakan dnsutils (host -t PTR 'IP MALANG') hasilnya ip tersebut dimiliki oleh domain **jarkom.com** !
2. Buatlah subdomain **ngerjain.jarkom.com**. Lalu buatlah subdomain dalam subdomain dalam subdomain **yyy.lagi.ngerjain.jarkom.com** ! (yyy = nama kelompok)

## References
* https://computer.howstuffworks.com/dns.htm
* http://knowledgelayer.softlayer.com/faq/what-does-serial-refresh-retry-expire-minimum-and-ttl-mean
* https://en.wikipedia.org/wiki/List_of_DNS_record_types
* https://kb.indowebsite.id/knowledge-base/pengertian-catatan-dns-atau-record-dns/
