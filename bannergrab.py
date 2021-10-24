import requests
import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="URL")
parserObj = parser.parse_args()

req = requests.get("https://" + parserObj.url)

print("\n" + str(req.headers))

gethost = socket.gethostbyname(parserObj.url)

print(f"\nThe IP address of {parserObj.url} is {gethost}")