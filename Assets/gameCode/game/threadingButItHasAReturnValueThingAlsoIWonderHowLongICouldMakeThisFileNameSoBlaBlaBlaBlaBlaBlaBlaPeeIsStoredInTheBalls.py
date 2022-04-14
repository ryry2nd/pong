"""
this makes a new thread return somthing
"""

#imports
from threading import Thread

#this is the thread class
class ThreadWthRet(Thread):
    #init class
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
        
    #run the thread
    def run(self):
        if self._target != None:
            self._return = self._target(*self._args, **self._kwargs)

    #join the thread
    def join(self, *args):
        Thread.join(self, *args)
        return self._return