from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6ec0a81e27f985f141f9ec99566519b3"
# Your Auth Token from twilio.com/console
auth_token  = "c58b0eec058b98aff4dae983f2b09365"

client = Client(account_sid, auth_token)

message = client.messages.create(
  to="+64226276202",
  from_="+14804187197",
  body="My name is Ron Burgandy")

print(message.sid)



