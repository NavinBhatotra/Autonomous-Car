import os                                                                       
from multiprocessing import Pool                                                

stream = "/home/pi/Desktop/Autonomous_Car/raspberryPi/stream_client.py"
ultrasonic = "/home/pi/Desktop/Autonomous_Car/raspberryPi/ultrasonic_client.py"
client = "/home/pi/Desktop/Autonomous_Car/raspberryPi/client.py"
ldr = "/home/pi/Desktop/Autonomous_Car/raspberryPi/ldr.py"
                                                                                                                                                          
processes = (ultrasonic,stream,client,ldr)                                    
                                                                                                                               
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
                                                                                                                                                               
pool = Pool(processes=4)                                                        
pool.map(run_process, processes)  

