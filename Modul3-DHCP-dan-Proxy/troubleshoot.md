# Troubleshoot
Silahkan baca terlebih dahulu sebelum kamu mengalami serangan panik akut hehehehe

#### 1. Ketika membuka UML langsung force close
* Penyebab: Koneksi terputus atau kelompok kamu tidak menutup UML dengan benar (`halt` atau `bye bash.sh`).
* Solusi:
    1. Jalankan `bash bye.sh` pada terminal terlebih dahulu.
    2. Jika status yang diberikan `OK`, maka jalankan topologi kamu kembali dengan `bash topologi.sh`.
    3. Jika UML masih force close, panggil asisten kesayangan kamu.
  
#### 2. Tidak bisa ping keluar (misal its.ac.id) dari UML selain router BAKSO
* Penyebab: Mungkin kamu belum mengetikkan `iptables –t nat –A POSTROUTING –o eth0 –j MASQUERADE –s 192.168.0.0/16` atau belum mengubah `/etc/sysctl.conf` di router.
* Solusi:
    1. Menjalankan `iptables –t nat –A POSTROUTING –o eth0 –j MASQUERADE –s 192.168.0.0/16` pada router **BAKSO** agar client bisa terhubung dengan internet.
    2. Ubah `/etc/sysctl.conf` seperti [Modul Pengenalan UML](https://github.com/rohanaq/Modul-Pengenalan-UML).

#### 3. Apt-get update gagal
* **Jenis 1**
  * Penyebab: Belum export proxy!
  * Solusi:
      1. Menjalankan **export proxy** pada **semua UML** menggunakan Akun VPN yang bisa didapatkan di [https://id.its.ac.id/otp/](https://id.its.ac.id/otp/).
          ```bash
          export http_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
          export https_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
          export ftp_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
          ```
          Export proxy dilakukan supaya kamu bisa melewati proxy ITS dan bisa menginstal sesuatu.

* **Jenis 2**
  * Muncul tulisan “Problem with MergeList”
  * Solusi: 
    1. Jalankan `rm -vf /var/lib/apt/lists/*` pada UML yang bersangkutan
    2. Lanjutkan dengan `apt-get update`

* **Jenis 3**
  ![Masalah 1](img/trouble-1.png)
  * Solusi: 
    1. Coba ketikkan `apt-get update` sekali lagi

* **Jenis 4**
  * Muncul tulisan “the package lists or status file could not be parsed or opened”
  * Solusi:
    1. Jalankan
        ```bash
        mv /var/lib/dpkg/status /var/lib/dpkg/status.bad
        cp /var/lib/dpkg/status-old /var/lib/dpkg/status
        apt-get update
        ```

* **Jenis 5**
  ![Masalah 2](img/trouble-2.png)
  * Solusi:
    1. Menjalankan `iptables –t nat –A POSTROUTING –o eth0 –j MASQUERADE –s 192.168.0.0/16` pada router.
    2. Ubah `/etc/sysctl.conf` seperti [Modul Pengenalan UML](https://github.com/rohanaq/Modul-Pengenalan-UML).

#### 4. Segmentation fault
* Penyebab: Mistis
* **Jenis 1**
  * Segmentation fault ketika `apt-get install` atau `apt-get update`
  * Solusi:
    1. Jalankan `rm -r /var/cache/'nama_aplikasi_yang_segfault'`
* **Jenis 2**
  * Segmentation fault ketika restart aplikasi
  * Solusi:
    1. Jalankan `apt-get purge 'nama_aplikasi_yang_segfault'`
    2. Jalankan `apt-get autoremove`
* **Jenis 3**
  * Ketika semua cara diatas tidak berhasil
  * Solusi:
    1. Ketik `halt` pada UML yang segfault
    2. Hapus UML yang segfault, misalnya yang segfault **BAKSO** ketikkan `rm BAKSO`
    3. Buka script `topologi.sh` dan comment script yang tidak butuh dijalankan ulang. Sisakan script untuk menjalankan **BAKSO** (dalam kasus ini, BAKSO yang segfault).
    4. Jalankan ulang script `topologi.sh` dengan `bash topologi.sh`
    5. Konfigurasi ulang UML yang segfault.

**SARAN:** 
Selalu back-up semua konfigurasi kamu pada setiap UML. Sehingga, jika sewaktu-waktu UML ada yang segfault, maka kamu tinggal copy-paste konfigurasi.