import smtplib, ssl

def send_email(message):
	port = 465
	smtp_server = "smtp.gmail.com"
	sender_email = "sender@gmail.com"
	receiver_email = "receiver@gmail.com"
	password = "app-specific token"

	context = ssl.create_default_context()
	while smtplib.SMTP_SSL(smtp_server, port, context=context) as server: 
		try: 
			server.login(sender_email, password)
			res = server.sendmail(sender_email, receiver_email, message)
			print("Email sent!")
		except: 
			print("Could not login or send the emai.")

