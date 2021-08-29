# Persiapan 

## 1. Membuat Topologi Baru

Berikut adalah topologi jaringan yang digunakan pada modul 3.

![](images/topologi.jpg)

1. Hapus terlebih dahulu file UML yang tidak diperlukan bekas praktikum kemarin

    ` rm SURABAYA SIDOARJO GRESIK MALANG MOJOKERTO switch1 switch2 `

    **Himbauan !!**
        
    * Jangan coba-coba melakukan `rm*` karena akan menghapus semuanya termasuk file **jarkom**. Jika file tersebut terhapus segera hubungi asisten. 

2. Sesuaikan script topologi.sh dengan gambar topologi di atas dengan tambahan ketentuan sebagai berikut: 

    * Memori client **SIDOARJO**, **GRESIK**, dan **BANYUWANGI** adalah **64M** 

    * Memori router **SURABAYA** adalah **256M** karena akan menjadi DHCP Server.

    * Memori server **MALANG** dan **MOJOKERTO** adalah **128M** karena menjadi DNS Server dan Proxy Server.

3. Langkah-langkah selengkapnya silahkan mengikuti panduan membuat UML pada [Modul Pengenalan UML](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/tree/modul-uml).

## 2. Konfigurasi Interface 

Konfigurasi interface sama seperti [Modul Pengenalan UML](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/tree/modul-uml), dengan tambahan: 

* **BANYUWANGI** (SEBAGAI CLIENT)
```
auto eth0
iface eth0 inet static
address 192.168.0.4
netmask 255.255.255.0
gateway 192.168.0.1
```

## 3. Instalasi 

Dalam modul 3, kita akan menggunakan 3 aplikasi, yaitu:

* **isc-dhcp-server** (DHCP Server)
* **bind9** (DNS Server)
* **squid3** (Proxy Server)

Lakukan langkah-langkah berikut:

1. Mengupdate package list pada **SURABAYA**, **MALANG** dan **MOJOKERTO**. 

    ```
    apt-get update
    ```

2. Menginstal **isc-dhcp-server** pada router **SURABAYA**

    ```
    apt-get install isc-dhcp-server
    ```

3. Menginstal **bind9** pada server **MALANG**

    ```
    apt-get install bind9
    ```

4. Menginstal **squid3** pada server **MOJOKERTO**

    ```
    apt-get install squid
    ```

# Penting untuk diingat

Lakukan beberapa hal dasar di bawah ini setiap kali kamu **menjalankan UML**:

1. Menjalankan `iptables –t nat –A POSTROUTING –o eth0 –j MASQUERADE –s 192.168.0.0/16` pada router SURABAYA agar client bisa terhubung dengan internet.
2. Menjalankan **export proxy** pada **semua UML** menggunakan Akun VPN yang bisa didapatkan di asisten masing-masing. 

    ```
    export http_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
    export https_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
    export ftp_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
    ```

    Export proxy dilakukan supaya kamu bisa melewati proxy ITS dan bisa menginstal sesuatu.
3. Melakukan `apt-get update` sebelum menginstal sesuatu.

## Selamat mengerjakan :)

n.b. Jika terjadi masalah, silahkan membuka [troubleshoot](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/troubleshoot.md). Jika masalah yang dihadapi tidak ada di troubleshoot tersebut, silahkan gugling. Jika masih juga belum menemukan solusinya, silahkan bertanya pada asisten kesayangan anda :') semangat, 2 modul lagi hahahahhahaha. 
