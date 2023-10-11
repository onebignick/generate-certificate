# generate-certificate
This script generates a self signed certificate

# Requirements
1. Python
2. Java

# Getting Started
clone this repository

```shell
git clone https://github.com/onebignick/generate-certificate
```

install dependencies
```shell
pip install -r requirements.txt
```

run script
```shell
python3 generate-certificate.py
```
upload file onto the Java Key Store (JKS)
```shell
keytool -import -keystore keystore.jks -file certificate.pem -alias my_alias
```
