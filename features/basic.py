import pyautogui
from time import sleep
import wmi
import datetime
from playsound import playsound
import os
import threading
import operator

state = ["Speaking..."]
chat = []
chat_prev = []
def listToString(query):
    # initialize an empty string
    str = ""
    # traverse in the string
    for ele in query:
        str += ele
    # return string
    return str
    
def mute():
    pyautogui.press("volumemute") #mute the system
    chatWalter("Systems Muted")

def unmute():
    pyautogui.press("volumemute")  # unmute the system
    chatWalter("Systems Unmuted")

def chatWalter(query): #function required for displaying the chat of Walter in chatbox
    global chat_prev    
    chat_prev = chat.copy() #copying the chat list in chat_perv list
    chat.append("Walter: " + query + "\n") #appending the latest query in the chat list

def chatUser(query):  # function required for displaying the chat of User in chatbox
    global chat_prev
    chat_prev = chat.copy()  # copying the chat list in chat_perv list
    chat.append("User: " + query + "\n") #appending the latest query in the chat list
    sleep(1)

def battery():
    c = wmi.WMI()
    t = wmi.WMI(moniker="//./root/wmi")
    batts1 = c.CIM_Battery(Caption='Portable Battery')
    batts = t.ExecQuery('Select * from BatteryFullChargedCapacity')
    for i, b in enumerate(batts):
        full = (b.FullChargedCapacity)
    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    for i, b in enumerate(batts):
      rem = (b.RemainingCapacity)
    per = int((rem/full)*100)
    return per

def alarm(timing):
    x = 0
    alarmtime = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
    alarmtime = alarmtime[11:-3]
    hour_alaram = alarmtime[:2]
    hour_alaram = int(hour_alaram)
    minute_alarm = alarmtime[3:5]
    minute_alarm = int(minute_alarm)
    while True:
        if timing != None:
            while True:
                cwd = os.getcwd()
                currentpath = cwd + r"\features\resources\a1.mp3"
                if hour_alaram == datetime.datetime.now().hour:

                    if minute_alarm == datetime.datetime.now().minute and x <= 4:
                        print("alarm running")
                        playsound(currentpath)
                        x += 1

                    elif minute_alarm < datetime.datetime.now().minute:
                        timing = 0
                        return
        else:
            return


def get_operator_fn(oper):
    return{
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '/': operator.truediv}[oper]


def eval_expr(op1, oper, op2):
    print(op1+oper+op2)
    op1, op2 = float(op1), float(op2)
    print(op1,oper,op2)
    return get_operator_fn(oper)(op1, op2)
