import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bowcar.upload import UploadBowCar
import time

def test_upload():
    print("Initializing UploadBowCar...")
    car = UploadBowCar()
    
    print("Generating code...")
    # Generate a simple blink pattern
    with car.bwhile("True"):
        car.red('on')
        car.delay(500)
        car.red('off')
        car.delay(500)
        
        car.blue('on')
        car.delay(500)
        car.blue('off')
        car.delay(500)
    
    print("Uploading code to Arduino...")
    try:
        car.upload_code()
        print("Upload command executed.")
    except Exception as e:
        print(f"Upload failed: {e}")

if __name__ == "__main__":
    test_upload()
