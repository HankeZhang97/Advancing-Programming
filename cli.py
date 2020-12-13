from command import commandInvoker

if __name__ == "__main__":

    while True:
        command = input("Input your command:\n")
        print("-------------------")
        if command == "exit":
            break
        res = commandInvoker.execute(command)
        print(res)
