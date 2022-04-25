from tkinter import *
import datetime
import time
import winsound


def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg ="Current Time: "+str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
            break

def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)

window = Tk()
window.title("Alarm Clock")
window.geometry("400x200")
window.config(bg="#7FFF00")
window.resizable(width=False,height=False)

time_format = Label(window, text= "Не забудьте установить время в 24-часовом формате!",fg="gold",bg="#000080",font=("Arial",10)).place(x=20,y=120)
addTime = Label(window, text= "Hour  Min   Sec", font=80,fg="blue",bg="lime").place(x=210)
setYourAlarm = Label(window,text= "Установите время для будильника: ", fg="red",bg="#0000FF",relief="solid", font=("Helevetica",12,"bold")).place(x=20, y=40)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(window,textvariable= hour,bg= "#66FFFF",width= 5, font=(30)).place(x=210,y=20)
minTime = Entry(window,textvariable= min,bg= "#66FFFF",width= 5, font=(30)).place(x=250,y=20)
secTime = Entry(window,textvariable= sec,bg= "#66FFFF",width= 5, font=(30)).place(x=310,y=20)

submit = Button(window, text="Установите свой будильник", fg="#CC66FF",width=30,command= get_alarm_time,font=(60)).place(x=100,y=80)

window.mainloop()