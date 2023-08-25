import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

async def say_world():
    await asyncio.sleep(1)
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_world())

asyncio.run(main())
# Output: (after 1 second) Hello
#         (after another second) World

# Fun Facts

import asyncio

async def count_to_three():
    for i in range(1, 4):
        print(i)
        await asyncio.sleep(1)

asyncio.run(count_to_three())
# Output: 1
#         (after 1 second) 2
#         (after another second) 3
