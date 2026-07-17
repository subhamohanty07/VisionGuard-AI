import time

import serial

from config import ESP8266_BAUDRATE, ESP8266_PORT


class ESP8266Controller:
    """
    Controls the ESP8266 over USB Serial.
    """

    def __init__(self):

        self.serial = None

        try:
            self.serial = serial.Serial(
                port=ESP8266_PORT,
                baudrate=ESP8266_BAUDRATE,
                timeout=1,
            )

            # Give the ESP8266 time to reset
            time.sleep(2)

            print("[ESP8266] Connected successfully.")

        except serial.SerialException as e:
            print(f"[ESP8266] Connection failed: {e}")

    def led_on(self):

        if self.serial and self.serial.is_open:
            self.serial.write(b"1")

    def led_off(self):

        if self.serial and self.serial.is_open:
            self.serial.write(b"0")

    def close(self):

        if self.serial and self.serial.is_open:
            self.serial.close()

            print("[ESP8266] Connection closed.")