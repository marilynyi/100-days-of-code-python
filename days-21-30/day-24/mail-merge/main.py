# Read each line to create a list of invited names
with open("./Input/Names/invited_names.txt") as invited_names:
    invited_names_list = invited_names.readlines()

# Check format for invitation list
# print(invited_names_list)

# Read the contents of the example letter as a string
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    starting_contents = starting_letter.read()

    # Instantiate placeholder name format
    placeholder_name = "[name]"

# Create a custom letter for each name on the invitation list
for invited_name in invited_names_list:

    # Strip off the trailing newline and replace spaces with underscores
    invited_name = invited_name.strip().replace(" ", "_")

    # Replace placeholder name text with invited name
    customized_letter = starting_contents.replace(placeholder_name, invited_name)

    # Write to a new file the customized letter with the invited name included in the file name
    with open(f"./Output/ReadyToSend/letter_for_{invited_name}.txt", mode = "w") as letter:
        letter.write(customized_letter)

