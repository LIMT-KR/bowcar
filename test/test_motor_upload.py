import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bowcar.upload import UploadBowCar
import time

def test_motor_upload():
    print("Initializing UploadBowCar...")
    car = UploadBowCar()

    print("Generating Motor Control Code...")
    
    # Forward
    car.motor(100, 100)
    car.delay(1000)
    
    # Stop
    car.motor(0, 0)
    car.delay(500)

    # Backward
    car.motor(-100, -100)
    car.delay(1000)

    # Stop
    car.motor(0, 0)
    car.delay(500)

    # Turn Left
    car.motor(-100, 100)
    car.delay(1000)

    # Stop
    car.motor(0, 0)
    car.delay(500)

    print("Uploading Code...")
    car.upload_code()
    
    print("Test Complete. Check if the car moves as expected.")

if __name__ == "__main__":
    test_motor_upload()
