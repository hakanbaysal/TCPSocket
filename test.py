#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint
from time import sleep

class test():

    def __init__(self):
        rand = randint(10, 100)
        print("thread begin: "+str(rand))
        sleep(rand)
        print("thread end: "+str(rand))
        sys.exit()
