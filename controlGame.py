import numpy as np
from PIL import ImageGrab
import cv2
import time
from directKeys import PressKey, W, A, S, D, R_A, L_A, ReleaseKey

# def process_image(image):
#   original_image = image
  
#   processed_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#   processed_image = cv2.Canny(processed_image, threshold1 = 200, threshold2=300)

#   return processed_image

for i in list(range(4))[::-1]:
  print(i+1)
  time.sleep(1)

def main():
  last_time = time.time()
  while True:
    # 800x600 windowed mode
    PressKey(R_A)
    screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    
    last_time = time.time()

    # Code to change the new image screen to gray  
    # new_image = process_image(screen)
    # cv2.imshow('window', new_image)

    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      break

main()