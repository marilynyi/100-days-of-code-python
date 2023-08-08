import morse_code

def main():
    message = input("Send a message: ").upper()
    encoded_message = encode(message)
    print(f"Message sent as: {decode(encoded_message)}")
    print(f"{encoded_message}")

def encode(message):
    coded_message = ""
    
    for index, char in enumerate(message.upper()):
        try:
            coded_message += morse_code.dictionary[char]
            if index == len(message)-1:
                break
            # Space between chars is equal to 3 dits
            coded_message += f"{' '*3}"
        except KeyError:
            if char == " ":
                # Space between words is equal to 7 dits
                coded_message += f"{' '*7}" 
            else:
                # Substitute char with filler '?' symbol if not in dict
                coded_message += "?"
                
    return coded_message
 
def decode(message):
    coded_words = message.split("       ")
    coded_words = [word.strip() for word in coded_words]
        
    decoder_dict = {value: key for key, value in morse_code.dictionary.items()}
    decoded_message = ""
     
    for index, word in enumerate(coded_words):
        coded_chars = word.split("   ")
        for char in coded_chars:
            try:    
                decoded_message += decoder_dict[char]
            except KeyError:
                decoded_message += "?"
        if index == len(coded_words)-1:
            break
        decoded_message += " "
    
    return decoded_message


if __name__ == "__main__":
    main()