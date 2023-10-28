# 1. DNS (Domain Name System)

## 1.1 Teori

### 1.1.A Pengertian

DNS (_Domain Name System_) adalah sistem penamaan untuk semua device (smartphone, computer, atau
network) yang terhubung dengan internet. DNS Server berfungsi menerjemahkan nama domain menjadi alamat IP. DNS dibuat guna untuk menggantikan sistem penggunaan file host yang dirasa tidak efisien.

### 1.1.B Cara Kerja

![DNS](images/1.jpg)

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

### 1.2.A Buat Topologi

Buat topologi seperti di [pengenalan GNS3](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/tree/master/Modul-GNS3#membuat-topologi) kemarin.

Kita akan membuat node `EniesLobby` sebagai DNS server.

### 1.2.A Instalasi bind

- Buka *EniesLobby* dan update package lists dengan menjalankan command:

	```
	apt-get update
	```

- Setalah melakukan update silahkan install aplikasi bind9 pada *EniesLobby* dengan perintah:

	```
	apt-get install bind9 -y
	```

![instal bind9](images/1.png)

### 1.2.B Pembuatan Domain
Pada sesilab ini kita akan membuat domain **jarkom2022.com**.

- Lakukan perintah pada *EniesLobby*. Isikan seperti berikut:

  ```
  nano /etc/bind/named.conf.local
  ```

- Isikan configurasi domain **jarkom2022.com** sesuai dengan syntax berikut:

  ```
  zone "jarkom2022.com" {
  	type master;
  	file "/etc/bind/jarkom/jarkom2022.com";
  };
  ```

![config jarkom2022.com](images/2-2.png)

- Buat folder **jarkom** di dalam **/etc/bind**

  ```
  mkdir /etc/bind/jarkom
  ```

- Copykan file **db.local** pada path **/etc/bind** ke dalam folder **jarkom** yang baru saja dibuat dan ubah namanya menjadi **jarkom2022.com**

  ```
  cp /etc/bind/db.local /etc/bind/jarkom/jarkom2022.com
  ```

- Kemudian buka file **jarkom2022.com** dan edit seperti gambar berikut dengan IP *EniesLobby* masing-masing kelompok:

  ```
  nano /etc/bind/jarkom/jarkom2022.com
  ```

![konfig jarkom2022](images/3-1.png)

- Restart bind9 dengan perintah 

  ```
  service bind9 restart
  
  ATAU
  
  named -g //Bisa digunakan untuk restart sekaligus debugging
  ```



### 1.2.C Setting nameserver pada client

Domain yang kita buat tidak akan langsung dikenali oleh client oleh sebab itu kita harus merubah settingan nameserver yang ada pada client kita.

- Pada client *Loguetown* dan *Alabasta* arahkan nameserver menuju IP *EniesLobby* dengan mengedit file _resolv.conf_ dengan mengetikkan perintah 

	```
	nano /etc/resolv.conf
	```

![ping](images/4-1.png)

- Untuk mencoba koneksi DNS, lakukan ping domain **jarkom2022.com** dengan melakukan  perintah berikut pada client *Loguetown* dan *Alabasta*

  ```
  ping jarkom2022.com -c 5
  ```

![ping](images/5-1.png)



### 1.2.D Reverse DNS (Record PTR)

Jika pada pembuatan domain sebelumnya DNS server kita bekerja menerjemahkan string domain **jarkom2022.com** kedalam alamat IP agar dapat dibuka, maka Reverse DNS atau Record PTR digunakan untuk menerjemahkan alamat IP ke alamat domain yang sudah diterjemahkan sebelumnya.

- Edit file **/etc/bind/named.conf.local** pada *EniesLobby*

  ```
  nano /etc/bind/named.conf.local
  ```

- Lalu tambahkan konfigurasi berikut ke dalam file **named.conf.local**. Tambahkan reverse dari 3 byte awal dari IP yang ingin dilakukan Reverse DNS. Karena di contoh saya menggunakan IP `192.168.2` untuk IP dari records, maka reversenya adalah `2.168.192` 

  ```
  zone "2.168.192.in-addr.arpa" {
      type master;
      file "/etc/bind/jarkom/2.168.192.in-addr.arpa";
  };
  ```

![](images/6-1.png)

- Copykan file **db.local** pada path **/etc/bind** ke dalam folder **jarkom** yang baru saja dibuat dan ubah namanya menjadi **2.168.192.in-addr.arpa**

  ```
  cp /etc/bind/db.local /etc/bind/jarkom/2.168.192.in-addr.arpa
  ```

  *Keterangan 2.168.192 adalah 3 byte pertama IP EniesLobby yang dibalik urutan penulisannya*

- Edit file **2.168.192.in-addr.arpa** menjadi seperti gambar di bawah ini


![konfig](images/7-1.png)

- Kemudian restart bind9 dengan perintah 

  ```
  service bind9 restart
  ```

- Untuk mengecek apakah konfigurasi sudah benar atau belum, lakukan perintah berikut pada client *Loguetown* 

  ```
  // Install package dnsutils
  // Pastikan nameserver di /etc/resolv.conf telah dikembalikan sama dengan nameserver dari Foosha
  apt-get update
  apt-get install dnsutils
  
  //Kembalikan nameserver agar tersambung dengan EniesLobby
  host -t PTR "IP EniesLobby"
  ```

![host](images/8-1.png)



### 1.2.E Record CNAME
Record CNAME adalah sebuah record yang membuat alias name dan mengarahkan domain ke alamat/domain yang lain.

Langkah-langkah membuat record CNAME:

- Buka file **jarkom2022.com** pada server *EniesLobby* dan tambahkan konfigurasi seperti pada gambar berikut:


![DNS](images/9-1.png)



- Kemudian restart bind9 dengan perintah

  ```
  service bind9 restart
  ```

- Lalu cek dengan melakukan `host -t CNAME www.jarkom2022.com` atau `ping www.jarkom2022.com -c 5`. Hasilnya harus mengarah ke host dengan IP *EniesLobby*.


![DNS](images/10-1.png)



### 1.2.F Membuat DNS Slave

DNS Slave adalah DNS cadangan yang akan diakses jika server DNS utama mengalami kegagalan. Kita akan menjadikan server *Water7* sebagai DNS slave dan server *EniesLobby* sebagai DNS masternya.

#### I. Konfigurasi Pada Server EniesLobby

- Edit file **/etc/bind/named.conf.local** dan sesuaikan dengan syntax berikut

  ```
  zone "jarkom2022.com" {
      type master;
      notify yes;
      also-notify { "IP Water7"; }; // Masukan IP Water7 tanpa tanda petik
      allow-transfer { "IP Water7"; }; // Masukan IP Water7 tanpa tanda petik
      file "/etc/bind/jarkom/jarkom2022.com";
  };
  ```

  ![DNS](images/11-2.png)



- Lakukan restart bind9

  ```
  service bind9 restart
  ```



#### II. Konfigurasi Pada Server Water7

- Buka *Water7* dan update package lists dengan menjalankan command:

  ```
  apt-get update
  ```

- Setalah melakukan update silahkan install aplikasi bind9 pada *Water7* dengan perintah:

  ```
  apt-get install bind9 -y
  ```

- Kemudian buka file **/etc/bind/named.conf.local** pada Water7 dan tambahkan syntax berikut:

  ```
  zone "jarkom2022.com" {
      type slave;
      masters { "IP EniesLobby"; }; // Masukan IP EniesLobby tanpa tanda petik
      file "/var/lib/bind/jarkom2022.com";
  };
  ```

![DNS](images/12-2.png)

- Lakukan restart bind9

  ```
  service bind9 restart
  ```



#### III. Testing

- Pada server *EniesLobby* silahkan matikan service bind9

  ```
  service bind9 stop
  ```

- Pada client *Loguetown* pastikan pengaturan nameserver mengarah ke IP *EniesLobby* dan IP *Water7*

  ![DNS](images/13-1.png)

- Lakukan ping ke jarkom2022.com pada client *Loguetown*. Jika ping berhasil maka konfigurasi DNS slave telah berhasil


![DNS](images/14-1.png)



### 1.2.G Membuat Subdomain

Subdomain adalah bagian dari sebuah nama domain induk. Subdomain umumnya mengacu ke suatu alamat fisik di sebuah situs contohnya: **jarkom2022.com** merupakan sebuah domain induk. Sedangkan **luffy.jarkom2022.com** merupakan sebuah subdomain.

- Pada *EniesLobby*, edit file **/etc/bind/jarkom/jarkom2022.com** lalu tambahkan subdomain untuk **jarkom2022.com** yang mengarah ke IP *Water7*.

  ```
  nano /etc/bind/jarkom/jarkom2022.com
  ```

- Tambahkan konfigurasi seperti pada gambar ke dalam file **jarkom2022.com**.

![DNS](images/15-1.png)

- Restart service bind  

  ```
  service bind9 restart
  ```

- Coba ping ke subdomain dengan perintah berikut dari client *Loguetown*

  ```
  ping luffy.jarkom2022.com -c 5
  
  ATAU
  
  host -t A luffy.jarkom2022.com
  ```

  ![DNS](images/16-1.png)



### 1.2.H Delegasi Subdomain

Delegasi subdomain adalah pemberian wewenang atas sebuah subdomain kepada DNS baru.

#### I. Konfigurasi Pada Server *EniesLobby*

- Pada *EniesLobby*, edit file **/etc/bind/jarkom/jarkom2022.com** dan ubah menjadi seperti di bawah ini sesuai dengan pembagian IP *EniesLobby* kelompok masing-masing.

  ```
  nano /etc/bind/jarkom/jarkom2022.com
  ```

![DNS](images/17-1.png)

- Kemudian edit file **/etc/bind/named.conf.options** pada *EniesLobby*.

  ```
  nano /etc/bind/named.conf.options
  ```

- Kemudian comment **dnssec-validation auto;** dan tambahkan baris berikut pada **/etc/bind/named.conf.options**

  ```
  allow-query{any;};
  ```


![DNS](images/18.png)

- Kemudian edit file **/etc/bind/named.conf.local** menjadi seperti gambar di bawah:

  ```
  zone "jarkom2022.com" {
      type master;
      file "/etc/bind/jarkom/jarkom2022.com";
      allow-transfer { "IP Water7"; }; // Masukan IP Water7 tanpa tanda petik
  };
  ```


![DNS](images/19-1.png)

- Setelah itu restart bind9

  ```
  service bind9 restart
  ```

#### II. Konfigurasi Pada Server *Water7*

- Pada *Water7* edit file **/etc/bind/named.conf.options**

  ```
  nano /etc/bind/named.conf.options
  ```

- Kemudian comment **dnssec-validation auto;** dan tambahkan baris berikut pada **/etc/bind/named.conf.options**

  ```
  allow-query{any;};
  ```

![DNS](images/18.png)

- Lalu edit file **/etc/bind/named.conf.local** menjadi seperti gambar di bawah:

![DNS](images/21-2.png)

- Kemudian buat direktori dengan nama **delegasi** 

- Copy **db.local** ke direktori tersebut dan edit namanya menjadi **its.jarkom2022.com** 

  ```
  mkdir /etc/bind/delegasi
  cp /etc/bind/db.local /etc/bind/delegasi/its.jarkom2022.com
  ```

- Kemudian edit file **its.jarkom2022.com** menjadi seperti dibawah ini

![DNS](images/22-1.png)

- Restart bind9

  ```
  service bind9 restart
  ```

#### III. Testing

- Lakukan ping ke domain **its.jarkom2022.com** dan **integra.its.jarkom2022.com** dari client *Loguetown*

![DNS](images/23-1.png)



### 1.2.I DNS Forwarder

DNS Forwarder digunakan untuk mengarahkan DNS Server ke IP yang ingin dituju.

- Edit file **/etc/bind/named.conf.options** pada server *EniesLobby*
- Uncomment pada bagian ini

```
forwarders {
    "IP nameserver dari Foosha";
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

![DNS](images/24-1.png)
- Restart bind9

  ```
  service bind9 restart
  ```

- Harusnya jika nameserver pada file **/etc/resolv.conf** di client diubah menjadi IP EniesLobby maka akan di forward ke IP DNS GNS3 yaitu IP nameserver yang ada di Foosha dan bisa mendapatkan koneksi.
- Coba ping google.com pada Loguetown, kalau benar maka tetap bisa mendapatkan respon dari google

![DNS](images/25.png)



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

   ![DNS](images/7-1.png)

2. #### Penggunaan Titik

   ![DNS](images/17-1.png)

   Pada salah satu contoh di atas, dapat kita amati pada kolom keempat terdapat record yang menggunakan titik pada akhir kata dan ada yang tidak. Penggunaan titik berfungsi sebagai penentu FQDN (Fully-Qualified Domain Name) suatu domain.

   Contohnya jika "**jarkom2022.com.**" di akhiri dengan titik maka akan dianggap sebagai FQDN dan akan dibaca sebagai "**jarkom2022.com**" , sedangkan ns1 di atas tidak menggunakan titik sehingga dia tidak terbaca sebagai FQDN. Maka ns1 akan di tambahkan di depan terhadap nilai $ORIGIN sehinga ns1 akan terbaca sebagai "**ns1.jarkom2022.com**" . Nilai $ORIGIN diambil dari penamaan zone yang terdapat pada  */etc/bind/named.conf.local*.

3. #### Penulisan Name Server (NS) record

   Salah satu aturan penulisan NS record adalah dia harus menuju A record., bukan CNAME. 



## Latihan

1. Buatlah agar bila kita mengecek *IP EniesLobby* menggunakan dnsutils (host -t PTR 'IP EniesLobby') hasilnya ip tersebut dimiliki oleh domain **jarkom.com** !
2. Buatlah subdomain **seru.jarkom.com**, **pre-test.jarkom.com**, dan **cool.jarkom.com** yang mengarah ke *IP Water7*!
3. Buatlah subdomain **kerja.jarkom.com**. Lalu buatlah subdomain dalam subdomain dalam subdomain **yyy.lagi.ngerjain.jarkom.com** yang mengarah ke EniesLobby ! (yyy = nama kelompok)
4. Buat record CNAME **bagus.jarkom.com** dan **semangat.yyy.jarkom.com** yang mengarah ke **jarkom.com**! (yyy = nama kelompok)
5. Delegasikan subdomain **yyy.ngerjain.jarkom.com** dan **asyik.yyy.ngerjain.jarkom.com** dari EniesLobby ke Water7 ! (yyy = nama kelompok)

## References
* https://computer.howstuffworks.com/dns.htm
* http://knowledgelayer.softlayer.com/faq/what-does-serial-refresh-retry-expire-minimum-and-ttl-mean
* https://en.wikipedia.org/wiki/List_of_DNS_record_types
* https://kb.indowebsite.id/knowledge-base/pengertian-catatan-dns-atau-record-dns/
