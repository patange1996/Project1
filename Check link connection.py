import csv
import urllib.request
import urllib.error

f=open("Links.csv", 'r')
f1=open("check.csv",'w')
headers = "Links,Status_code\n"
f1.write(headers)
next(f)
for line in f:
    url = "https://www.mediamarkt.at" + line
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        #print('HTTPError: {}'.format(e.code))
        result = 'HTTPError: {}'.format(e.code)
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        #print('URLError: {}'.format(e.reason))
        result = 'URLError: {}'.format(e.reason)
    else:
        # 200
        # ...
        result=200
    f1.write("https://www.mediamarkt.at"+line.strip()+","+str(result)+"\n")
print("success")