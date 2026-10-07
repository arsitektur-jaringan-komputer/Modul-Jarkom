# Computer Network - 3rd Module

## Table of Contents

- [1. Static Routing](#1-static-routing)
  - [1.1 Definition](#11-definition)
  - [1.2 Implementation](#12-implementation)
  - [1.3 Troubleshooting](#13-troubleshooting)
  - [1.4 References](#14-references)

## 1. Static Routing

Now that we understand how computer networks around the world generally work, the devices used to support communication on the internet, the protocols they follow, and so on, we will move on to a concept that is just as important and that we will often encounter, namely **Routing**.

### 1.1 Definition

If an IP Address can be likened to a house address, then now let's imagine we are in a housing complex, say complex A. In this complex, the residents follow the same house address rule, namely the letter A followed by a number. For example, your neighbor Mr. Hassan has the house address A-17, Mrs. Rumrowi has the house address A-32, and so on. As a local resident, you know them and know how to visit their houses without anyone else's help.

One day, you are given the task of delivering food to the house address B-03. However, you do not recognize this address because it does not begin with the letter A as usual. So, you contact the complex's post office at address A-01 (whose location you know) and ask for their help in delivering the food. As a post office, they have address data for the entire city, so they know where house B-01 is located and where to deliver the food. So, you simply go to A-01 and hand over the food, which has the destination B-01. The rest will be taken care of by the post office.

The concept of routing is more or less the same as the illustration above. In essence, routing is a process that determines the best path for sending a packet/data from one network to another. Generally, this is done by a _Router_, which is responsible for forwarding packets from one network segment to another. A _Router_ performs this path determination based on the data it has, namely the _Routing Table_, which contains information on how to reach a network segment, even one that looks far away.

Referring to the illustration above, you and all your neighbors can be regarded as hosts and your complex as a _subnet_ (we will explore this in Module 4). Then, the post office can be regarded as a _Router_ and the address data for the whole city that they hold can be regarded as the _Routing Table_.

![image](../Modul-2/images/routing_id.png)

Based on how a _Router_ obtains information about its _Routing Table_, _Routing_ can be divided into 2 categories, namely **Static Routing** and **Dynamic Routing**. Dynamic Routing will be discussed briefly in Module 4, while Static Routing is what we will study in this module.

In Static Routing, a _network administrator_ (or team) is responsible for filling in the _Routing Table_ on every _Router_. Using the post office analogy, the government is responsible for informing all existing post offices about the other post offices and how a post office can contact other post offices or other housing complexes. This is quite simple when done on a network with a small number of _Routers_ and network segments, but becomes more difficult and tiring as the number and complexity of the network grow. Not only that, if there is a new network segment, all _Routers_ must be informed about it, which is certainly very inefficient and will consume a lot of time.

However, because we will use a simple topology that does not change much, with few network segments, Static Routing can make things easier for us because we will have full control over our topology. Next, we will try doing it in GNS3.

![image](../Modul-2/images/static_routing.webp)

### 1.2 Implementation

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

For this case, set all netmasks to `255.255.255.0` for now (further explanation is in Module 4). Then, for all hosts (all nodes except Water7, Dressrosa, and Foosha), set their gateway to the IP Address of the connected _Router_. For example, EniesLobby and Water7 are connected on Water7's eth0, so the gateway for both of them is `10.40.1.1`. Then, set the gateways for the routers as follows:

```
# leave the gateway empty for Water7's eth0 interface and Foosha's eth1 & eth2 interfaces
eth1 Water7: 10.40.2.2
eth0 Foosha: 10.40.3.1
# also leave Dressrosa's gateway empty for all interfaces
```

#### 1.2.1 Before Routing

Once you have finished the configuration, test connectivity by pinging between nodes within the same network segment (complex). For example, make sure **Westalis** can ping **EniesLobby** and **Water7**, **Dressrosa** can ping **Foosha**, and so on.

> Tip: There is no need to log in to every node. Just log in to **Water7** and **Foosha** and ping all the devices connected to them, because in general ping is symmetric (if host A can ping host B, the reverse also holds) unless there is additional configuration such as a Firewall or NAT.

Now, please try pinging between complexes that are quite far apart, for example **Dressrosa** (`10.40.3.1`) to **Alabasta** (`10.40.4.2`). You should get output like the following

![image](../Modul-2/images/dressrosa_alabasta_before_v1.jpg)

or

![image](../Modul-2/images/dressrosa_alabasta_before_v2.jpg)

You may not get output exactly like the above (it may even _hang_ when pinging). However, in essence the result is the same, namely that you cannot ping.

> If you ping between complexes that are still close together and connected to the same _router_ (for example complex B and complex C), there is a possibility that ping communication can still be carried out.

Therefore, we will tell the _router_ how to reach the other complexes.

#### 1.2.2 The Routing Process

The first way is quite simple, which is to only tell **Dressrosa** how to reach all network segments. For that, we will use the following command:

```
ip route add <DESTINATION SUBNET>/<NETMASK> via <GATEWAY>
```

Explanation:

- **DESTINATION SUBNET** contains the NID or the network segment to be reached. In our case, the first 3 octets contain the complex's IP and the last octet contains `0`. A more detailed explanation will be explored in module 4.

- **NETMASK** for our case will simply be filled with `24`.

- **GATEWAY** contains the IP Address of the _router_ used to reach that network segment.

For example:

```
ip route add 10.40.5.0/24 via 10.40.3.2
```

When we run the command above on **Dressrosa**, it is as if we are telling it, "Hello Dressrosa, if there is a _packet_ with a destination IP Address in complex C (`10.40.5.X`), then the way to reach it is by passing through `10.40.3.2` (which is **Foosha**)"

![image](../Modul-2/images/dressrosa_after.jpg)

Before running the command above, Dressrosa did not know how to reach complex C (`10.40.5.X`). Therefore, it said that the network could not be reached (`Network is unreachable`). After we told it, it now has the information on how to reach that network segment. So, it and the external devices directly connected to it (in this case, **Water7**) can contact addresses in that network segment.

![image](../Modul-2/images/water7_ok.jpg)

However, complex A still cannot ping complex C. Although packets sent from complex A (`10.40.1.X`) can reach complex C (`10.40.5.X`) because all the _routers_ already know the way, they still do not know how to reach complex A for the replies. Therefore, we need to tell **Dressrosa** again how to reach complex A by running the following command:

```
ip route add 10.40.1.0/24 via 10.40.2.1
```

![image](../Modul-2/images/enieslobby_before_after.jpg)

As in the picture, at first **EniesLobby**, as a resident of complex A, could not contact complex C. After we ran the command above on **Dressrosa**, EniesLobby can _ping_ complex C.

> Do the same for complex B. Do you know the _command_ used and on which node?

#### 1.2.3 After Routing

Perhaps while doing the implementation, several questions arose in your mind, such as:

- _Why was only **Dressrosa** configured, when there are 3 routers?_

- _Does that mean **Water7** and **Foosha** know how to reach all of the existing complexes? How can that be?_

- _What will happen if a new complex is added, such as complex D at `10.40.6.X`?_

The last piece of the _puzzle_ that makes all of this happen and can answer your questions is the **Default Gateway**.

Simply put, a Default Gateway can be likened to the person you ask (following the initial illustration, the complex's post office) when you do not know the way. When there is a _packet_ with an unfamiliar destination, instead of giving up and discarding it, we simply send that _packet_ to the Default Gateway. This is what happened in the implementation above and why only **Dressrosa** was configured.

**Case Study: Ping from EniesLobby to Jipangu**

Run the command below on **EniesLobby**:

```
mtr 10.40.5.2
```

![image](../Modul-2/images/mtr.jpg)

Through `mtr`, we can find out which nodes the _packet_ we send passes through. This command is similar to `traceroute`. In this case, we want to find out which path the _packet_ takes from **EniesLobby** (`10.40.1.3`) to **Jipangu** (`10.40.5.2`). The explanation of the route flow is as follows:

1. First, because the destination IP Address (namely `10.40.5.2`) is not in the same network segment, **EniesLobby** does not know how to send it. However, because it has a Default Gateway, namely **Water7**, it simply sends the _packet_ there (namely `10.40.1.1`)

2. The same thing happens to **Water7**. It actually does not know how to send this _packet_ either, but because it also has a Default Gateway, namely **Dressrosa**, it will send it there (namely `10.40.2.2`)

3. Unlike EniesLobby and Water7, **Dressrosa** knows how to reach the network segment of this _packet_'s destination. According to the data it has (or its _Routing Table_), to reach that packet's destination it must send it to **Foosha**, namely `10.40.3.2`

4. Finally, because **Foosha** is directly connected to **Jipangu**, the _packet_ can be sent directly to the destination, namely `10.40.5.2`.

> If **Water7** and **Foosha** did not have a Default Gateway, then we would have to run the `ip route add` command to fill in their _Routing Tables_ just as we did on **Dressrosa**.

#### 1.2.4 Routing Table

It would be good to close with a brief explanation of the last component on our journey, namely the **Routing Table**.

A Routing Table is a data structure that stores information about how to reach a network segment. Usually, a Routing Table contains information about the destination network segment, its _next hop_ or _gateway_, the _network interface_ used, and additional information.

Let's look at the Routing Table on **Dressrosa** with:

```
ip route show
```

![image](../Modul-2/images/routing_table.jpg)

- `10.40.1.0/24 via 10.40.2.1 dev eth0`: To reach the network segment `10.40.1.0/24`, send the _packet_ to `10.40.2.1` through the `eth0` _interface_.

- `10.40.2.0/24 dev eth0 proto kernel scope link src 10.40.2.2`: The network segment `10.40.2.0/24` is directly connected through the `eth0` _interface_. **Dressrosa**'s own IP on this connection is `10.40.2.2`

> Can you translate the rest?

### 1.3 Troubleshooting

If you have configured the _router_ but still cannot ping, there is a possibility that your _router_ is not willing to forward _packets_ (_packet forwarding_ is disabled).

To check, you can run:

```
cat /proc/sys/net/ipv4/ip_forward
```

`1` means _packet forwarding_ is active and `0` means it is inactive. To enable it, you can run:

```
sysctl -w net.ipv4.ip_forward=1
```

or by making sure `net.ipv4.ip_forward=1` is present (usually commented out) in `/etc/sysctl.conf`. Apply it with

```
sysctl -p
```

### 1.4 References

- https://www.geeksforgeeks.org/computer-networks/open-systems-interconnection-model-osi/

- https://www.tutorialspoint.com/data_communication_computer_network/computer_network_models.htm

- https://www.geeksforgeeks.org/computer-networks/computer-network-models/

- https://www.lifewire.com/layers-of-the-osi-model-illustrated-818017
