import requests,re
reqlist = requests.get('https://api.kawalcorona.com').json()
cari = input("masukkan nama negara : ")
for x in reqlist:
	a = re.search(cari,x['attributes']['Country_Region'].lower())
	if a!=None:
		print("______________________________________\n"+x['attributes']['Country_Region']+"\nterdeteksi \t: "+str(x['attributes']['Confirmed'])+"\nmati \t\t: "+str(x['attributes']['Deaths'])+"\nsembuh \t\t: "+str(x['attributes']['Recovered'])+"\nsakit \t\t: "+str(x['attributes']['Confirmed']-x['attributes']['Deaths']-x['attributes']['Recovered']))