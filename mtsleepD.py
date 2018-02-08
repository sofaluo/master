#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [16,12,8,4]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop,nesc):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nesc)
    print 'loop',nloop,' done at:', ctime()

def main():
    print 'starting at:',ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all thread done at:', ctime()

if __name__ == '__main__':
    main()
