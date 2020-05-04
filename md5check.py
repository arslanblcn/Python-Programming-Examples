import hashlib
import datetime
time = datetime.datetime.now()
fileValue = "514a5ddc659b9510bebd7546e63a1540"
md5Hash = hashlib.md5()
openFile = open("/home/arslan/Desktop/creds.txt","rb")
content = openFile.read()
md5Hash.update(content)
digest = md5Hash.hexdigest()
if fileValue != digest :
    f = open("/home/arslan/Desktop/warning.txt","a")
    f.write("File had changed.")
    f.write(str(time))
    f.write("\n")
    f.close()
else:
    f = open("/home/arslan/Desktop/note.txt","a")
    f.write("File still seems the same. Date : ")
    f.write(str(time))
    f.write("\n")
    f.close()