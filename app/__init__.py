

def start():
    choice=input("Would you like to view or add? (v/a)> ")
    if choice.lower()=="v":
        view()
    elif choice.lower()=="a":
        add()


def add():
    u=input("Enter your username: ")
    p=input("Enter your password: ")
    with open("up.txt", "a") as f:
        f.write(f"{u}|{p}")


def view():
    with open("up.txt", "r") as fo:
        for line in fo.readlines():
            u,p = line.split("|")
            print(f"username: {u} and password: {p}")


if __name__=="__main__":
    start()