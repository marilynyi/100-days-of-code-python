import main

def test_letters():
    message = "ThiS mESsAgE hAs OnLy leTteRs"
    encoded_message = main.encode(message)
    decoded_message =  main.decode(encoded_message)
    assert decoded_message == "THIS MESSAGE HAS ONLY LETTERS"
    
def test_numbers():
    message = "1234567890"
    encoded_message = main.encode(message)
    decoded_message =  main.decode(encoded_message)
    assert decoded_message == "1234567890"

def test_recognized_symbols():
    message = f'!@$?&()-_,.+=/:;\"'
    encoded_message = main.encode(message)
    decoded_message =  main.decode(encoded_message)
    assert decoded_message == f'!@$?&()-_,.+=/:;\"'
    
def test_not_in_dict():
    message = f"<> %* ^# []\\"
    encoded_message = main.encode(message)
    decoded_message =  main.decode(encoded_message)
    assert decoded_message == "? ? ? ?"   
