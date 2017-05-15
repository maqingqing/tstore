#!/usr/bin/python
from app import Monitor

if __name__ == '__main__':
    monitor = Monitor()
    monitor.start()
    monitor.join()
