# Persiapan

![image](https://c.tenor.com/A-zBK3Pr8YQAAAAM/suuuper-franky.gif)

## 1. Membuat Topologi Baru

Buat topologi baru sesuai dengan peta topologi jaringan dibawah.

![image](../Modul-3/Reverse%20Proxy/img/prequesites.png)

## 2. Konfigurasi Interface

Konfigurasi interface sama seperti [Modul GNS3](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/tree/modul-uml), dengan tambahan:

* **Dressrosa** (SEBAGAI REVERSE PROXY)
```
auto eth0
iface eth0 inet static
	address [Prefix IP].2.2
	netmask 255.255.255.0
	gateway [Prefix IP].2.1
```
* **Jipangu** (SEBAGAI WORKER)

```
auto eth0
iface eth0 inet static
	address [Prefix IP].2.5
	netmask 255.255.255.0
	gateway [Prefix IP].2.1
```

## 3. Instalasi

Dalam modul 3, kita akan menggunakan 3 aplikasi, yaitu:

* **isc-dhcp-server** digunakan untuk DHCP Server
* **bind9** digunakan untuk DNS Server
* **nginx** digunakan untuk Reverse Proxy

Lakukan langkah-langkah berikut:

1. Mengupdate package list pada **Foosha**, **EniesLobby** dan **Dressrosa**.

    ```
    apt-get update
    ```

2. Menginstal **isc-dhcp-server** pada router **Foosha**

    ```
    apt-get install isc-dhcp-server
    ```

3. Menginstal **bind9** pada server **EniesLobby**

    ```
    apt-get install bind9
    ```

4. Menginstal **nginx** pada server **Dressrosa**

    ```
    apt-get install nginx
    ```

# Inget ini yaa 👋

Lakukan beberapa hal dasar di bawah ini setiap kali kamu **menjalankan GNS3**:

1. Menjalankan `iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s [Prefix IP].0.0/16` pada router **Foosha** agar semua node bisa terhubung dengan internet.
2. Jangan lupa cek Domain Name System resolver di `/etc/resolv.conf` setiap node. Samakan Domain Name System resolver setiap node dengan miliknya **Foosha**
3. Melakukan `apt-get update` sebelum menginstal sesuatu.

## Selamat mengerjakan :)

n.b. Jika terjadi masalah, silahkan restart GNS3 nya atau VM nya. Jika masih juga belum menemukan solusinya, silakan tanya ke asisten masing-masing. **Jika** masih belum belum juga nemuin solusinya, silakan kontak [master](https://github.com/kuuhaku86). Suemangatttt 🤓

![](https://64.media.tumblr.com/fb2eb1aa1d88b93a8fec36fd81b051cb/fbcc43fc5be59b7e-17/s500x750/b90ad78abd57064acf96ae5bde0ffed0b23ac968.gifv)
