from functions.misc import *
from os.path import exists


# Thanks HaxUnit
def install_nrich():
	for nrich_cmd in (
			"wget https://gitlab.com/api/v4/projects/33695681/packages/generic/nrich/latest/nrich_latest_amd64.deb",
			"sudo dpkg -i nrich_latest_amd64.deb",
			"rm nrich_latest_amd64.deb",
	):
		cmd(nrich_cmd)


def install_rustscan():
	for rustscan_cmd in (
			"wget https://github.com/RustScan/RustScan/releases/download/2.0.1/rustscan_2.0.1_amd64.deb",
			"sudo dpkg -i rustscan_2.0.1_amd64.deb",
			"rm rustscan_2.0.1_amd64.deb",
	):
		cmd(rustscan_cmd)


def install_uro():
	cmd("pip3 install uro")


def install_wafw00f():
	for wafw00f_cmd in (
			"git clone https://github.com/EnableSecurity/wafw00f.git",
			"cd wafw00f",
			"sudo python setup.py install",
			"sudo rm -r wafw00f"
	):
		cmd(wafw00f_cmd)

   
def install_webanalyze():
	for webanalyze_cmd in (
			"wget https://github.com/rverton/webanalyze/releases/download/v0.3.6/webanalyze_0.3.6_Linux_x86_64.tar.gz",
			"tar xvf webanalyze_0.3.6_Linux_x86_64.tar.gz",
			"rm webanalyze_0.3.6_Linux_x86_64.tar.gz",
			"sudo mv webanalyze /usr/bin/",
			"sudo rm technologies.json"
	):
		cmd(webanalyze_cmd)


def install_whatweb():
	for whatweb_cmd in (
			"sudo apt install ruby ruby-dev",
			"wget https://github.com/urbanadventurer/WhatWeb/archive/refs/tags/v0.5.5.tar.gz",
			"tar xvf v0.5.5.tar.gz",
			"rm v0.5.5.tar.gz",
			"cd WhatWeb-0.5.5; sudo make install",
			"sudo rm -r WhatWeb-0.5.5"
	):
		cmd(whatweb_cmd)

	
# Golang tools
def install_golang_tools():
	for golang_tool in (
		"go install github.com/sensepost/gowitness@latest",
		"go install github.com/jaeles-project/gospider@latest",
		"go install github.com/bp0lr/gauplus@latest",
		"go install github.com/projectdiscovery/httpx/cmd/httpx@latest",
		"go install github.com/lc/subjs@latest"
	):
		cmd(golang_tool)


def install_linkfinder():
	for linkfinder_cmd in (
		"cd tools;git clone https://github.com/GerbenJavado/LinkFinder.git",
		"pip3 install -r tools/LinkFinder/requirements.txt",
		"cd tools/LinkFinder/;sudo python setup.py install",
	):
		cmd(linkfinder_cmd)


def install_secretfinder():
	for secretfinder_cmd in (
		"cd tools;git clone https://github.com/m4ll0k/SecretFinder.git secretfinder",
		"pip3 install -r tools/secretfinder/requirements.txt",
	):
		cmd(secretfinder_cmd)


# Thanks HaxUnit
def install_acunetix():
	if not exists("acunetix_docker"):
		cmd("git clone https://github.com/vncloudsco/acu807155.git acunetix_docker")

		new_email = input("\n\nPlease enter acunetix email (leave blank for default: contact@manhtuong.net): ")
		if new_email:
			cmd(f"sed -i 's/contact@manhtuong.net/{new_email}/g' acunetix_docker/Dockerfile")
			acunetix_email = new_email

		new_password = input("\nPlease enter acunetix password (leave blank for default: Abcd1234): ")
		if new_password:
			cmd(f"sed -i 's/Abcd1234/{new_password}/g' acunetix_docker/Dockerfile")
			acunetix_password = "new_password"

		cmd("docker build -t aws acunetix_docker")
		cmd("docker run --name acunetix-lioscan -it -d -p 3443:3443 aws")

		print("Acunetix", "Installed successfully - available at https://localhost:3443/")
		cmd(f"{BROWSER} https://localhost:3443/ &")


def check_goland_version():
	test_go = cmd("go version")
	version = '.'.join(test_go.split('go')[-1].split()[0].split('.')[:-1])
	return float(version) >= 1.17


def install_all():
	start_print("INSTALLING TOOLS")

	yes_answer = ["y", "yes", "ye", "ys"]
	answer = input("Do you really want to start the installation process ? ")
	if answer.lower() in yes_answer:
		if check_goland_version():
			install_golang_tools()
			install_rustscan()
			install_nrich()
			install_uro()
			install_wafw00f()
			install_webanalyze()
			install_whatweb()
			install_linkfinder()
			install_secretfinder()
			install_acunetix()
		else:
			print("You need at least golang 1.17")
			exit()
	else:
		print("See ya !")
		exit()
	
	end_print("INSTALLING TOOLS")
