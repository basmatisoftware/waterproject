import serial
import datetime
ser = serial.Serial("/dev/ttyACM0")
ser.flushInput();
while True:
    ser_bytes = ser.readline()
    stripped = ser_bytes.strip()
#    now = datetime.datetime.now().time();
    now = datetime.datetime.now().strftime('%s.%f');
    print (str(now) + "\t" + str(stripped))
