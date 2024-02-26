class Synchronous:

    def __init__():
        print("Synchronous class created")

    def startTasks(self):
        self.task1()

    def task1(self):
        print("Send email")
        print("Receive email")
        print("Reply email")
        self.task2()
    
    def task2(self)
        print("Call friend")
        print("Receive call")
        print("End call")
        self.task3()

    def task3(self):
        print("Read book")
        print("Sleep")
        print("Dream")

if __name__ == "__main__":
    sync = Synchronous()
    sync.startTasks()


