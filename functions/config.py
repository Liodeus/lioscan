from subprocess import PIPE, Popen
import urllib3


# Disable warnings
urllib3.disable_warnings()

# Folders creation
FOLDER_TECHNOLOGIE = "/TECHNOLOGIE/"
FOLDER_CRAWL = "/CRAWL/"
FOLDER_JS = "/JS/"

# Path off the tools
WEB_ANALYZE_TECHNO_PATH = "./tools/technologies.json"
LINKFINDER_PATH = "./tools/LinkFinder/linkfinder.py"
SECRETFINDER_PATH = "./tools/secretfinder/SecretFinder.py"

# Browser used
BROWSER = "firefox"