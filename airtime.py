# Import the Africa's Talking module here
import africastalking

#Define credentials here
username = "muhia"
api_key = "4825ff253c9a270e417e5059ea53f36bc64ed41d1a64a67a0b135378e7796a04"

#Authenticate with the service
africastalking.initialize(username, api_key)

#Define the airtime service
airtime = africastalking.Airtime 

#Define user variables
phone_number = "+254718139814"
amount = "8"
currency_code = "KES"

#Send the airtime!
response = airtime.send(phone_number = phone_number, amount = amount, currency_code = currency_code)
print(response)