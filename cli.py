from command import commandInvoker


class Client(object):
    def __init__(self):
        self.invoker = commandInvoker
        print("server ready")

    def run(self):
        while True:
            command = input("Input your command:\n")
            print("-------------------")
            if command == "exit":
                break
            res = commandInvoker.execute(command)
            print(res)


if __name__ == "__main__":
    c = Client()
    c.run()

