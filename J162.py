time_zones = {
	"PST" : -8,
	"MST" : -7,
	"EST" : -5,
	"GMT" : 0,
	"MSK" : 3,
	"IST" : 5.5,
	"NPT" : 5.75,
	"HKT" : 8,
	"JST" : 9,
	"ACDT" : 10.5
}
temp = list(map(int, input().split())) #break this apart for the 24 hour format time in zone B for now
h = temp[0]
m = temp[1]
zone1 = input()
z1 = time_zones.get(zone1)
zone2 = input()
z2 = time_zones.get(zone2)
h += int(z2-z1)
temp2 = int(((z2-z1)-int(z2-z1))*60)
m += temp2

if (m>60):
	h += int(m/60)
	m = m % 60

while (m<0):
	m += 60
	h -= 1

if (h>24):
	h = h % 24

while (h<0):
	h += 24

if (h<10 and m<10):
	print ("0"+str(h)+" 0"+str(m))
elif (h<10):
	print ("0"+str(h)+" "+str(m))
elif (m<10):
	print (str(h)+" 0"+str(m))
else:
	print (h, m)
