from twilio.rest import Client



account_sid=''
auth_token=''

client=Client(account_sid,auth_token)

message=client.messages \
  .create(
    body='hello Hodan wa najah said ahmed o Marakeykanka ka so Hadleyseee HHHH',
    from_='',
    to=''
  )



print(message.sid)