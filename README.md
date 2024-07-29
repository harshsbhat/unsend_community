# Unsend Python Package
The Unsend Python package lets you interact with the Unsend API to send and manage emails as well as domains. This README provides a quick guide on using the package to send emails and retrieve email information.

## Installation
To install the Unsend package, you can use pip:

```bash 
pip install unsendcommunity
```

## Usage
Below is an example of how to use the Unsend package to send an email and retrieve email information.

### Initialize
Change the URL accordingly if you are using self self-hosted version of Unsend. The default URL will be https://app.unsend.dev.
```python

from unsendcommunity import Unsend

# Initialize the Unsend client
api_key = 'us_cpm5q0d77f_bea486174ee656b6d5f12d415871185c'
client = Unsend(key=api_key, url='https://app.unsend.dev')

```

### Sending Emails
To send an email you will need to define the payload. After definition, you can use the ```.send_emails``` method to send emails with the payload as a parameter.

```python
payload = {
    "to": "youremail@gmail.com",
    "from": "hello@domainname.com",
    "subject": "Unsend test email",
    "text": "hello,\n\nUnsend is the best open source sending platform",
    "html": "<p>hello,</p><p>Unsend is the best open source sending platform</p><p>check out <a href='https://unsend.dev'>unsend.dev</a></p>",
}```

# Send the email
response = client.send_email(payload)
print("Send Email Response:", response)
```
### Retrieve Emails using the id 
The email will be retrieved using the ID you get after sending the mail. 
```python
email_id = 'email-id-from-unsend'
email_response = client.get_email(email_id)
print("Get Email Response:", email_response)
```

The sample response of ``get_email`` is shown below:


```bash
{
  "data": {
    "id": "clz6iydbu000d8kmcjnf4aimv",
    "teamId": 1,
    "to": [
      "harsh121102@gmail.com"
    ],
    "from": "hello@mail.harshbhat.me",
    "subject": "Unsend test email",
    "html": "<p>hello,</p><p>Unsend is the best open source sending platform</p><p>check out <a href='https://unsend.dev'>unsend.dev</a></p>",
    "text": "hello,\n\nUnsend is the best open source sending platform",
    "createdAt": "2024-07-29T05:04:21.498Z",
    "updatedAt": "2024-07-29T05:04:27.130Z",
    "emailEvents": [
      {
        "emailId": "clz6iydbu000d8kmcjnf4aimv",
        "status": "FAILED",
        "createdAt": "2024-07-29T05:04:27.124Z",
        "data": {
          "error": "MessageRejected: Email address is not verified. The following identities failed the check in region US-EAST-1: harsh121102@gmail.com"
        }
      }
    ]
  },
  "error": null
}
```

### Retrieve domain information

Retrieves domain information 
Domains that are associated with this account will be displayed with their detailed information. 

```python
domain_response = client.get_domain()
print("Get Domain Response:", domain_response)
```

Sample response of the ``get_domain`` method

```bash
{
  "data": [
    {
      "id": 1,
      "name": "mail.harshbhat.me",
      "teamId": 1,
      "status": "SUCCESS",
      "region": "us-east-1",
      "clickTracking": false,
      "openTracking": false,
      "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5dFn1FdRfU1243apb5aMtxVSihb0QJdoJopzr3JmKLQSsyrnwKdX7sfQ8v9Az0Xh0GTIyTUGVwHQdxM79gewSn7MyCVzteGBzoQMpuMzDaIoP5lprvxap1D1iosMJYztGdAM4694R+GuU+XSI/0OasDDlYYo7Ua8gYO8LLAHrxQrtvUOgCvbOQYfkz6zQUu9B0Zba+xNp04klHHcB32Ik2Tn6oWFTpvxbTpfFXOq94uB1TxqeBeEGAdMaQu/PpiB8eumKhxHwIA3vJeYfJ3YbLzI+NbnBAlAEMXOmrX59KvVaEKgtTHIQ//yT8gkDtasGvO6uengi8D53MkLO6/ScwIDAQAB",
      "dkimStatus": "SUCCESS",
      "spfDetails": "SUCCESS",
      "dmarcAdded": false,
      "errorMessage": null,
      "subdomain": "mail",
      "isVerifying": false,
      "createdAt": "2024-07-26T05:52:17.199Z",
      "updatedAt": "2024-07-26T05:57:27.790Z"
    }
  ],
  "error": null
}
```

#### Note: This is not an official unsend library.