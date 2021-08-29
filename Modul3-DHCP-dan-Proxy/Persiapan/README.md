# Persiapan

## 1. Membuat Topologi Baru

Berikut adalah topologi jaringan yang akan digunakan pada modul 3.

![Topologi Modul 3](images/topologi.png)

1. Hapus terlebih dahulu file UML yang tidak diperlukan bekas praktikum kemarin
    ```bash
    rm BAKSO SOTO SUSHI PIZZA KATSU switch1 switch2
    ```
    **Himbauan!!!**
    * Jangan coba-coba melakukan `rm *` karena akan menghapus semuanya, termasuk file **jarkom**. Jika file tersebut terhapus, segera hubungi asisten.
2. Sesuaikan script ```topologi.sh``` dengan gambar topologi di atas dengan tambahan ketentuan sebagai berikut:
    * Memori client **SOTO**, **KARI**, dan **PECEL** adalah **64M**
    * Memori router **BAKSO** adalah **256M** karena akan menjadi DHCP Server.
    * Memori server **KATSU** dan **PIZZA** adalah **128M** karena akan menjadi DNS Server dan Proxy server.
4. Langkah-langkah selengkapnya silahkan mengikuti panduan membuat UML pada [Modul Pengenalan UML](https://github.com/rohanaq/Modul-Pengenalan-UML).

## 2. Konfigurasi Interface
Konfigurasi interface sama seperti [Modul Pengenalan UML](https://github.com/rohanaq/Modul-Pengenalan-UML), dengan tambahan:

* **PECEL (Sebagai Client)**
    ```bash
    auto eth0
    iface eth0 inet static
    address 192.168.0.4
    netmask 255.255.255.0
    gateway 192.168.0.1
    ```
## 3. Instalasi
Dalam modul 3, kita akan menggunakan 3 aplikasi, yaitu:
* **isc-dhcp-server** (DHCP Server)
* **squid3** (Proxy Server)
* **bind9** (DNS Server)

Lakukan langkah-langkah berikut:
1. Mengupdate package list pada **BAKSO**, **KATSU** dan **PIZZA**.
    ```bash
    apt-get update
    ```
2. Menginstal **isc-dhcp-server** pada router **BAKSO**
    ```bash
    apt-get install isc-dhcp-server
    ```
3. Menginstal **squid3** pada server **PIZZA**
    ```bash
    apt-get install squid3
    ```
4. Menginstal **bind9** pada server **KATSU**
    ```bash
    apt-get install bind9
    ```
# PENTING UNTUK DIINGAT!!!
Lakukan beberapa hal dasar di bawah ini setiap kali kamu **menjalankan UML**:
1. Menjalankan `iptables –t nat –A POSTROUTING –o eth0 –j MASQUERADE –s 192.168.0.0/16` pada router **BAKSO** agar client bisa terhubung dengan internet.
2. Menjalankan **export proxy** pada **semua UML** menggunakan Akun VPN yang bisa didapatkan di [https://id.its.ac.id/otp/](https://id.its.ac.id/otp/).
    ```bash
    export http_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
    export https_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
    export ftp_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
    ```
    Export proxy dilakukan supaya kamu bisa melewati proxy ITS dan bisa menginstal sesuatu.
3. Melakukan `apt-get update` sebelum menginstal sesuatu.

## Selamat Menyiapkan :)
n.b. Jika terjadi masalah, silahkan membuka [troubleshoot](../troubleshoot.md). Jika masalah yang dihadapi tidak ada di troubleshoot tersebut, silahkan gugling. Jika masih juga belum menemukan solusinya, silahkan bertanya pada asisten kesayangan kamu :3
