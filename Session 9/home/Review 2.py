import requests
# API
# Weather App -> openweather
# APIkey -> kilide khase karbar
# Library -> requests

url = "link + APIkey + variable"
response = requests.get(url) # Response 200
# HTTP Code -> 200 OK
# 404 -> Page not found
# 500 -> server error
data = response.json()
data = {
    "weather": [ {"main": 12} ]
}
# json -> dictionary
condition = data["weather"][0]["main"]


# Function
# karmand hayi ke ma estekhdam mikonim
# az tekrar code jologiri mikonim
# Arguments -> maqadire vorodi tabe
# Start def
def kharid_nan(pol):
    return pol - 100
# End def

# Start main
# End main
