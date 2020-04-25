# -DDNS
这是涉及到ipv4和ipv6的动态域名解析.注意提前在阿里云服务端准备好一条解析记录（ip可以随意填）。
code/set.json:
#### RR:你的主机名

#### Domain:Your Main Domain（你购买的域名）

#### IPV4:IPV4 DDNS On(true)/Off(false)

#### IPV6:IPV6 DDNS On(true)/Off(false)

#### accessKeyId:Your AliDNS accessKeyId

#### accessSecret:Your AliDNS accessSecret

# About Language/Enviroment
python3 pip3

### Core Code is Python

#### Python Use These Extend（Need To Install)：

#### requests

#### aliyun-python-sdk-core

#### aliyun-python-sdk-alidns

### Install Command(pip):

#### pip install requests

#### pip install aliyun-python-sdk-core

#### pip install aliyun-python-sdk-alidns
