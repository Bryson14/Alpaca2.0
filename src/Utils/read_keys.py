import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent.parent
KEYS_FILE = BASE_DIR.joinpath('Data').joinpath("Alpaca_Keys.txt")


with open(KEYS_FILE) as fil:
	data = fil.read()
	data = data.splitlines()
	keys = {"keyID": "", "secretKey": ""}

	for line in data:
		if line.startswith('keyID'):
			keys["keyID"] = line.split("=")[-1].strip(" ")
		elif line.startswith("secretKey"):
			keys["secretKey"] = line.split("=")[-1].strip(" ")


def get_keys():
	return keys
