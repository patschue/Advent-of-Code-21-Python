# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 07:25:33 2021

@author: Patrick
"""

import pandas as pd

with open("InputDay2.txt") as f:
    cmd = f.readline().split()
    horizontal = 0
    vertical = 0
    route = pd.DataFrame(columns = ["Distanz", "Tiefe"])
    while cmd:
        if cmd[0] == "forward":
            horizontal += int(cmd[1])
        elif cmd[0] == "down":
            vertical += int(cmd[1])
        else:
            vertical -= int(cmd[1])
        # koordinaten = [horizontal, vertical]
        koordinaten = {'Distanz': horizontal, "Tiefe": vertical * -1}
        route = route.append(koordinaten, ignore_index = True)
        cmd = f.readline().split()
    print(horizontal, vertical, horizontal * vertical)
    route.plot.line(x='Distanz', y='Tiefe')

# with open("InputDay2.txt") as f:
#     cmd = f.readline().split()
#     horizontal = 0
#     vertical = 0
#     aim = 0
#     while cmd:
#         if cmd[0] == "forward":
#             horizontal += int(cmd[1])
#             vertical += int(cmd[1]) * aim
#         elif cmd[0] == "down":
#             aim += int(cmd[1])
#         else:
#             aim -= int(cmd[1])
#         cmd = f.readline().split()
#     print(horizontal, vertical, horizontal * vertical)