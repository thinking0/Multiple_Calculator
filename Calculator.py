import json
import time
import datetime
from multi import ThreadManager

class Calculator(ThreadManager):
    def do_work(self,filepath,search_name):
        try:
            time.sleep(1)
            print("### do workd : "+search_name+", "+filepath)
            print("runtime : "+search_name+", " + str(datetime.datetime.now()))
            fp=open(filepath)
            raw_data = fp.read().replace("\n","")
            #print(raw_data)
            json_obj=json.loads(raw_data)
            self.Result[search_name]=json_obj[search_name]
            
            print("result : " + str(json_obj[search_name]))
            fp.close()
        except Exception as e:
            print(str(e))
