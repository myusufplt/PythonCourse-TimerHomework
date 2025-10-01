import time
sn = int(input("Kronometre Kaç Saniye Olsun ="))
start_time = time.time()
for i in range(sn,0,-1):
    time.sleep(1)
    if i>3:
        print(i)
    else:
        print(f"Son {i} saniye!!")
end_time = time.time()
elapsed_time = end_time - start_time
time.sleep(1)
print("Sure doldu!! Alarm Devrede !!")
print(f"Gecen Sure = {int(elapsed_time)} saniye.")
from playsound import playsound
playsound("alarm.mp3")
