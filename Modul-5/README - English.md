# FIREWALL

1. [Definition](#1-definition)
2. [Functions of Firewall](#2-functions-of-firewall)
3. [How Firewall works](#3-how-firewall-works)
4. [Types of Firewall](#4-types-of-firewall)
5. [IPTables](#5-iptables)

#

### 1. Definition
Firewall is a security system on a computer network that is used to protect a computer from several types of attacks from external computer based on pre determined security rules.

According to Wikipedia, Firewall is a wall of fire or a protective wall which is designed to prevent unwanted access from or into a network.

### 2. Functions of firewall
Firewall is needed because of security, among the considerations or the existence of firewall are:

- Data theft on internal network
- Accessing data by unauthorized person
- Denial of Service 

### 3. How Firewall works
![Illustration of firewall](img/ilustrasi.jpg) 

illustration on firewall (Source: https://id.wikipedia.org/wiki/Berkas:Ilustrasi-Firewall.png)

Firewall is a mechanism to protect the security of a computer in a network by allowing network traffic that is considered safe to pass through and preventing unsafe network traffic to pass through. The packet traffic regulation is in the form of filtering incoming and outgoing data packets on the network.

Data packets that are 'good' are allowed to pass through the network and packets that are considered 'bad' are not allowed to pass through the network. Firewall can be a software or hardware embedded software to filter data packets. Generally, a Firewall is implemented in a dedicated machine, which runs on the gateway between the local network (a subnet) and another network (subnet). Firewall is also generally used to control access to anyone who has access to a private network from outside parties.

Other ways for Firewall to protect an internal network, including:

- Reject and block incoming data packets from unwanted sources and destinations.
- Reject and filter data packets coming from the internal network to the internet. For example, when there are internet network users will access sites that are not safe.
- Reject and filter data packets based on unwanted content. For example, an integrated firewall in an antivirus will filter and prevent files that have been infected with viruses from entering the internal network.
- Report all network activity and firewall activity (log).

### 4. Types of Firewall
There are several types of firewall to protect a network, including :


1. __Packet-Filtering Firewall__ 

    __Packet-filtering Firewall__ is a type of firewall that checks and compares the source address of the packet passing with the rules or policies that have been registered in the filtering firewall. In this type of firewall, it will be set whether the data packet will be allowed to pass or reject it. At the OSI layer, this firewall works at the network layer.

    On Linux, the packet filtering firewall is embedded in the kernel (as a kernel module, or bundled into the kernel) and can be configured using IPTables which is a built-in application package in Linux. Data packet inspection rules or policies are based on information that can be captured from the packet header, including:

    - IP address of source and destination.
    - TCP/UDP port number of source and destination.
    - Type of ICMP message.

2. __Application Filter Firewall__ 

    This firewall works at the OSI application layer so that it can filter applications that are used to access the Internet. This type of firewall is generally a bit expensive because it is more complex.

3. __Proxy Firewall__ 

    The proxy server facility uses an intermediary (proxy) as a bridge between the LAN and WAN/Internet. Proxy servers generally function at the application layer, therefore they are often also called application firewalls.

    If __packet filter__ only functions to filter received packets without changing the packets, the proxy server accepts and changes the packet address by providing the proxy server address, thereby hiding the real return address.

    For this reason, proxy servers generally use a method called Network Address Translation (NAT), which serves to hide the private IP address used by the LAN. In addition to checking the packet address, the proxy server also checks the contents of the packet.

4. __Stateful Inspection Firewall__ 

    This stateful inspection firewall works between the data link layer and the OSI model reference network. If a data packet is received, the first step taken by this stateful inspection is to check the data packet header information with the state table to see if there is already a path available for the packet. If the path is already available, stateful inspection makes the assumption that the packet is allowed to be received and forwarded to its destination. If the path is not yet available, stateful inspection matches the data packet with the security policy that has been created to determine whether the packet has permission to be forwarded. Stateful inspection constantly monitors every connection that occurs and makes a record of its status table.

In this module we will learn how to do Packet-Filtering with Firewall using the `# iptables` command. For documentation and how to use it, see `# man iptables`.

### 5. IPTables
![iptables](img/iptables.jpg)

(Source : https://medium.com/@pamungkasjayuda/protect-server-dengan-iptables-fail2ban-b3cb3d4a42b7)

Iptables is a tool in the Linux operating system that functions as a tool for filtering data traffic. In simple terms, iptables is described as a data traffic controller. Traffic rules in iptables are in a table, where __table__ is a group of __chain__ and __chain__ is a group of __rules__. In _high-level_ iptables, it is possible to have _multiple tables_ with _multiple chains_. By default, iptables runs without any rules.

Work structure of IPTables,
```
iptables -> Tables -> Chains -> Rules
```

![struktur-iptables](img/struktur-iptables.png)

(Source : https://musaamin.web.id/cara-setting-firewall-dengan-iptables-di-linux/)

Macam-macam chain pada IPTables :

1. __PREROUTING__

    The point where we can manipulate the network packet before it enters the routing decision, whether it will enter our Linux machine or just 'pass'.

    Used to translate addresses before the routing process occurs. This is done by changing the Destination IP of the data packet.

2. __POSTROUTING__

    Used to translate addresses after the routing process. This is done by changing the source IP address of the data packet.

3. __INPUT__

    Perform a packet filter that enters through the firewall.

4. __OUTPUT__

    Performs a packet filter that exits the firewall before routing.

5. __FORWARD__

    To filter packets going to another NIC in another server or host (only forwarded/past the firewall).

#### 5.1 Tables and Chains
There are 3 main tables that exist in IPTables can be described as follows :

![iptables table](img/tabel.png)

(Source : https://static.thegeekstuff.com/wp-content/uploads/2011/01/iptables-filter-nat-mangle-tables.png)

__a. Filter Table__

This table is the default table in iptables. So, if we don't define the table that we use in iptables, then by default it uses Filter table.

__Filter table__ is the table responsible for packet filtering.

The Filter Table has a built-in chain, namely :

- __INPUT chain__ – To filter packets going to the local network. Syntax example:
```
# iptables --append INPUT --source 10.151.36.0/24 --jump DROP

Can also be written as :

# iptables -A INPUT -s 10.151.36.0/24 -j DROP
```
Description :

The syntax will DROP all incoming packets (INPUT) originating from the 10.151.36.0/24 subnet

- __OUTPUT chain__ – To filter packets from the local network to the outside network before the routing process is carried out. Syntax example:
```
# iptables --append OUTPUT --destination 10.151.36.5 --jump DROP

Can also be written as :

# iptables -A OUTPUT -d 10.151.36.5 -j DROP
```
Description :

The syntax will DROP all outgoing packets (OUTPUT) heading to 10.151.36.5

- __FORWARD chain__ – To filter packets that are forwarded (bypass) the firewall. Syntax example:
```
# iptables --append FORWARD --source 10.151.36.0/24 --jump ACCEPT

Can also be written as :

# iptables -A FORWARD -s 10.151.36.0/24 -j ACCEPT
```
Description :

This syntax will ACCEPT all outgoing packets bypassing that come from subnet 10.151.36.0/24

![filter](img/filter.jpg)

(Source : https://musaamin.web.id/wp-content/uploads/2018/07/iptabes-tutorial-input-forward-output.jpg)

__b. NAT Table__

NAT Table serves to translate the local network that passes through the firewall to the outside network. NAT Table has a built-in chain, namely:

- __PREROUTING chain__ – in the PREROUTING chain, DNAT (Destination NAT) is executed i.e. when you change the destination address of the first packet in other words you change where the communication is going.

    Destination NAT is always performed before routing, when packets come in from the network. Port forwarding, load sharing and transparent proxies are all forms of DNAT.
    
    Destination NAT is done on the PREROUTING chain, when the packet comes in, this means that all the tools in the router will see the packet will go to the actual destination. This also means that the -i (incoming interface) option can be used.
    
    Destination NAT is specified using -j DNAT and the --to-destination option specifies an IP address, range of IP addresses and range of ports (only for UDP and TCP protocols) which are optional.
    
    For example, we have an internal LAN network that we want to secure. On the network there is a DMZ as an HTTP server whose server has an IP of 10.151.73.98. We want all HTTP requests coming from the outside network (interface eth0) to be directed to the DMZ.

    ```
    # iptables --table nat --append PREROUTING --in-interface eth0 --protocol tcp --dport 80 --jump DNAT --to-destination 10.151.73.98:80

    Can also be written as :

    # iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 10.151.73.98:80
    ```
- __POSTROUTING chain__ – the POSTROUTING chain executes SNAT (Source NAT), i.e. when you change the origin address of the first packet in other words you change where the connection is from.

    Source NAT is always performed __after routing__, before packets exit the network. Masquerading is an example of SNAT. To do Source NAT you have to change the origin of the connection. This is done in the POSTROUTING chain, just before exiting.

    This is very important, because it means that other tools in the router (routing, packet filtering) will see the packet unchanged. This also means the -o (outgoing interface) option can also be used. Source is specified using -j SNAT, and the --to-source option to specify an IP address, IP address range and port or port range (only for UDP and TCP protocols) which is optional.
    
    For example, in the UML introduction module we have run IP masquerading with the following syntax:
    ```
    # iptables --table nat --append POSTROUTING --out-interface eth0 --jump MASQUERADE

    Can also be written as : 

    # iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    ```
    The above rule means, the source address of each outgoing packet (-o) via eth0 will be changed to the IP of eth0 (MASQUERADE).

    ![nat](img/nat.gif)

    (Source : https://www.karlrupp.net/en/computer/computer/graphics/nat-chains.gif)

__c. Mangle Table__

Mangle Table is used to make changes to data packets. Changes made to the TCP header to modify the QOS (Quality of Service) of the packet. Mangle Table has a built-in chain, namely :

- __PREROUTING chain__
- __OUTPUT chain__
- __FORWARD chain__
- __INPUT chain__
- __POSTROUTING chain__

#### 5.2 Rules
Things to remember to enforce rules on IPTables, that is :

- Rules have criteria and target.
- If the criteria are met, the firewall will execute a rule on the target or a value (parameter) specified on the target.
- If the criteria do not match, the firewall will execute the next rule.

The destination of the packet can be defined on the target, some of the targets that are often used are :

1. __ACCEPT__ – Firewall will allow data packets.
2. __DROP__ – The firewall will reject the data packet.
3. __RETURN__ – The firewall will stop executing the chain of rules for that data packet and the rules on the chain are re-executed.
4. __MASQUERADE__ – Target that only applies to the NAT Table. Used to define which subnet packets are directed to. Usually only used for dynamic IP, if using static IP, then use SNAT target.
5. __REJECT__ – The firewall will reject the packet and send an error message.
6. __REDIRECT__ – Target that only applies to the NAT Table. The firewall will direct packets to the device (machine) it uses using the Primary IP address (localhost address) of its interface.

For more complete types of targets, see the extension documentation from iptables
```
# man iptables-extension
```

__Syntax__

In general, to modify the rules that apply to IPTables by running :
```
# iptables [-t table] command chain rules
```
If the table is not mentioned, the default is to use a filter table.

Some commands that are often used in iptables :

| Command and Syntax | Description | Example |
| :- | :- | :- |
| `-A, --append chain rule-specification` | add rules to chain | `# iptables -A INPUT -s 10.151.36.0/24 -j DROP` 
| `-C, --check chain rule-specification` | check what rules apply to the chain | `iptables -C INPUT -s 10.151.36.0/24 -j DROP`
| `-D, --delete chain {rule-specification \ rulenum}` | delete rules on chain | `# iptables -D INPUT -s 10.151.36.0/24 -j DROP`
| `-I, --insert chain [rulenum] rule-specification` | insert rules in a certain order | `# iptables -I OUTPUT 2 -s 10.151.36.0/24 -j DROP`
| `-R, --replace chain rulenum rule-specification` | change the rules on a certain chain | `# iptables -R OUTPUT 2 -s 10.151.36.0/24 -j DROP`
| `-L, --list [chain]` | see a list of rules that apply based on the chain | `# iptables -L INPUT`
| `-S, --list-rules [chain]` | see all the rules that apply to the firewall | `# iptables -S INPUT`, `iptables -n -L -v --line-numbers`
| `-F, --flush [chain]` | removes all rules on a given chain (all chains if chain is not specified) | `# iptables -F INPUT`

**Explanation :**

- `rule-specification` = `[matches...] [target]`
- `match` = `-m matchname [per-match-options]`
- `target` = `-j targetname [per-target-options]`
- `[]` = Syntax is optional

Some parameters to know :

| Parameter | Descripton |
| - | :- |
| `[!] -p, --protocol protocolename` | defines the port options the packet uses
| `[!] -s, --source address` | defines the origin address option of the packet
| `[!] -d, --destination address` | defines the destination address option of the packet
| `-m, --match matchname` | defines the suitability of the rule for its purpose
| `-j, --jump targetname` | define the target of the rule; i.e. what to do if the packet matches
| `[!] -i, --in-interface name` | names the interface from where packets are received
| `[!] -o, --out-interface name` | name of the interface by which a packet is being sent

**Explanation :**
- `[!]` = can be negated

For more complete command options and parameters, see the `iptables` documentation,

```bash
# man iptables-extension
```

# **Practice**

#### List default policy for every chain
```bash
# iptables -L | grep policy
```
#### 
#### Change default policy for a Chain
```bash
# iptables --policy {ACCEPT | DROP | REJECT}
```
Example :
```bash
# iptables --policy FORWARD ACCEPT
```
####

#### ACCEPT connection from an IP address

```bash
# iptables -A INPUT -s 10.151.36.201 -j ACCEPT
```
Explanation : 
- ACCEPTS all connections from IP 10.151.36.201
#####
#### DROP connections from a subnet

```bash
# iptables -A INPUT -s 10.151.36.0/24 -j DROP
```
Explanation :
- BLOCK all connections from subnet 10.151.36.0/24 


#### DROP all connections, only ALLOW connections to 10.151.36.201

```bash
# iptables --policy OUTPUT DROP
# iptables -A OUTPUT -d 192.168.36.201 -j ACCEPT
```
Explanation :
- DROP all outgoing connections
- ALLOW connections to IP address 10.151.36.201

#### DROP HTTP connection

```bash
# iptables -A INPUT -p tcp --dport 80 -j DROP
```
Explanation :
- DROP all packets whose protocol is tcp and going to port 80 (http)

#### Saving IPTables Rules

```bash
# sudo /sbin/iptables-save
```

#### Erase all rules on IPTables

```bash
# iptables -F
```

#### View all Rules on IPTables

```bash
# iptables -L
```

# Exercise

![image](https://user-images.githubusercontent.com/58405725/143586683-ffbf45db-13a0-48d9-abde-454a8ac8de39.png)

1. Baratie PC not allowed to access the Water7 server
2. Arabasta PC cannot be accessed at 07.00 - 17.00
3. Water7 server is not allowed to accept HTTP connections
4. All packets going to the Baratie PC will be directed to Mariejois
