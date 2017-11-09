from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0e5fd1e196e1afb6ef8e4af4a187f622"
# Your Auth Token from twilio.com/console
auth_token  = "8ea6e06d779b765c3e2d29dc3b14e0f3"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+971526464173",
    from_="+16073912311",
    body="Hello from Python!")

print(message.sid)
