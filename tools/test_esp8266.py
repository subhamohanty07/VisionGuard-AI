import time

from hardware.esp8266_controller import ESP8266Controller


def main():

    esp = ESP8266Controller()

    print("LED ON")
    esp.led_on()

    time.sleep(3)

    print("LED OFF")
    esp.led_off()

    esp.close()


if __name__ == "__main__":
    main()