class Synchronous:

    def __init__(self):
        print("Synchronous class created")

    def startTasks(self):
        self.task1()

    def task1(self):
        print("Send email")
        print("Receive email")
        print("Reply email")
        self.task2()

    def task2(self):
        print("Send email")
        print("Receive email")
        print("Reply email")
        self.task3()

    def task3(self):
        print("Send email")
        print("Receive email")
        print("Reply email")


if __name__ == "__main__":
    syncTask = Synchronous()
    syncTask.startTasks()
