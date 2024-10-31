# Implementasi Terraform

## A. Implementasi Terraform Dengan Virtual Box

Pada modul ini, kita akan mencoba melakukan _spawning_ vm dengan menggunakan Terraform pada Virtual Box. Setelah melakukan _spawning_, kita akan mencoba mengonfigurasikan routing dan subnetting yang terdapat di dalam VM.

### 1. Prerequisites

Pastikan kalian sudah menginstall virtual box dan terraform pada laptop kalian.

### 2. Atur network

Buatlah VirtualBox Host-Only Ethernet Adapter dengan cara:
1. Klik tulisan network pada sidebar atas
2. Klik create, jika ada pop up mengenai warning pembuatan interface, maka klik yes
3. Klik VirtualBox Host-Only Ethernet Adapter baru yang muncul setelah melakukan create
4. Lalu pada adapter, kalian bisa atur IPv4 address dan netmask sesuai yang kalian mau

Pada contoh implementasi ini, kita akan menggunakan IPv4 address berupa `192.168.10.0/24` dan `192.168.20.0/24`.

### 3. Topologi

Pada contoh ini kita akan membuat contoh subnetting dan routing yang sangat sederhanaaaaaa.

[Images](../../assets/topo.png)

Pada gambar topologi di atas, terdiri dari satu router yang akan diconnect pada 2 node, dengan masing-masing node memiliki subnet `192.168.10.0/24` dan `192.168.20.0/24`

### 3. Terraform script

Pada contoh ini, kita akan membuat 3 file terraform, yaitu `main.tf`, `variables.tf`, dan `outputs.tf`.

Pada `main.tf`, kita akan isi dengan ini:
```
terraform {
  required_providers {
    virtualbox = {
      source  = "terra-farm/virtualbox"
      version = "0.2.2-alpha.1"
    }
  }
}

resource "virtualbox_vm" "router" {
  name      = var.router_name
  image     = var.image
  cpus      = var.cpus
  memory    = var.memory
  user_data = file(var.user_data_file)

  network_adapter {
    type = "nat"
  }

  network_adapter {
    type           = "hostonly"
    host_interface = var.host_only_adapter1
  }

  network_adapter {
    type           = "hostonly"
    host_interface = var.host_only_adapter2
  }
}

resource "virtualbox_vm" "node1" {
  name      = var.node1_name
  image     = var.image
  cpus      = var.cpus
  memory    = var.memory
  user_data = file(var.user_data_file)

  network_adapter {
    type           = "hostonly"
    host_interface = var.host_only_adapter1
  }
}

resource "virtualbox_vm" "node2" {
  name      = var.node2_name
  image     = var.image
  cpus      = var.cpus
  memory    = var.memory
  user_data = file(var.user_data_file)

  network_adapter {
    type           = "hostonly"
    host_interface = var.host_only_adapter2
  }
}
```

Oke, sekarang mari kita breakdown code di atas:
1. Di sini kita akan menggunakan provider `terrafarm` untuk membantu melakukan spawning vm pada virtualbox dengan menggunakan terraform.

    ```
    terraform {
        required_providers {
            virtualbox = {
                source  = "terra-farm/virtualbox"
                version = "0.2.2-alpha.1"
            }
        }
    }
    ```

2. Di code di atas, juga didefine 3 resources yang akan dipakai, yaitu router, node1, dan node2. Pada setiap resources tersebut memiliki konfigurasi sebagai berikut

-   name: nama vm
-   image: file image untuk vm
-  cpus: jumlah cpu yang dialokasikan
-  memory: jumlah memori yang dialokasikan
-  user_data: file konfigurasi yang dapat digunakan untuk inisialisasi VM

    Karena dari code di atas mengunakan file yang bernama `user_data`. Maka, buatlah file dengan nama tersebut tanpa isi apapun.

-   network_adapter: menentukan bagaimana VM dapat terhubung dengan jaringan maupun berkomunikasi dengan node lain
    
    Pada network adapter, terdapat beberapa jenis. Dalam contoh di atas, digunakan 2, yaitu `nat` yang digunakan untuk memungkingkan VM mengakses internet melalui ip host-nya dan `hostonly`yang menghubungkan VM ke host tanpa akses eksternal ke internet.


Jika kalian liat di code pada `main.tf`, maka kalian akan menemukan beberapa penulisan `var`. Dalam hal ini, `var` merupakan variable. Untuk code yang akan ada di `variables.tf` dapat dilihat dalam berikut:

```
variable "router_name" {
  description = "Name of the router VM"
  type        = string
  default     = "router"
}

variable "node1_name" {
  description = "Name of the first node VM"
  type        = string
  default     = "node-1"
}

variable "node2_name" {
  description = "Name of the second node VM"
  type        = string
  default     = "node-2"
}

variable "image" {
  description = "Image for the VMs"
  type        = string
  default     = "https://app.vagrantup.com/ubuntu/boxes/bionic64/versions/20180903.0.0/providers/virtualbox.box"
}

variable "cpus" {
  description = "Number of CPUs for the VMs"
  type        = number
  default     = 1
}

variable "memory" {
  description = "Memory allocated for the VMs in MiB"
  type        = string
  default     = "512 mib"
}

variable "user_data_file" {
  description = "Path to the user data file"
  type        = string
  default     = "${path.module}/user_data"
}

variable "host_only_adapter1" {
  description = "Host-only Ethernet Adapter for Node 1"
  type        = string
  default     = "VirtualBox Host-Only Ethernet Adapter #4"
}

variable "host_only_adapter2" {
  description = "Host-only Ethernet Adapter for Node 2"
  type        = string
  default     = "VirtualBox Host-Only Ethernet Adapter #5"
}
```

Nah kode di atas memiliki format berupa:

```
variable "<nama variable>" {
  description = "<deskripsi variable>"
  type        = <jenis variable>
  default     = "<default isi variable>"
}
```
Penjelasan:
- `variable` adalah blok untuk mendeklarasikan variabel input dalam Terraform.
- `description` memberikan deskripsi singkat tentang kegunaan variabel ini.
- `type` mendefinisikan tipe data variabel.
- `default` menentukan nilai awal atau bawaan untuk variabel. Jika tidak ada nilai lain yang diberikan, Terraform akan menggunakan nilai default ini.

### 4. Terraform command

Untuk menjalankan kode di atas, dapat dilakukan dengan langkah-langkah berikut:

#### a. Navigasi ke Direktori Proyek
Pastikan bahwa kamu sudah berada pada direktori yang menyimpan `main.tf`

#### b. Membuat Rencana (Plan)
```bash
terraform plan
```
Terraform akan menampilkan rencana implementasi. Pastikan untuk meninjau hasil rencana ini. Jika hasilnya sesuai dengan yang diharapkan, kamu bisa melanjutkan ke langkah berikutnya.

#### c. Menerapkan Konfigurasi (Apply)
```bash
terraform apply
```
Setelah meninjau rencana, Terraform akan meminta konfirmasi. Ketik yes untuk melanjutkan. Namun, jika ingin melewati konfirmasi yes, maka lakukan perintah ini
```bash
terraform apply -auto-approve
```

#### d. Memeriksa Output
Setelah `terraform apply` selesai, Terraform akan menampilkan output yang telah didefinisikan (seperti IP Router dan Node).

### 5. Konfigurasi dalam VM
Setelah menjalankan perinrah `terraform apply` dan VM telah terbuat dalam virtualbox, maka kita bisa 