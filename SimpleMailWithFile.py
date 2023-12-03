import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
sender_email = 'satyamkashid11@gmail.com'

sender_password = 'uxcd vyiy yfsq btli'

print("How Many Email Id You Want to enter")
size = int(input())

receiver_emails = []

for i in range(size):

    # receiver_email = 'akshayunavane4@gmail.com'
    print("Enter Your Email id")
    receiver_email = str(input())

    receiver_emails.append(receiver_email)

subject = 'Hello, this is a test email with attachments!'

message_body = 'This is the body of the email.'

# Create a MIME message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the message body
message.attach(MIMEText(message_body, 'plain'))

# Attach files
files_to_attach = ['D:/Important/DBMS_Notes.pdf']  # Replace with your file paths

for file_path in files_to_attach:
    attachment = open(file_path, 'rb')
    base = MIMEBase('application', 'octet-stream')
    base.set_payload((attachment).read())
    encoders.encode_base64(base)
    base.add_header('Content-Disposition', f'attachment; filename={file_path}')
    message.attach(base)

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
    for receiver_email in receiver_emails:
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print('Email with attachments sent successfully!')

except Exception as e:
    print(f'Error: {str(e)}')

finally:
    # Close the SMTP server connection
    server.quit()
