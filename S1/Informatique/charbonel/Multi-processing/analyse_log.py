#!/bin/env python3


import os,sys
import time, datetime
import re
import pandas as pd  

path = 'log'

pattern = r"PID: (\d+) - Execution : (.*?) is (\d+\.\d+)"

df = pd.DataFrame(columns=["PID","Jobs", "Time_ex"])

with open(path,'r') as f:
    for l in f:
        match = re.search(pattern, l)
        if match:
            df.loc[len(df)] = [match.group(1), match.group(2), match.group(3)]
print(df)