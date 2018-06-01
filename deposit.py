# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:12:42 2018

@author: P
"""
from datetime import datetime
from datetime import timedelta 

class Deposit: 
    '''Represent one sort of financial instruments, which generate interests'''
    def __init__(self, amount: int, interest: int, date_from, date_to):
        '''Initiate deposit with some arguments'''
        self.amount = amount
        self.interest = interest
        self.date_from = datetime.strptime(date_from, '%Y-%m-%d')
        self.date_to = datetime.strptime(date_to, '%Y-%m-%d')

    def duration(self):
        '''Return duration of Deposit in days'''
        return self.date_to - self.date_from

    def interests(self):
        '''Calculate interests, which you will receive from Deposit'''
        dt = (self.date_to) - (self.date_from)
        return self.amount * self.interest / 365 * (dt.total_seconds() / timedelta (days=1).total_seconds())

