<p align="center">
  <img src="https://github.com/Liodeus/lioscan/blob/main/images/logo.png" alt="Logo">
  
<p align="center">A python3 script, which automate my scans :)

<p align="center">
  <a href="#introduction">Introduction</a>
 • <a href="#requirements">Requirements</a>
 • <a href="#installation">Installation</a>
 • <a href="#acunetix-api-key">Acunetix API key</a>
 • <a href="#usage">Usage</a>
</p>

<div align="center">
  <sub>Created by
  <a href="https://liodeus.github.io/">Liodeus</a>
</div>


## Introduction

TODO

## Requirements

- python3 (sudo apt install python3)
- pip3 (sudo apt install python3-pip)
- Go (>=1.17)
- Docker
- Firefox

## Installation

```
git clone https://github.com/Liodeus/lioscan
cd lioscan

# Create a virtual env
python3 -m venv .venv

# Activate the virtual env
. .venv/bin/activate

pip install -r requirements.txt
python lioscan.py -i
```

## Docker - Run image
```
$ docker build . -t liodeus ; docker run -it liodeus /bin/bash
```


## Acunetix API key

Once the installation process is finished (cf. [Installation](https://github.com/Liodeus/lioscan#installation)), you need to get your API key from the acunetix docker.

- Go to https://localhost:3443/
  - Default credentials :
      - email -> contact@manhtuong.net
      - password -> Abcd1234
  - You should now be connected. Go to the "Profile" page 
	</br><img src="https://github.com/Liodeus/lioscan/blob/main/images/profile.png" alt="profile">
  - Scroll to the "API Key" part
	</br><img src="https://github.com/Liodeus/lioscan/blob/main/images/api_zone.png" alt="api_part">
  - Then click on copy
  - You know have your API key for Acunetix :)

## Usage

```
 _      _                                 
| |    (_)                                
| |     _   ___   ___   ___   __ _  _ __  
| |    | | / _ \ / __| / __| / _` || '_ \ 
| |____| || (_) |\__ \| (__ | (_| || | | |
\_____/|_| \___/ |___/ \___| \__,_||_| |_|
	
	
usage: lioscan.py [-h] [-u URL] [-o OUT] [-a APIKEY] [-i]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to scan
  -o OUT, --out OUT     Output directory
  -a APIKEY, --apikey APIKEY
                        Acunetix API key
  -i, --install         Install all tools
```

TODO
