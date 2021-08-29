# Troubleshoot

Tulisan ini didedikasikan kepada praktikan yang mengalami panik akut karena uml nya bermasalah. Diharapkan tidak ada lagi muncul mantra sakti yang sering diucapkan oleh praktikan yaitu `"mas ini kok gabisa ya"`

wise man said - `"lah ini bisa kawan"`

## Mantra Mantra
 *  [Troubleshoot](#Troubleshoot)
     * [Mantra Mantra](#mantra-mantra)
        * [UML Force Close](#uml-force-close)
        * [Tidak Bisa Ping Keluar](#tidak-bisa-ping-keluar)
        * [Gagal Apt-get Update](#gagal-apt-get-update)
        * [Segmentation Fault](#segmentation-fault)
     *  [Mantra Mantra Plus](#mantra-mantra-plus)

### UML Force Close
Pada kasus ini yang terjadi adalah ketika membuka UML langsung force close, jangan bersedih kawan, mari kita kupas tuntas masalah ini.
 
 * Penyebab: Koneksi terputus atau anda menutup UML secara sadis yaitu tidak menggunakan `halt` atau `bye.sh`
 * Solusi: 
    
    1. Jalankan `bash bye.sh` pada terminal terlebih dahulu.
    2. Jika status yang diberikan `ok`, maka jalankan topologi kamu kembali dengan `bash topologi.sh`.
    3. Jika UML masih force close, panggil asisten kesayangan anda.

### Tidak Bisa Ping Keluar 
Pada kasus kali ini yang terjadi adalah tidak bisa ping keluar misal ke its.ac.id dari UML selain router SURABAYA. Haha boekan ini bukan salah wifi kamu tapi ...

* Penyebab: Mungkin anda belum mengetikkan `iptables –t nat –A POSTROUTING –o eth0 –j MASQUERADE –s 192.168.0.0/16` atau belum mengubah `/etc/sysctl.conf` di router.

* Solusi: 
    
    1. Menjalankan `iptables –t nat –A POSTROUTING –o eth0 –j MASQUERADE –s 192.168.0.0/16` pada router **SURABAYA** agar client bisa terhubung dengan internet.
    2. Ubah `/etc/sysctl.conf` seperti pada [Modul Pengenalan UML ](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/tree/modul-uml)

### Gagal Apt-get update
Pada kasus ini yang terjadi adalah tidak bisa apt-get update. Jangan khawatir karena kami bisa mengatasinya, tapi bohong, bercanda kok bro aku buatin kok, *yuk langsung ke pidionya*

* Jenis 1

    * Penyebab: Belum export proxy!!!!
    * Solusi:
        
        1. Menjalankan export proxy pada semua UML menggunakan Akun VPN yang bisa didapatkan di asisten kesayangan anda
            ```
            export http_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
            export https_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
            export ftp_proxy="http://usernameVPN:passVPN@proxy.its.ac.id:8080";
            ``` 
        2. Jika anda sudah memiliki script untuk proxy nya cara agar bisa tereksekusi gunakan command `source` bukan command `bash` kawan, misal `source proxy.sh`

* Jenis 2

    * Muncul tulisan "Problem with MergeList"
    * Solusi:
        
        1. Jalankan `rm -vf /var/lib/apt/lists/*` pada UML yang bersangkutan
        2. Lanjutkan dengan `apt-get update`

* Jenis 3
    
    * Muncul tulisan "w: failed to fetch.." "E: Some index files failed to download.."
    * Solusi:

        1. Coba ketikkan `apt-get update` sekali lagi

* Jenis 4
    
    * Muncul tulisan “the package lists or status file could not be parsed or opened”
    * Solusi:

        1. Jalankan pada UML yang bersangkutan
            ```
            mv /var/lib/dpkg/status /var/lib/dpkg/status.bad
            cp /var/lib/dpkg/status-old /var/lib/dpkg/status
            apt-get update
            ```
* Jenis 5
    
    * apt-get update stuck 0%[connecting to proxy.its.ac.id]
    * Solusi:

        1. Menjalankan `iptables –t nat –A POSTROUTING –o eth0 –j MASQUERADE –s 192.168.0.0/16` pada router.
        2. Ubah `/etc/sysctl.conf` seperti pada [Modul Pengenalan UML ](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/tree/modul-uml)

### Segmentation Fault
Segmentation nya fault

* Penyebab: Penyakit bawaan UML
* Jenis 1
    * Segmentation fault ketika apt-get install atau apt-get update
    * Solusi: Jalankan `rm -r /var/cache 'nama_aplikasi_yang_segfault'`
* Jenis 2
    * Segmentation fault ketika restart aplikasi
    * Solusi: 
        
        1. Jalankan `apt-get purge 'nama_aplikasi_yang_segfault'`
        2. Jalankan `apt-get autoremove`
* Jenis 3 
    * Ketika semua cara diatas tidak berhasil
    * Solusi:

        1. Ketik halt pada UML yang segfault
        2. Hapus UML yang segfault, misalnya yang segfault SURABAYA ketikkan rm SURABAYA
        3. Buka script topologi.sh dan comment script yang tidak butuh dijalankan ulang. Sisakan script untuk menjalankan SURABAYA (dalam kasus ini, SURABAYA yang segfault).
        4. Jalankan ulang script topologi.sh dengan bash topologi.sh 
        5. Konfigurasi ulang UML yang segfault.


### Mantra Mantra Plus
Jika sampai di bagian ini tetapi anda tidak juga menemukan solusi dari masalah yang anda alami, tenang saja kawan, tidak perlu bersedih, tenangkan fikiran anda, rehat sejenak. Kemudian periksa kembali konfigurasi yang sudah anda kerjakan, biasanya masalahnya terjadi karena `typo` iya karena `typo` kawan. Yang seharusnya `jarkom.2020.com.` malah ditulis `jarkom.2020.com` yang seharusnya tulisan "IP MALANG" diganti jadi ip-nya MALANG tapi ini malah ngga diganti, malah copas cuma-cuma jadi hots -t PTR "IP MALANG" :) jika anda pernah mengalami hal di atas tenang saja kawan, kami semua pernah mengalaminya, tidak perlu berkacil hati. Tetap semangat, karena badai pasti berlalu.
