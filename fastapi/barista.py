import asyncio
import time

def brew_coffee(delay):
    print("Coffee is brewing")
    time.sleep(delay)
    print("coffee is ready")

async def brew_coffee_async(delay):
    print("Coffee is brewing")
    await asyncio.sleep(delay)
    print("coffee is ready")

def run_sync():
    print("\n sync brewing")
    start = time.time()
    
    for i in range(3):
        brew_coffee(2)
    
    end = time.time()
    print(f"total time = {end-start: .2f} seconds")

async def run_async():
    print("\n async brewing")
    start = time.time()
    
    tasks = []
    for i in range(3):
        task = asyncio.create_task(brew_coffee_async(2))
        tasks.append(task)

    await asyncio.gather(*tasks)

    end = time.time()
    print(f"total time = {end-start: .2f} seconds")



if __name__ == "__main__":
    
    print("order is given")
    
    run_sync()

    asyncio.run(run_async())