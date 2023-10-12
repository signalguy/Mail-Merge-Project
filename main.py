#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def open_list():
    name_list = []
    list_file = open(r"Input\Names\invited_names.txt")
    name_list = list_file.readlines()
    list_file.close()
    return name_list

def open_letter():
    letter_file = open(r"Input\Letters\starting_letter.txt")
    letter = letter_file.read()
    letter_file.close()
    return letter

def generate_letter(letter, name):
    name = name.replace("\n", "")
    letter = letter.replace("[name]", name)
    file = open(f"Output\ReadyToSend\letter for {name}.txt", mode = "w")
    file.write(letter)
    file.close()

letter = open_letter()
names = open_list()

for name in names:
    generate_letter(letter, name)
    