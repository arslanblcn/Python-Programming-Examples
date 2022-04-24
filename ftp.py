from email.policy import default
from ftplib import FTP
import argparse
from time import sleep
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Getting arguments from user in order to login to FTP

parser = argparse.ArgumentParser(description="FTP Connection Tool")
parser.add_argument("-s", "--server", required=True, help="FTP Server")
parser.add_argument("-p", "--port", required=False, help="FTP Port - Default is 21", default=21)
parser.add_argument("-u", "--user", required=True, help="Username")
parser.add_argument("-pw", "--password", required=True, help="Password")
parser.add_argument("-f", "--file", required=False, help="Choose file to upload")
parse = parser.parse_args()   

# Connecting to FTP
ftp = FTP()
ftp.connect(parse.server, int(parse.port))
print(f"{Fore.CYAN}[*] Connecting to FTP")
sleep(0.3)
try:
    # Login process
    ftp.login(parse.user, parse.password)
    sleep(0.5)
    print(f"{Fore.LIGHTCYAN_EX}[*] Logged into FTP - To Getting interactive write \"help\"")
    ftp.cwd("ftp/upload")
except:
    print(f"{Fore.RED}[!] Username or Password is wrong")
    exit()

# Command Methods
def printHelp(): # Help Method
    text = f"""{Fore.LIGHTMAGENTA_EX}
    dir \t\t\t put \t\t\t get
    mkdir \t\t\t rmdir \t\t\t rename
    delete
    """
    print(text)

def listDir(): # Directory listing
    ftp.dir()

def createDir(): # Create Directories
    dirname = input("(dir-name : )")
    ftp.mkd(dirname)
    print(f"{Fore.LIGHTCYAN_EX}[*] {dirname} has been created!")

def removeDir(): # Remove Directories
    dirname = input("(dir-name : )")
    ftp.rmd(dirname)
    print(f"{Fore.LIGHTRED_EX}[*] {dirname} has been deleted!")

def loadFile(): # Upload Files
    filename = input("(local-file) : ")
    with open(filename, "rb") as file:
        ftp.storbinary(f"STOR {filename}", file)
    print(f"{Fore.LIGHTCYAN_EX}[*] {filename} has been stored!")

def downloadFile(): # Download Files
    filename = input("(remote-file) : ")
    with open(filename, "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)
    print(f"{Fore.LIGHTCYAN_EX}[*] {filename} just downloaded!")   

def renameFile(): # Rename Files
    rFile = input("(file-name):")
    tFile = input("(to-name):")
    ftp.rename(rFile, tFile)
    print(f"{Fore.LIGHTCYAN_EX}[*] File's name changed!")

def deleteFile(): # Delete files
    rFile = input("(file-name:)")
    ftp.delete(rFile)
    print(f"{Fore.LIGHTRED_EX}[*] File's deleted!")  

## Handling Commands
switcher = {
    "dir": listDir,
    "put": loadFile,
    "get": downloadFile,
    "mkdir": createDir,
    "rmdir": removeDir,
    "rename": renameFile,
    "delete": deleteFile,
}

commandList = ["dir", "put", "get", "mkdir", "rmdir", "rename", "delete"]

def switch(cmd):
    return switcher.get(cmd, default)()

def mainFTP():
    while True:
        command = input(">>> ")
        if(command == "help"):
            printHelp()
        elif(command == "exit"):
            print(f"{Fore.LIGHTYELLOW_EX}Exiting FTP")
            ftp.close()
            break
        elif(command in commandList):
            print(switch(command))
        else:
            print(f"{Fore.RED}Unknown command")

if __name__ == "__main__":
    mainFTP()