import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = 'satyamkashid11@gmail.com'

sender_password = 'uxcd vyiy yfsq btli'

receiver_email = 'akshayunavane4@gmail.com'

subject = 'Hello, this is a test email!'

message_body = 'Hello Sir,This Mail is Auto generated by Satyam Kashid For his Project Purpose'

# Create a MIME message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the message body
message.attach(MIMEText(message_body, 'plain'))

# Connect to the SMTP server (in this case, Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # For TLS
smtp_username = sender_email
smtp_password = sender_password

# Establish a secure connection with the SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('Email sent successfully!')

except Exception as e:
    print(f'Error: {str(e)}')

finally:
    # Close the SMTP server connection
    server.quit()