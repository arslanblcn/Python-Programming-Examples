import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="URL")
parserURL = parser.parse_args()
with open("subdomain-1000.txt", "r") as fp:
    lines = fp.readlines()
    for subdomain in lines:
        check_domain = f"http://{subdomain.strip()}.{parserURL.url}"
        
        try:
            requests.get(check_domain)
        except requests.exceptions.ConnectionError:
            print("Connection Refused by the server")
            pass
        else:
            print (f"Valid Domain {check_domain}")