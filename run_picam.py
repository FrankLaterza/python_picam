import subprocess
from gpiozero import Button
from time import sleep



button = Button(2)



list_files = subprocess.run("ls")
print("The exit code was: %d" % list_files.returncode)


def init():
    #start isntance
    cmd = "./picam --alsadev hw:2,0 -w 1920 -h 1080 -f 25 &"
    #subprocess.run(cmd, shell=True)
    
    subprocess.Popen(cmd, shell=True, stdin=None, stderr=None, close_fds=True)
    
    #very bad way of waiting for an init to finish
    sleep(4)
    #subprocess.call("./picam -h")
    
def start_recording():
    
    #start recoding    
    cmd = "touch hooks/start_record"
    subprocess.run(cmd, shell=True)


def stop_recording():
    
    #start recoding    
    cmd = "touch hooks/stop_record"
    subprocess.run(cmd, shell=True)
    
def kill_process():

    #endes process
    cmd = "pkill picam"
    subprocess.run(cmd, shell=True)    

while True:
    
    init()
    
    print("init finished")
    #start the recording and wait for a button press
    start_recording()
    button.wait_for_press()
    
    
    #this will stop the recording and kill the process
    stop_recording()
    kill_process()

    #button delay
    sleep(5)
    
    #when button ress it will go to start of loop
    button.wait_for_press()
    
    
    
    
    
