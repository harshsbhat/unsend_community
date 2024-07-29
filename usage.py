from unsendcommunity import Unsend

api_key = 'us_cpm5q0d77f_bea486174ee656b6d5f12d415871185c' 
client = Unsend(key=api_key, url='http://localhost:3000')



payload = {
    "to": "harsh121102@gmail.com",
    "from": "hello@mail.harshbhat.me",
    "subject": "Unsend test email",
    "text": "hello,\n\nUnsend is the best open source sending platform",
    "html": "<p>hello,</p><p>Unsend is the best open source sending platform</p><p>check out <a href='https://unsend.dev'>unsend.dev</a></p>",
}


response = client.send_email(payload)
print("Send Email Response:", response)


email_id = 'clz6iydbu000d8kmcjnf4aimv' 
email_response = client.get_email(email_id)
print("Get Email Response:", email_response)

domain_response = client.get_domain()
print("Get Domain Response:", domain_response)