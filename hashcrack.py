import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--string", help="String")
parser.add_argument("-c", "--crack", help="Crack hash", action="store_true")
parser.add_argument("-ch", "--hash", help="Create Hash", action="store_true")
parser.add_argument("-w", "--wordlist", help="Wordlist")
ps = parser.parse_args()

def crack_hash(hash):
    cracked_hash = ""
    with open(ps.wordlist) as fp:
        for line in fp:
            line = line.strip()
            if hashlib.md5(bytes(line, encoding="utf-8")).hexdigest() == hash:
                cracked_hash = line
    return cracked_hash  

if ps.string and ps.hash:
    hash = hashlib.md5(ps.string.encode())
    print(hash.hexdigest())
elif ps.string and ps.crack:
    hash = ps.string
    if hash:
        print(f"Hash was found : {crack_hash(hash)}")
    else:
        print("[!] Not found")
else:
    print("Something went wrong. Try --help ")