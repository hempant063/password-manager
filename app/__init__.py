

def start():
    choice=input("Would you like to view or add? (v/a)> ")
    if choice.lower()=="v":
        view()
    elif choice.lower()=="a":
        add()


def add():
    u=input("Enter your username: ")
    p=input("Enter your password: ")
    with open("up.txt", "w") as f:
        f.write(f"{u}|{p}")


def view():
    pass


if __name__=="main":
    start()