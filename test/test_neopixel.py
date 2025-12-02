import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bowcar.live import LiveBowCar
import time

def test_neopixel():
    print("Initializing LiveBowCar for NeoPixel Test...")
    car = LiveBowCar()
    
    print("Uploading firmware to ensure NeoPixel support...")
    car._upload_firmware()
    
    print("1. NeoPixel All Red")
    car.neopixel_all(255, 0, 0)
    time.sleep(1)
    
    print("2. NeoPixel All Green")
    car.neopixel_all(0, 255, 0)
    time.sleep(1)
    
    print("3. NeoPixel All Blue")
    car.neopixel_all(0, 0, 255)
    time.sleep(1)
    
    print("4. Individual Pixel Control")
    car.neopixel_clear()
    time.sleep(0.5)
    car.neopixel(0, 255, 0, 0) # Red
    time.sleep(0.5)
    car.neopixel(1, 0, 255, 0) # Green
    time.sleep(0.5)
    car.neopixel(2, 0, 0, 255) # Blue
    time.sleep(0.5)
    car.neopixel(3, 255, 255, 255) # White
    time.sleep(1)
    
    print("5. Brightness Control")
    car.neopixel_all(255, 255, 255)
    for b in range(255, 0, -50):
        print(f"Brightness: {b}")
        car.neopixel_brightness(b)
        time.sleep(0.2)
        
    print("6. Clear")
    car.neopixel_clear()
    car.close()
    print("Test Complete.")

if __name__ == "__main__":
    test_neopixel()
