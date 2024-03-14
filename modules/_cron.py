#!/usr/bin/env python3

from crontab import CronTab
import pandas as pd

class cron:
    def __init__(self, user: str):
        self._user = ''
        if self._user=='':
            self._cron_ = CronTab(user=True)
        else:
            self._cron_ = CronTab(user=self._user)
        
        self._jobs = pd.read_csv('_jobs_.csv')
        self._jobs = self._jobs['job-location']