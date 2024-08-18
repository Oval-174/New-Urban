#m13-hw1.py
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1/power)  # Задержка, обратно пропорциональная силе
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = start_strongman('Ivan', 2)
    task2 = start_strongman('Alex', 3)
    task3 = start_strongman('Dmitry', 1)
    await asyncio.gather(task1, task2, task3)

asyncio.run(start_tournament())
