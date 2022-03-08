from functions.misc import *


def launch_spider(url, domain, path):
	"""
		Start gospider scan
	"""
	start_print("GOSPIDER")
	cmd_screen(f"gospider -a -r --sitemap -q -d 3 -s {url} -o {path}{FOLDER_CRAWL}")
	end_print("GOSPIDER")


def launch_gauplus(domain, path):
	"""
		Start gauplus scan
	"""
	start_print("GAUPLUS")
	# Get more results if some where missings
	cmd_screen(f"gauplus --random-agent -b css,jpg,png,gif,svg,ico,woff,woff2,pdf,ttf,otf,jpeg,JPG,mp4,mp3,avi,eot -o {path}{FOLDER_CRAWL}gauplus {domain}")
	end_print("GAUPLUS")


def merge_files(domain, path):
	"""
		Merge gospider paths and gauplus paths
	"""
	start_print("MERGING")
	cmd(f"cat {path}{FOLDER_CRAWL}{domain.replace('.', '_')} {path}{FOLDER_CRAWL}gauplus > {path}{FOLDER_CRAWL}merge")
	end_print("MERGING")


def parse_data_merge_gospider_gauplus(domain, path):
	"""
		Parse date return from gospider and gauplus (merge)
	"""
	start_print("PARSING")
	
	# Get subdomains
	cmd(f"cat {path}{FOLDER_CRAWL}merge | grep " + "'\[subdomains\]'" + f" | awk -F'- ' '{{print $2}}' > {path}{FOLDER_CRAWL}gospider.subdomains")

	# Remove subdomains
	cmd(f"cat {path}{FOLDER_CRAWL}merge | grep -v " + "'\[subdomains\]'" + f" > {path}{FOLDER_CRAWL}gospider_subdomain_remove")

	# Get forms
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_subdomain_remove | grep " + "'\[form\]'" + f" | awk -F'- ' '{{print $2}}' > {path}{FOLDER_CRAWL}gospider.forms")
	# Remove forms
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_subdomain_remove | grep -v " + "'\[form\]'" + f" > {path}{FOLDER_CRAWL}gospider_forms_remove")

	# Get upload-form
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_forms_remove | grep " + "'\[upload-form\]'" + f" | awk -F'- ' '{{print $2}}' > {path}{FOLDER_CRAWL}gospider.upload_forms")
	# Remove upload-form
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_forms_remove | grep -v " + "'\[upload-form\]'" + f" > {path}{FOLDER_CRAWL}gospider_upload_forms_remove")

	# Get href, javascript, linkfinder
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_upload_forms_remove | grep -E " + "'\[href|javascript|linkfinder\]'" + f" | awk -F'- ' '{{print $2}}' > {path}{FOLDER_CRAWL}gospider_href_js_link_temp 2>/dev/null")
	# Remove href, javascript, linkfinder
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_upload_forms_remove | grep -Ev " + "'\[href|javascript|linkfinder\]'" + f" > {path}{FOLDER_CRAWL}gospider_href_js_link_remove")
	
	# Get url
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_href_js_link_remove | grep " + "'\[url\]'" + f" | awk  -F'] -' '{{print $3}}' > {path}{FOLDER_CRAWL}gospider_url_temp")
	# Remove url
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_href_js_link_remove | grep -v " + "'\[url\]'" + f" > {path}{FOLDER_CRAWL}gospider_url_remove")

	# Remove twitter.com, linkedin.com, lines starting with mailto://, file://
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_url_remove " + "| grep -Ev '(mailto://|file://|twitter\.com|linkedin\.com)'" + f" > {path}{FOLDER_CRAWL}gospider_unwanted_remove")

	# Sort, remove duplicates
	cmd(f"cat {path}{FOLDER_CRAWL}gospider_unwanted_remove | uro | sort -u > {path}{FOLDER_CRAWL}out_temp")
	# Remove domain not in scope
	cmd(f"cat {path}{FOLDER_CRAWL}out_temp| grep -E '{domain.split('.')[0]}" + "\.'" + f"{domain.split('.')[1]} > {path}{FOLDER_CRAWL}gospider.out")

	# Get .js files
	cmd(f"cat {path}{FOLDER_CRAWL}gospider.out | grep " + "'\.js' | grep -v '\.json'" + f" > {path}{FOLDER_CRAWL}gospider.js")
	# Remove .js files
	cmd(f"cat {path}{FOLDER_CRAWL}gospider.out | grep -v " + "'\.js'" + f" > {path}{FOLDER_CRAWL}gospider_removed_js.out")

	# Before scanning, make sure that you only have 200 codes
	cmd_screen(f"cat {path}{FOLDER_CRAWL}gospider_removed_js.out | httpx -sc -cl -nc -fr -silent | tee {path}{FOLDER_CRAWL}httpx.http")
	cmd(f"cat {path}{FOLDER_CRAWL}httpx.http | grep " + "'200\]'" + f" | awk -F' ' '{{print $1}}' > {path}{FOLDER_CRAWL}httpx_200.http")

	end_print("PARSING")


def remove_unused_files_gospider_gauplus(domain, path):
	"""
		Used to clean unnecessary files
	"""
	start_print("REMOVING CRAWLER")
	cmd(f"rm {path}{FOLDER_CRAWL}merge {path}{FOLDER_CRAWL}gospider.out {path}{FOLDER_CRAWL}gospider_unwanted_remove {path}{FOLDER_CRAWL}gospider_removed_js.out {path}{FOLDER_CRAWL}out_temp {path}{FOLDER_CRAWL}gospider.out {path}{FOLDER_CRAWL}gospider_url_remove {path}{FOLDER_CRAWL}gospider_upload_forms_remove {path}{FOLDER_CRAWL}merge_temp {path}{FOLDER_CRAWL}gauplus {path}{FOLDER_CRAWL}{domain.replace('.', '_')} {path}{FOLDER_CRAWL}gospider_href_js_link_remove {path}{FOLDER_CRAWL}gospider_href_js_link_temp {path}{FOLDER_CRAWL}gospider_url_temp {path}{FOLDER_CRAWL}gospider_url_remove {path}{FOLDER_CRAWL}gospider_subdomain_remove {path}{FOLDER_CRAWL}gospider_forms_remove {path}{FOLDER_CRAWL}{domain}.gospider_href_js_link_remove {path}{FOLDER_CRAWL}{domain}.gospider_url_remove {path}{FOLDER_CRAWL}{domain}.gauplus 2>/dev/null")
	end_print("REMOVING CRAWLER")