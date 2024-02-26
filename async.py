import asyncio


class Asynchronous:

    def __init__(self):
        print("Asynchronous class created")

    def runTasks(self):
        asyncio.run(self.task1())

    async def task1(self):
        print("Send 1st email")
        asyncio.create_task(self.task2())
        await asyncio.sleep(5)
        print("Recieved 1st email")

    async def task2(self):
        print("Send 2nd email")
        asyncio.create_task(self.task3())
        await asyncio.sleep(2)
        print("Recieved 2nd email")

    async def task3(self):
        print("Send 3rd email")
        await asyncio.sleep(2)
        print("Recieved 3rd email")


if __name__ == "__main__":
    asyncTask = Asynchronous()
    asyncTask.runTasks()
