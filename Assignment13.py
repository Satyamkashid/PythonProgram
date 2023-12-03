import os
import hashlib
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import sys

# Function to calculate the checksum (MD5 hash) of a file
def calculate_checksum(path, blocksize=1024):
    try:
        with open(path, 'rb') as file:
            hasher = hashlib.md5()
            while True:
                data = file.read(blocksize)
                if not data:
                    break
                hasher.update(data)
            return hasher.hexdigest()
    except Exception as e:
        print(f"Error calculating checksum for {path}: {e}")
        return None

# Function to find and delete duplicate files in a directory
def delete_duplicate_files(directory, log_directory):
    try:
        log_filename = os.path.join(log_directory, f'DuplicateFilesLog_{time.strftime("%Y-%m-%d_%H-%M-%S")}.log')
        duplicates = {}
        scanned_files = 0

        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                checksum = calculate_checksum(file_path)
                if checksum:
                    scanned_files += 1
                    if checksum in duplicates:
                        duplicates[checksum].append(file_path)
                    else:
                        duplicates[checksum] = [file_path]

        deleted_files = 0
        with open(log_filename, 'w') as log_file:
            for checksum, file_paths in duplicates.items():
                if len(file_paths) > 1:
                    log_file.write(f'Deleted duplicate files with checksum {checksum}:\n')
                    for file_path in file_paths[1:]:
                        log_file.write(f'- {file_path}\n')
                        try:
                            os.remove(file_path)
                            deleted_files += 1
                        except Exception as e:
                            print(f'Error deleting file {file_path}: {str(e)}')

        return log_filename, scanned_files, deleted_files
    except Exception as e:
        print(f"Error deleting duplicate files: {e}")
        return None, 0, 0

# Function to send an email with statistics
def send_email(receiver_email, log_filename, start_time, total_files_scanned, total_duplicates_found, deleted_files):
    try:
        sender_email = 'satyamkashid11@gmail.com'
        sender_password = 'uxcd vyiy yfsq btli'

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f'Duplicate File Removal Report - {time.strftime("%Y-%m-%d %H:%M:%S")}'

        body = f'Starting time of scanning: {start_time}\n'
        body += f'Total number of files scanned: {total_files_scanned}\n'
        body += f'Total number of duplicate files found: {total_duplicates_found}\n'
        body += f'Total number of deleted files: {deleted_files}\n'

        msg.attach(MIMEText(body, 'plain'))

        with open(log_filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(log_filename)}')
            msg.attach(part)

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # For TLS

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print('Email sent successfully!')
        except Exception as e:
            print(f'Error sending email: {str(e)}')
        finally:
            server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    try:
        if len(sys.argv) != 4:
            print("Usage: DuplicateFileRemoval.py <Directory> <IntervalMinutes> <ReceiverEmail>")
            sys.exit(1)

        directory = sys.argv[1]
        interval_minutes = int(sys.argv[2])
        receiver_email = sys.argv[3]

        if not os.path.exists(directory):
            print("Error: The specified directory does not exist.")
            sys.exit(1)

        log_directory = 'Marvellous'
        if not os.path.exists(log_directory):
            os.mkdir(log_directory)

        start_time = time.strftime("%Y-%m-%d %H:%M:%S")

        def job():
            log_filename, total_files_scanned, deleted_files = delete_duplicate_files(directory, log_directory)
            if log_filename:
                # Calculate the number of duplicate files found
                total_duplicates_found = deleted_files
                send_email(receiver_email, log_filename, start_time, total_files_scanned, total_duplicates_found, deleted_files)

        # Schedule the job to run at specified intervals (in minutes)
        schedule.every(interval_minutes).minutes.do(job)

        # Run the job immediately and then continue with scheduled runs
        job()

        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Script terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
