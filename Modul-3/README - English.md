# Computer Network Module 3

## Table of Contents

- [0. TCP vs UDP](#0-tcp-vs-udp)
  - [0.1 Definition of TCP vs UDP](#01-definition-of-tcp-vs-udp)
  - [0.2 TCP Protocol Three-way Handshake](#02-tcp-protocol-three-way-handshake)
  - [0.3 Sequence Number and ACK Number](#03-sequence-number-and-ack-number)
  - [0.4 Retransmission and Duplicate ACK](#04-retransmission-and-duplicate-ack)
  - [0.5 TCP Congestion Control](#05-tcp-congestion-control)
- [1. Network Analysis and Simulation Tools](#1-network-analysis-and-simulation-tools)
  - [1.0 Topology Setup](#10-topology-setup)
  - [1.1 iperf3 (Client and Server)](#11-iperf3-client-and-server)
  - [1.2 tcpdump](#12-tcpdump)
  - [1.3 Network Simulation with tc qdisc](#13-network-simulation-with-tc-qdisc)
    - [a. Basic `tc qdisc` Syntax](#a-basic-tc-qdisc-syntax)
    - [b. `tc qdisc add`](#b-tc-qdisc-add)
    - [c. `tc qdisc replace`](#c-tc-qdisc-replace)
    - [d. `tc qdisc del`](#d-tc-qdisc-del)
    - [e. `tc qdisc show`](#e-tc-qdisc-show)
  - [1.4 TCP Metrics and Congestion Control Algorithms](#14-tcp-metrics-and-congestion-control-algorithms)
  - [1.5 Wireshark and termshark](#15-wireshark-and-termshark)
- [2. Static Routing](#2-static-routing)
  - [2.1 OSI Model and TCP/IP Model](#21-osi-model-and-tcpip-model)
  - [2.2 Definition](#22-definition)
  - [2.3 Implementation](#23-implementation)
  - [2.4 Troubleshooting](#24-troubleshooting)
  - [2.5 References](#25-references)

## 0. TCP vs UDP

### 0.1 Definition of TCP vs UDP

<img width="1320" height="600" alt="image" src="https://github.com/user-attachments/assets/71194561-2487-404b-91eb-f891b371bf09" />


TCP and UDP can be likened to the process of transferring goods:

- **Transmission Control Protocol (TCP)** is a _connection-oriented_ _transport_ protocol. This means that before data is sent, both parties must first agree to establish a connection.

  Every packet sent is guaranteed to reach its destination. If a packet is lost along the way, for example due to network disruption, the packet will be resent from the beginning. TCP is widely used for file transfers/_downloads_ because of its _reliable_ nature.

- **User Datagram Protocol (UDP)** is a _connectionless_ _transport_ protocol. UDP sends data directly without establishing a connection, does not require confirmation from the destination _host_, and does not resend failed packets. As a result, UDP excels in data transfer speed and is widely used for _streaming_, _video games_, and so on.

### 0.2 TCP Protocol Three-way Handshake

As we know, TCP requires an agreement first when it is about to start a connection with another _host_. This agreement process is called the _three-way handshake_. This process ensures that both _hosts_ are ready to communicate and prevents packet loss, while also exchanging **Initial Sequence Numbers (ISN)**. The ISN is the initial sequence number that will be used to number the data being sent.

The following is the _three-way handshake_ process that occurs between _host_ 1 as the _client_ and _host_ 2 as the _server_:

![alt text](/Modul-3/images/2-3-way-handhsake.png)

1. The _client_ sends a packet with the `SYN` _flag_ to the _server_ to _request_ a connection, along with a random initial sequence number, for example `seq = m`.
2. The _server_ replies with the `SYN-ACK` _flag_ to accept the connection _request_. The _server_ sends its own initial sequence number (`seq = n`) while also confirming the `SYN` from the _client_ (`ack = m + 1`).
3. The _client_ confirms the `SYN` from the _server_ (`ack = n + 1`) and replies again with `ACK` to begin the packet transfer. After this stage, the connection status becomes _established_ and data can be sent.

### 0.3 Sequence Number and ACK Number

TCP treats data as a _byte stream_, where every _byte_ has its own number. There are two _fields_ in the TCP _header_ used to track these numbers, namely:

- _Sequence number_ (`seq`): the number of the first _byte_ of the data carried by that _segment_.
- _Acknowledgment number_ (`ack`): the number of the next _byte_ the receiver is waiting for. If the receiver sends `ack = N`, it means all _bytes_ before `N` have been received.

The relationship between `SEQ` and `ACK` can be written as follows:

```
ack = received seq + data length (len)
```

There is an exception to the formula above, namely that packets with the SYN or FIN flag are considered to carry 1 byte of data even though they do not actually carry any data (len = 0). Therefore, the sequence number after a SYN or FIN is still considered to increase by 1, as if len = 1.

For example, in the three-way handshake process in section [0.2](#02-tcp-protocol-three-way-handshake): the client sends a SYN with seq = m. Even though this SYN packet carries no data, the server still replies with ack = m + 1 and not ack = m, because the SYN itself is counted as 1 byte. The same applies to FIN when the connection is closed: if the sender sends a FIN with seq = x, then the ACK reply is ack = x + 1.

### 0.4 Retransmission and Duplicate ACK

When sending packets, there is a possibility that the packets will experience _packet loss_ due to internet connection problems and so on. In TCP, if a packet is lost, this can be detected in two ways, namely _Retransmission Timeout_ and _Duplicate ACK_.

- **Retransmission Timeout (RTO)**

  Every time it sends a _segment_, the _sender_ runs a _timer_. If the `ACK` for that _segment_ is not received before the _timer_ runs out, the _segment_ is considered lost and will be resent. The RTO value is calculated based on the _Round Trip Time_ (RTT), which is the time it takes for a packet to go and come back. The slower and more unstable the network, the larger the RTO value.

- **Fast Retransmit (Duplicate ACK)**

  Waiting for the _timer_ to run out certainly takes quite a long time. Therefore, TCP has another, faster mechanism. Suppose _segment_ `seq=101` is lost, but the _segments_ after it (`201`, `301`, `401`) are successfully received. Because _byte_ `101` has not been received, the receiver will keep replying with the same `ACK`, namely `ACK 101`. This repeatedly sent `ACK` is called a _duplicate ACK_ (dup `ACK`).

  When the _sender_ receives 3 _duplicate ACKs_, the _segment_ is considered lost and is immediately resent without waiting for the RTO to run out. This mechanism is called _fast retransmit_.

### 0.5 TCP Congestion Control

If every _sender_ sent data as fast as possible, the network would be flooded with packets and _congestion_ would occur. This congestion causes many packets to be lost and to have to be resent, making the network even more congested. To prevent this, TCP has a mechanism called _congestion control_.

_Congestion control_ works by regulating the value of the _congestion window_ or `cwnd`, which is the amount of data that may be sent without having to wait for an `ACK`. The larger the `cwnd`, the faster the data is sent. Besides `cwnd`, there is also the _slow start threshold_ or `ssthresh`, which is the limit that marks when `cwnd` should stop doubling and start growing slowly.

The `cwnd` and `ssthresh` values are regulated by a _congestion control_ algorithm, the most classic of which is **TCP Reno**. The TCP Reno algorithm works through the following four phases:

- **Slow start**: the `cwnd` value starts from a small value, then doubles every RTT (1, 2, 4, 8, and so on).
- **Congestion avoidance**: after `cwnd` reaches the `ssthresh` value, `cwnd` increases by 1 _segment_ every RTT.
- **Fast recovery**: occurs when the sender receives 3 dup `ACKs`. The `ssthresh` value is lowered to half of `cwnd`, then `cwnd` is set equal to the new `ssthresh` value and the process continues to the _congestion avoidance_ phase.
- **Timeout**: occurs when the RTO runs out. The `ssthresh` value is lowered to half of `cwnd`, then `cwnd` is reset to 1 and the process starts again from the _slow start_ phase.

Besides Reno, there are several other _congestion control_ algorithms provided by Linux:

| Algorithm | Explanation |
| --- | --- |
| Reno | The classic _congestion control_ algorithm. The `cwnd` value increases by 1 _segment_ every RTT and is halved when _packet loss_ occurs. |
| CUBIC | The Linux default algorithm. The increase in `cwnd` is calculated using a cubic function of the time since the last _packet loss_. When _packet loss_ occurs, `cwnd` is lowered to about 70% of its previous value. |
| BBR | An algorithm that does not depend on _packet loss_. BBR measures the maximum _bandwidth_ and minimum RTT, then adjusts the _sender_'s speed based on those measurements. |

## 1. Network Analysis and Simulation Tools

After understanding the theory above, we will try to observe the behavior of TCP and UDP directly. In this section, we will use the following _tools_.

| Tool | Function |
| --- | --- |
| `iperf3` | Measures the _throughput_ between two _nodes_ |
| `tcpdump` | Captures packets passing through an _interface_ |
| `tc qdisc` | Simulates network conditions, such as _delay_, _packet loss_, and _bandwidth_ limiting |
| `ip tcp_metrics` and `sysctl` | Configure TCP behavior in the _kernel_ |
| Wireshark / termshark | Analyze packet _capture_ results |

### 1.0 Topology Setup

Create the following topology in GNS3 using the **netics-pc** _node_.

![Topologi Modul 3](images//3-topology-1.png)

<!-- TODO-SCREENSHOT: Loguetown - Foosha - Alabasta + NAT topology in GNS3 (new netics-pc), with interface labels shown -->

Then, fill in the _network configuration_ on each _node_ as follows. Adjust `[Prefix IP]` to your own respective IP Prefix.

- **Foosha** (_router_)

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

- **Loguetown** (_client_)

  ```
  auto eth0
  iface eth0 inet static
  	address [Prefix IP].1.2
  	netmask 255.255.255.0
  	gateway [Prefix IP].1.1
  ```

- **Alabasta** (_server_)

  ```
  auto eth0
  iface eth0 inet static
  	address [Prefix IP].2.2
  	netmask 255.255.255.0
  	gateway [Prefix IP].2.1
  ```

After all _nodes_ are running, enable _IP forwarding_ and NAT on **Foosha** so that Loguetown and Alabasta can connect to each other and access the internet.

```sh
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s [Prefix IP].0.0/16
cat /etc/resolv.conf
```

Then, on **Loguetown** and **Alabasta**, fill in the _nameserver_ with the DNS IP found in Foosha's `/etc/resolv.conf`.

```sh
echo nameserver [IP DNS] > /etc/resolv.conf
```

The packages required for this section are `iperf3`, `tcpdump`, `iproute2`, `tshark`, and `termshark`. These packages can be checked using the _command_ below to see whether they are already available by default on the netics-pc _appliance_.

### 1.1 iperf3 (Client and Server)

`iperf3` is a _tool_ used to measure the _throughput_ or data transfer speed between two _nodes_. `iperf3` uses a _client-server_ architecture, where the _server_ waits for a connection, while the _client_ sends data for a few seconds.

```sh
command -v iperf3 tcpdump tc ip tshark termshark
```

#### Running the Server

Run the following command on Alabasta.

```sh
iperf3 -s
```

#### Running the Client

Run the following command on Loguetown.

```sh
iperf3 -c 10.40.2.2 -t 5
```

Result on the Alabasta _server_:  
![](/Modul-3/images/4-server-alabasta.png)

Result on the Loguetown _client_:  
![](/Modul-3/images/5-client-loguetown.png)

### 1.2 tcpdump

`tcpdump` is a _tool_ used to capture and display packets passing through an _interface_. Because all traffic between Loguetown and Alabasta passes through Foosha, we can run `tcpdump` on Foosha to see the communication between the two _nodes_ by observing the _three-way handshake_ process.

1. On Alabasta, run a simple TCP _server_ on _port_ 9999 using the `nc` (netcat) _command_.

   ```sh
   nc -l -p 9999
   ```

2. On Foosha, run `tcpdump` on the _interface_ connected to Alabasta.

   ```sh
   tcpdump -i eth2 -nn port 9999
   ```

3. On Loguetown, connect to Alabasta and then type a message.

   ```sh
   nc 10.40.2.2 9999
   hello from Loguetown
   ```

4. On Alabasta, the message from Loguetown will appear. Type the reply `hello from Alabasta`, then press `Ctrl+C` to close the connection.

The following is the `tcpdump` _output_ on Foosha.  
![](/Modul-3/images/6-foosha.png)

#### Commonly Used Options and Filters

| Option | Function |
| --- | --- |
| `-i <iface>` | The _interface_ to capture (`-i any` for all _interfaces_) |
| `-n` / `-nn` | Does not convert IPs to _host_ names (`-nn` also does not convert _ports_ to service names) |
| `-c <n>` | Stops after capturing n packets |
| `-w <file>` | Saves the _capture_ result to a `.pcap` _file_ |
| `-r <file>` | Reads a `.pcap` _file_ |
| `-s <byte>` | Only saves the first n _bytes_ of each packet |
| `-S` | Displays absolute _sequence numbers_ |
| `-v`, `-vv` | Displays more complete details |
| `-A` / `-X` | Displays packet contents in ASCII / hex and ASCII |

Filters can be written at the end of the command and can be combined using `and`, `or`, and `not`.

```sh
tcpdump -i eth2 -nn host 10.40.2.2
tcpdump -i eth2 -nn tcp port 5201
tcpdump -i eth2 -nn udp
tcpdump -i eth2 -nn icmp
tcpdump -i eth2 -nn 'tcp[tcpflags] & tcp-syn != 0'
tcpdump -i eth2 -nn -c 100 -w /root/iperf.pcap port 5201
```

### 1.3 Network Simulation with tc qdisc

A network can experience _delay_, limited _bandwidth_, and _packet loss_. To observe TCP behavior under these conditions, network conditions can be simulated with `tc` (_traffic control_).

`tc` works by attaching a _queueing discipline_ (qdisc) to an _interface_. A qdisc is a queueing rule that every packet goes through before leaving the _interface_. With a qdisc, packets can be delayed, dropped, or rate-limited.

In this module, we will use two types of qdisc, namely:

- **netem** (_network emulator_): to add _delay_, _jitter_, _packet loss_, duplication, corruption, and packet reordering.
- **tbf** (_token bucket filter_): to limit _bandwidth_.

#### a. Basic `tc qdisc` Syntax

```
tc qdisc <add|replace|change|del|show> dev <interface> root <qdisc type> <parameter>
```

- `dev <interface>`: the _interface_ to be configured, for example `eth2`.
- `root`: the qdisc is attached as the main qdisc on that _interface_.
- `<qdisc type>`: the type of qdisc used, for example `netem` or `tbf`.

#### b. `tc qdisc add`

`tc qdisc add` is used to attach a new qdisc to an _interface_. Before that, check the initial state of the _interface_ first.

```
foosha:~# tc qdisc show dev eth2
qdisc fq_codel 0: root refcnt 2 limit 10240p flows 1024 quantum 1514 target 5ms interval 100ms memory_limit 32Mb ecn drop_batch 64
```

The `fq_codel` above is the _default_ qdisc that is automatically attached even though it has never been _added_ manually. Before attaching the _delay_, first `ping` from Loguetown to Alabasta as a comparison.

```sh
ping -c 5 10.40.2.2
```

Next, on Foosha, attach a 100 ms _delay_ using netem.

```sh
tc qdisc add dev eth2 root netem delay 100ms
```

Repeat the same `ping` from Loguetown.

```sh
ping -c 5 10.40.2.2
```

![](/Modul-3/images/7-delay-100ms.png)

Several parameters can also be combined in one command.

```sh
# Foosha
tc qdisc add dev eth2 root netem delay 50ms 10ms loss 2%
```

![](/Modul-3/images/8-delay-part2.png)

To limit _bandwidth_, we can also use tbf.

```
foosha:~# tc qdisc add dev eth2 root tbf rate 20mbit burst 32kbit latency 400ms
foosha:~# tc qdisc show dev eth2
qdisc tbf 8001: root refcnt 3 rate 20Mbit burst 4Kb lat 400ms
```

- `rate`: the speed limit.
- `burst`: the amount of data that may be sent at once.
- `latency`: the maximum time a packet may wait in the queue before being dropped.

Run `iperf3` again from Loguetown as in section [1.1](#11-iperf3-client-and-server). The following is the `iperf3` result from Loguetown after the _bandwidth_ is limited to 20 Mbit/s.

#### c. `tc qdisc replace`

`tc qdisc replace` is used to replace a qdisc that is already attached. If no qdisc is attached yet, a new qdisc will be created.

```
foosha:~# tc qdisc replace dev eth2 root tbf rate 5mbit burst 32kbit latency 400ms
foosha:~# tc qdisc show dev eth2
qdisc tbf 8001: root refcnt 3 rate 5Mbit burst 4Kb lat 400ms
```

Besides `replace`, there is also `tc qdisc change`, which is used to change the parameters of a qdisc that is already attached, for example from `delay 100ms` to `delay 200ms`. The `change` command will fail if no qdisc is attached yet. To change the qdisc type from tbf to netem, `replace` can be used.

#### d. `tc qdisc del`

`tc qdisc del` is used to delete the qdisc on an _interface_.

```
foosha:~# tc qdisc del dev eth2 root
foosha:~# tc qdisc show dev eth2
qdisc fq_codel 0: root refcnt 2 limit 10240p flows 1024 quantum 1514 target 5ms interval 100ms memory_limit 32Mb ecn drop_batch 64
```

After the qdisc is deleted, the _interface_ will return to its _default_ qdisc (`fq_codel`), rather than having no qdisc at all.

#### e. `tc qdisc show`

`tc qdisc show` is used to view the attached qdiscs.

```sh
tc qdisc show
tc qdisc show dev eth2
tc -s qdisc show dev eth2
```

### 1.4 TCP Metrics and Congestion Control Algorithms

There are two Linux _kernel_ settings that need attention, namely TCP metrics and the _congestion control_ algorithm.

#### `ip tcp_metrics` and `tcp_no_metrics_save`

Every time a TCP connection is closed, Linux stores some information about the destination _host_, such as RTT, `cwnd`, and `ssthresh`. This information will be used as initial values when creating a new connection to the same _host_. This feature is useful for speeding up connections, but it can affect experiment results because the results of the second test will be influenced by the first test.

The stored information can be viewed using the following command on Loguetown.

```
loguetown:~# ip tcp_metrics show
10.40.2.2 age 0.004sec cwnd 1155 reordering 300 rtt 16443us rttvar 29586us source 10.40.1.2
```

To delete all stored information, use the following command.

```
loguetown:~# ip tcp_metrics flush
loguetown:~# ip tcp_metrics show
loguetown:~#
```

Then, disable TCP metrics saving so that the information is not stored again.

```
loguetown:~# sysctl -w net.ipv4.tcp_no_metrics_save=1
net.ipv4.tcp_no_metrics_save = 1
```

After the settings above are applied, `ip tcp_metrics show` will remain empty even if `iperf3` is run again.

| Command | Function |
| --- | --- |
| `ip tcp_metrics show` | Displays the stored TCP metrics |
| `ip tcp_metrics flush` | Deletes all stored TCP metrics |
| `ip tcp_metrics delete <IP>` | Deletes the TCP metrics for a specific IP |
| `sysctl -w net.ipv4.tcp_no_metrics_save=1` | Disables TCP metrics saving (`0` to re-enable it) |

> Perform `flush` and set `tcp_no_metrics_save=1` on both the _client_ and _server_ before conducting experiments.

#### `sysctl net.ipv4.tcp_congestion_control`

The _congestion control_ algorithm in use can be viewed and changed using `sysctl`.

```
loguetown:~# sysctl net.ipv4.tcp_available_congestion_control
net.ipv4.tcp_available_congestion_control = reno bbr cubic
loguetown:~# sysctl net.ipv4.tcp_congestion_control
net.ipv4.tcp_congestion_control = cubic
loguetown:~# sysctl -w net.ipv4.tcp_congestion_control=reno
net.ipv4.tcp_congestion_control = reno
loguetown:~# sysctl -w net.ipv4.tcp_congestion_control=cubic
net.ipv4.tcp_congestion_control = cubic
```

- `tcp_available_congestion_control` displays the algorithms available in the _kernel_.
- `tcp_congestion_control` displays the algorithm currently in use.

The _congestion control_ algorithm runs on the sender side. In a regular `iperf3` test, the data sender is Loguetown, so the algorithm that needs to be changed is the one on Loguetown. Besides using `sysctl`, you can also use the `iperf3 -C reno` option for a single test.

> The available algorithms depend on the GNS3 VM _kernel_, because all netics-pc _nodes_ use the same _kernel_. If the message `sysctl: setting key "net.ipv4.tcp_congestion_control": Operation not permitted` appears, it means the algorithm is not included in `net.ipv4.tcp_allowed_congestion_control` on the _host kernel_.

### 1.5 Wireshark and termshark

#### Capturing Directly from a GNS3 Link

GNS3 can capture packets on a _link_ and open them directly in Wireshark on your computer. Make sure Wireshark is _installed_ on your computer.

1. Right-click on the _link_ between Foosha and Alabasta.
2. Select _Start capture_, then select the side of the _link_ you want to capture.
3. Wireshark will open and display the packets being _captured_.
4. To stop the _capture_, right-click on that _link_, then select _Stop capture_.

![](/Modul-3/images/10-capture-packets.png)

For the full tutorial, see the following video: [wireshark packet capture documentation](/Modul-3/images/12-capture-ws.mp4)

[![Alt text](https://github.com/user-attachments/assets/4f058e5a-6c89-4966-9b06-63dddb7df3ed)](https://github.com/user-attachments/assets/c377eba0-dfaf-4f8e-9987-69c3b0997a50)

References : 
- [Wireshark Download](https://www.wireshark.org/download.html)
- [Wireshark + GNS3 Integration](https://gns3.com/step-by-step-setup-wireshark-gns3-integration)

#### termshark

**termshark** is an application with a Wireshark-like interface that runs in the terminal. termshark requires `tshark`, the _command line_ version of Wireshark, which we have already _installed_ on Loguetown.

```sh
# capture packets
termshark -i eth0

# open a tcpdump result file
tcpdump -i eth0 -nn -w /root/iperf.pcap port 5201
termshark -r /root/iperf.pcap
```

The termshark display consists of three parts, namely the packet list, packet details, and packet contents in hex. Some basic keys in termshark are as follows.

| Key | Function |
| --- | --- |
| Filter field at the top + `Enter` | Applies a _display filter_ |
| `Tab` / arrow keys | Moves between parts and selects packets |
| `?` | Displays help |
| `q` | Quits |

#### Display Filter

_Display filters_ in Wireshark and termshark use the same format. The following are some _display filters_ that can be used in this module.

| Filter | Description |
| --- | --- |
| `ip.addr == 10.40.2.2` | Packets from or to 10.40.2.2 |
| `tcp.port == 5201` | iperf3 traffic |
| `udp` | UDP packets |
| `tcp.flags.syn == 1` | SYN and SYN-ACK packets |
| `tcp.flags.fin == 1` | FIN packets |
| `tcp.analysis.retransmission` | Resent _segments_ |
| `tcp.analysis.fast_retransmission` | _Retransmissions_ that occur due to _duplicate_ ACKs |
| `tcp.analysis.duplicate_ack` | _Duplicate ACK_ |
| `tcp.analysis.flags` | All TCP anomalies |

#### Example Analysis of Retransmission and Duplicate ACK

## 2. Static Routing

Now that we understand how computer networks around the world generally work, the devices used to support communication on the internet, the protocols they follow, and so on, we will move on to a concept that is just as important and that we will often encounter, namely **Routing**.

### 2.1 OSI Model and TCP/IP Model

In Module 2, we learned that network communication is divided into several _layers_. There are 2 commonly used models, namely the OSI Model, which consists of 7 layers, and the TCP/IP Model, which consists of 4 layers. In the TCP/IP Model, _Layer_ 5 to _Layer_ 7 are combined into the _Application Layer_, while _Layer_ 1 and _Layer_ 2 are combined into the _Network Access Layer_.

![OSI vs TCP/IP](/Modul-3/images/11-osi-vs-tcp.png)

The material in this module relates to the following two layers.

| Layer | Material |
| --- | --- |
| _Transport Layer_ (Layer 4) | TCP and UDP, _ports_, _three-way handshake_, and _congestion control_ |
| _Network Layer_ (Layer 3) | IP Address and _routing_ |

A _Router_ works at _Layer_ 3 and reads the destination IP of a packet, then determines where the packet should be forwarded.

### 2.2 Definition

If an IP Address can be likened to a house address, then now let's imagine we are in a housing complex, say complex A. In this complex, the residents follow the same house address rule, namely the letter A followed by a number. For example, your neighbor Mr. Hassan has the house address A-17, Mrs. Rumrowi has the house address A-32, and so on. As a local resident, you know them and know how to visit their houses without anyone else's help.

One day, you are given the task of delivering food to the house address B-03. However, you do not recognize this address because it does not begin with the letter A as usual. So, you contact the complex's post office at address A-01 (whose location you know) and ask for their help in delivering the food. As a post office, they have address data for the entire city, so they know where house B-01 is located and where to deliver the food. So, you simply go to A-01 and hand over the food, which has the destination B-01. The rest will be taken care of by the post office.

The concept of _routing_ is more or less the same as the illustration above. In essence, _routing_ is a process that determines the best path for sending a packet/data from one network to another. Generally, this is done by a _Router_, which is responsible for forwarding packets from one network segment to another. A _Router_ performs this path determination based on the data it has, namely the _Routing Table_, which contains information on how to reach a network segment, even one that looks far away.

Referring to the illustration above, you and all your neighbors can be regarded as _hosts_ and your complex as a _subnet_ (we will explore this in Module 4). Then, the post office can be regarded as a _Router_ and the address data for the whole city that they hold can be regarded as the _Routing Table_.

![image](../Modul-2/images/routing_id.png)

Based on how a _Router_ obtains information about its _Routing Table_, _Routing_ can be divided into 2 categories, namely **Static Routing** and **Dynamic Routing**. Dynamic Routing will be discussed briefly in Module 4, while Static Routing is what we will study in this module.

In Static Routing, a _network administrator_ (or team) is responsible for filling in the _Routing Table_ on every _Router_. Using the post office analogy, the government is responsible for informing all existing post offices about the other post offices and how a post office can contact other post offices or other housing complexes. This is quite simple when done on a network with a small number of _Routers_ and network segments, but becomes more difficult and tiring as the number and complexity of the network grow. Not only that, if there is a new network segment, all _Routers_ must be informed about it, which is certainly very inefficient and will consume a lot of time.

However, because we will use a simple topology that does not change much, with few network segments, Static Routing can make things easier for us because we will have full control over our topology. Next, we will try doing it in GNS3.

![image](../Modul-2/images/static_routing.webp)

### 2.3 Implementation

Of course, we will understand it more easily by directly implementing it. For that, we will use the following topology:

![image](../Modul-2/images/topologi.jpg)

Then, the IP Address allocation for this case is as follows:

```
# Complex A: 10.40.1.X
eth0 Water7: 10.40.1.1
EniesLobby: 10.40.1.2
Westalis: 10.40.1.3

# Left Street Complex: 10.40.2.X
eth1 Water7: 10.40.2.1
eth0 Dressrosa: 10.40.2.2

# Right Street Complex: 10.40.3.X
eth1 Dressrosa: 10.40.3.1
eth0 Foosha: 10.40.3.2

# Complex B: 10.40.4.X
eth1 Foosha: 10.40.4.1
Alabasta: 10.40.4.2

# Complex C: 10.40.5.X
eth2 Foosha: 10.40.5.1
Jipangu: 10.40.5.2
Loguetown: 10.40.5.3
```

For this case, set all _netmasks_ to `255.255.255.0` for now (further explanation is in Module 4). Then, for all _hosts_ (all _nodes_ except Water7, Dressrosa, and Foosha), set their _gateway_ to the IP Address of the connected _Router_. For example, EniesLobby and Water7 are connected on Water7's eth0, so the _gateway_ for both of them is `10.40.1.1`. Then, set the _gateways_ for the _routers_ as follows:

```
# leave the gateway empty for Water7's eth0 interface and Foosha's eth1 & eth2 interfaces
eth1 Water7: 10.40.2.2
eth0 Foosha: 10.40.3.1
# also leave Dressrosa's gateway empty for all interfaces
```

#### 2.3.1 Before Routing

Once you have finished the configuration, test connectivity by _pinging_ between _nodes_ within the same network segment (complex). For example, make sure **Westalis** can _ping_ **EniesLobby** and **Water7**, **Dressrosa** can _ping_ **Foosha**, and so on.

> Tip: There is no need to log in to every _node_. Just log in to **Water7** and **Foosha** and _ping_ all the devices connected to them, because in general _ping_ is symmetric (if _host_ A can _ping_ _host_ B, the reverse also holds) unless there is additional configuration such as a _Firewall_ or NAT.

Now, please try _pinging_ between complexes that are quite far apart, for example **Dressrosa** (`10.40.3.1`) to **Alabasta** (`10.40.4.2`). You should get _output_ like the following.

![image](../Modul-2/images/dressrosa_alabasta_before_v1.jpg)

or

![image](../Modul-2/images/dressrosa_alabasta_before_v2.jpg)

You may not get _output_ exactly like the above (it may even _hang_ when _pinging_). However, in essence the result is the same, namely that you cannot _ping_.

> If you _ping_ between complexes that are still close together and connected to the same _router_ (for example complex B and complex C), there is a possibility that _ping_ communication can still be carried out.

Therefore, we will tell the _router_ how to reach the other complexes.

#### 2.3.2 The Routing Process

The first way is quite simple, which is to only tell **Dressrosa** how to reach all network segments. For that, we will use the following command:

```
ip route add <DESTINATION SUBNET>/<NETMASK> via <GATEWAY>
```

Explanation:

- **DESTINATION SUBNET** contains the NID or the network segment to be reached. In our case, the first 3 octets contain the complex's IP and the last octet contains `0`. A more detailed explanation will be explored in Module 4.
- **NETMASK** for our case will simply be filled with `24`.
- **GATEWAY** contains the IP Address of the _router_ used to reach that network segment.

For example:

```
ip route add 10.40.5.0/24 via 10.40.3.2
```

When we run the command above on **Dressrosa**, it is as if we are telling it, "Hello Dressrosa, if there is a packet with a destination IP Address in complex C (`10.40.5.X`), then the way to reach it is by passing through `10.40.3.2` (which is **Foosha**)".

![image](../Modul-2/images/dressrosa_after.jpg)

Before running the command above, Dressrosa did not know how to reach complex C (`10.40.5.X`). Therefore, it said that the network could not be reached (`Network is unreachable`). After we told it, it now has the information on how to reach that network segment. So, it and the external devices directly connected to it (in this case, **Water7**) can contact addresses in that network segment.

![image](../Modul-2/images/water7_ok.jpg)

However, complex A still cannot _ping_ complex C. Although packets sent from complex A (`10.40.1.X`) can reach complex C (`10.40.5.X`) because all the _routers_ already know the way, they still do not know how to reach complex A for the replies. Therefore, we need to tell **Dressrosa** again how to reach complex A by running the following command:

```
ip route add 10.40.1.0/24 via 10.40.2.1
```

![image](../Modul-2/images/enieslobby_before_after.jpg)

As in the picture, at first **EniesLobby**, as a resident of complex A, could not contact complex C. After we ran the command above on **Dressrosa**, EniesLobby can _ping_ complex C.

> Do the same for complex B. Do you know the _command_ used and on which _node_?

#### 2.3.3 After Routing

Perhaps while doing the implementation, several questions arose in your mind, such as:

- _Why was only **Dressrosa** configured, when there are 3 routers?_
- _Does that mean **Water7** and **Foosha** know how to reach all of the existing complexes? How can that be?_
- _What will happen if a new complex is added, such as complex D at `10.40.6.X`?_

The last piece of the _puzzle_ that makes all of this happen and can answer your questions is the **Default Gateway**.

Simply put, a Default Gateway can be likened to the person you ask (following the initial illustration, the complex's post office) when you do not know the way. When there is a packet with an unfamiliar destination, instead of giving up and discarding it, we simply send that packet to the Default Gateway. This is what happened in the implementation above and why only **Dressrosa** was configured.

**Case Study: Ping from EniesLobby to Jipangu**

Run the _command_ below on **EniesLobby**:

```
mtr 10.40.5.2
```

![image](../Modul-2/images/mtr.jpg)

Through `mtr`, we can find out which _nodes_ the packet we send passes through. This command is similar to `traceroute`. In this case, we want to find out which path the packet takes from **EniesLobby** (`10.40.1.3`) to **Jipangu** (`10.40.5.2`). The explanation of the route flow is as follows:

1. First, because the destination IP Address (namely `10.40.5.2`) is not in the same network segment, **EniesLobby** does not know how to send it. However, because it has a Default Gateway, namely **Water7**, it simply sends the packet there (namely `10.40.1.1`).
2. The same thing happens to **Water7**. It actually does not know how to send this packet either, but because it also has a Default Gateway, namely **Dressrosa**, it will send it there (namely `10.40.2.2`).
3. Unlike EniesLobby and Water7, **Dressrosa** knows how to reach the network segment of this packet's destination. According to the data it has (or its _Routing Table_), to reach that packet it must send it to **Foosha**, namely `10.40.3.2`.
4. Finally, because **Foosha** is directly connected to **Jipangu**, the packet can be sent directly to the destination, namely `10.40.5.2`.

> If **Water7** and **Foosha** did not have a Default Gateway, then we would have to run the `ip route add` command to fill in their _Routing Tables_ just as we did on **Dressrosa**.

#### 2.3.4 Routing Table

It would be good to close with a brief explanation of the last component on our journey, namely the **Routing Table**.

A Routing Table is a data structure that stores information about how to reach a network segment. Usually, a Routing Table contains information about the destination network segment, its _next hop_ or _gateway_, the _network interface_ used, and additional information.

Let's look at the Routing Table on **Dressrosa** with:

```
ip route show
```

![image](../Modul-2/images/routing_table.jpg)

- `10.40.1.0/24 via 10.40.2.1 dev eth0`: To reach the network segment `10.40.1.0/24`, send the packet to `10.40.2.1` through the `eth0` _interface_.
- `10.40.2.0/24 dev eth0 proto kernel scope link src 10.40.2.2`: The network segment `10.40.2.0/24` is directly connected through the `eth0` _interface_. **Dressrosa**'s own IP on this connection is `10.40.2.2`.

> Can you translate the rest?

### 2.4 Troubleshooting

If you have configured the _router_ but still cannot _ping_, there is a possibility that your _router_ is not willing to forward packets (_packet forwarding_ is disabled).

To check, you can run:

```
cat /proc/sys/net/ipv4/ip_forward
```

`1` means _packet forwarding_ is active and `0` means it is inactive. To enable it, you can run:

```
sysctl -w net.ipv4.ip_forward=1
```

or by making sure `net.ipv4.ip_forward=1` is present (usually _commented_ out) in `/etc/sysctl.conf`. Restart with:

```
sysctl -p
```

### 2.5 References

- https://www.geeksforgeeks.org/computer-networks/open-systems-interconnection-model-osi/
- https://www.tutorialspoint.com/data_communication_computer_network/computer_network_models.htm
- https://www.geeksforgeeks.org/computer-networks/computer-network-models/
- https://www.lifewire.com/layers-of-the-osi-model-illustrated-818017
- https://www.avg.com/en/signal/tcp-vs-udp

1. [Web Server](Web%20server/README.md)
2. [DNS (Domain Name System)](DNS/README.md)
3. [Reverse Proxy](Reverse%20Proxy/README.md)
