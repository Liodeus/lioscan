from functions.misc import *


def launch_js(url, domain, path):
	start_print("JS")
	# Find more js path
	cmd(f"echo {url} | subjs -c 40 | grep -E '{domain.split('.')[0]}" + "\.'" + f"{domain.split('.')[1]} > {path}{FOLDER_JS}subjs.out")
	# Merge js files and remove duplicate
	cmd(f"cat {path}{FOLDER_JS}subjs.out {path}{FOLDER_CRAWL}gospider.js | sort -u > {path}{FOLDER_JS}js.out")

	# Before scanning, make sure that you only have 200 codes
	cmd(f"cat {path}{FOLDER_JS}js.out | httpx -sc -cl -nc -fr -silent | tee {path}{FOLDER_JS}httpx.js")
	cmd(f"cat {path}{FOLDER_JS}httpx.js | grep " + "'200\]'" + f" | awk -F' ' '{{print $1}}' > {path}{FOLDER_JS}httpx_200.js")

	# Find new path/links in js files
	cmd(f"for line in $(cat {path}{FOLDER_JS}httpx_200.js); do python3 {LINKFINDER_PATH} -i $line -o cli >> {path}{FOLDER_JS}linkfinder.out; done")
	# Get http/https path (URL)
	cmd(f"cat {path}{FOLDER_JS}linkfinder.out| sort -u | grep -E 'https?://' > {path}{FOLDER_JS}new_urls.out")
	# Remove URLs from the path
	cmd(f"cat {path}{FOLDER_JS}linkfinder.out| sort -u | grep -Ev 'https?://' > {path}{FOLDER_JS}linkfinder_without_urls.out")

	# Add all the new path to new URL
	with open(f"{path}{FOLDER_JS}new_path.out", 'w') as file:
		with open(f"{path}{FOLDER_JS}linkfinder_without_urls.out") as lines:
			for line in lines:
				line = line.strip()
				first_char = line[0]

				# If first char is a point, remove the point -> url/line
				if first_char == '.':
					file.write(f"{url}{line[1:]}\n")
				# If first char is a slash -> append the path to the url
				elif first_char == '/':
					file.write(f"{url}{line}\n")
				# Else append the path a slash and the path
				else:
					file.write(f"{url}/{line}\n")

	cmd(f"for line in $(cat {path}{FOLDER_JS}httpx_200.js); do python3 {SECRETFINDER_PATH} -i $line -o cli >> {path}{FOLDER_JS}secretfinder.out; done")
	end_print("JS")


def remove_unused_files_js(domain, path):
	start_print("REMOVING JS")
	cmd(f"rm {path}{FOLDER_JS}subjs.out {path}{FOLDER_JS}js.out {path}{FOLDER_JS}linkfinder_without_urls.out {path}{FOLDER_JS}linkfinder.out {path}{FOLDER_CRAWL}gospider.js 2>/dev/null")
	end_print("REMOVING JS")