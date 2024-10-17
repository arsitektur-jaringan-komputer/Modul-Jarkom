# 3. APACHE JMETER

Pada submodul ini kita akan belajar bagaimana cara menggunakan Apache JMeter sebagai tools benchmarking. Apache JMeter adalah alat open-source untuk menguji kinerja dan beban dari berbagai jenis aplikasi, terutama aplikasi web. JMeter dapat dijalankan baik melalui antarmuka grafis (GUI) maupun melalui command-line interface (CLI). CLI sangat bermanfaat untuk pengujian otomatisasi dan lingkungan server.

## Benchmarking

Benchmarking adalah metode evaluasi untuk menguji kemampuan sebuah aplikasi, instance, atau service dalam memproses request yang diberikan. Jenis testing dalam benchmarking memilii beberapa jenis, seperti load testing, spike testing, dan stress testing.

![image](https://github.com/user-attachments/assets/ddc68a4c-9f24-41ae-9efa-1ebae5266969)


Berikut adalah perbedaan dari masing masing jenis testing:

| Jenis Pengujian    | Tujuan                                    | Karakteristik Beban               | Contoh Skenario                          |
|--------------------|-------------------------------------------|-----------------------------------|-------------------------------------------|
| **Load Testing**    | Memvalidasi kinerja sistem di bawah beban yang diharapkan | Peningkatan bertahap hingga beban yang diharapkan | Mensimulasikan 1000 pengguna di situs e-commerce |
| **Spike Testing**   | Menguji perilaku sistem di bawah lonjakan tiba-tiba | Lonjakan mendadak, singkat, dalam beban tinggi | Penjualan kilat yang menyebabkan lalu lintas melonjak hingga 5000 pengguna |
| **Stress Testing**  | Menentukan batas dan titik kerusakan sistem | Peningkatan bertahap hingga kegagalan | Menyulut server dengan 200% dari kapasitasnya |


## Persiapan

Apache jmeter bisa digunakan untuk melakukan testing melalui Command Line Interface (CLI). Tetapi akan lebih mudah apabila konfigurasinya dilakukan menggunakan Graphical User Interface (GUI).
Untuk sementara, kita cukup akan mengimplementasikan load testing sederhana menggunakan ``Thread Group``.


Cek apakah java sudah terinstall
```sh
java -version
```

Jika belum maka install dengan command berikut:
```sh
sudo apt-get install openjdk-11-jre
```

Download apache jmeter website Apche JMeter
```sh
wget https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.6.3.zip
```

Lalu extract Apacher jmeternya
```sh
unzip apache-jmeter-5.6.3.zip
```

## Membuat Benchmark Testplan

Karena membuat testplan lebih mudah dilakukan dengan GUI, maka lakukan hal serupa pada host os.

1. Setelah berhasil mengekstrak apache benchmark, masuk ke dalam folder bin dan klik 2 kali file ``ApacheJmeter``:

<img width="457" alt="image" src="https://github.com/user-attachments/assets/3b1d0e78-95d3-4bdc-adf8-75e0654eb53f">

2. Setelah itu window dari apache jmeter akan muncul seperti berikut:

<img width="759" alt="image" src="https://github.com/user-attachments/assets/89eeee27-2462-4241-a902-46b11f4c6a6f">

3. Buat Thread Group baru dengan ``klik kanan (nama testplan) -> Add -> Threads (Users) -> Thread Group``:

<img width="759" alt="image" src="https://github.com/user-attachments/assets/a3ccc8b0-e09e-4e2c-826e-acbcda7c3bef">

Berikut adalah tampilan dari thread group yang telah dibuat:

<img width="759" alt="image" src="https://github.com/user-attachments/assets/909c4fe0-521b-43d9-874d-8d9a0cdee17b">

Kita bisa mengatur sebanyak apa request yang akan dilakukan secara serentak, berapa kali looping thread melakukan request, dll. Pada kasus ini kita akan melakukan tes dengan 100 thread secara serentak.

<img width="527" alt="image" src="https://github.com/user-attachments/assets/1da311d1-8d74-4bb0-ba0f-1204a2448706">

4. Buat HTTP Request sampler dengan ``klik kanan Thread Group -> Sampler -> HTTP Request``:

<img width="759" alt="image" src="https://github.com/user-attachments/assets/4c0bd864-fd5c-4a48-b468-60732391cf01">

5. Pada sampler http request, kalian bisa menambahkan definisi dari informasi dari target yang akan diuji, seperti protokol, domain atau ip, port, path, dan jenis request. Berikut adalah contoh apabila kita ingin melakukan testing pada https://google.com/ dengan path /:

<img width="547" alt="image" src="https://github.com/user-attachments/assets/14abbbb6-4d8d-4ca6-ba31-bdb91c38cff0">

6. Untuk mengetahui hasil pengujian, kalian bisa menambahkan listener dengan ``klik kanan (Test Plan) -> Add -> Listener -> View Result Tree``:

<img width="759" alt="image" src="https://github.com/user-attachments/assets/6d3208f1-84a0-443e-8306-ea5c23232810">

Setelah itu klik tombol play berwarna hijau di atas, lalu lihat bahwa hasil request akan tercatat

<img width="472" alt="image" src="https://github.com/user-attachments/assets/76f805bd-7c1d-4801-ac45-33e43a1cd1d4">

Berikut adalah contoh dari request yang berhasil:
<img width="759" alt="image" src="https://github.com/user-attachments/assets/c91d819d-a48f-4685-a883-87603f4d402f">

## Melakukan pengujian dengan cli

*Note: Kalau kalian ingin menjalankan di dalam gns3, kalian bisa copy kontent dari file testplan yang sudah disimpan di host os, lalu paste kontennya ke sebuah file di node gns3 dengan format file [nama file].jmx

1. Simpan testplan
2. Masuk ke folder bin di apache jmeter
lalu jalankan perintah seperti berikut di terminal
```sh
jmeter -n -t <nama test plan> -l <[nama log output].csv> -e -o <[direktori output]>
```
3. Berikut adalah contoh penggunaan jmeter melalui cli dan isi folder output:

<img width="927" alt="image" src="https://github.com/user-attachments/assets/cccce392-d9f0-487b-948b-808d5bee18c9">

Isi dari folder output adalah report visual dari hasil pengujian salah satunya adalah file html yang bisa dilihat hasilnya bisa dilihat lewat browser

<img width="960" alt="image" src="https://github.com/user-attachments/assets/28482ef2-45d7-440b-a1bc-69d6654edfe6">
