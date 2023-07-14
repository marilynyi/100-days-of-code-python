def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        add_function = function(args[0], args[1])
        print(f"It returned: {add_function}")
    return wrapper

@logging_decorator
def add_or_remove(animal, *kwargs):
    with open("zoo.txt", "r+") as file:
        
        zoo = [line.strip() for line in file.readlines()]

        if kwargs[0].lower() == "add":
            if animal not in zoo:
                file.write(f"{animal}\n")
                return f"{animal.title()} added."
            else:
                return f"{animal.title()} not added (already exists)."
        elif kwargs[0].lower() == "remove":
            if animal in zoo:
                zoo = [line for line in zoo if line != animal]
                file.seek(0)
                file.truncate() 
                file.write('\n'.join(zoo))
                file.write('\n')
                return f"{animal.title()} removed."
            else:
                return f"{animal.title()} not removed (does not exist)."
        else:
            return "Invalid entry. Check your inputs."


group = "test"

if group == "test":
    
    # Add new element
    add_or_remove("bear", "add")
     
    # Add existing element
    add_or_remove("gazelle", "add")
    
    # Remove new element
    add_or_remove("cheetah", "remove")
    
    # Remove existing element
    add_or_remove("lion", "remove")
    
elif group == "reset":
    
    add_or_remove("bear", "remove")
    add_or_remove("gazelle", "add")
    add_or_remove("cheetah", "remove")
    add_or_remove("lion", "add")
    