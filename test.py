#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint
from time import sleep
from datetime import datetime

class test():

    def __init__(self):
        rand = randint(0, 100)
        print("thread begin: "+str(rand))
        #sleep(rand)
        t1 = datetime.now()
        while (datetime.now() - t1).seconds <= 10:
            print("thread running: "+str(rand))
        print("thread end: "+str(rand))
        sys.exit()
