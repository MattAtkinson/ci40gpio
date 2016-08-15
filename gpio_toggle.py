from letmecreate.core import gpio
from time import sleep

GPIO_NUM = 83

gpio.init(GPIO_NUM)
gpio.set_direction(GPIO_NUM, 0)

while True:

        gpio.set_value(GPIO_NUM, 1)

        sleep(0.1)

        gpio.set_value(GPIO_NUM, 0)

        sleep(0.1)
