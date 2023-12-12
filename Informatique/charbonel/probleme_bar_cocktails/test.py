#!/bin/env python3

import os, sys, time
import numpy as np 
import asyncio

t0 = time.time()
l = []

async def f1(l):
    while len(l)<=5:
        print(l)
        l.append(f'f1 au temps {time.time()-t0}')
        print(l)
        await asyncio.sleep(2)
        print(l)
        
    

async def f2(l):
    while len(l)<=5:
        print(l)
        l.append(f'f2 au temps {time.time()-t0}')
        print(l)
        await asyncio.sleep(2)

   
        

async def f3(l):

    while len(l)<=5:
        l.append(f'f3 au temps {time.time()-t0}')
        await asyncio.sleep(4)
        print(l)
    
    if len(l)>=5:
        print('OUI')
    
    while len(l)<=8:
        l.append(f'f3 au temps {time.time()-t0}')
        await asyncio.sleep(1)
        print(l)
   
        

async def main():
    task = [f1(l),f2(l),f3(l)]

    await asyncio.gather(*task)

    print(l)


asyncio.run(main())



