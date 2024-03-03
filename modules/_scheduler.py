#!/usr/bin/env python3

from datetime import datetime

class schedule:
    def __init__(self, day: int, month: int, year: int):
        if len(str(day))==1:
            day = "0"+str(day)
        if len(str(month))==1:
            month = "0"+str(month)
        while(True):
            if datetime.today()==f"{year}-{month}-{day}":
                if datetime.now().strftime("%H:%M") == "07:00":
                    print(" ")