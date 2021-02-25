from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC2f2de3002b7e48264aca16ef97deeb02'
auth_token = 'df9670b4c07d1cbff20701edd0b50f88'


def send_intruder_alert():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Intruder ALERT!\nUnknown person has entered the monitored area',
        from_='whatsapp:+14155238886',
        to='whatsapp:+5216623294059'
    )
    print('Intruder alert sent with message id: %s' % message.sid)


if __name__ == '__main__':
    send_intruder_alert()
