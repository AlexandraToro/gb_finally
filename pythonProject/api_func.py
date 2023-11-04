import requests
import yaml

with open("testdata.yaml", "r") as f:
	d = yaml.safe_load(f)


def auth():
	data = {
		"username": d["username"],
		"password": d["password"]
	}
	print(d["url_auth"])
	res = requests.post(url=d["url_auth"], data=data)
	return res.status_code


def username():
	headers = {
		'X-Auth-Token': d["token"]
	}
	res = requests.get(url=d["url_id"], headers=headers)
	return res.json()['username']


if __name__ == '__main__':
	print(auth())
	print(username())