import abc
import json
import datetime
import time
import os
import shutil
import  threading
from Queue import Queue

class ThreadManager:
    Task_queue = Queue()
    Result={}
    THREAD_COUNT=2
    CLONE_DIR="back"
    ORIGIN_PATH="origin1"
    #LOCK = threading.Lock()
    Clone_files_path=[]
    Result_data = []
    #DATA=["test1","test2","test3","test4"]

    def init_worker(self,n):

        print('worker :' + str(n))
        print("thread name : " + threading.currentThread().getName())
        clone_filepath=self.cloneFile(n)
        while True:
            #self.LOCK.acquire()
            item = self.Task_queue.get()
            self.do_work(clone_filepath,item)
            self.Task_queue.task_done()
            #self.LOCK.release()

    
    def clean(self):
        for filepath in self.Clone_files_path:
            os.remove(filepath)

    def cloneFile(self,index):
        clone_path=self.CLONE_DIR+"/"+self.ORIGIN_PATH+"_"+str(index)

        try:
            #print("clonefile : "+clone_path)
            if not os.path.exists(clone_path):
                shutil.copyfile(self.ORIGIN_PATH,clone_path)
                self.Clone_files_path.append(clone_path)
        except Exception as e:
            print("clone error : " +str(e))
        return clone_path 
    
    def init_multithreading(self):
        for thread_num in range(self.THREAD_COUNT):
            t = threading.Thread(target=self.init_worker,args=(thread_num,))
            t.daemon = True
            t.start()
    
    
    def __init__(self,filepath,origin_data):
        print('init')
        self.ORIGIN_PATH=filepath
        #self.DATA=origin_data
        if not os.path.exists(self.CLONE_DIR):
            os.mkdir(self.CLONE_DIR)
        self.init_multithreading()
    

    @abc.abstractmethod
    def do_work(self,filepath,search_name):
        pass
