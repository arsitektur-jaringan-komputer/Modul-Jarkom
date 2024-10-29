# Terraform

## A. Pengenalan

### 1. Infrastructure as Code (IaC)

![Gambar](../assets/rumah.png)

Bayangkan kamu harus membangun sebuah rumah dengan spesifikasi khusus. Untuk satu rumah, mungkin cukup mudah memberi tahu tukang tentang detailnya, dan mereka bisa membangunnya sesuai keinginanmu. Tapi, bayangkan jika kamu melamar seorang wanita, dan dia meminta dibuatkan 1000 rumah dalam semalam. Tentu sangat sulit jika kamu harus menjelaskan spesifikasi rumah yang sama ke setiap tukang satu per satu!

Karena kamu orang yang cerdas, akhirnya kamu membuat rencana dan instruksi pembangunan rumah tersebut dalam satu dokumen yang detail. Dengan begitu, cukup memberikan instruksi ini kepada setiap tukang, dan mereka bisa membangun rumah dengan spesifikasi yang sama persis, tanpa harus bertanya lagi.

Nah, begitulah cara kerja *Infrastructure as Code* (IaC). Di sini, kamu menuliskan rencana dan instruksi pembuatan infrastruktur dalam bentuk kode. Kode ini bisa dijalankan kapan saja untuk membangun infrastruktur sesuai spesifikasi yang sudah ditulis.

#### Manfaat dari IaC
- <b> Efisien dan otomatis</b>

    Kamu tinggal pakai petunjuk yang sudah ada tanpa harus jelaskan ulang dari awal. Mau bangun 1 rumah atau 100 rumah, petunjuknya tinggal dipakai saja!

- <b> Konsistensi </b>

    Semua rumah yang dibangun dari petunjuk ini akan seragam. Tidak ada yang lebih tinggi, atau kurang jendela, karena semuanya mengikuti instruksi yang sama.

- <b> Mudah dikelola </b>

    Kalau mau ubah sedikit desain rumah, kamu tinggal edit petunjuknya saja. Hal ini juga dapat diimplementasikan pada code dalam memmbentuk infrastruktur.

#### Contoh Implementasi IaC Dalam Kasus Nyata


Saat hari belanja besar seperti 11.11, biasanya pengunjung situs e-commerce meningkat pesat. Dengan IaC, tim infrastruktur bisa menyiapkan autoscaling untuk menambah server atau kapasitas saat pengunjung melonjak. Setelah selesai, mereka cukup menonaktifkan server tambahan melalui kode, menghemat biaya karena kapasitas tambahan hanya aktif saat diperlukan.

#### Contoh Tools IaC
- <b> Terraform </b>

    Terraform merupakan alat yang digunakan untuk membuat dan mengelola infrastruktur IT secara otomatis dengan menggunakan kode.

    <b> Contoh penggunaan: </b>
    
    Jika kamu ingin menyiapkan 10 server dan database di cloud, kamu cukup menuliskan konfigurasi di Terraform, dan dengan satu perintah, akan dibuat secara otomatis sesuai dengan spesifikasi yang ditentukan.

<br>

- <b> Ansible </b>
    
    Ansible merupakan alat otomatisasi yang fokus pada pengaturan dan manajemen konfigurasi sistem.


    <b> Contoh penggunaan: </b>

    Jika kamu memiliki beberapa server dan ingin menginstal perangkat lunak atau mengatur konfigurasi tertentu, Ansible bisa melakukan semuanya sekaligus, tanpa perlu melakukan instalasi satu per satu.

<br>

### 2. Terraform

#### Pengertian
Terraform merupakan alat untuk melakukan otomatisasi dalam pembuatan, pengaturan, dan penghapusan infrastruktur IT. Terraform membantu dalam penulisan konfigurasi (atau dalam analogi sebelumnya adalah "rencana pembangunan") yang dapat digunakan kembali dan diatur dengan mudah.


#### Penggunaan dan Manfaat
a. Penggunaan
- Membuat server, jaringan, dan layanan cloud hanya dengan satu konfigurasi dan perintah
- Menerapkan infrastruktur yang sama di beberapa _environment_ (seperti produksi, pengujian, atau pengembangan).
- Menyesuaikan atau mengubah infrastruktur dengan cepat hanya dengan memperbarui konfigurasi.

b. Manfaat
- <b> Efisiensi</b>, hal ini didapat dalam mudahnya melakukan otomasisasi dan pengelolaan infrastruktur menggunakan konfigurasi Terraform.
- <b> Konsistensi</b>, dikarenakan diatur dengan menggunakan satu konfigurasi, maka banyak node akan konsisten dengan pengaturan satu konfigurasi.
- <b> Skalabilitas</b>, dengan menggunakan satu konfigurasi Terraform, kalian dapat membuat/mengelola banyak infrastruktur dengan mudah.