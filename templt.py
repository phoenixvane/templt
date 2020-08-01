from microbit import *
import time

log_count = 0
log_file = "log.csv"
log_data = "time, temp, lt\n"
display.scroll("temp/lt")

while not button_a.was_pressed():
    sleep(1000)

display.show(Image.SNAKE)
sleep(1000)
display.clear()

with open(log_file, "w") as f:
    f.write(log_data)

while True:
    log_count += 1
    temp = temperature()
    lt = display.read_light_level()
    print((temp, lt))
    with open(log_file, "r") as f:
        log_data = f.read()
    with open(log_file, "w") as f:
        f.write(log_data + str(log_count) + "," + str(temp) + "," + str(lt) + "\n")
    time.sleep(3600)
