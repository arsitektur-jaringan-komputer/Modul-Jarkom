GNS3 Introductory Module
===============

- [GNS3 Introductory Module](#gns3-introductory-module)
  - [what is GNS3?](#what-is-gns3)
  - [GNS3 Installation](#gns3-installation)
    - [Import Image on VirtualBox](#import-image-on-virtualbox)
    - [Import Image on VMWare](#import-image-on-vmware)
    - [Insert Ubuntu Image into GNS3](#insert-ubuntu-image-into-gns3)
  - [GNS3 Usage](#gns3-usage)
    - [Setup IP](#setup-ip)
      - [Prefix IP Distribution](#prefix-ip-distribution)
      - [Setup IP in Node](#setup-ip-in-node)
    - [Internet access of a Node](#internet-access-of-a-node)
    - [Making Topology](#making-topology)
  - [Terms](#terms)
  - [Warnings, Advice, Tips and Tricks](#warnings-advice-tips-and-tricks)
  - [Troubleshooting](#troubleshooting)
  - [References](#references)

## what is GNS3?
**GNS3 (Graphical Network Simulator-3)** is a tool that helps you to be able to run a simulation from a small topology consisting of only a few tools on your computer to a topology that has many tools hosted on several servers.

## GNS3 Installation
### Import Image on VirtualBox
1. Installing VirtualBox
Please download from [following link](https://www.oracle.com/virtualization/technologies/vm/downloads/virtualbox-downloads.html)

2. Download Image VM GNS3
Please download from [following link](https://github.com/GNS3/gns3-gui/releases/download/v2.2.19/GNS3.VM.VirtualBox.2.2.19.zip). After that, extract it.

3. Import .ova file to VirtualBox

![import-ova](images/import-ova.jpg)

![import-ova-2](images/import-ova-2.jpg)

4.  Creating a new host network adapter
  - Select File Menu -> Host Network Manager <br/>
![new-host-network-adapter](images/new-host-network-adapter-1.jpg)
  - Click Create <br/>
![new-host-network-adapter-2](images/new-host-network-adapter-2.jpg)
  - Then set the IPv4 Address to `192.168.0.1`, and the IPv4 Network Mask to `255.255.255.0` then click apply
![new-host-network-adapter-4](images/new-host-network-adapter-4.jpg)
![new-host-network-adapter-5](images/new-host-network-adapter-5.jpg)

5. Change Network Adapter in VM
  - Go to Settings -> Network
  - Change Adapter 1 to Host-only Adapter and match it with the previously created network host
![setting-network-vm-1](images/setting-network-vm-3.jpg)
  - And change Adapter 2 to NAT <br/>
![setting-network-vm-3](images/setting-network-vm-2.jpg)
  - Then click OK

6.  Run the VM
  - Then the VM should be able to display this
![vm](images/new-vm-1.png)
  - Then open the address with the caption "To launch the Web-UI" in the browser
![vm-2](images/vm-2.jpg)

After that please proceed to import the Ubuntu image into GNS3 [here](#insert-ubuntu-image-into-gns3)


### Import Image on VMWare
1. Install VMWare
Please download from [VMware Workstation 17](https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html).

2. Download Image VM GNS3
Please download from [GNS3 VM 2.2.42](https://github.com/GNS3/gns3-gui/releases/download/v2.2.42/GNS3.VM.VMware.Workstation.2.2.42.zip). After that, just extract.

3. Import the .ova file into VMWare and name the VM.

![import-ova](images/insert-image-vmware-1.png)

![import-ova-2](images/insert-image-vmware-2.png)

![import-ova-3](images/insert-image-vmware-3.png)

4. Adjust VMWare settings by clicking `Edit virtual machine settings`.
- Make sure the Network settings are correct.

![settingan-vmware-1](images/settingan-vmware-1.png)

- If there is an error `Virtualized ... Not Supported on Platform` when the vm is running, try disabling virtualization in the processor settings

![settingan-vmware-2](images/settingan-vmware-2.png)

5.  Run the VM
  - Then the VM should be able to display this
![vm](images/new-vm-2.png)
  - Then open the address with the caption "To launch the Web-UI" in the browser
![vm-2](images/new-vm-vmware-2.png)

After that please continue to import the Ubuntu image into GNS3 [here](#insert-ubuntu-image-into-gns3)

### Insert Ubuntu Image into GNS3

1. Import ubuntu image
  - Click `Go to preferences`
  - Click `Docker`
  - Click `Add Docker container template`
  - `Server type` choose `Run this Docker container locally`
  - Click `Docker Virtual Machine`, choose `New image` fill `danielcristh0/ubuntu-bionic:1.1` in Image name<br>
![insert-image-1](images/insert-imaget-2.jpg)
  - Click `Container name` fill `ubuntu-1` as container name
  - Click `Network adapters` and enter the number 4
  - Leave the `Start command` blank.
  - Then click `Add template` button on the bottom.

2. Try the imported image
  - Click `Servers` on upper left
  - Click `local`
  - Click `Add blank project`
  - Enter the project name (any name)
  - Click `Add project`
  - Click `Add a node` button on the left <br/>
![test-image-1](images/test-image-1.jpg)
  - Then drag `ubuntu-1` to an empty area on the page
  - Wait until loading is complete
  - If successful will display a display similar to this
![test-image-2](images/test-image-2.jpg)
  - We can start by right-clicking on node and click `Start` <br/>
![test-image-3](images/test-image-3.jpg)

3. Access the node
  - Can be done with `Web console` <br/>
![akses-node-1](images/akses-node-1.jpg)
  - This can be done using the command `telnet [VM IP] [Port node]` according to the one on the right, if you use the example in the picture, the command is `telnet 192.168.0.16 5000`
![akses-node-2](images/akses-node-2.jpg)
  - If using telnet, be careful if you want to exit the node. Use `Ctrl + ]` then type quit to exit the node.
  - If the command prompt doesn't come out, you can click enter many times until it comes out

## GNS3 Usage

### Setup IP
In computer network practicum, you will often do the setting for the IP of the node used. Then to distinguish the network ip of each group, the initial 2 octets (IP Prefix) of the IP used have been determined as below.

#### Prefix IP Distribution

**Class A**
Group | Prefix IP |
---------|------------ |
A01 | 192.169 |
A02 | 10.0 |
A03 | 192.170 |
A04 | 10.1 |
A05 | 192.171 |
A06 | 10.2 |
A07 | 192.172 |
A08 | 10.3 |

**Class B**
Group | Prefix IP |
---------|------------ |
B01 | 192.173 |
B02 | 10.4 |
B03 | 192.174 |
B04 | 10.5 |
B05 | 192.175 |
B06 | 10.6 |
B07 | 192.176 |
B08 | 10.7 |
B09 | 192.177 |
B10 | 10.8 |
B11 | 192.178 |
B12 | 10.9 |
B13 | 192.179 |

**Class C**
Group | Prefix IP |
---------|------------ |
C01 | 10.10 |
C02 | 192.180 |
C03 | 10.11 |
C04 | 192.181 |
C05 | 10.12 |
C06 | 192.182 |
C07 | 10.13 |
C08 | 192.183 |
C09 | 10.14 |
C10 | 192.184 |
C11 | 10.15 |

**Class D**
Group | Prefix IP |
---------|------------ |
D01 | 192.185 |
D02 | 10.16 |
D03 | 192.186 |
D04 | 10.17 |
D05 | 192.187 |
D06 | 10.18 |
D07 | 192.188 |
D08 | 10.19 |
D09 | 192.189 |
D10 | 10.20 |
D11 | 192.190 |
D12 | 10.21 |
D13 | 192.191 |
D14 | 192.192 |

**Class E**
Group | Prefix IP |
---------|------------ |
E01 | 10.22 |
E02 | 192.193 |
E03 | 10.23 |
E04 | 192.194 |
E05 | 10.24 |
E06 | 192.195 |
E07 | 10.25 |
E08 | 192.196 |
E09 | 10.26 |
E10 | 192.197 |
E11 | 10.27 |
E12 | 192.198 |
E13 | 10.28 |
E14 | 192.199 |

**Class F**
Group | Prefix IP |
---------|-----------|
F01 | 10.29 |
F02 | 192.200 |
F03 | 10.30 |
F04 | 192.201 |
F05 | 10.31 |
F06 | 192.202 |
F07 | 10.32 |
F08 | 192.203 |
F09 | 10.33 |
F10 | 192.204 |
F11 | 10.34 |
F12 | 192.205 |
F13 | 10.35 |
F14 | 192.206 |

**Class IUP**
Group | Prefix IP |
---------|------------ |
I01 | 10.36 |
I02 | 192.207 |
I02 | 10.37 |
I03 | 192.208 |
I04 | 10.38 |
I05 | 192.209 |
I06 | 10.39 |
I07 | 192.210 |

**Class IT A**
Group | Prefix IP |
---------|------------ |
ITA01 | 10.40 |
ITA02 | 192.211 |
ITA03 | 10.41 |
ITA04 | 192.212 |
ITA05 | 10.42 |
ITA06 | 192.212 |
ITA07 | 10.43 |
ITA08 | 192.213 |
ITA09 | 10.44 |
ITA10 | 192.214 |

**Class IT B**
Group | PREFIX IP |
---------|-----------|
ITB01 | 10.45 |
ITB02 | 192.215 |
ITB03 | 10.46 |
ITB04 | 192.216 |
ITB05 | 10.47 |
ITB06 | 192.217 |
ITB07 | 10.48 |
ITB08 | 192.218 |
ITB09 | 10.49 |
ITB10 | 192.219 |

If there is a command using IP `[Prefix IP].1.2` then example if I am group A2 the IP is `10.0.1.2`

#### Setup IP in Node

1. Right click on the node, go to `Configure`
2. In the `General settings` menu, look for the `Edit network configuration` button
3. There you can setup IP according to the interface used. An interface is something that is used to connect two devices

### Internet access of a Node
1. Open the Add a Node menu
2. Drag NAT to empty area <br/>
![using-internet-1](images/using-internet-1.jpg)
3. Use activate the `Add a Link` menu <br/>
![using-internet-2](images/using-internet-2.jpg)
4. Then click the node, select the interface `eth0`, and click the NAT node that was drawn earlier <br/>
![using-internet-3](images/using-internet-3.jpg)
5. Then configure the IP of the ubuntu node
  - Look for 2 lines like this
  ```
  # auto eth0
  # iface eth0 inet dhcp
  ```
  - Uncomment the two lines, then save
  ```
  auto eth0
  iface eth0 inet dhcp
  ```
6. Start node
7. Access the console from node, and try to ping google, if it works then your settings are correct
![using-internet-4](images/using-internet-4.jpg)
8. This node will be used later as a router for this module, rename this node to `Foosha` with the `Change hostname` feature on the node, and also change the symbol to the router symbol with the `Change symbol` feature

### Making Topology
1. Add some ethernet switch nodes and ubuntu nodes, then make the connection between the nodes and the names of the nodes to like in the image <br/>
![create-topology-1](images/create-topology-1.jpg)
2. Gunakan fitur `Change hostname` untuk merubah nama-nama dari node
3. Then we set the network of each node with the `Edit network configuration` feature as shown [here](#setup-ip-in-node) before, we can delete all the settings and fill in the settings below
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
**Explanation of Understanding**
- **Gateway**: The path on the network that data packets must pass to enter another network.

4. Restart all nodes
5. Check all ubuntu nodes whether they have the appropriate ip with the `ip a` command. Here is an example for `Foosha` node with IP Prefix `10.40`, adjust it to your respective group IP Prefix
![create-topology-2](images/create-topology-2.jpg)
6. The topology that has been created can run locally, but we can't access the outgoing network yet. Then we need to do a few things.
- Type **`iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s [IP Prefix].0.0/16`** on router `Foosha`
**Explanation:**
  - **iptables:** iptables is a tool in the Linux operating system that functions as a filter on data traffic. With this iptables we will manage all traffic on the computer, both incoming, outgoing, and or just passing through traffic on our computer. Further explanation will be discussed in Module 5.
  - **NAT (Network Address Translation):** A network address interpretation method that is used to connect more than one computer to the internet network using one IP address.
  - **Masquerade:** Used to disguise packets, for example replacing the sender's address with the router's address.
  - **-s (Source Address):** Specifications on source. The address can be a network name, host name, or IP address.
- Type command `cat /etc/resolv.conf` in `Foosha` <br/>
![create-topology-3](images/create-topology-3.jpg)
- Remember that IP because it is DNS IP, then type this command in another ubuntu node `echo nameserver [DNS IP] > /etc/resolv.conf`. In the example case, the command is `echo nameserver 192.168.122.1 > /etc/resolv.conf`.
- All nodes should now be able to ping google, which means they are connected to the internet

## Terms
- Practician **only** allowed to use docker image `kuuhaku86/gns3-ubuntu`

## Warnings, Advice, Tips and Tricks
- What's installed on node **is not persistent**, meaning when you work on the project again you need to re-install the app
- So, **always** save the config on the node to the `/root` directory before exiting the project
- You can enter the commands you want to always run on that node into the `/root/.bashrc` file at the very bottom. (Example: iptables command and echo nameserver earlier)<br>
![tips-trik-1](images/tips-trik-1.jpg)
- You can export a project if you are working as a team by going to the `Project settings` -> `Export portable project` menu.
![tips-trik-2](images/tips-trik-2.jpg)
- If working using a VM on your own local. You can prevent the loss of applications or config files by turning off the VM in save state mode.
- Take advantage of bash scripting to install the necessary applications so you don't have to enter commands one by one, then save to `/root`.
## Troubleshooting
- Something you used to do but suddenly couldn't? Try turning off the VM first and then turning it back on. Still not able? Try another way to install GNS3 before asking the assistant.
- Can't install in one method? Try another install method first before asking the assistant.


## References
- https://docs.gns3.com/docs/
