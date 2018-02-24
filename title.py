import urllib.request
import urllib

# url = "https://www.google.com/"

url = input("Enter url : ")

sock = urllib.request.urlopen(url)
data = sock.read()


fh = open("hello.txt", "wb")

fh.write(data)

fh.close()

try :
	f = open("hello.txt", encoding="utf8")
	searchlines = f.readlines()
except :
	f = open("hello.txt", "r")
	searchlines = f.readlines()

f.close()

start = -1
last = -1

# for i in searchlines:
# 	print (i)
# 	print (20 * '*-')
count = 0
for i in searchlines:
	if start == -1:
		start = i.find("<title>")
		if start != -1:
			val = count
			break
	count = count + 1


for i in searchlines:
	if last == -1:
		last = i.find("</title>")
		if last != -1:
			break

print( searchlines[count][start+7:last] )