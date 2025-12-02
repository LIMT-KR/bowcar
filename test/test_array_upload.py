import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bowcar.upload import UploadBowCar

def test_array_upload():
    print("Initializing UploadBowCar for Array Test...")
    car = UploadBowCar()
    
    # 1. Integer Array
    print("1. Setting Integer Array")
    car.set_array("int", "myIntArray", [10, 0, 0, 0, 0])
    
    # 2. String Array
    print("2. Setting String Array")
    car.set_array("String", "myStrArray", ["Hello", "World", "BowCar"])
    
    # 3. Use Array in Loop (NeoPixel Brightness)
    # Set all pixels to White first
    car.neopixel_all(255, 255, 255)
    
    with car.bfor("int i=0; i<5; i++"):
        # Set brightness based on array value
        car.neopixel_brightness("myIntArray[i]")
        car.delay(1000)
        
        # Modify array value for next iteration (increase brightness)
        car.set_array_value("myIntArray", "i+1", "myIntArray[i] + 20")
        with car.bif("myIntArray[i] > 255"):
             car.set_array_value("myIntArray", "i", 10) # Reset if too bright
    
    car.neopixel_clear()
    
    print("Generating Code...")
    print("="*20)
    print(car.get_full_code())
    print("="*20)
    
    print("Uploading Code...")
    car.upload_code()
    print("Upload Complete.")

if __name__ == "__main__":
    test_array_upload()
