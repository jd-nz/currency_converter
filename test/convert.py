import requests

def convert(amount, currency1, currency2):
    #Create URL
    url = "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=93f60be53c2effb9f511".format(currency1, currency2)
    #Request API Data
    resp = requests.get(url=url)
    #Format Data into JSON 
    data = resp.json()
    #Format JSON into STR
    value = data["{}_{}".format(currency1, currency2)]

    totalValue = amount * value

    return totalValue