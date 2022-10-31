# 2. Proxy Server
## Outline
- [2. Proxy Server](#2-proxy-server)
  - [Outline](#outline)
  - [2.1 Definition, Usage, and Benefits](#21-definition-usage-and-benefits)
    - [2.1.1 Definition](#211-definition)
    - [2.1.2 Usage](#212-usage)
    - [2.1.3 Benefits](#213-benefits)
    - [2.1.4 Proxy Server Software](#214-proxy-server-software)
    - [2.1.5 How it Works](#215-how-it-works)
  - [2.2 Implementation](#22-implementation)
    - [2.2.1 Instalasi Squid](#221-instalasi-squid)
    - [2.2.2 Konfigurasi Dasar Squid](#222-konfigurasi-dasar-squid)
    - [2.2.3 Making User Login](#223-making-user-login)
    - [2.2.4 Access Time Restriction](#224-access-time-restriction)
    - [2.2.5 Specific Website Access Restriction](#225-specific-website-access-restriction)
    - [2.2.6 Bandwidth Restriction](#226-bandwidth-restriction)
  - [2.3 Proxy Activation and Deactivation](#23-proxy-activation-and-deactivation)
    - [Proxy Activation](#proxy-activation)
    - [Proxy Deactivation](#proxy-deactivation)
  - [2.4 Excercises](#24-excercises)
	

##  2.1 Definition, Usage, and Benefits
### 2.1.1 Definition
Proxy server is a server or a software that acts like a bridge between a computer and the internet network. In other words, Proxy server is a network that bridges the local network and the internet network. Internet program such as browser, download manager, and so interact with the proxy server, and that proxy server will be the one that communicate with other server in the internet.
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/master/Modul-3/Proxy%20Server/img/proxy%20server.png?raw=true)
Proxy server can be a computer system or an application that is used as a gateaway, bridging our computer with the outside network.

### 2.1.2 Usage
1.  _**Connection sharing**_  : Proxy acts as a gateaway that becomes a barrier between local network and the outer network. Gateway also acts like a point where several connections from the local clients and the outer network connected to it. Therefore, the connections from the local network to the internet will use the bridge that the gateway has together.
    
2.  _**Filtering**_  : Proxy also can be used to work on the application layer as a firewall and packet filter to protect the local network from any disruption or adversary threat from the outer network. The filtering function also can be configured to deny access from specific time and websites.
    
3.  _**Caching**_  : A Proxy server has an object storing mechanism from anything that is requested from any server on the internet. With this caching mechanism, it will also store the objects that are requested by the client from the internet and received from the internet.

### 2.1.3 Benefits
Proxy server has several benefits:

-   Connection sharing
-   Hides IP
-   Blocking access to unwanted sites
-   Accessing the blocked sites
-   Setting the bandwidth

### 2.1.4 Proxy Server Software
A few example of a proxy server software are listed below:

1.  CCProxy
2.  WinGate
3.  Squid
4.  Nginx

### 2.1.5 How it Works
![image](https://user-images.githubusercontent.com/61197343/139414632-c0e8515a-1a0d-43f2-a479-5dd189307102.png)


## 2.2 Implementation
For this session, the proxy server software we are using is **squid** and the node that will be used as a proxy server is **Water7**.

### 2.2.1 Instalasi Squid
**Step 1** - Install squid on node  **Water7**
```
apt-get install squid
```

**Step 2** - Check squid status to confirm whether squid already runs correctly
```
service squid status
```
![image](https://user-images.githubusercontent.com/61197343/139424987-892e322e-59ef-410e-864f-a0b503c3b9f6.png)

If shown **ok** then the installation is successful.

### 2.2.2 Konfigurasi Dasar Squid
**Step 1** - Backup the default configuration file provided by Squid.
```
mv /etc/squid/squid.conf /etc/squid/squid.conf.bak
```

**Step 2** - Make a new Squid configuration.
On the file `/etc/squid/squid.conf`

**Step 3** - Then, on the new config file, enter below script:
```
http_port 8080
visible_hostname Water7
```

![image](https://user-images.githubusercontent.com/61197343/139425202-442b599a-2b56-4d56-829e-80153b8627ea.png)

**Keterangan:**

-   `http_port 8080`  : Port that is used to access the proxy, in this case **8080**. (Syntax:  `http_port 'WANTED_PORT'`)
-   `visible_hostname Water7`  : Proxy name that will be visible to the user. (Syntax:  `visible_hostname 'WANTED_NAME'`)

**STEP 4**  - Restart squid with the following command:
```
service squid restart
```
If the squid status shown **ok**, then it's time to move on the client.

**STEP 5** - On Loguetown, do the proxy configuration

Look at [Proxy Activation and Deactivation](#23-proxy-activation-and-deactivation)

Then try to access the site **[http://its.ac.id](http://its.ac.id/)**. It would show a screen like this:

![image](https://user-images.githubusercontent.com/61197343/139426103-fb4a72fc-b4f5-40b9-b56d-3cb1e0402523.png)

**Step 6** - To be able to access **[http://its.ac.id](http://its.ac.id/)**, you have to add a line of script on the Squid configuration. Open the previous configuration file and add this line:
```
http_access allow all
```

![image](https://user-images.githubusercontent.com/61197343/139426209-003df7ba-fc39-4d88-b2c0-ed7ad75cb726.png)

**Keterangan:**

-   `http_access allow all`  : Allow all to access the proxy via HTTP. This setting needs to be added because the default from Squid is **deny**. (Syntax:  `http_access allow 'TARGET'`)
-   To deny access, simply change **allow** to **deny**.
- 
**Step 7** - **Save**  the configuration file, and  **restart**  squid. Refresh the site **[http://its.ac.id](http://its.ac.id/)**.

Seharusnya halaman yang ditampilkan kembali normal.
![image](https://user-images.githubusercontent.com/61197343/139426331-008ff04c-7cbb-4fe1-ba8b-312421d96106.png)

### 2.2.3 Making User Login


**STEP 1**  - Install  `apache2-utils`  on node  **Water7**. Before that, make sure to do `apt-get update`

**STEP 2**  - Make a new user and password. Type in:
```
htpasswd -c /etc/squid/passwd jarkom203
```
Type in the password you want. If done, then this notification will appear:

![image](https://user-images.githubusercontent.com/61197343/139426496-fde1564a-bad8-4ae4-b1cd-57e333dc256e.png)

**STEP 3** - Edit the Squid configuration as follow:
```
http_port 8080
visible_hostname Water7

auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd
auth_param basic children 5
auth_param basic realm Proxy
auth_param basic credentialsttl 2 hours
auth_param basic casesensitive on
acl USERS proxy_auth REQUIRED
http_access allow USERS
```
![image](https://user-images.githubusercontent.com/61197343/139426611-a96bb572-2dec-42f4-bfca-23c152f5b4d7.png)

**Additional Information:**

-   `auth_param`  used to configure authentication (Syntax:  `auth_param 'SCHEME' 'PARAMETER' 'SETTING'`. More info on [http://www.squid-cache.org/Doc/config/auth_param/](http://www.squid-cache.org/Doc/config/auth_param/)).
-   `program`  : Command to define external authenticator.
-   `children`  : Define the maximum shown authenticator.
-   `realm`  : Text that will be shown on the authentication pop-up.
-   `credentialsttl`  : Set the active period an authentication applied.
-   `casesensitive`  : Set whether the **username** is case sensitive or not.
-   `acl`  used to define a specific access setting. (General syntax:  **acl ACL_NAME ACL_TYPE ARGUMENT**  . More info on [http://www.squid-cache.org/Doc/config/acl/](http://www.squid-cache.org/Doc/config/acl/))
-   To see the list of configurable setting with acl, you can see: [https://wiki.squid-cache.org/SquidFaq/SquidAcl](https://wiki.squid-cache.org/SquidFaq/SquidAcl))

**STEP 4**  - Restart squid

**STEP 5**  - Change the browser proxy setting. Use **Water7's IP** as a host, and fill in **8080** as the port.
![](https://github.com/arsitektur-jaringan-komputer/Modul-Jarkom/blob/modul-3/Proxy%20Server/img/setting-proxy-system.PNG)

Then try to access **its.ac.id**, the authentication will be shown.

![recording](https://user-images.githubusercontent.com/61197343/139427026-f6a01919-b5fa-4ba3-a1f9-9d945550ba52.gif)

**STEP 6**  - Fill in the username and password.

**STEP 7**  - The website will succesfully loaded 🙆‍♂️

### 2.2.4 Access Time Restriction
We will try to restrict the proxy access to a specific time and day. Assume that the proxy can only be used on Monday to Friday, starting from 08:00 up until 17:00.

**STEP 1**  - Make a new file called acl.conf in the Squid folder
```
nano /etc/squid/acl.conf
```

**STEP 2**  - Add below line:
```
acl AVAILABLE_WORKING time MTWHF 08:00-17:00
```
![image](https://user-images.githubusercontent.com/61197343/139427316-cac65710-c5d5-4c82-a017-097f8fe9f863.png)

**STEP 3**  - Save the acl.conf file.

**STEP 4**  - Open squid.conf file.

**STEP 5**  - Change the configuration to:
```
include /etc/squid/acl.conf

http_port 8080
http_access allow AVAILABLE_WORKING
http_access deny all
visible_hostname Water7
```
![image](https://user-images.githubusercontent.com/61197343/139427485-b85aa7cc-6f06-47ef-bba1-d846c1ed9ce5.png)

**STEP 6**  - Save the file and restart Squid.

**STEP 7** - Try to access http://its.ac.id. The error will be shown when accessing outside the allowed time.

![recording (2)](https://user-images.githubusercontent.com/61197343/139428083-7cf40267-0beb-4668-8aea-ce589a3dd374.gif)

**Addtional Information:**
-   **MTWHF** is the days when the users are allowed to use the proxy. (S: Sunday, M: Monday, T: Tuesday, W: Wednesday, H: Thursday, F: Friday, A: Saturday)
-   Time format is as follow: **h1:m1-h2:m2**. With the conditions **h1<h2** and **m1<m2**

### 2.2.5 Specific Website Access Restriction
We will try to restrict access to several sites. In this example, we will block the access to **monta.if.its.ac.id** and **monkp.if.its.ac.id**.

**STEP 1**  - Make a file named restrict-sites.acl in the Squid folder with:
```
nano /etc/squid/restrict-sites.acl
```
**STEP 2**  - Add the URL that will be blocked as follow:
```
monta.if.its.ac.id
monkp.if.its.ac.id
```
![image](https://user-images.githubusercontent.com/61197343/139428263-1d3894f4-0699-4627-b40f-7ae654147006.png)

**STEP 3**  - Change the Squid configuration file as follow:
```
http_port 8080
visible_hostname Water7

acl BLACKLISTS dstdomain "/etc/squid/restrict-sites.acl"
http_access deny BLACKLISTS
http_access allow all
```
![image](https://user-images.githubusercontent.com/61197343/139428335-efeaca07-697d-4776-a5ef-bcaee5686780.png)

**STEP 4**  - Restart squid. Try to access **monta.if.its.ac.id** , **monkp.if.its.ac.id** , and **google.com**. It should then showing screen like below.

![recording (3)](https://user-images.githubusercontent.com/61197343/139428715-5ead80be-3a9e-4391-9fe5-2d24dee8f63f.gif)

**Keterangan:**
-   dstdomain means the destination domain. The syntax can be followed with the destination domain or a file that contains a list of websites.

### 2.2.6 Bandwidth Restriction
We will try to restrict the bandwidth that will be provided to the proxy user. In this example, we will restrict the bandwidth to a maximum of 512Kbps.

**STEP 1** - Make a file named acl-bandwidth.conf in the Squid folder.
```
nano /etc/squid/acl-bandwidth.conf
```

**STEP 2**  - Enter following script:
```
delay_pools 1
delay_class 1 1
delay_access 1 allow all
delay_parameters 1 16000/64000
```
![image](https://user-images.githubusercontent.com/61197343/139428802-f4caeacd-f807-4008-bde6-48e0d14bf04e.png)

**STEP 3**  - Change the configuration file squid.conf to:
```
include /etc/squid/acl-bandwidth.conf
http_port 8080
visible_hostname Water7

http_access allow all
```
![image](https://user-images.githubusercontent.com/61197343/139428864-e4bcb4ef-6fb8-4bea-9c1f-a9bbf109f07c.png)

**STEP 4**  - Restart Squid

**STEP 5**  - Try to do a speedtest.

To do the speedtest on a CLI, we will use [Speedtest CLI](https://www.speedtest.net/apps/cli). Run below script:

_Note: Don't forget to deactivate the proxy first. Look at [Proxy Activation and Deactivation](#23-proxy-activation-and-deactivation)

```
apt-get update
apt install speedtest-cli
```

If already installed, run `export PYTHONHTTPSVERIFY=0` to deactivate certificate verification when running a Python script.

Next, run the speedtest with `speedtest`.

Try to compare the speed with the proxy on and off.

- Non Active
![image](https://user-images.githubusercontent.com/61197343/139430867-baa17fe9-fbed-45d5-ab35-34dab8901aec.png)
- Active
![image](https://user-images.githubusercontent.com/61197343/139431490-efa75289-83eb-4738-888c-71ba16ebe606.png)

**Additional Information:**
-   **delay_pools** is used to set the number of pool will be made (Syntax: **delay_pools TOTAL_NUMBER**. More info on [http://www.squid-cache.org/Doc/config/delay_pools/](http://www.squid-cache.org/Doc/config/delay_class/)).
-   **delay_class** is used to set the type/class of bandwidth distribution on every pool. (Syntax: **delay_class POOL_NUMBER CLASS**.) More info on [http://www.squid-cache.org/Doc/config/delay_class/](http://www.squid-cache.org/Doc/config/delay_class/).
-   **delay_access** is similar to http_access, but is used for accessing the pool that has been made. (Syntax: **delay_access POOL_NUMBER allow/deny TARGET**. More info on [http://www.squid-cache.org/Doc/config/delay_access/](http://www.squid-cache.org/Doc/config/delay_access/).
-   **delay_parameters** is used to set the parameters of a pool that has been made. Syntax is different following the type/class of a pool. More info on [http://www.squid-cache.org/Doc/config/delay_parameters/](http://www.squid-cache.org/Doc/config/delay_parameters/)

## 2.3 Proxy Activation and Deactivation

### Proxy Activation

Here is a syntax from the proxy configuration:

```
export http_proxy="http://ip-proxy-server:port"
```

In this case, `ip-proxy-server` is the IP from Water7, with the port that has been defined when configuring Squid.

![image](https://user-images.githubusercontent.com/61197343/139425703-eb521f0f-2fb2-45fb-9963-85c76ce8f5d8.png)

To check whether the configuration on the client is successful, run `env | grep -i proxy`. If successful, then our environment is successfully using proxy.

![image](https://user-images.githubusercontent.com/61197343/139425807-eb2430de-0c06-46a7-942a-1da42ad0bba6.png)

### Proxy Deactivation

Run `unset http_proxy` on the client that the proxy will be deactivated at.

## 2.4 Excercises
Usopp sangat kangen dengan bapaknya, Yasopp. Sehingga Usopp ingin mencari bapaknya di lautan. Maka, Usopp membuat kapal dengan proxynya sendiri.

Proxy yang akan dibuat nantinya harus bisa diakses dengan nama yasoppdicariusopp.xxx.id dengan port yang digunakan adalah 420 (1)

Untuk bisa mengakses proxynya perlu dilakukan login terlebih dahulu (2) Usopp sebagai bajak laut yang baik, menggunakan username adalah kangenyasopp dan password BapakkuHilangNjirAkuSedih (3)

Karena Usopp merupakan bajak laut yang gigih tetapi juga taat beribadah, Usopp hanya bisa mengakses proxy pada waktu selain hari Jumat jam 11 siang sampai jam 1 siang (4)

Karena Usopp ingin fokus mencari bapaknya saja tanpa menjadi Soge King, Usopp memutuskan untuk memblokir website sogeking.jp dan website monkp.if.its.ac.id (5)

Usopp juga mengatur di proxynya agar user mendapatkan bandwith 1024 kbps (6)

Help Usopp so that he can succeed! 🔥🎉😭♥
