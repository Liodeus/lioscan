from functions.misc import *
import socket


def detect_techno(url, path):
	start_print("TECHNOLOGIE")
	cmd(f"whatweb {url} | tee {path}{FOLDER_TECHNOLOGIE}whatweb.out")
	cmd(f"webanalyze -host {url} -silent -apps {WEB_ANALYZE_TECHNO_PATH} | tee {path}{FOLDER_TECHNOLOGIE}webanalyze.out")
	end_print("TECHNOLOGIE")


def detect_waf(url, path):
	start_print("WAF")
	cmd(f"wafw00f -a -v {url} | tee {path}{FOLDER_TECHNOLOGIE}wafw00f.out")
	end_print("WAF")


def port_scan_tcp(domain, path):
	start_print("PORT SCAN TCP")
	cmd(f"rustscan -a {domain} --ulimit 5000 -n -t 4000 -- -A -sC -sV -oN {path}{FOLDER_TECHNOLOGIE}rustcan.out")
	end_print("PORT SCAN TCP")


def cve_nrich(domain, path):
	start_print("CVE NRICH")
	ip = socket.gethostbyname(domain)
	cmd(f"echo {ip} | nrich - | tee {path}{FOLDER_TECHNOLOGIE}nrich.out")
	end_print("CVE NRICH") 


def make_screenshot(url, path):
	start_print("SCREENSHOT")
	cmd(f"gowitness single {url} --timeout=25 --screenshot-path {path}{FOLDER_TECHNOLOGIE} --db-path {path}{FOLDER_TECHNOLOGIE}gowitness.sqlite3")
	# Start server in background to view the screenshot 
	cmd(f"gowitness report serve --screenshot-path {path}{FOLDER_TECHNOLOGIE} --db-path {path}{FOLDER_TECHNOLOGIE}gowitness.sqlite3 &")
	cmd(f"{BROWSER} http://localhost:7171 &")
	end_print("SCREENSHOT") 