from functions.misc import *
from json import dumps
import requests


# Thanks HaxUnit
def acunetix(apikey, domain, path):
	start_print("ACUNETIX")

	# if docker not started start it 
	# start docker acunetix

	r = requests.Session()
	data = {}
	cookies = {'ui_session': apikey}
	headers = {'x-auth': apikey, 'Content-Type': 'application/json'}

	target_group_data = {"name": domain, "description": ""}
	group_id = r.post('https://localhost:3443/api/v1/target_groups', headers=headers, cookies=cookies, data=dumps(target_group_data), verify=False).json()["group_id"]

	print(f"Launching scan for : {domain}")
	data = {
		"targets": [{
			"address": domain,
			"description": ""
		}],
		"groups": [group_id]
	}

	if data:
		response = r.post('https://localhost:3443/api/v1/targets/add', headers=headers, cookies=cookies, data=dumps(data), verify=False).json()

		for target in response["targets"]:
			data = {
				"profile_id": "11111111-1111-1111-1111-111111111111",
				"ui_session_id": "56eeaf221a345258421fd6ae1acca394",
				"incremental": False,
				"schedule": {
					"disable": False,
					"start_date": None,
					"time_sensitive": False
				},
				"target_id": target["target_id"]
			}

			r.post('https://localhost:3443/api/v1/scans', headers=headers, cookies=cookies, data=dumps(data), verify=False)

	end_print("ACUNETIX")