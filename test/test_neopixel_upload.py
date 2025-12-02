import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bowcar.upload import UploadBowCar

def test_neopixel_upload():
    print("Initializing UploadBowCar for NeoPixel Test...")
    car = UploadBowCar()
    
    # 1. Setup - Clear pixels
    car.neopixel_clear()
    car.delay(1000)
    
    # 2. Red
    car.neopixel_all(255, 0, 0)
    car.delay(1000)
    
    # 3. Green
    car.neopixel_all(0, 255, 0)
    car.delay(1000)
    
    # 4. Blue
    car.neopixel_all(0, 0, 255)
    car.delay(1000)
    
    # 5. Individual Pixels
    car.neopixel_clear()
    car.delay(500)
    
    car.neopixel(0, 255, 0, 0) # Red
    car.delay(500)
    car.neopixel(1, 0, 255, 0) # Green
    car.delay(500)
    car.neopixel(2, 0, 0, 255) # Blue
    car.delay(500)
    car.neopixel(3, 255, 255, 255) # White
    car.delay(1000)
    
    # 6. Brightness
    car.neopixel_all(255, 255, 255)
    car.neopixel_brightness(50)
    car.delay(1000)
    car.neopixel_brightness(255)
    car.delay(1000)
    
    print("Generating and Uploading Code...")
    car.upload_code()
    print("Upload Complete.")

if __name__ == "__main__":
    test_neopixel_upload()
