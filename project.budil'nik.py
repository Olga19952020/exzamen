from datetime import datetime
from playsound import playsound
def validate_time(alarm_time):
    if len(alarm_time) !=11:
        return "Неверный формат времени!Пожалуйста,попробуйте снова..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Недопустимый формат часов!Пожалуйста,попробуйте снова..."
        elif int(alarm_time[3:5]) > 59:
            return "Недопустимый формат минут!Пожалуйста,попробуйте снова..."
        elif int(alarm_time[6:8]) > 59:
            return "Недопустимый формат секунд!Пожалуйста,попробуйте снова..."
        else:
            return "Ok"

while True:
    alarm_time = input("Введите время в формате  HH:MM:SS    AM/PM : ")

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Установка будильника для {alarm_time}...")
        break
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

while True:
    now = datetime.now()

    current_hous = now.strftime("%H")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hous:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Проснись!")
                    playsound('D://Просыпайся мой хозяин!.mp3')
                    break

