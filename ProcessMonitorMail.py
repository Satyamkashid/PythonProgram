import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import psutil
from email import encoders
import time
import schedule
from sys import*
import os

# Email configuration
sender_email = 'satyamkashid11@gmail.com'

sender_password = 'uxcd vyiy yfsq btli'

receiver_email = 'akshayunavane4@gmail.com'

subject = """ Marvellous InfoSystem Process log genereated at : %s"""%(time)

message_body = """ Hello %s,Welcome to Marvellous InfoSystems.
        Please find attached document which contain Log of Running processes.
        Log file is created at : %s
        
        This is auto generated mail.
        
        Thanks & Regards,
        Satyam Kashid """%(receiver_email,time)

# Function to send an email with the log file
def send_email(log_filename):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(message_body, 'plain'))

    with open(log_filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(log_filename)}')
        message.attach(part)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # For TLS
    smtp_username = sender_email
    smtp_password = sender_password

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print('Email sent successfully!')

    except Exception as e:
        print(f'Error: {str(e)}')

    finally:
        server.quit()

def ProcessLog(log_dir = "Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = "-" * 80

    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")  # Format the timestamp
    log_path = os.path.join(log_dir, f"MarvellousLog_{current_time}.log")  # Use underscores instead of spaces and remove colons

    f = open(log_path,'w')
    f.write(seperator + "\n")
    f.write("Marvellous Infosystem Process Logger :" + current_time + "\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)

            listprocess.append(pinfo);
        
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    print("Log File Successfully generated at location %s" %(log_path))

    send_email(log_path)

def main():
    print("------Marvellous Infosystem by Piyush Khairnar------")

    print("Application name :"+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=="-h") or (argv[1]=='-H'):
        print("This Script is used log record of running process")
        exit()
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError as E:
        print("Error : Invalid Input",E)

    except Exception as E:
        print("Error :",E)

if __name__ == "__main__":
    main()

# In command Line Argument give time interval in command line to execute the program