import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import schedule
import time
from datetime import datetime, timedelta

def send_birthday_email(recipient_email, recipient_name, sender_email, sender_password):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # For TLS
        smtp_username = sender_email
        smtp_password = sender_password

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Create a MIME message for the birthday email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = 'Happy Birthday!'
        
        custom_message = f'Happy Birthday, {recipient_name}!\n\nBest wishes from Python Script'
        message.attach(MIMEText(custom_message, 'plain'))

        # Send the birthday email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)

        # Close the SMTP server connection
        server.quit()

    except Exception as e:
        print(f'Error: {str(e)}')

def schedule_birthday_emails(csv_file_path, sender_email, sender_password):
    try:
        with open(csv_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row

            for row in reader:
                if len(row) >= 3:
                    recipient_email = row[0].strip()
                    recipient_name = row[1].strip()
                    birthdate_str = row[2].strip()

                    # Parse the birthdate string into a datetime object
                    birthdate = datetime.strptime(birthdate_str, '%d-%m-%Y')

                    # Calculate the time until the recipient's birthday
                    current_datetime = datetime.now()
                    current_year = current_datetime.year

                    if current_datetime > birthdate.replace(year=current_year):
                        # If the birthday has already passed this year, set it for next year
                        current_year += 1

                    time_until_birthday = birthdate.replace(year=current_year) - current_datetime

                    # Print the time remaining before sending the email
                    print(f'Time until next birthday email for {recipient_name}: {time_until_birthday}')
                    
                    # Schedule the birthday email to be sent at the calculated time
                    schedule.every(time_until_birthday.total_seconds()).seconds.do(
                        send_birthday_email, recipient_email, recipient_name, sender_email, sender_password)

    except Exception as e:
        print(f'Error: {str(e)}')

def main():
    try:  
        if len(sys.argv) != 2:
            print("Usage: python script.py <csv_file>")
            sys.exit(1)

        csv_file_path = sys.argv[1]
        sender_email = 'satyamkashid11@gmail.com'
        sender_password = 'uxcd vyiy yfsq btli'  # Store your password securely, don't keep it in plain text in your script.
        # Schedule the task to read the CSV file and send birthday emails
        schedule_birthday_emails(csv_file_path, sender_email, sender_password)

        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        print("Script terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
