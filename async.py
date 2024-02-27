import asyncio


class Asynchronous:

    def __init__(self):
        print("Asynchronous class created")

    def runTasks(self):
        asyncio.run(self.task1())

    async def task1(self):
        print("Send 1st email")
        asyncio.create_task(self.task2())
        await asyncio.sleep(5)  # once completed, return to next line
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

    async def fetchData(self):
        print("Fetching data...")
        await asyncio.sleep(2)
        print("Data fetched")
        return {"data": 100}  # return data as dictionary

    async def timer(self):
        for i in range(10):
            print(i)
            await asyncio.sleep(2)


async def main():
    asyncTask = Asynchronous()

    x = asyncio.create_task(asyncTask.fetchData())
    y = asyncio.create_task(asyncTask.timer())
    data = await x
    print(data)
    await y


asyncio.run(main())
