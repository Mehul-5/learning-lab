import asyncio


async def fetch_data(id, delay):
    print("Fatch data..")
    await asyncio.sleep(delay)
    print("data fetched")
    return{"id": id, "data": "some data from {id}"}



async def main():
    # print("start of main corutine")
    # task1 = asyncio.create_task(fetch_data(1, 2))
    # task2 = asyncio.create_task(fetch_data(2, 1))

    # result1 = await task1
    # result2 = await task2
    # print(f"Received result: {result1}, {result2}")   
    # print("end of main corutine")

    # results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

    # for result in results:
    #     print(f"Received results: {result}")

    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # after the task group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")



asyncio.run(main())