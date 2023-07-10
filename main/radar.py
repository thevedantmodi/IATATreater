import requests

url = "https://flight-radar1.p.rapidapi.com/flights/list-by-airline"

querystring = {"airline":"AXM"}

headers = {
	"X-RapidAPI-Key": "cf4c415c3dmshe884aac01254dbfp1e015djsn3b64b6288519",
	"X-RapidAPI-Host": "flight-radar1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())