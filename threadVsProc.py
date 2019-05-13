#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from test import *
import multiprocessing

class threadVsProc():
    def __init__(self):
        print("threads 5000 test")

        for x in range(10):
            threading.Thread(target=test, args=()).start()
            # multiprocessing.Process(target=test, args=()).start()

if __name__ == '__main__':
    threadVsProc()