# Preliminaries
1. The following is the network topology used in the 4th module
## Topology on CPT
![Gambar](assets/topologicisco.png)
## Topology on GNS3
![Gambar](assets/topologigns3.png)
- Please follow the guide to make GNS3 on [GNS3 Introduction Module](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/tree/master/Modul-GNS3)
- For the manufacture of the topology on GNS3, switches are also made between routers.
- Naming For GNS3 Topology:  
  - San Faldo (100 Host) 
  - Merveille (50 Host) 
  - Rakesh (20 Host) 
  - Enies Lobby (10 Host) 
2. Install the latest (_latest_) version of *Cisco Packet Tracer*, downloadable at https://www.netacad.com/resources/lab-downloads
     - Step 1: Download the application according to the operating system used
     - Step 2: Create a netacad account, click the login button, then click the sign up button
    - Step 3: Install the application
    - Step 4: Open the application, then login with Skills For All **(The Green One)** using the account you created earlier

Translated with DeepL.com (free version)

# SUBNETTING AND ROUTING

-   [A. INTRODUCTION](#a-introduction)
    -   [Term](#Term)
    -   [IP Address](#ip-address)
    -   [Subnet](#subnet)
    -   [Network ID, Broadcast Address, dan Available Hosts](#network-id-broadcast-address-dan-available-hosts)
        -   [Network ID](#network-id)
        -   [Broadcast Address](#broadcast-address)
        -   [Available Hosts](#available-hosts)
    -   [Public IP and Private IP](#public-ip-and-private-ip)
-   [B. SUBNETTING](#b-subnetting)
    -   [Definition](#definition)
    -   [Subnet Calculation](#subnet-calculation)
        -   [A. Classful](#a-classful)
        -   [B. Classless](#b-classless)
            -   [1. VLSM (Variable Length Subnet Masking)](#vlsm-(variable-length-subnet-masking))
            -   [2. CIDR (Classless Inter Domain Routing)](#2-cidr-(classless-inter-domain-routing))
-   [C. ROUTING](#c-routing)
    -   [Definition](#definition)
    -   [Practice](#practice)
        -   [1) Creating a Topology](#1-make-topology)
        -   [2) Subnetting](#2-subnetting)
        -   [3) Routing](#3-routing)
        -   [4) Testing](#4-testing)
-   [EXERCISE!](#-exercise!)

## A. Introduction



### Term

| Terms | Explanation |
|--|--|
| iface | Called as the network interface, the interface that connects the 2 layer protocols. Each interface has a different name  |
| eth0 | One of the interface names used to connect to a subnet |
| address | A unique IP address for computers on a network |
| netmask | A combination of 32-bit numbers that functions to divide IP into subnets and determine the range of IP addresses on the subnet that can be used |
| gateway | The IP address that is the exit to another subnet, usually the IP address of the nearest router |

**Why Need Subnetting?**

For example, Indonesian territory needs to be divided into small parts (provinces, cities, and so on). The goal is to make it easier for the government to regulate policies according to the conditions of their respective regions. This also happens on the internet network. The network includes all connections between computers connected to the internet. Benefits of subnetting:

-   Improve routing efficiency
-   Can set own policies for network security
-   Reduced broadcast domain size

**Why Need Routing?**

For example, when you want to deliver a package, it is necessary to include the destination address. Then you send it to the post office, then the post office will send the package to the intended address. In order for the package to arrive at the correct destination, Mr. Pos who sent the package needs to know the route to reach the destination of the package, the process is called _**routing**_. That is, notifying the route of the trip to Mr. Pos to reach the destination address of the package he delivered.

### IP Address

IP Address (Version 4)

-   An IP address is a unique address assigned to a computer connected to a network.
-   The IP address consists of 32 binary bits which in writing are converted to decimal numbers.
-   The IP address (which is 32 bits long) is divided into 4 octets (each octet contains 8 bits) separated by a period.

### Subnet

![Gambar](assets/1.png)


### Network ID, Broadcast Address, dan Available Hosts

If a PC has the address 10.151.36.5/24, then the information that can be extracted from that IP is:

1.  IP Address
2.  Netmask
3.  Network ID (NID) : An IP address that identifies an area network/subnet
4.  Broadcast Address : An IP address that plays a role for sending broadcast messages in a network / subnet
5.  Available Hosts: Range of IP addresses that can be used in a network/subnet

Example scenario: Find the Network ID (NID), Broadcast Address, and IP address range of an address 10.151.36.5/24!

Solution: The provisional information obtained from 10,151.36.5/24 is

```
    1. IP : 10.151.36.5
    2. Netmask : 255.255.255.0 (/24)
    3. Network ID?
    4. Broadcast Address?
    5. Available Host?
```

The following will explain how to find NID, Broadcast Address, and Available Host:

#### Network ID

Searching Network ID (NID)

![Gambar](assets/2.PNG)

#### Broadcast Address

Searching Broadcast Address

![Gambar](assets/3.PNG)

#### Available Hosts

Searching IP address range

![Gambar](assets/4.PNG)

### Public IP and Private IP

IP addresses are divided into 2 types, namely:

-   Public IP = IP address used in the global network of the Internet, its characteristic IP address can be accessed via the Internet directly.
-   Private IP = IP address in use (recognized) and only accessible by local network.

Private IP Range :

-   10.0.0.0/8 (Class A)
-   172.16.0.0/12, 172.31.0.0/12 (Class B)
-   192.168.0.0/16 (Class C)

The Public IP range is in addition to the Private IP range above.

## B. SUBNETTING

### Definition

**Subnet** is a sub-network of a larger network. With the subnet, we can do a better management of a network.

**The main goal** we learn about subnetting is **the division of IP addresses for certain needs**. For example, in the Informatics Department building where there are several laboratories, and each laboratory has more than 1 computer that must be configured in such a way that they can communicate with each other and access the internet.

From this example, one of the most basic configurations in solving this problem emerges, namely the distribution of IP addresses for each laboratory in the Informatics Department building, such as:

1.  The LP laboratory has a network with a subnet **10.151.34.0/24**
2.  AJK laboratory has a network with a subnet **10.151.36.0/24**

### Subnet Calculation

There are two known IP sharing methods in the network, namely Classful

#### A. Classful

IP distribution using this method is based on the class division of the IP address. Each subnet will be given a size or netmask that can accommodate the number of computers/hosts contained in the subnet. The following table shows the classes contained in the  _**Classful**_ method.

| Class | Netmask | Number of Hosts |
|--|--|--|
| Class A | /8 | 16777216 |
| Class B | /16 | 65536 |
| Class C | /24 | 256 |

An example of implementing IP address sharing with the _**Classful**_ method is as follows.

![Gambar](assets/topologicisco.png)

Suppose we have a network topology like the image above. Then, determine the number of subnets in the topology.

![Gambar](assets/classful.png)

There are 8 subnets in the topology. By using the classful technique, each subnet will have a netmask of /24 because all subnets have a number of hosts below 256. So the possible IP divisions for the above topology are as follows.

![Gambar](assets/8.PNG)

#### B. Classless

##### 1. VLSM (Variable Length Subnet Masking)

The main point of using VLSM techniques is to streamline IP sharing in the network. The netmask size is adjusted to the number of computers/hosts that require an IP address.

> So, in the **VLSM** technique, the subnet mask (netmask) will be given according to the number of IP addresses needed for the subnet.

As an example of its implementation, we will use a topology such as the _**Classful**_ method.

**Step 1** - Determine the number of IP addresses required by each subnet and perform a  netmask _labelling_ based on the number of IPs required.

| Subnet | Number of IP | Netmask |
|--|--|--|
| A1 | 101 | /25 |
| A2 | 2 | /30 |
| A3 | 51 | /26 |
| A4 | 2 | /30 |
| A5 | 2 | /30 |
| A6 | 2 | /30 |
| A7 | 11 | /28 |
| A8 | 21 | /27 |
| **Total** | **192** | **/24** |


Based on the total IP and netmask required, we can use netmask **/24** to provide IP addressing on the subnet.

**Notes**

> Determination of the subnet mask (netmask) _**root**_ in the IP division is not only based on the **number** of IPs needed, but also how many netmasks are needed by the subnets in the topology. As in the example we are using, because the largest required netmask is **/25** and there is only 1 subnet that requires that subnet, therefore the IP division can be done starting from the netmask **/24**.

**Step 2** - The created large subnet has a NID **192.168.1.0** with a netmask **/24**. Calculate the IP share based on the NID and netmask using a tree as shown below.

![Gambar](assets/9.png)

**Step 3** - Perform subnetting using the tree for IP distribution according to the needs of each existing subnet.

![Gambar](assets/10.png)

From the tree, we will get the IP division as follows.

![Gambar](assets/11.PNG)

##### 2. CIDR (Classless Inter Domain Routing)

Calculations on the CIDR technique are also based on the number of computers/hosts in the subnet. But how to get a large subnet is not the same as VLSM. The application of the CIDR technique can be done with the following steps.

**Step 1** - Determine the subnets in the topology and do a  netmask _labelling_ for each subnet. An example can be seen in the following image.

![Gambar](assets/cidr_1.png)

**Step 2** - Merge the lowest subnets in the topology. The bottommost means the subnet farthest from the internet (cloud image). So in the topology used this time, the subnets that can be combined are A1 with A2 and A7 with A8 subnets. The merged subnets will form a subnet larger than the smaller subnets in it.

![Gambar](assets/cidr_2.png)

**B1** subnet is the result of the merger of **A1** and **A2** subnets, **B2** subnet is the result of merging of **A7** and **A8** subnets.

> _**Why does subnet B1 have a netmask of /24? And subnet B2 has a netmask of /26?**_

Note the **A1** and **A2** subnets. The subnet **A1** has a netmask of /25, and the subnet **A2** has a netmask of /30. In **CIDR** the combined subnet will have a netmask that is **1 level above the largest subnet that is combined**. Based on the example above, A1 = /25 and A2 = /30, so if merged, it will become a **B1** subnet with a netmask **/24**. Likewise with the B2 subnet.

Then repeat these steps until it becomes a large subnet that includes 1 topology that we have.

![Gambar](assets/cidr_3.png)
![Gambar](assets/cidr_4_.jpg)
![Gambar](assets/cidr_5_.jpg)

**Step 3** - From the merging process that has been done, we got a large subnet with a netmask **/21**. This time can use NID **192.168.0.0**, netmask **255.255.248.0**.

**Step 4** - Calculate IP division by tree based on merged subnets that have been done.

![Gambar](assets/17.PNG)

> **Notes**

> **The difference** between a VLSM tree and a CIDR tree is that when a subnet is derived, the netmask that will be formed **is adjusted to the merging of subnets** that has been done previously. For example, from a large netmask of /21, in the VLSM technique it will be divided in half into /22 each. However, in the previous merger, /21 resulted from the merger of /22 and /24, the subnet formed had a netmask of /22 and /24.

**Step 5** - Based on the calculation, the IP distribution is obtained as follows.

![Gambar](assets/18.PNG)

If you use CIDR, the netmask formed will be larger than using VLSM. However, one of the **advantages** of the **CIDR** technique is that when a new subnet is added to the topology, **no need to re-compute** because there is likely to be an unused IP interval (_range_). In addition, the CIDR technique also streamlines routing because generally the routing table is simpler than the VLSM technique.

## C. ROUTING

### Definition

After knowing how to _**Subnetting**_ a network and IP sharing methods, there is one other thing that needs to be known, namely _**Routing**_.

In the development of the network world, there are many routing protocols that can facilitate network administrators because they can update their routing tables automatically, the technique is called _**Dynamic Routing**_. Some well-known dynamic routing protocols include RIP, RIP version 2, EIGRP, and OSPF. These protocols are not studied in this module, but can be studied further in the TAJ course in semester 7 (odd).

The routing discussed is _**Static Routing**_, which requires the network administrator to add/notify a new route (_route_) into the routing table when there are additional subnets in the network.

The concept of _static routing_ is simple, register the existing NID and netmask and specify the gateway to go to the subnet. To try the static routing technique, we will use the **Cisco Packet Tracer** application.

### Practice

Open the Cisco Packet Tracer application, we will create a new topology.

#### 1) Creating a Topology

![Gambar](assets/topologicisco.png)

Please create a topology using **Cisco Packet Tracer**. To add a Router, Switch, and PC can be done by _drag and drop_ in the menu. In this practical, adjust the _device_ with the selection with the red box in the image below

-   to add Cloud

![Gambar](assets/20.png)

-   to add Router

![Gambar](assets/21.png)

-   to add Switch

![Gambar](assets/22.png)

-   to add PC

![Gambar](assets/23.png)

-   to add Cable

![Gambar](assets/24.png)

-   if there is a warning (_alert_) when connecting the cable between devices, add a port on the router first.

![Gambar](assets/PortIns.png)

In GNS3, create the topology as taught in [GNS3 Introduction Module](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/tree/master/Modul-GNS3) with **note** every _device_ to be connected **must** be connected using _**switch**_.


#### 2) Subnetting

This practice will apply the routing method for the _subnetting_ **VLSM** technique that we have done previously.

![Gambar](assets/classful.png)

![Gambar](assets/27.png)

Set the IP for each **interface** that is on each _device_ according to the subnet division in the **VLSM** tree.

On GNS3, go to `Configure > Edit Network Configuration` to set the interface on each device.

In CPT, the interface can be set in the **Config** menu > **INTERFACE** > **“interface name”** (example: FastEthernet0/0). Fill in the IP address and subnet mask of the subnet interface. Here's an example to set the IP on the subnet **A4**.

> To see the port direction, you can hover the device while in *logic view*, or you can always activate it in **Options** > **Preferences** > **Always Show Port Labels in Logical Workspace**

Set the IP on the Foosha interface pointing to Pucci with **192.168.1.5**.

![Gambar](assets/fooshatopucci.png)

Set the IP on the Pucci interface pointing to Foosha with **192.168.1.6**.

![Gambar](assets/puccitofoshaa.png)

Next set the IP on the A3 subnet. Set the IP on the Pucci interface pointing to _client_ with **192.168.1.65**.

![Gambar](assets/puccitoclient.png)

Set the IP on _client_ by:

-   Login to _client_
-   Select the Desktop tab
-   Select IP Configuration

![Gambar](assets/hostdesktop.png)

![Gambar](assets/hostipconfig.png)

Do the same thing to set the IP address of each _**interface**_ on the device in the topology. When finished, do the next step, namely _** Routing**_ so that the topology can function properly.

#### 3) Routing

In CPT, _**Routing**_ can be done on the **Config** menu > **Routing** > **Static** on the **Router** device. Then fill in **Static Routes** as shown below on Foosha and press the **Add** button

![Gambar](assets/routingfoosha.png)

In _static routing_ also required _**default routing**_ so that the router can send packets according to the destination. Default routing is required for routers that are under the main router (internet-connected router), for example Pucci

![Gambar](assets/routingpucci.png)

_**Information**_ :

1.  Network 192.168.1.64 is the Network ID to be connected
2.  Mask 255.255.255.192 is the netmask of subnet A3
3.  Next Hop 192.168.1.65 (called **gateway**), is the destination IP when you want to go to subnet point 1, namely the interface on Pucci that leads to Foosha

In **GNS3**, _routing_ is performed on the _**router**_ device with the command:

```
route add -net <NID subnet> netmask <netmask> gw <IP gateway>

```

Then see the  _routing_ results with the command:

```
route -n

```

So now, (GNS3 name) and _host_ on (GNS3 name) are connected to each other. So that all subnets can be connected to each other, add the following static routing in GNS3 and CPT according to their respective syntax:

1.  On Foosha
    
    ```
     Network 192.168.1.128 Netmask 255.255.255.128 Next Hop 192.168.1.6
     Network 192.168.1.0 Netmask 255.255.255.252 Next Hop 192.168.1.6
     Network 192.168.1.12 Netmask 255.255.255.252 Next Hop 192.168.1.10
     Network 192.168.1.16 Netmask 255.255.255.240 Next Hop 192.168.1.10
     Network 192.168.1.32 Netmask 255.255.255.224 Next Hop 192.168.1.10
    ```
    
2.  On Pucci
    
    ```
     Network 192.168.1.128 Netmask 255.255.255.128 Next Hop 192.168.1.2    
    ```
    
3.  On Water7
    
    ```
     Network 0.0.0.0 Netmask 0.0.0.0 Next Hop 192.168.1.1    
    ```
    
4.  On Guanhao
    
    ```
     Network 0.0.0.0 Netmask 0.0.0.0 Next Hop 192.168.1.9
     Network 192.168.1.16 Netmask 255.255.255.240 Next Hop 192.168.1.14
     Network 192.168.1.32 Netmask 255.255.255.224 Next Hop 192.168.1.14    
    ```
    
5.  On Arabasta
    
    ```
     Network 0.0.0.0 Netmask 0.0.0.0 Next Hop 192.168.1.13    
    ```
    

**Conclusion** for doing _static routing_, is to adjusted to the existing NID list. The more NIDs in a topology, the more routes that need to be added to the router, so we need the right grouping technique (_**Subnetting**_) to simplify _**Routing**_.

#### 4) Testing

To test it can be done by pinging the client to the destination IP or using the button with the letter icon on the toolbar.

![Gambar](assets/35.PNG)

### Exercise!

![Gambar](assets/soal.png)

Implement the above subnetting and routing topology on Cisco Packet Tracer and GNS3 using different subnetting techniques! Example on Cisco Packet Tracer using CIDR, on GNS3 using VLSM or vice versa. (each subnet is represented by one client/computer only)