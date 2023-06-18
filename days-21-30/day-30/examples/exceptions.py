try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdfs"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else: # if try succeeds, it jumps to this line
    content = file.read()
    print(content)
finally: # runs regardless
    file.close()
    print("File was closed.")