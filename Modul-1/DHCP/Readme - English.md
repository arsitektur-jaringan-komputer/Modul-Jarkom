# **2. Dynamic Host Configuration Protocol (DHCP)**

This module has the following _outline_.

## **Outline**

- [**2. Dynamic Host Configuration Protocol (DHCP)**](#2-dynamic-host-configuration-protocol-dhcp)
  - [**Outline**](#outline)
  - [**2.1 Concept**](#21-konsep)
    - [**2.1.1 Introduction**](#211-pendahuluan)
    - [**2.1.2 What is DHCP?**](#212-apa-itu-dhcp)
    - [**2.1.3 Bootstrap Protocol and Dynamic Host Configuration Protocol**](#213-bootstrap-protocol-and-dynamic-host-configuration-protocol)
    - [**2.1.4 DHCP Message Header**](#214-dhcp-message-header)
    - [**2.1.5 How DHCP Works**](#215-cara-kerja-dhcp)
    - [**2.1.6 DHCP Relay**](#216-dhcp-relay)
      - [A. Concept DHCP Relay](#a-konsep-dhcp-relay)
      - [B. Why is DHCP Relay needed?](#b-mengapa-dhcp-relay-diperlukan)
    - [**2.7 DHCP Lease Time**](#27-dhcp-lease-time)
      - [A. Lease Time in DHCP](#a-lease-time-dalam-dhcp)
      - [B. The Importance of Lease Time Configuration](#b-pentingnya-pengaturan-lease-time)
  - [**2.2 Implementation**](#22-implementasi)
    - [**2.2.1 ISC-DHCP-Server Installation**](#221-instalasi-isc-dhcp-server)
    - [**2.2.2 DHCP Server Configuration**](#222-konfigurasi-dhcp-server)
      - [A. Determining the _Interface_ to Be Provided with DHCP Service](#a-menentukan-interface-that-will-diberi-layanan-dhcp)
        - [A.1. Open the _Interface_ Configuration _File_](#a1-buka-file-konfigurasi-interface)
        - [A.2. Determine the _Interface_](#a2-tentukan-interface)
      - [B. Configuring `isc-dhcp-server`](#b-melakukan-konfigurasi-on-isc-dhcp-server)
        - [B.1. Open the DHCP Configuration _File_](#b1-buka-file-konfigurasi-dhcp)
        - [B.2. Add the Configuration _Script_](#b2-tambahkan-script-konfigurasi)
        - [A.3. Restart the `isc-dhcp-server` Service With the Following Command](#a3-restart-service-isc-dhcp-server-with-perintah)
    - [**2.2.3 DHCP Relay Configuration**](#223-konfigurasi-dhcp-relay)
      - [A. Installation](#a-melakukan-instalasi)
      - [B. Configuring `isc-dhcp-relay`](#b-melakukan-konfigurasi-on-isc-dhcp-relay)
      - [C. Configuring IP Forwarding](#c-melakukan-konfigurasi-ip-forwarding)
    - [**2.2.4 DHCP Client Configuration**](#224-konfigurasi-dhcp-client)
      - [A. Configuring the _Client_](#a-mengonfigurasi-client)
        - [A.1. Check Alabasta's IP with `ip a`](#a1-periksa-ip-alabasta-with-ip-a)
        - [A.2. Open `/etc/network/interfaces` to Configure the **Alabasta** _Interface_](#a2-buka-etcnetworkinterfaces-for-mengonfigurasi-interface-alabasta)
        - [A.3. _Comment_ or Delete the Old Configuration (Static `IP Address` Configuration)](#a3-comment-or-hapus-konfigurasi-that-lama-konfigurasi-ip-address-statis)
        - [A.4. Restart Alabasta](#a4-restart-alabasta)
      - [B. Testing](#b-testing)
      - [C. Repeat the steps above on the Loguetown and Water7 clients](#c-lakukan-kembali-langkah---langkah-di-atas-on-client-loguetown-and-water7)
    - [**2.2.5 Leasing Times**](#225-leasing-times)
    - [**2.2.6 Fixed Address**](#226-fixed-address)
      - [A. Configuring the `DHCP Server` on _Router_ Foosha](#a-konfigurasi-dhcp-server-di-router-foosha)
        - [A.1. Open the `isc-dhcp-server` Configuration File](#a1-buka-file-konfigurasi-isc-dhcp-server)
        - [A.2. Add the Following _Script_](#a2-tambahkan-script-following)
        - [A.3. _Restart_ the `isc-dhcp-server` _Service_ on **EniesLobby**](#a3-restart-service-isc-dhcp-server-on-enieslobby)
      - [B. Konfigurasi `DHCP Client`](#b-konfigurasi-dhcp-client)
        - [B.1. Configuring the **Water7** _Network Interface_](#b1-konfigurasi-network-interface-water7)
        - [B.2. Add the following configuration](#b2-tambah-konfigurasi-following)
      - [B.3. _Restart_ the Water7 _Node_](#b3-restart-node-water7)
      - [C. _Testing_](#c-testing)
    - [**2.2.7 Testing the DHCP Configuration on the Topology**](#227-menguji-konfigurasi-dhcp-on-topologi)
  - [**Practice Questions**](#soal-latihan)
  - [**References**](#referensi)
- [**Love Sign from Oniel 🙆‍♀️🙆‍♂️**](#love-sign-from-oniel-️️)

</br>

## **2.1 Concept**

Before going further, we will get acquainted with DHCP step by step. You will learn the concepts, operation, and implementation of DHCP. Happy reading!

### **2.1.1 Introduction**

In a simple topology, we can configure the `IP Address`, `nameserver`, `gateway`, and `subnetmask` on a _node_ manually/staticaly. This manual method is fine when implemented on a network with only a few _hosts_. But what if the network has many hosts? A public WiFi network, for example. Would the network administrator have to configure each _host_ one by one? Just imagining it is terrifying, right?

This is where DHCP is very much needed.

### **2.1.2 What is DHCP?**

**Dynamic Host Configuration Protocol (DHCP)** is a protocol based on a _client-server_ architecture that is used to simplify the allocation of `IP Address`es within a network. DHCP will automatically lease an `IP Address` to the _host_ requesting it.

![how DHCP works](../../Modul-2/images/cara-kerja.png)

Without DHCP, the network administrator would have to enter the `IP Address` of each computer on a network manually. However, if DHCP is installed on the network, all computers connected to the network will automatically receive an `IP Address` from the `DHCP Server`.

### **2.1.3 Bootstrap Protocol and Dynamic Host Configuration Protocol**

Besides DHCP, there is another protocol that also simplifies the allocation of `IP Address`es in a network, namely `Bootstrap Protocol (BOOTP)`. The difference between `BOOTP` and DHCP lies in their configuration process, as follows.

| BOOTP                                                                                                       | DHCP                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The network administrator configures a _mapping_ of the _client_'s `MAC Address` to a specific `IP Address`. | The _Server_ leases an `IP Address` and other configurations for a certain period of time. This protocol was designed based on how `BOOTP` works. |

### **2.1.4 DHCP Message Header**

![DHCP header](../../Modul-2/images/DHCP-message-header.png)

![DHCP header legend](../../Modul-2/images/DHCP-message-header-keterangan.png)

### **2.1.5 How DHCP Works**

DHCP works by involving two parties, namely the **Server** and **Client**, as follows.

1. **DHCP Server** provides a service that can give `IP Address`es and other parameters to all _clients_ requesting them.
2. **DHCP Client** is a _client_ machine running _client_ software that allows it to communicate with the `DHCP Server`.
   `DHCP Server` generally has a set of distributed `IP Address`es called a `DHCP Pool`. Each _client_ will lease one for a period of time determined by DHCP itself (in the configuration, this is called _leasing time_). When the period expires, the client will request a new `IP Address` or renew it. This is why the client's `IP Address` is dynamic.

![How DHCP works](../../Modul-2/images/DHCP.gif)

There are 5 stages in the DHCP `IP Address` leasing process, as follows.

1. **DHCPDISCOVER**: The _Client_ sends a _broadcast_ request to find an active `DHCP Server`. `DHCP Server` menggunwill UDP port 67 for menerima broadcast from client melalui port 68.
2. **DHCPOFFER**: The `DHCP Server` offers an `IP Address` (and other configurations, if any) to the _client_. The offered `IP Address` is one of the addresses available in the `DHCP Pool` on the corresponding `DHCP Server`.
3. **DHCPREQUEST**: The _Client_ accepts the offer and agrees to lease the `IP Address` from the `DHCP Server`.
4. **DHCPACK**: The DHCP server accepts the _client_'s `IP Address` request by sending an `ACKnoledgment` packet containing confirmation of the `IP Address` and other information. Then, the _client_ initializes by binding the `IP Address`, and the _client_ can operate on the network. The `DHCP Server` records the lease.
5. **DHCPRELEASE**: The _Client_ stops leasing the `IP Address` (when the lease expires or it receives `DHCPNAK`).

![Flowchart how DHCP works](../../Modul-2/images/cara-kerja-2.png)

Furthermore, you can watch or view visualizations of how DHCP works from various sources to improve your understanding. One of them is the following video [https://youtu.be/S43CFcpOZSI](https://youtu.be/S43CFcpOZSI).

### **2.1.6 DHCP Relay**

Previously, it was mentioned that DHCP involves two parties, namely `DHCP Server` and `DHCP Client`. This section discusses another party involved in the `IP Address` leasing process, namely `DHCP Relay`. What is `DHCP Relay`?

#### A. Concept DHCP Relay

`DHCP Relay` is a network device (in the most common scenario, this network device is a `router`) that acts as an intermediary or (_forwarder_) between a `DHCP Client` and a `DHCP Server` that are not on the same network segment. `DHCP Relay` receives a _request_ from the `DHCP Client` and forwards it to the `DHCP Server`. Conversely, `DHCP Relay` receives a _response_ from the `DHCP Server` and forwards it to the `DHCP Client`. With `DHCP Relay`, the `DHCP Client` and `DHCP Server` do not need to be on the same network segment.

> Some of you may think, after reading the first sentence of the `DHCP Relay` explanation, that `DHCP Relay` has the same role as a switch. Well, that understanding is incorrect!

The placement of `DHCP Relay` in a network can be illustrated as follows.

![DHCP Relay](../../Modul-2/images/relay.png)

As a _forwarder_, the way DHCP works with `DHCP Relay` involved is the same as described previously, but with some adjustments. In short, it works as follows.

- `DHCP Relay` will receive `DHCPDISCOVER` from `DHCP Client`, then forward it to `DHCP Server`.
- `DHCP Server` will send `DHCPOFFER` keon `DHCP Relay`, then `DHCP Relay` will forward it to `DHCP Client`.
- `DHCP Relay` will also forward `DHCPREQUEST` from `DHCP Client` to `DHCP Server`, then `DHCP Server` will send `DHCPACK` to `DHCP Relay`, and `DHCP Relay` will forward it to `DHCP Client`.
- `DHCP Relay` will also forward `DHCPRELEASE` from `DHCP Client` to `DHCP Server`, then `DHCP Server` will send `DHCPNAK` to `DHCP Relay`, and `DHCP Relay` will forward it to `DHCP Client`.

> Surely you are familiar with that term? Yes, the term is similar to the _handshake_ process in the TCP protocol!

#### B. Why is DHCP Relay needed?

There are several reasons why `DHCP Relay` is needed, as follows.

- Allows `DHCP Server` serve `DHCP Client` that are outside the local network segment. Without `DHCP Relay`, DHCP can only operate within a single local network segment.
- Saves `IP Address`. With `DHCP Relay`, only one `DHCP Server` is needed to serve many network segments. Without `DHCP Relay`, each network segment requires its own `DHCP Server`.
- Simplifies network management. The network administrator only needs to configure and manage a single `DHCP Server`, rather than each one individually.
- Improves network security by limiting `DHCP Server` access to `DHCP Relay` only.

### **2.7 DHCP Lease Time**

`DHCP Lease Time` is the amount of time allocated by the `DHCP Server` when an `IP Address` is leased to a _client_ computer. In short, after this lease period ends, the `IP Address` can be leased again by the same _client_ computer, or the _client_ may receive another `IP Address` if the previously leased `IP Address` is being used by another _client_ computer.

#### A. Lease Time in DHCP

`DHCP Lease Time` determines how long a DHCP _client_ can use the `IP Address` allocated by the `DHCP Server`. There are several types of _lease time_ in DHCP, as follows.

- Infinite Lease Time

  Simply put, the _client_ gets the right to use a specific `IP Address` forever or until the _lease_ is manually cancelled by the administrator. This type of _lease time_ is usually applied to _static_ `IP Address` _assignment_ on devices such as _servers_, _routers_, _switches_, _printers_, and other important devices. The advantage is that the _client_ will always receive the same `IP Address` even after a _restart_ or _reconnect_. However, it can potentially waste `IP Address`es if the allocated `IP Address` is not used.

- Finite Lease Time

  With this type of _lease time_, _client_ can only use `IP Address` for a certain period of time (hours, days, weeks). After the _lease expires_, _client_ must _request_ a new `IP Address` from the `DHCP server`. This type of _lease time_ is generally used for _client_ seperti komputer, laptop, and _smartphone_. The advantage is that `IP Address` can be reused, _client_ receives a new `IP Address` periodically. However, it may cause connection interruptions during _renew lease_.

- Dynamic Lease Time

  `DHCP Server` automatically determines the _lease time_ based on _availability_ `IP Address` and _request client_. This can result in a _lease time_ ranging from very short to long depending on `IP Address` availability. Its advantage is that it provides administrators with flexibility in managing `IP Address`es.

#### B. The Importance of Lease Time Configuration

Some reasons why configuring DHCP lease time is important are as follows.

- Ensures the availability of `IP Address` by limiting usage per _client_ to a specific period of time.
- Prevents a _single_ _client_ from monopolizing a particular `IP Address` for a long period; `IP Address` it can be used by another _client_ after it _expires_.
- Provides _clients_ with new `IP Address`es periodically from the `IP Address` _pool_ for security & performance reasons.
- Allows the `DHCP Server` to reclaim unused or _inactive_ `IP Address`es and redistribute them to other _clients_ that need them.
- Helps administrators _troubleshoot_ network problems related to the _client_'s `IP Address`.

</br>

## **2.2 Implementation**

After understanding the concepts, how do we implement them? For the implementation, we will use the following topology

![contoh-topologi-dhcp](../../Modul-2/images/jarkom-modul-github-dhcp-topologi.png)

<!-- ``` -->
<!--                     NAT / internet -->
<!--                           | -->
<!--                         eth0 (DHCP from NAT) -->
<!--                      +----------+ -->
<!--                      |  Foosha  |  router + DHCP relay -->
<!--                      +----------+ -->
<!--               eth1 10.40.1.1   eth2 10.40.2.1 -->
<!--                     |                | -->
<!--                 Switch 1          Switch 2 -->
<!--                 10.40.1.0/24      10.40.2.0/24 -->
<!--                  |       |         |         | -->
<!--             Loguetown Alabasta  EniesLobby  Water7 -->
<!--             (client)  (client)  (DHCP       (client) -->
<!--                                  server) -->
<!-- ``` -->
 
In this case, we configure the IP Address of each node as follows:
 
```
Foosha eth0:  from NAT cloud (192.168.122.x)
Foosha eth1:  10.40.1.1/24      (sisi Loguetown and Alabasta)
Foosha eth2:  10.40.2.1/24      (sisi EniesLobby and Water7)
 
EniesLobby:   10.40.2.2/24, gateway 10.40.2.1   (static, DHCP Server)
Loguetown:    DHCP (pool 10.40.1.10 - 10.40.1.100)
Alabasta:     DHCP (pool 10.40.1.10 - 10.40.1.100)
Water7:       DHCP (pool 10.40.2.20 - 10.40.2.100, fixed address on 2.2.6)
```
 
The software used in this module:
 
| Role | Software | Node |
| ----- | --------------- | ---- |
| DHCP Server | `kea-dhcp4` (ISC Kea) | EniesLobby |
| DHCP Relay | `dhcp-helper` | Foosha |
| DHCP Client | `udhcpc` (included with busybox) | Loguetown, Alabasta, Water7 |
 
`kea-dhcp4` replaces `isc-dhcp-server` (`dhcpd`), and `dhcp-helper` replaces `isc-dhcp-relay`. Kea only functions as a DHCP Server and does not include a relay, so the relay is run using a separate program.
 
The nodes in this module use Alpine Linux, which does not have `rc-service`. Therefore, the programs are run directly from the command line, and at boot they are run from `/root/init.sh` (see [2.2.8](#228-menjaga-konfigurasi-setelah-restart)).

#### Initial Configuration

1. Configure the network interface on **Foosha**:
```
auto eth0
iface eth0 inet dhcp
 
auto eth1
iface eth1 inet static
    address 10.40.1.1
    netmask 255.255.255.0
 
auto eth2
iface eth2 inet static
    address 10.40.2.1
    netmask 255.255.255.0
```
 
2. Enable routing and NAT on **Foosha** so that clients can access the internet:
```sh
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -s 10.40.0.0/16 -o eth0 -j MASQUERADE
```
 
3. Configure `/etc/network/interfaces` on **EniesLobby**. The gateway must be specified because replies to clients on `10.40.1.0/24` must return through Foosha:
```
auto lo
iface lo inet loopback
 
auto eth0
iface eth0 inet static
    address 10.40.2.2
    netmask 255.255.255.0
    gateway 10.40.2.1
```
 
Then configure DNS so that the node can download packages:
 
```sh
echo "nameserver 8.8.8.8" > /etc/resolv.conf
```


### **2.2.1 Instalasi Kea-DHCP Server**

In this topology, we will use **EniesLobby** as the DHCP Server. Therefore, we need to _install_ **isc-dhcp-server** on **EniesLobby** by following these steps.

1. Update the _package lists_ on **EniesLobby** with the following command.

```
apk update
```

2. _Install_ **isc-dhcp-server** on **EniesLobby**.

```
apk add kea-dhcp4
```

3. Make sure **isc-dhcp-server** has been _installed_ with the command.

```
kea-dhcp4 -V
```

![image](./../../Modul-2/images/kea-dhcp4_version.png)

### **2.2.2 DHCP Server Configuration**

The steps to perform after installation are as follows.

#### A. Determining the _Interface_ to Be Provided with DHCP Service

##### A.1. Open the _Interface_ Configuration _File_

Please edit the configuration _file_ at `/etc/kea/kea-dhcp4.conf`

```sh
nano /etc/kea/kea-dhcp4.conf
```

![image kea dhcp4 conf default isi](../../Modul-2/images/kea-dhcp4_conf_default.png)

##### A.2. Determine the _Interface_


Observe the topology that has been created. Interface on **EniesLobby** that points to the switch is `eth0`, so we choose interface `eth0` to be provided with DHCP service. In Kea, this is configured in the `interfaces-config`:
 
```json
"interfaces-config": {
  "interfaces": ["eth0"]
}
```

#### B. Melakukan Konfigurasi on `kea-dhcp4`

There are many things that can be configured, including the following.

- Range IP
- DNS Server
- Netmask Information
- Default Gateway
- dll.

##### B.1. Open the DHCP Configuration _File_

The configuration is done in the same file, namely `/etc/kea/kea-dhcp4.conf`.

##### B.2. Add the Configuration _Script_

Parameters in `isc-dhcp-server` are mapped to Kea as follows:
 
| **No** | **ISC dhcpd** | **Kea (`kea-dhcp4.conf`)** | **Description** |
| ------ | ------------- | -------------------------- | -------------- |
| 1 | `INTERFACES=` | `"interfaces-config": { "interfaces": ["eth0"] }` | The interface that receives DHCP requests. |
| 2 | `subnet 'NID' netmask 'Netmask'` | `"subnet": "NID/prefix"` | The subnet Network ID in CIDR notation, for example `10.40.1.0/24`. Kea selects the subnet based on the relay address (or interface) where the request arrives. |
| 3 | `range 'Start_IP' 'End_IP'` | `"pools": [{ "pool": "Start_IP - End_IP" }]` | The IP range distributed dynamically. More than one pool is allowed. |
| 4 | `option routers 'IP_Gateway'` | `{ "name": "routers", "data": "IP_Gateway" }` | The gateway IP given to the client. |
| 5 | `option domain-name-servers 'DNS'` | `{ "name": "domain-name-servers", "data": "DNS" }` | The DNS given to the client. |
| 6 | `option broadcast-address` | (otomatis) | Kea calculates the broadcast address itself. |
| 7 | `default-lease-time 'Waktu'` | `"valid-lifetime": Waktu` | IP lease duration in seconds. |
| 8 | `max-lease-time 'Waktu'` | `"max-valid-lifetime": Waktu` | Maximum lease duration in seconds. |
| 9 | `host X { hardware ethernet ...; fixed-address ...; }` | `"reservations": [{ "hw-address": "...", "ip-address": "..." }]` | Fixed address for a specific host (see 2.2.6). |
 
**About NID:** NID is the Network ID of the interface facing the client, with the host portion set to 0. For example, if the router interface for a subnet has the IP `10.40.1.1/24`, then the subnet is `10.40.1.0/24`. **NB: The correct way to calculate NID will be explained in module 4.**
 
In this example, we use `8.8.8.8` as the DNS. Replace the entire contents of `/etc/kea/kea-dhcp4.conf` on **EniesLobby** with the following configuration. This configuration serves two subnets: `10.40.2.0/24` directly (Water7 is on the same segment as the server), and `10.40.1.0/24` through the relay on Foosha.

```json
{
  "Dhcp4": {
    "interfaces-config": {
      "interfaces": ["eth0"]
    },
    "lease-database": {
      "type": "memfile",
      "persist": true,
      "name": "/var/lib/kea/kea-leases4.csv"
    },
    "valid-lifetime": 600,
    "max-valid-lifetime": 7200,
    "subnet4": [
      {
        "id": 1,
        "subnet": "10.40.1.0/24",
        "pools": [
          { "pool": "10.40.1.10 - 10.40.1.100" }
        ],
        "option-data": [
          { "name": "routers", "data": "10.40.1.1" },
          { "name": "domain-name-servers", "data": "192.168.122.1" }
        ]
      },
      {
        "id": 2,
        "subnet": "10.40.2.0/24",
        "pools": [
          { "pool": "10.40.2.20 - 10.40.2.100" }
        ],
        "option-data": [
          { "name": "routers", "data": "10.40.2.1" },
          { "name": "domain-name-servers", "data": "192.168.122.1" }
        ]
      }
    ]
  }
}
```

![image kea-dhcp4 conf after](../../Modul-2/images/kea-dhcp4_conf_after.png)

<!-- ```conf -->
<!-- subnet 'NID' netmask 'Netmask' { -->
<!--     range 'IP_Awal' 'IP_Akhir'; -->
<!--     option routers 'iP_Gateway'; -->
<!--     option broadcast-address 'IP_Broadcast'; -->
<!--     option domain-name-servers 'DNS_that_diinginkan'; -->
<!--     default-lease-time 'Waktu'; -->
<!--     max-lease-time 'Waktu'; -->
<!-- } -->
<!-- ``` -->
<!---->
<!-- _Script_ tersebut mengatur parameter jaringan that can didistribusikan oleh DHCP, seperti informasi `netmask`, `default gateway`, and `DNS Server`. Berikut ini beberapa parameter jaringan dasar that biasanya digunwill. -->
<!---->
<!-- | **No** | **Parameter Jaringan**                             | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | -->
<!-- | ------ | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -->
<!-- | 1      | `subnet 'NID'`                                     | Network ID on subnet interface. Sederhananya on kasus pembelajaran praktikum kita, nilai NID is 3 bytes from IP interface tujuan (sesuai with langkah [A2](#a2-tentukan-interface)) **on router** (dalam kasus ini is Foosha) with byte terakhirnya is 0. Sebagai contoh saja, jika interface that kamu pilih is `eth0` with IP 10.40.0.1, maka NID subnetnya is 10.40.0.0. **NB: Cara menentukan NID that proper will dijelaskan on modul 4** | -->
<!-- | 2      | `netmask 'Netmask`                                 | Netmask on subnet. Dapat dilihat on konfigurasi network router with cara: Ke topologi (GNS3) → klik kanan router → Configure → Edit Network Configuration → Lihat nilai netmask on interface that diinginkan                                                                                                                                                                                                                                                                | -->
<!-- | 3      | `range 'IP_Awal' 'IP_Akhir'`                       | Rentang `IP Address` that will didistribusikan and digunwill secara dinamis                                                                                                                                                                                                                                                                                                                                                                                                         | -->
<!-- | 4      | `option routers 'Gateway'`                         | IP gateway from router menuju client sesuai konfigurasi subnet                                                                                                                                                                                                                                                                                                                                                                                                                      | -->
<!-- | 5      | `option broadcast-address 'IP_Broadcast'`          | IP broadcast on subnet                                                                                                                                                                                                                                                                                                                                                                                                                                                            | -->
<!-- | 6      | `option domain-name-servers 'DNS_that_diinginkan'` | DNS that ingin kita berikan on client                                                                                                                                                                                                                                                                                                                                                                                                                                             | -->
<!-- | 7      | Lease time                                         | Waktu that dialokasikan ketika sebuah IP dipinjamkan keon komputer client. Setelah waktu pinjam ini selesai, maka IP tersebut can dipinjam lagi oleh komputer that sama or komputer tersebut mencankan `IP Address` lain jika `IP Address` that sebelumnya dipinjam, dipergunwill oleh komputer lain                                                                                                                                                                        | -->
<!-- | 8      | `default-lease-time 'Waktu'`                       | Lama waktu DHCP server meminjamkan `IP Address` keon client, dalam satuan detik. Default 600 detik                                                                                                                                                                                                                                                                                                                                                                                | -->
<!-- | 9      | `max-lease-time 'Waktu'`                           | Waktu maksimal that di alokasikan for peminjaman IP oleh DHCP server ke client dalam satuan detik. Default 7200 detik                                                                                                                                                                                                                                                                                                                                                             | -->
<!---->
<!-- Pada contoh following, kita will menggunwill DNS 192.168.122.1. Maka konfigurasinya menjadi as following: -->

![subnet on kea dhcp]()

##### A.3. Run the `kea-dhcp4` Service With the Following Command

First check that the configuration file has no errors:
 
```sh
kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
```

![image kea-dhcp4 test conf normal](../../Modul-2/images/kea-dhcp4_conf_test_normal.png)
 
Correct output displays both subnets and has no `ERROR` lines. The `WARN` line about multi-threading is normal. As shown in the image above
 
Create the directories required by Kea, then run it. For the first test, run it in the *foreground* with debug mode so that we can see each DISCOVER, OFFER, REQUEST, and ACK:
 
```sh
mkdir -p /var/lib/kea /run/kea
kea-dhcp4 -d -c /etc/kea/kea-dhcp4.conf
```

![kea-dhcp4 run normal](../../Modul-2/images/kea-dhcp4_run.png)
 
Press `Ctrl+C` to stop it. To run it in the *background*:
 
```sh
kill $(pidof kea-dhcp4) 2>/dev/null
kea-dhcp4 -c /etc/kea/kea-dhcp4.conf > /root/kea.log 2>&1 &
```


### **2.2.3 DHCP Relay Configuration**

When the DHCP Server is on a different subnet from the DHCP client, we need `DHCP Relay`. Therefore, the following steps must be performed on the device designated as the `DHCP Relay` (usually a _router_). Therefore, _router_ **Foosha** will be the DHCP Relay. The steps to perform are as follows.
In this case, we use router **Foosha** as the DHCP Relay. Follow these steps:
 
#### A. Installation
 
First, we need to install the relay program on **Foosha**.
 
```sh
apk update
apk add dhcp-helper
```
 
#### B. Melakukan Konfigurasi on `dhcp-helper`
 
`dhcp-helper` is configured through command-line options. Run it on **Foosha**:
 
```sh
dhcp-helper -n -s 10.40.2.2 -i eth1
```

![dhcp helper foosha node](../../Modul-2/images/dhcp-helper-foosha.png)

- `-s 10.40.2.2` is the DHCP Server IP address. In this case, it is the IP address of **EniesLobby**. What is its IP address?
- `-i eth1` is the interface that listens for client requests. Its value must match the interface connected to the clients. In this case, **Foosha** has interface `eth1`, which is connected to the Loguetown and Alabasta clients. If there is more than one interface connected to clients, repeat the option: `-i eth1 -i eth3`.
- `-n` makes the relay run in the *foreground* so that we can see error messages. Remove this option to run it as a daemon in the *background*.
Water7 does not need to be served through the relay because it is on the same segment as the DHCP Server.
 
> **Catatan:** each additional client subnet also requires a corresponding `subnet4` block in the Kea configuration on the server, covering the Foosha interface address on that subnet.

#### C. Configuring IP Forwarding

Make sure IP Forwarding is enabled on **Foosha**:
 
```sh
sysctl -w net.ipv4.ip_forward=1
```
 
To keep it enabled after restart, also add the following line to `/etc/sysctl.conf`:
 
```
net.ipv4.ip_forward=1
```

> What is `IP Forwarding`? `IP Forwarding` is a feature that allows a _router_ to forward packets from one network to another. A _Router_ has at least two network _interfaces_; for example, _interface_ A is connected to network A and _interface_ B is connected to network B. When an IP packet enters from network A destined for network B, the _router_ will forward the packet from _interface_ A to _interface_ B. and vice versa.

Congratulations 🎉, the `DHCP Relay` configuration is complete!

---

### **2.2.4 DHCP Client Configuration**

After configuring the _server_, we also need to configure the _client_ _interface_ so it can receive service from the `DHCP Server`. In this topology, the example _clients_ are **Alabasta**, **Loguetown**, and **Water7**.

#### A. Configuring the _Client_

##### A.1. Check Alabasta's IP with `ip a`

From the previous configuration, **Alabasta** was assigned the static `IP Address` 10.40.1.3.

##### A.2 Shut down the Alabasta node and open the network configuration from GNS3 Desktop

_Comment_ or delete the old configuration (konfigurasi `IP Address` statis)

Then add the following configuration.

```
auto eth0
iface eth0 inet dhcp
```

##### A.4. Start node Alabasta

Start the Alabasta node again. When you open the Alabasta console, the DHCP IP Lease from EniesLobby should appear automatically.

![can ip dhcp](../../Modul-2/images/dhcp-client-alabasta-inetdhcp.png)

or use the command `udhcpc -i eth0`

![can ip dhcp from udhcpc](../../Modul-2/images/dhcp-client-alabasta-udhcpc.png)

#### B. Testing

Check **Alabasta**'s `IP Address` again by running `ip a`.

Also check whether **Alabasta** has received the `DNS Server` according to the `DHCP Server` configuration. Check `/etc/resolv.conf` using the following command. You can also check by pinging `google.com`

![image etc resolv.conf](../../Modul-2/images/dhcp-client-alabasta-cek-etcresolv.png)

If **Alabasta**'s `IP Address` and nameserver have changed according to the configuration provided by DHCP and it can successfully ping `google.com`, congratulations! You have succeeded! 🎉🎉

**Description**:

- If **Alabasta**'s IP has not changed yet, don't panic. Please _restart_ the _node_ through the GNS3 page.
- If it still has not changed, don't ask right away. Check all the configurations you have made again; there may be a typo.

#### C. Repeat the steps above on the Loguetown and Water7 clients

- Client **Loguetown** and **Water7**.

Once an `IP Address` has been leased to a client, that `IP Address` will not be given to another _client_. As a result, no _client_ receives the same `IP Address`.

---

### **2.2.5 Leasing Times**

In this section, we will see for ourselves how lease time works. We will shorten the lease on subnet `10.40.1.0/24` to 2 minutes.
 
#### A. Change the lease time on the server
 
On **EniesLobby**, edit `/etc/kea/kea-dhcp4.conf` and add `valid-lifetime` and `max-valid-lifetime` to the `10.40.1.0/24` subnet block. Subnet-level settings override the global settings:
 
```json
{
  "id": 1,
  "subnet": "10.40.1.0/24",
  "valid-lifetime": 120,
  "max-valid-lifetime": 600,
  "pools": [
    { "pool": "10.40.1.10 - 10.40.1.100" }
  ],
  "option-data": [
    { "name": "routers", "data": "10.40.1.1" },
    { "name": "domain-name-servers", "data": "192.168.122.1, 8.8.8.8, 8.8.4.4" }
  ]
}
```
 
- `valid-lifetime` is the default lease time (in seconds). This value is used if the client does not request a specific time.
- `max-valid-lifetime` is the upper limit if the client requests a longer lease.
Check and restart Kea:
 
```sh
kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
kill $(pidof kea-dhcp4) 2>/dev/null
kea-dhcp4 -c /etc/kea/kea-dhcp4.conf > /root/kea.log 2>&1 &
```
 
#### B. Observe on the client
 
On **Alabasta**, request an IP address and observe the output:
 
```sh
udhcpc -i eth0 -f
```
 
The output shows the received lease time, for example `lease of 10.40.1.x obtained ... lease time 120`. Let it run for more than one minute. At half of the lease period (about 60 seconds), `udhcpc` will send a renewal (*renew*) request directly to the server.
 
On **EniesLobby**, view the lease records:
 
```sh
cat /var/lib/kea/kea-leases4.csv
```
 
The `expire` column shows when the lease expires (in epoch format), and its value increases each time the client renews.
 
You can also force a renewal or release the lease manually:
 
```sh
kill -USR1 $(pidof udhcpc)     # renew
kill -USR2 $(pidof udhcpc)     # release
```
 
When finished, restore the lease time values to their original settings (remove the two lines in the subnet block, or change them to `600` and `7200`), then restart Kea.


### **2.2.6 Fixed Address**

The configuration can be done as follows.

![](https://thumbs.gfycat.com/FalseNiftyCrab-max-1mb.gif)

> **Case Study**:
>
> It turns out that Franky's ship parked in **Water7**, besides being a _client_, will also be used as the _server_ for a ship trading application, which would make things difficult if its `IP Address` kept changing every time **Water7** connected to the internet. Therefore, **Water7** needs a fixed `IP Address` that does not change.

The problem Franky faces is that Water7's IP address keeps changing. Therefore, the requirement is a fixed `IP address`. Therefore, the solution offered is a DHCP Server feature that can "lease" an `IP Address` permanently to a _host_, namely **Fixed Address**. In this case, **Water7** will receive a fixed `IP Address`, namely `10.40.2.13`.

#### A. Configuration of the `DHCP Server` on EniesLobby
 
##### A.1. Buka File Konfigurasi `kea-dhcp4`
 
Open and edit `/etc/kea/kea-dhcp4.conf` on **EniesLobby**.
 
First, find out Water7's hardware address. Run `ip a` on **Water7**, look at the interface connected to the switch (`eth0`), then copy the value after `link/ether`.

![dhcp client water7 cek ip a](../../Modul-2/images/dhcp-client-water7-ip-a.png)
 
##### A.2. Tambahkan Script Berikut
 
Add the `reservations` list to subnet `10.40.2.0/24` (the subnet with `id` 2):
 
```json
{
  "id": 2,
  "subnet": "10.40.2.0/24",
  "pools": [
    { "pool": "10.40.2.20 - 10.40.2.100" }
  ],
  "option-data": [
    { "name": "routers", "data": "10.40.2.1" },
    { "name": "domain-name-servers", "data": "192.168.122.1, 8.8.8.8, 8.8.4.4" }
  ],
  "reservations": [
    {
      "hw-address": "aa:bb:cc:dd:ee:ff",
      "ip-address": "10.40.2.13"
    }
  ]
}
```
 
Replace `aa:bb:cc:dd:ee:ff` with the Water7 hardware address you copied.
 
**Explanation**:
 
- `hw-address` is the MAC address of the Water7 interface.
- `ip-address` is the IP address that is always leased to **Water7**.

##### A.3. Restart the `kea-dhcp4` Service on EniesLobby
 
```sh
kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
kill $(pidof kea-dhcp4) 2>/dev/null
kea-dhcp4 -c /etc/kea/kea-dhcp4.conf > /root/kea.log 2>&1 &
```
 
#### B. Konfigurasi `DHCP Client`
 
##### B.1. Konfigurasi Network Interface Water7
 
The network interface can be accessed through the network configuration in the GNS3 application on the **Water7** node.
 
##### B.2. Add the following configuration
 
```
auto eth0
iface eth0 inet dhcp
    hwaddress ether aa:bb:cc:dd:ee:ff
```
 
Use the same MAC address as the one in the reservation. The hardware address needs to be *set* in `/etc/network/interfaces` so that the hwaddress does not change when the GNS3 project is shut down or exported.
 
##### B.3. Restart Node Water7
 
Restart the Water7 node from the GNS3 page, or run:
 
```sh
kill -USR2 $(pidof udhcpc)
ifdown eth0; ifup eth0
```

or

```
udhcpc -i eth0
```

![water7 can ip preserved from dhcp](../../Modul-2/images/dhcp-client-water7-ip-preserved.png)
 
#### C. Testing
 
Check **Water7**'s IP with `ip a`.
 
```sh
ip a
```
 
The **Water7** IP should now have changed to **10.40.2.13**, according to the fixed address provided by the DHCP Server.

<!-- #### A. Configuration of the `DHCP Server` on **EniesLobby** -->
<!---->
<!-- ##### A.1. Open the `isc-dhcp-server` Configuration File -->
<!---->
<!-- Open and edit the file `/etc/dhcp/dhcpd.conf`. -->
<!---->
<!-- ##### A.2. Add the Following _Script_ -->
<!---->
<!-- ``` -->
<!-- host Water7 { -->
<!--     hardware ethernet 'hwaddress_milik_Water7'; -->
<!--     fixed-address 10.40.2.13; -->
<!-- } -->
<!-- ``` -->
<!---->
<!-- ![image](./../../Modul-2/images/host_water7.jpg) -->
<!---->
<!-- **Explanation**: -->
<!---->
<!-- - To find `hwaddress_milik_Water7` (Water7's _hardware_ _address_), you can execute `ip a` on Water7, then look at the _interface_ connected to the `DHCP Relay`, which in this case is `eth0`, and look at the `link/ether` section. _Copy_ that _address_ and enter it in the `isc-dhcp-server` configuration on **EniesLobby**. -->
<!---->
<!-- ![image](./../../Modul-2/images/hwaddress_water7.jpg) -->
<!---->
<!-- - **fixed-address** is the `IP Address` that is permanently "leased" to **Water7** -->
<!---->
<!-- ##### A.3. _Restart_ the `isc-dhcp-server` _Service_ on **EniesLobby** -->
<!---->
<!-- #### B. Konfigurasi `DHCP Client` -->
<!---->
<!-- ##### B.1. Configuring the **Water7** _Network Interface_ -->
<!---->
<!-- _Network interface_ can diakses on `/etc/network/interfaces`. -->
<!---->
<!-- ##### B.2. Add the following configuration -->
<!---->
<!-- ``` -->
<!-- hwaddress ether 'hwaddress_milik_Water7' -->
<!-- ``` -->
<!---->
<!-- ![image](./../../Modul-2/images/interfaces_jipangu.png) -->
<!---->
<!-- **Description**: -->
<!-- The _hardware address_ also needs to be _set_ in `/etc/network/interfaces` to prevent the `hwaddress` from changing when the GNS3 _project_ is shut down or _exported_. -->
<!---->
<!-- #### B.3. _Restart_ the Water7 _Node_ -->
<!---->
<!-- Please _restart_ the Water7 _node_ from the GNS3 page. -->
<!---->
<!-- #### C. _Testing_ -->
<!---->
<!-- Check **Water7**'s IP by running `ip a`. -->
<!---->
<!-- ![image](./../../Modul-2/images/ip_water7.jpg) -->
<!---->
<!-- `IP Address` **Water7** has changed to `10.40.2.13` according to the _Fixed_ _Address_ provided by the `DHCP Server`. 👋👋👋 -->
<!---->
---


### **2.2.7 Testing the DHCP Configuration on the Topology**
 
After completing the configurations above, you can verify whether the DHCP Server works by following these steps:
 
1. Shut down all nodes through the GNS3 page
2. Start all nodes again
3. Run `ip a` on each node
If all client node IPs change according to the range configured on the DHCP Server (Loguetown and Alabasta from `10.40.1.10 - 10.40.1.100`) and **Water7** continues to receive IP `10.40.2.13`, then the DHCP Server configuration is successful. All clients should also be able to `ping google.com`.
 
To view the leases recorded on the server, run the following on **EniesLobby**:
 
```sh
cat /var/lib/kea/kea-leases4.csv
```
 
### **2.2.8 Keeping the Configuration After Restart**
 
On the Alpine appliance in GNS3, only `/etc`, `/etc/network`, and `/root` are persistent. This means the configuration files above remain after a restart, but packages installed with `apk add` will be lost. The solution is to save the packages in `/root` while there is an internet connection, then reinstall them at boot through a script called from `/root/init.sh`.
 
> The commands below assume `/root/init.sh` is run at boot. First, view its contents with `cat /root/init.sh` and make sure the script does not reset your network configuration. Add the invocation line only once.
 
#### A. EniesLobby (DHCP Server)
 
Create `/root/boot.sh`:
 
```sh
cat > /root/boot.sh <<'EOF'
#!/bin/sh
exec >>/root/boot.log 2>&1
 
apk update
apk add kea-dhcp4
 
mkdir -p /var/lib/kea /run/kea
kill $(pidof kea-dhcp4) 2>/dev/null
kea-dhcp4 -t /etc/kea/kea-dhcp4.conf && \
  kea-dhcp4 -c /etc/kea/kea-dhcp4.conf >/root/kea.log 2>&1 &
EOF

chmod +x /root/boot.sh
echo 'sh /root/boot.sh &' >> /root/init.sh
```

You can also place the kea-dhcp4 configuration in the `/root` folder and, by modifying the `init.sh` script, copy the configuration file to `/etc/kea/kea-dhcp4.conf`.
 
#### B. Foosha (Router, NAT, Relay)
 
Create `/root/boot.sh`:
 
```sh
cat > /root/boot.sh <<'EOF'
#!/bin/sh
exec >>/root/boot.log 2>&1

apk update
apk add dhcp-helper
 
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -s 10.40.0.0/16 -o eth0 -j MASQUERADE
 
kill $(pidof dhcp-helper) 2>/dev/null
dhcp-helper -s 10.40.2.2 -i eth1
EOF

chmod +x /root/boot.sh
echo 'sh /root/boot.sh &' >> /root/init.sh
```
 
#### C. Client
 
Clients do not require additional packages or a boot script. `udhcpc` is already included in busybox, and `/etc/network/interfaces` is persistent, so `iface eth0 inet dhcp` is applied again at every boot.
 
After restarting, read `/root/boot.log` on the node to see what the boot script did.
 
### **2.2.9 Troubleshooting**
 
If a client does not receive an IP address, find out where its request stops. Check from the server side first.
 
1. **Test the server without the relay.** On **EniesLobby**, run Kea in the foreground (`kea-dhcp4 -d -c /etc/kea/kea-dhcp4.conf`), then run `udhcpc -i eth0 -f -n` on **Water7**. Water7 is on the same segment as the server, so the relay is not involved.
   - If Water7 receives an IP address, the server is working and the problem is in the relay path.
   - If Kea does not display DISCOVER, make sure `eth0` EniesLobby benar-benar memiliki `10.40.2.2` (`ip a`) and that Water7 is connected to the same switch.
2. **Check the relay.** On **Foosha**, check `ip a` (`eth1` must memiliki `10.40.1.1`), `cat /proc/sys/net/ipv4/ip_forward` (must `1`), and `ps | grep dhcp-helper`. Run the relay in the foreground (`-n`) to see error messages.
3. **Observe the packets.** On Foosha, run `apk add tcpdump`, then run the following commands when a client requests an IP address:
```sh
tcpdump -ni eth1 port 67 or port 68
tcpdump -ni eth2 port 67 or port 68
```
 
You should see DISCOVER on `eth1`, the request forwarded to `10.40.2.2` on `eth2`, then the OFFER returning on `eth2` and then on `eth1`. The point where the trace stops indicates which part is having a problem.
 
4. **Check the subnet match.** If the request reaches Kea but receives no response, make sure there is a `subnet4` block covering the Foosha address on the interface facing the client (`10.40.1.1` is within `10.40.1.0/24`).
5. **Check the return route.** EniesLobby must have a default route through `10.40.2.1` (`ip route`), otherwise replies to clients through the relay will be lost.
6. **If `-i eth1` does not cause replies to reach the client**, try running the relay while excluding the NAT interface: `dhcp-helper -n -s 10.40.2.2 -e eth0`. As a result, Water7 requests on `eth2` will also be forwarded to the server, so the server may see duplicate requests. This is harmless in this lab.
## Practice Questions
 
1. Create a DHCP configuration so that Loguetown and Alabasta receive IPs in the ranges `10.40.1.69 - 10.40.1.70` and `10.40.1.200 - 10.40.1.225` with the following conditions: every 2 minutes, the client's IP changes along with its DNS. However, the client must still be able to access the internet at all times.
   *Hint: a subnet can have more than one entry in `pools`, and the lease duration is configured with `valid-lifetime` (in seconds).*
## References
 
- <https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html>
- <https://www.isc.org/kea/>
- <https://thekelleys.org.uk/dhcp-helper/>
- <https://busybox.net/downloads/BusyBox.html#udhcpc>
- <http://www.tcpipguide.com/free/t_DHCPGeneralOperationandClientFiniteStateMachine.htm>
# _Yeay, Tamat. Jempol from NabilPolres 👍_
