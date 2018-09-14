from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACccab7228249520188d243e3ab91bd96e"
# Your Auth Token from twilio.com/console
auth_token  = "b2690c3cc2551fde497c6e8a4456c015"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+9647506513237", 
    from_="+17573849442",
    body="Hello from Python!")

print(message.sid)
