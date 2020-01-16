#from __future__ import print_function

from Calculator import Calculator


if __name__ == "__main__":
    data=["test1","test2","test3","test4"]
    origin_path="origin1"
    #calculator=Calculator(origin_path,data)
    calculator=Calculator(origin_path,data)

    try:
        #init()
        #time.sleep(5)
        for item in data:
            #print("put itme : " + str(item))
            calculator.Task_queue.put(item)
        #q.put(55)
        calculator.Task_queue.join()
        print("done")
        calculator.clean()
        print(calculator.Result)
    except Exception as e:
        print(str(e))
