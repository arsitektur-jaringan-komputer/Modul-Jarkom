Modul Pengenalan GNS3
===============

- [Modul Pengenalan GNS3](#modul-pengenalan-gns3)
  - [Apakah GNS3 itu?](#apakah-gns3-itu)
  - [Instalasi GNS3](#instalasi-gns3)
    - [Import Image di VirtualBox](#import-image-di-virtualbox)
    - [Import Image di VMWare](#import-image-di-vmware)
    - [Memasukkan Image Ubuntu ke GNS3](#memasukkan-image-ubuntu-ke-gns3)
  - [Penggunaan GNS3](#penggunaan-gns3)
    - [Setup IP](#setup-ip)
      - [Pembagian Prefix IP](#pembagian-prefix-ip)
      - [Setup IP di Node](#setup-ip-di-node)
    - [Akses Sebuah Node ke Internet](#akses-sebuah-node-ke-internet)
    - [Membuat Topologi](#membuat-topologi)
  - [Ketentuan](#ketentuan)
  - [Peringatan, Saran, Tips, dan Trik](#peringatan-saran-tips-dan-trik)
  - [Troubleshooting](#troubleshooting)
  - [Sumber](#sumber)

## Apakah GNS3 itu?
**GNS3 (Graphical Network Simulator-3)** adalah alat yang membantu Anda untuk bisa menjalankan sebuah simulasi dari topologi kecil yang hanya terdiri dari beberapa alat saja di komputer Anda sampai dengan topologi yang memiliki banyak alat yang di-hosting di beberapa server.

## Instalasi GNS3
### Import Image di VirtualBox
1. Install VirtualBox
Silahkan mendownload dari link berikut [VirtualBox 7.0](https://www.oracle.com/virtualization/technologies/vm/downloads/virtualbox-downloads.html).

2. Download Image VM GNS3
Silahkan mendowload dari link berikut [GNS3 VM 2.2.42](https://github.com/GNS3/gns3-gui/releases/download/v2.2.42/GNS3.VM.VirtualBox.2.2.42.zip). Sehabis itu langsung saja extract.

3. Import file .ova ke VirtualBox

![import-ova](images/import-ova.jpg)

![import-ova-2](images/import-ova-2.jpg)

4.  Membuat host network adapter baru
  - Pilih File Menu -> Host Network Manager <br/>
![new-host-network-adapter](images/new-host-network-adapter-1.jpg)
  - Klik Create <br/>
![new-host-network-adapter-2](images/new-host-network-adapter-2.jpg)
  - Lalu setting agar IPv4 Address adalah `192.168.0.1`, dan IPv4 Network Mask `255.255.255.0` lalu klik apply
![new-host-network-adapter-4](images/new-host-network-adapter-4.jpg)
![new-host-network-adapter-5](images/new-host-network-adapter-5.jpg)

5. Ubah Network Adapter di VM
  - Pergi ke Settings -> Network
  - Ubah Adapter 1 ke Host-only Adapter dan sesuaikan dengan host network yang telah dibuat sebelumnya
![setting-network-vm-1](images/setting-network-vm-3.jpg)
  - Dan ubah Adapter 2 menjadi NAT <br/>
![setting-network-vm-3](images/setting-network-vm-2.jpg)
  - Lalu klik OK

6.  Jalankan VM
  - Maka VM seharusnya bisa menampilkan ini
![vm](images/new-vm-1.png)
  - Lalu buka alamat dengan keterangan "To launch the Web-UI" di browser
![vm-2](images/vm-2.jpg)

Setelah itu silahkan lanjutkan untuk mengimpor image Ubuntu ke GNS3 [disini](#memasukkan-image-ubuntu-ke-gns3)


### Import Image di VMWare
1. Install VMWare
Silahkan mendownload dari [VMware Workstation 17](https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html).

2. Download Image VM GNS3
Silahkan mendowload dari [GNS3 VM 2.2.42](https://github.com/GNS3/gns3-gui/releases/download/v2.2.42/GNS3.VM.VMware.Workstation.2.2.42.zip). Sehabis itu langsung saja extract.

3. Import file .ova ke VMWare dan namai VM.

![import-ova](images/insert-image-vmware-1.png)

![import-ova-2](images/insert-image-vmware-2.png)

![import-ova-3](images/insert-image-vmware-3.png)

4. Sesuaikan settingan VMWare dengan klik `Edit virtual machine settings`.
- Pastikan settingan Network sudah sesuai.

![settingan-vmware-1](images/settingan-vmware-1.png)

- Jika ada error `Virtualized ... Not Supported on Platform` saat vm nanti dijalankan, coba disable virtualisasi di settingan processor

![settingan-vmware-2](images/settingan-vmware-2.png)

5.  Jalankan VM
  - Maka VM seharusnya bisa menampilkan ini
![vm](images/new-vm-2.png)
  - Lalu buka alamat dengan keterangan "To launch the Web-UI" di browser
![vm-2](images/new-vm-vmware-2.png)

Setelah itu silahkan lanjutkan untuk mengimpor image Ubuntu ke GNS3 [disini](#memasukkan-image-ubuntu-ke-gns3)

### Memasukkan Image Ubuntu ke GNS3

1. Import image ubuntu
  - Klik `Go to preferences`
  - Klik `Docker`
  - Klik `Add Docker container template`
  - `Server type` pilih `Run this Docker container locally`
  - Klik `Docker Virtual Machine`, pilih `New image` isikan `danielcristh0/ubuntu-bionic:1.1` di Image name<br>
  ![insert-image-1](images/insert-imaget-2.jpg)
  - Klik `Container name` masukkan `ubuntu-1` sebagai nama container
  - Klik `Network adapters` dan masukkan angka 4
  - Kosongi bagian `Start command`.
  - Lalu klik tombol `Add template` di bawah sendiri

2. Coba image yang telah di-import
  - Klik `Servers` di kiri atas
  - Klik `local`
  - Klik `Add blank project`
  - Masukkan nama project (terserah)
  - Klik `Add project`
  - Klik tombol `Add a node` di samping kiri <br/>
![test-image-1](images/test-image-1.jpg)
  - Lalu tarik `ubuntu-1` ke area kosong di halaman
  - Tunggu sampai loading selesai
  - Jika berhasil akan menampilkan tampilan yang mirip dengan ini
![test-image-2](images/test-image-2.jpg)
  - Kita bisa start dengan klik kanan di node dan klik `Start` <br/>
![test-image-3](images/test-image-3.jpg)

3. Akses node
  - Bisa dilakukan dengan `Web console`  <br/>
![akses-node-1](images/akses-node-1.jpg)
  - Bisa dilakukan menggunakan command `telnet [IP VM] [Port node]` di terminal lokal pc kita, jika menggunakan contoh di gambar, maka commandnya adalah `telnet 192.168.0.16 5000`
![akses-node-2](images/akses-node-2.jpg)
  - Jika menggunakan telnet, hati-hati jika ingin keluar dari node. Gunakan `Ctrl + ]` lalu ketik quit untuk keluar dari node.
  - Jika command prompt tidak kunjung keluar, bisa klik enter berkali-kali sampai keluar

## Penggunaan GNS3

### Setup IP
Dalam praktikum jaringan komputer, Anda akan sering melakukan setting untuk IP dari node yang digunakan. Lalu untuk membedakan ip jaringan dari masing-masing kelompok, maka 2 oktet awal (Prefix IP) dari IP yang digunakan sudah ditentukan seperti di bawah.

#### Pembagian Prefix IP

**Kelas A**

| Kelompok | Prefix IP |
|----------|-----------|
| A01      | 192.169   |
| A02      | 10.0      |
| A03      | 192.170   |
| A04      | 10.1      |
| A05      | 192.171   |
| A06      | 10.2      |
| A07      | 192.172   |
| A08      | 10.3      |
| A09      | 192.173   |
| A10      | 10.4      |
| A11      | 192.174   |
| A12      | 10.5      |
| A13      | 192.175   |
| A14      | 10.6      |
| A15      | 192.176   |
| A16      | 10.7      |
| A17      | 192.177   |
| A18      | 10.8      |
| A19      | 192.178   |

**Kelas B**

| Kelompok | Prefix IP |
|----------|-----------|
| B01      | 10.9      |
| B02      | 192.179   |
| B03      | 10.10     |
| B04      | 192.180   |
| B05      | 10.11     |
| B06      | 192.181   |
| B07      | 10.12     |
| B08      | 192.182   |
| B09      | 10.13     |
| B10      | 192.183   |
| B11      | 10.14     |
| B12      | 192.184   |
| B13      | 10.15     |
| B14      | 192.185   |
| B15      | 10.16     |
| B16      | 192.186   |
| B17      | 10.17     |
| B18      | 192.187   |
| B19      | 10.18     |
| B20      | 192.188   |
| B21      | 10.19     |
| B22      | 192.189   |
| B23      | 10.20     |
| B24      | 192.190   |
| B25      | 10.21     |
| B26      | 192.191   |

**Kelas D**

| Kelompok | Prefix IP |
|----------|-----------|
| D01      | 10.22     |
| D02      | 192.192   |
| D03      | 10.23     |
| D04      | 192.193   |
| D05      | 10.24     |
| D06      | 192.194   |
| D07      | 10.25     |
| D08      | 192.195   |
| D09      | 10.26     |
| D10      | 192.196   |
| D11      | 10.27     |
| D12      | 192.197   |
| D13      | 10.28     |
| D14      | 192.198   |
| D15      | 10.29     |
| D16      | 192.199   |
| D17      | 10.30     |
| D18      | 192.200   |
| D19      | 10.31     |
| D20      | 192.201   |
| D21      | 10.32     |
| D22      | 192.202   |
| D23      | 10.33     |
| D24      | 192.203   |
| D25      | 10.34     |
| D26      | 192.204   |
| D27      | 10.35     |
| D28      | 192.205   |
| D29      | 10.36     |
| D30      | 192.206   |


**Kelas E**

| Kelompok | Prefix IP |
|----------|-----------|
| E01      | 10.37     |
| E02      | 192.207   |
| E03      | 10.38     |
| E04      | 192.208   |
| E05      | 10.39     |
| E06      | 192.209   |
| E07      | 10.40     |
| E08      | 192.210   |
| E09      | 10.41     |
| E10      | 192.211   |
| E11      | 10.42     |
| E12      | 192.212   |
| E13      | 10.43     |
| E14      | 192.213   |
| E15      | 10.44     |
| E16      | 192.214   |
| E17      | 10.45     |
| E18      | 192.215   |
| E19      | 10.46     |
| E20      | 192.216   |
| E21      | 10.47     |
| E22      | 192.217   |
| E23      | 10.48     |
| E24      | 192.218   |
| E25      | 10.49     |
| E26      | 192.219   |
| E27      | 10.50     |
| E28      | 192.220   |
| E29      | 10.51     |
| E30      | 192.221   |

**Kelas F**

| Kelompok | Prefix IP |
|----------|-----------|
| F01      | 10.52     |
| F02      | 192.222   |
| F03      | 10.53     |
| F04      | 192.223   |
| F05      | 10.54     |
| F06      | 192.224   |
| F07      | 10.55     |
| F08      | 192.225   |
| F09      | 10.56     |
| F10      | 192.226   |
| F11      | 10.57     |
| F12      | 192.227   |
| F13      | 10.58     |
| F14      | 192.228   |

**Kelas IUP**

| Kelompok | Prefix IP |
|----------|-----------|
| I01      | 10.59     |
| I02      | 192.229   |
| I03      | 10.60     |
| I04      | 192.230   |
| I05      | 10.61     |
| I06      | 192.231   |
| I07      | 10.62     |
| I08      | 192.232   |
| I09      | 10.63     |
| I10      | 192.233   |

**IT**

| Kelompok | Prefix IP |
|----------|-----------|
| IT01     | 10.64     |
| IT02     | 192.234   |
| IT03     | 10.65     |
| IT04     | 192.235   |
| IT05     | 10.66     |
| IT06     | 192.236   |
| IT07     | 10.67     |
| IT08     | 192.237   |
| IT09     | 10.68     |
| IT10     | 192.238   |
| IT11     | 10.69     |
| IT12     | 192.239   |
| IT13     | 10.70     |
| IT14     | 192.240   |
| IT15     | 10.71     |
| IT16     | 192.241   |
| IT17     | 10.72     |
| IT18     | 192.242   |
| IT19     | 10.73     |
| IT20     | 192.243   |
| IT21     | 10.74     |
| IT22     | 192.244   |
| IT23     | 10.75     |
| IT24     | 192.245   |
| IT25     | 10.76     |
| IT26     | 192.246   |
| IT27     | 10.77     |
| IT28     | 192.247   |
| IT29     | 10.78     |
| IT30     | 192.248   |


Jika ada perintah menggunakan IP `[Prefix IP].1.2` maka contoh jika saya adalah kelompok A2 IP adalah `10.0.1.2`

#### Setup IP di Node

1. Klik kanan pada node, buka `Configure`
2. Pada menu `General settings`, cari tombol `Edit network configuration`
3. Di situ kalian bisa setup IP sesuai dengan interface yang digunakan. Interface adalah sesuatu yang digunakan untuk menghubungkan dua device

### Akses Sebuah Node ke Internet
1. Buka menu Add a Node
2. Tarik NAT ke area kosong <br/>
![using-internet-1](images/using-internet-1.jpg)
3. Gunakan aktifkan menu `Add a Link` <br/>
![using-internet-2](images/using-internet-2.jpg)
4. Lalu klik node, pilih interface `eth0`, dan klik node NAT yang ditarik tadi <br/>
![using-internet-3](images/using-internet-3.jpg)
5. Lalu konfigurasi IP dari node ubuntu
  - Cari 2 line yang seperti ini
  ```
  # auto eth0
  # iface eth0 inet dhcp
  ```
  - Uncomment kedua line tersebut, lalu save
  ```
  auto eth0
  iface eth0 inet dhcp
  ```
6. Start node
7. Akses console dari node, dan coba ping ke google, jika berhasil maka settingan Anda benar
![using-internet-4](images/using-internet-4.jpg)
8. Node ini akan nanti digunakan sebagai router untuk modul ini, ganti nama node ini menjadi `Foosha` dengan fitur `Change hostname` di node, dan juga ganti symbol ke simbol router dengan fitur `Change symbol`

### Membuat Topologi
1. Tambahkan beberapa node ethernet switch dan ubuntu, lalu buat hubungan antar node dan nama-nama dari node hingga seperti di gambar <br/>
![create-topology-1](images/create-topology-1.jpg)
2. Gunakan fitur `Change hostname` untuk merubah nama-nama dari node
3. Lalu kita setting network masing-masing node dengan fitur `Edit network configuration` seperti yang ditunjukkan [disini](#setup-ip-di-node) sebelumnya, kita bisa menghapus semua settingnya dan mengisi dengan settingan di bawah
  - Foosha
  ```
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
  ```
  auto eth0
  iface eth0 inet static
  	address [Prefix IP].1.2
  	netmask 255.255.255.0
  	gateway [Prefix IP].1.1
  ```
  - Alabasta
  ```
  auto eth0
  iface eth0 inet static
  	address [Prefix IP].1.3
  	netmask 255.255.255.0
  	gateway [Prefix IP].1.1
  ```
  - EniesLobby
  ```
  auto eth0
  iface eth0 inet static
  	address [Prefix IP].2.2
  	netmask 255.255.255.0
  	gateway [Prefix IP].2.1
  ```
  - Water7
  ```
  auto eth0
  iface eth0 inet static
  	address [Prefix IP].2.3
  	netmask 255.255.255.0
  	gateway [Prefix IP].2.1
  ```
**Penjelasan Pengertian**
- **Gateway**: Jalur pada jaringan yang harus dilewati paket-paket data untuk dapat masuk ke jaringan yang lain.

4. Restart semua node
5. Cek semua node ubuntu apakah sudah memiliki ip yang sesuai dengan settingan dengan command `ip a`. Berikut adalah contoh untuk node `Foosha` dengan Prefix IP `10.40`, sesuaikan dengan Prefix IP kelompok kalian masing-masing
![create-topology-2](images/create-topology-2.jpg)
6. Topologi yang dibuat sudah bisa berjalan secara lokal, tetapi kita belum bisa mengakses jaringan keluar. Maka kita perlu melakukan beberapa hal.
- Ketikkan **`iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s [Prefix IP].0.0/16`** pada router `Foosha`
**Keterangan:**
  - **iptables:** iptables merupakan suatu tools dalam sistem operasi Linux yang berfungsi sebagai filter terhadap lalu lintas data. Dengan iptables inilah kita akan mengatur semua lalu lintas dalam komputer, baik yang masuk, keluar, maupun yang sekadar melewati komputer kita. Untuk penjelasan lebih lanjut nanti akan dibahas pada Modul 5.
  - **NAT (Network Address Translation):** Suatu metode penafsiran alamat jaringan yang digunakan untuk menghubungkan lebih dari satu komputer ke jaringan internet dengan menggunakan satu alamat IP.
  - **Masquerade:** Digunakan untuk menyamarkan paket, misal mengganti alamat pengirim dengan alamat router.
  - **-s (Source Address):** Spesifikasi pada source. Address bisa berupa nama jaringan, nama host, atau alamat IP.
- Ketikkan command `cat /etc/resolv.conf` di `Foosha` <br/>
![create-topology-3](images/create-topology-3.jpg)
- Ingat-ingat IP tersebut karena IP tersebut merupakan IP DNS, lalu ketikkan command ini di node ubuntu yang lain `echo nameserver [IP DNS] > /etc/resolv.conf`. Jika pada kasus contoh maka command-nya adalah `echo nameserver 192.168.122.1 > /etc/resolv.conf`.
- Semua node sekarang seharusnya sudah bisa melakukan ping ke google, yang artinya adalah sudah tersambung ke internet

## Ketentuan
- Praktikan **hanya** diperbolehkan menggunakan image docker `kuuhaku86/gns3-ubuntu`

## Peringatan, Saran, Tips, dan Trik
- Apa yang diinstal di node **tidak persisten**, artinya saat Anda mengerjakan project tersebut lagi Anda perlu menginstal aplikasi itu kembali
- Maka **selalu** simpan config di node ke directory `/root` sebelum keluar dari project
- Anda bisa memasukkan command yang ingin selalu dijalankan di node tersebut ke file `/root/.bashrc` di bagian paling bawah. (Contoh : command iptables dan echo nameserver tadi)</br>
![tips-trik-1](images/tips-trik-1.jpg)
- Anda bisa melakukan ekspor project jika bekerja secara tim dengan pergi ke menu `Project settings` -> `Export portable project`.</br>
![tips-trik-2](images/tips-trik-2.jpg)
- Jika mengerjakan menggunakan VM di local kalian sendiri. Kalian bisa mencegah hilangnya aplikasi atau file config dengan mematikan VM di mode save state.
- Manfaatkan bash scripting untuk install-install aplikasi yang diperlukan sehingga tidak perlu memasukkan command satu-satu, lalu save ke `/root`.
## Troubleshooting
- Ada sesuatu yang biasanya bisa tetapi tiba-tiba tidak bisa? Coba matikan dulu VM nya baru nyalakan kembali. Masih tidak bisa? Coba cara instal GNS3 yang lain dahulu sebelum bertanya ke asisten.
- Tidak bisa instal di satu metode? Coba cara instal yang lain dulu sebelum bertanya ke asisten.


## Sumber
- https://docs.gns3.com/docs/
