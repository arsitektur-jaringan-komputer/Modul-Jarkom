# Modul Pengenalan GNS3

- [Modul Pengenalan GNS3](#modul-pengenalan-gns3)
  - [Apakah GNS3 itu?](#apakah-gns3-itu)
  - [Instalasi VMWare Workstation](#instalasi-vmware-workstation)
  - [Instalasi GNS3 VM](#instalasi-gns3-vm)
  - [Instalasi GNS3 GUI](#instalasi-gns3-gui)
  - [Instalasi netics-pc appliance](#instalasi-netics-pc-appliance)
  - [Penggunaan GNS3](#penggunaan-gns3)
    - [Setup IP di Node](#setup-ip-di-node)
    - [Akses Sebuah Node ke Internet](#akses-sebuah-node-ke-internet)
    - [Membuat Topologi](#membuat-topologi)

<br>

## Apakah GNS3 itu?

**GNS3 (Graphical Network Simulator-3)** adalah alat yang membantu Anda untuk bisa menjalankan sebuah simulasi dari topologi kecil yang hanya terdiri dari beberapa alat saja di komputer Anda sampai dengan topologi yang memiliki banyak alat yang di-hosting di beberapa server.

<br>

## Instalasi VMWare Workstation
1. Buka situs web https://support.broadcom.com/ lalu daftarkan akun baru (disarankan menggunakan email pribadi).
2. Buka menu **VMWare Cloud Foundation → My Downloads → Free Software Downloads** untuk mengakses daftar software yang tersedia secara gratis.

   ![Registrasi](images/vmware-1.png)

   ![Download](images/vmware-2.png)

3. Pilih menu **VMWare Workstation Pro**, lalu tentukan versi yang akan diinstal. Untuk Windows, disarankan memilih **VMWare Workstation Pro 17.0 for Windows** versi terbaru.

   ![VMware](images/vmware-3.png)

   ![Versi](images/vmware-4.png)

4. Centang box **Terms & Conditions**, lalu lengkapi data screening untuk memulai proses instalasi.

   ![Formulir](images/vmware-5.png)

<br>

## Instalasi GNS3 VM
1. Buka tautan GitHub berikut https://github.com/gns3/gns3-gui/releases?page=2#release-v3.0.6, lalu unduh file **GNS3-3.0.6-all-in-one.exe** dan **GNS3.VM.VMware.Workstation.3.0.6.zip**.

   ![Releases](images/gns3-vm-1.png)

2. Ekstrak file **GNS3.VM.VirtualBox.2.2.61.zip** yang telah diunduh.

3. Buka VMWare Workstation, lalu pilih menu **File → Open** dan pilih file **.ova** dari folder hasil ekstraksi.

   ![Import](images/gns3-vm-2.png)

4. Setelah proses import berhasil, nyalakan virtual machine dan tunggu hingga alamat IP beserta port GNS3 muncul. Catat alamat IP beserta port tersebut, karena keduanya akan digunakan untuk terhubung dengan GNS3 GUI.

   ![IP](images/gns3-vm-3.png)

5. Jika muncul kendala saat menyalakan virtual machine, buka menu **Settings → Processors**, lalu hapus tanda centang pada opsi **Virtualize Intel VT-x/EPT or AMD-V/RVI**.

   ![Processor](images/gns3-vm-4.png)

<br>

## Instalasi GNS3 GUI
1. Jalankan file **.exe** GNS3 yang telah diunduh, lalu ikuti proses instalasi hingga selesai.

2. Buka menu **Edit → Preferences → Server → Remote servers**, lalu isi kolom **Host** dan **Port** dengan alamat IP dan port yang telah diperoleh dari GNS3 VM sebelumnya.

   ![Preferences](images/gns3-gui-1.png)

   ![Host](images/gns3-gui-2.png)

3. Untuk memulai proyek baru, pilih menu **File → New blank project**.

<br>

## Instalasi netics-pc appliance
1. Pilih menu **File → New Template**.

   ![Template](images/netics-pc-appliance-1.png)

2. Pilih opsi **Import an appliance file**, lalu pilih berkas **netics-alpinet.gns3a** yang telah diunduh. Untuk berkas **netics-alpinet.gns3a** bisa anda dapatkan dari [sini](netics-pc-alpinet\netics-alpinet.gns3a)

   ![Appliance](images/netics-pc-appliance-2.png)

3. Pilih opsi **Install appliance on a remote server**.

   ![Remote](images/netics-pc-appliance-3.png)

4. Drag and drop appliance **netics-pc** ke area kosong untuk mencoba.

   ![Netics](images/netics-pc-appliance-4.png)

<br>

## Penggunaan GNS3

### Setup IP di Node
1. Klik kanan pada node, buka `Configure`
2. Pada menu `General settings`, cari tombol `Edit network configuration`
3. Di situ kalian bisa setup IP sesuai dengan interface yang digunakan. Interface adalah sesuatu yang digunakan untuk menghubungkan dua device

### Akses Sebuah Node ke Internet

1. Tarik NAT ke area kosong
2. Hubungkan NAT ke netics-pc dengan link

   ![NAT](images/using-internet-1.png)

3. Klik menu **Show/Hide interface labels** untuk menampilkan informasi interface node

   ![Interface](images/using-internet-2.png)

4. Lalu klik node, pilih interface `eth0`, dan klik node NAT yang ditarik tadi

   ![Koneksi](images/using-internet-3.png)

5. Lalu konfigurasi IP dari node netics-pc

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

   ![Ping](images/using-internet-4.png)

8. Node ini akan nanti digunakan sebagai router untuk modul ini, ganti nama node ini menjadi `Foosha` dengan fitur `Change hostname` di node, dan juga ganti symbol ke simbol router dengan fitur `Change symbol`

<br>

### Membuat Topologi

1. Tambahkan beberapa node ethernet switch dan ubuntu, lalu buat hubungan antar node dan nama-nama dari node hingga seperti di gambar

   ![Topologi](images/create-topology-1.png)

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
5. Cek semua node ubuntu apakah sudah memiliki ip yang sesuai dengan settingan dengan command `ip a`. Berikut adalah contoh untuk node `Foosha` dengan Prefix IP `10.105`, sesuaikan dengan Prefix IP kelompok kalian masing-masing

   ![Foosha](images/create-topology-2.png)

6. Topologi yang dibuat sudah bisa berjalan secara lokal, tetapi kita belum bisa mengakses jaringan keluar. Maka kita perlu melakukan beberapa hal.
- Install tool iptables
  ```
  apk update
  apk add iptables
  ```
- Ketikkan **`iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s [Prefix IP].0.0/16`** pada router `Foosha`
  **Keterangan:**
  - **iptables:** iptables merupakan suatu tools dalam sistem operasi Linux yang berfungsi sebagai filter terhadap lalu lintas data. Dengan iptables inilah kita akan mengatur semua lalu lintas dalam komputer, baik yang masuk, keluar, maupun yang sekadar melewati komputer kita. Untuk penjelasan lebih lanjut nanti akan dibahas pada Modul 5.
  - **NAT (Network Address Translation):** Suatu metode penafsiran alamat jaringan yang digunakan untuk menghubungkan lebih dari satu komputer ke jaringan internet dengan menggunakan satu alamat IP.
  - **Masquerade:** Digunakan untuk menyamarkan paket, misal mengganti alamat pengirim dengan alamat router.
  - **-s (Source Address):** Spesifikasi pada source. Address bisa berupa nama jaringan, nama host, atau alamat IP.
- Ketikkan command `cat /etc/resolv.conf` di `Foosha`

  ![Resolv](images/create-topology-3.png)

- Ingat-ingat IP tersebut karena IP tersebut merupakan IP DNS, lalu ketikkan command ini di node ubuntu yang lain `echo nameserver [IP DNS] > /etc/resolv.conf`. Jika pada kasus contoh maka command-nya adalah `echo nameserver 192.168.153.2 > /etc/resolv.conf`.
- Berikut merupakan contoh saat melakukan ping sebelum dan sesudah menambahkan nameserver pada node Water7

  ![Nameserver](images/create-topology-4.png)

- Semua node sekarang seharusnya sudah bisa melakukan ping ke google, yang artinya adalah sudah tersambung ke internet

<br>

## Ketentuan

- Praktikan **hanya** diperbolehkan menggunakan appliances **netics-alpinet.gns3a**

<br>

## Peringatan, Saran, Tips, dan Trik

- Apa yang diinstal di node **tidak persisten**, artinya saat Anda mengerjakan project tersebut lagi Anda perlu menginstal aplikasi itu kembali
- Maka **selalu** simpan config di node ke directory `/root` sebelum keluar dari project
- Anda bisa memasukkan command yang ingin selalu dijalankan di node tersebut ke file `/root/.bashrc` di bagian paling bawah. (Contoh : command iptables dan echo nameserver tadi)

  ![Bashrc](images/tips-trick-1.png)

- selain `/root/.bashrc`, anda dapat menambahkan startup script dengan meletakkan command pada `network config` dengan didahului kata `up` seperti contoh berikut:

  ![Network](images/tips-trick-2.png)

- Anda bisa melakukan ekspor project jika bekerja secara tim dengan pergi ke menu `File` -> `Export portable project`
- Jika mengerjakan menggunakan VM di local kalian sendiri. Kalian bisa mencegah hilangnya aplikasi atau file config dengan mematikan VM di mode save state.
- Manfaatkan bash scripting untuk install-install aplikasi yang diperlukan sehingga tidak perlu memasukkan command satu-satu, lalu save ke `/root`.
- Tidak disarankan untuk menggunakan gns3 pada WSL ataupun windows(GUI) _*jika-ada-masalah-selesaikan-sendiri*_
- Ada sesuatu yang biasanya bisa tetapi tiba-tiba tidak bisa? Coba matikan dulu VM nya baru nyalakan kembali. Masih tidak bisa? Coba cara install GNS3 yang lain dahulu sebelum bertanya ke asisten.
- Tidak bisa install di satu metode? Coba cara install yang lain dulu sebelum bertanya ke asisten.

## Sumber

- https://docs.gns3.com/docs/