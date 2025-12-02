import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bowcar.live import LiveBowCar
import time

def test_motor():
    print("Initializing LiveBowCar...")
    try:
        car = LiveBowCar()
    except Exception as e:
        print(f"Failed to initialize LiveBowCar: {e}")
        return

    if not car.port:
        print("Arduino not found. Exiting test.")
        return

    print("Testing Motor Control...")
    
    print("Forward (100, 100)")
    car.motor(100, 100)
    time.sleep(1)
    
    print("Stop (0, 0)")
    car.motor(0, 0)
    time.sleep(0.5)

    print("Backward (-100, -100)")
    car.motor(-100, -100)
    time.sleep(1)

    print("Stop (0, 0)")
    car.motor(0, 0)
    time.sleep(0.5)

    print("Turn Left (-100, 100)")
    car.motor(-100, 100)
    time.sleep(1)

    print("Stop (0, 0)")
    car.motor(0, 0)
    time.sleep(0.5)

    print("Turn Right (100, -100)")
    car.motor(100, -100)
    time.sleep(1)

    print("Stop (0, 0)")
    car.motor(0, 0)
    
    print("Test Complete.")
    car.close()

if __name__ == "__main__":
    test_motor()
