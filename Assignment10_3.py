from sys import *
import os
import shutil
import time

def DirectoryCopy(source_dir, destination_dir):
    try:
        # Ensure the source directory exists
        if not os.path.exists(source_dir):
            print(f"Source directory '{source_dir}' does not exist.")
            return

        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Copy the contents of the source directory to the destination directory
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            destination_item = os.path.join(destination_dir, item)

            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item)
            else:
                shutil.copy2(source_item, destination_item)

        print(f"Directory '{source_dir}' copied to '{destination_dir}' successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to perform File Automations")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument Second_Argument")
        print("Example : DirectoryCopy.py Satyam Satyam1")
        exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()

    else:
        starttime = time.time()
        DirectoryCopy(argv[1],argv[2])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if __name__ == "__main__":
    main()

# python FileAutomation.py Directory_Name File_Name