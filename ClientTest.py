import ClassUriSeperator as CUS  # imported as CUS for convience

instance = CUS.UriSeperator()  # Create object from class
stop = False  # Setup ending
while not stop:  # Loop test for convience
    print(instance.parse(input("String here: ")))  # Terminal input string
    if input("want to stop? [y/n]") == "y":  # continue loop?
        stop = True

