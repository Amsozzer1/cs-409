import picar_4wd as fc
import sys
import tty
import termios
import asyncio
import time


def main():
    #fc.angle(330)
    fc.forward(33)
    time.sleep(1)
    fc.stop()
    
    
main()