import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
# Output: 'Hello' (after 1 second) 'World'

# Fun Facts

import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

asyncio.run(say_after(1, 'Hello'))
# Output: (after 1 second) 'Hello'