import sys
import os
import uos
import machine
import time

def fun1():
    print('wdt feed')
    wdt_feed()
    print('sleep 3 mins')
    time.sleep(3*60)
    print('PASS')
    
def fun2():
    print('wdt feed')
    wdt_feed()
    print('sleep 100 mins')
    time.sleep(100*60)
    print('PASS')

def run_test():
    fun1() # PASS
    fun1() # PASS
    fun2() # .. machine reboot

run_test()
    