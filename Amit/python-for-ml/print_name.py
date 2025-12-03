while True:
    name = input("Please enter your name: ")

    if name:
        print(f"Hello, {name}! Welcome!")
        break
    else:
        print("Name cannot be empty,Please try again.")
