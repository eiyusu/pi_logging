import serial
import logging

ser = serial.Serial("COM3", 115200)
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s %(message)s")

while True:
    cc=str(ser.readline())
    print(cc)
    logging.debug(cc)