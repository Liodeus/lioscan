<p align="center">
  <img src="https://github.com/Liodeus/lioscan/blob/main/images/logo.png" alt="Logo">
  
<p align="center">A python3 script, which automate my scans :)

<p align="center">
  <a href="#introduction">Introduction</a>
 • <a href="#requirements">Requirements</a>
 • <a href="#installation">Installation</a>
 • <a href="#acunetix-api-key">Acunetix API key</a>
 • <a href="#usage">Usage</a>
 • <a href="#thanks">Thanks</a>
</p>

<div align="center">
  <sub>Created by
  <a href="https://liodeus.github.io/">Liodeus</a>
</div>


## Introduction

This tool is made to automate the different tools that I use. It took a URL as input and start detecting technologies/waf/open ports, crawl the URL and retrieve URLs from many sources, parse the data, js related scans and active scan (acunetix/nuclei).

## Requirements

- python3 (sudo apt install python3)
- pip3 (sudo apt install python3-pip)
- Go (>=1.17)
- Docker
- Firefox

## Installation

### Without virtual env

```bash
git clone https://github.com/Liodeus/lioscan
cd lioscan
pip install -r requirements.txt
python lioscan.py -i
```

### With virtual env

```bash
git clone https://github.com/Liodeus/lioscan
cd lioscan

# Create a virtual env
python3 -m venv .venv

# Activate the virtual env
. .venv/bin/activate

pip install -r requirements.txt
python lioscan.py -i
```

### Special uro
I'm using uro to parse some data and uro remove all .pdf extensions. I don't like this behavior so I made some change in the code, as follow :

```bash
# Find the script
locate uro.py

# Mine was located here
/usr/local/lib/python3.8/dist-packages/uro/uro.py

# Edit the file
vim /usr/local/lib/python3.8/dist-packages/uro/uro.py
```

Remove the "pdf", from the variable "static_exts" (line 13 at the time of redaction), then save.

## Docker - Run image

NOT FUNCTIONNAL YET !

```bash
docker build . -t liodeus
docker run -it liodeus /bin/bash
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

```bash
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

### Simple scan

#### Without virtual env
```bash
python3 lioscan.py -u https://example.com
```

#### With virtual env
```bash
# Activate the virtual env
. .venv/bin/activate
python3 lioscan.py -u https://example.com
```

### Simple scan + acunetix

#### Without virtual env
```bash
python3 lioscan.py -u https://example.com -a API_KEY
```

#### With virtual env
```bash
# Activate the virtual env
. .venv/bin/activate
python3 lioscan.py -u https://example.com -a API_KEY
```

## Thanks

Thanks to :
  - [HaxUnit](https://github.com/Bandit-HaxUnit/haxunit), for the idea and code about acunetix
  - @technoo10201 for the virtual env and the docker image
  - Different creator of the tool that I use