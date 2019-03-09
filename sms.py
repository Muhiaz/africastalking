#Import the AfricasTalking SDK into your app
import africastalking

#Create your credentials
username = "muhia"
apikey = "f70b7e1e40b0cbc2111e0bae9c469c6d03a3ad8c4dca0031c7c5a1d922b99ab6"

#Initialize the SDK
africastalking.initialize(username, apikey)

#Get the SMS service
sms = africastalking.SMS

#Define some options that we will use to send the SMS
recipients = ['+254700132577']
message = 'You have successfully toped up your account'
# sender = 'swahilibox'

#Send the SMS
try:
    #Once this is done, that's it! We'll handle the rest
    response = sms.send(message, recipients)
    print(response)
except Exception as e:
    print('Houston, we have a problem {e}')