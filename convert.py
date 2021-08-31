import requests

def convert(x, y, z):
	x = x.get()
	y = y.get()
	z = z.get()

	x = int(x)
	y = str(y[0]+y[1]+y[2])
	z = str(z[0]+z[1]+z[2])

    #Create URL
	url = "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=93f60be53c2effb9f511".format(y, z)
    #Request API Data
	resp = requests.get(url=url)
    #Format Data into JSON 
	data = resp.json()
    #Format JSON into STR
	value = data["{}_{}".format(y, z)]

	c = x * value

	print(c)
	return value