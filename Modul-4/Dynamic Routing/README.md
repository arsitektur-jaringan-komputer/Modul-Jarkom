# DYNAMIC ROUTING

- [A. Pengenalan](#a-pengenalan)
  - [Definisi](#definisi)
  - [Tujuan](#tujuan)
- [B. Pembagian](#b-pembagian)
  - [Algoritma](#algoritma)
    - [1. Link State](#1-link-state)
    - [2. Distance Vector](#2-distance-vector)
  - [Batasan](#batasan)
    - [1. IGP](#1-igp)
    - [2. EGP](#2-egp)
- [C. Protokol](#c-protokol)
  - [RIP](#rip)
    - [Route Poisoning](#route-poisoning)
    - [Poison Reverse](#poison-reverse)
    - [Split Horizon](#split-horizon)
  - [OSPF](#ospf)
    - [???]
- [D. Implementasi](#d-implementasi)

## A. Pengenalan

### Definisi

Pada modul sebelumnya, kita sudah membahas mengenai routing, cara kerja, serta fungsinya. Tak hanya itu, kita juga telah membahas salah satu jenis routing berdasarkan cara _Router_ mendapatkan informasi terkait _Routing Table_-nya, yaitu Static Routing. Di modul ini, kita akan membahas sekilas mengenai jenis yang kedua, yaitu **Dynamic Routing**.

Pada Dynamic Routing, _Router_ akan mendapatkan informasi mengenai jaringan dari komunikasi dengan _Router_ lainnya. Hal ini tentu akan memudahkan _network administrator_ dalam melakukan konfigurasi _routing_ pada jaringan yang besar. Selain itu, sifatnya yang adaptif membuat perubahan topologi dalam jaringan bukan lagi suatu masalah yang besar, karena _Router_ akan menyesuaikan dan membuat jalur komunikasi yang baru (bila ada). Namun berbeda dengan Static Routing, pada Dynamic Routing terdapat protokol-protokol berbeda yang menentukan cara komunikasi antar-_Router_ dengan kelebihan dan kekurangannya masing-masing. Pada modul ini, kita hanya akan menyinggung 2 protokol yang sering digunakan, yaitu **RIP** dan **OSPF**.

### Tujuan

Jika dibandingkan dengan Static Routing, penggunaan Dynamic Routing lebih tepat diterapkan pada jaringan berskala besar karena memiliki beberapa keunggulan berikut:

1. Router hanya perlu mengetahui dan mengenalkan jaringan yang terhubung langsung dengannya.
2. Tidak perlu mengonfigurasi atau mengetahui seluruh jaringan yang ada secara manual.
3. Ketika terdapat penambahan atau perubahan jaringan, hanya router yang terkait langsung yang akan memperbarui tabel routing-nya secara otomatis. Sehingga, tidak perlu ada konfigurasi ulang di seluruh jaringan.

## B. Pembagian
