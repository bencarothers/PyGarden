import SprinklerGPIO
import time

if __name__ == "__main__":
    drip = SprinklerGPIO.SprinklerGPIO(1)
    drip.setStationStatus(0,1)
    for x in range(10):
        print x
        time.sleep(1)
    drip.setStationStatus(0,0)
    print "drip was turned off"
