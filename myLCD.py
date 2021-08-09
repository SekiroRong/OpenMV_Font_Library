# Untitled - By: sekiro - 周六 7月 31 2021

import sensor, image, time
import lcd
from ZIKU import ziku

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QQVGA2) # Special 128x160 framesize for LCD Shield.
sensor.skip_frames(time = 2000)     # Wait for settings take effect.

lcd.init() # Initialize the lcd screen.
#lcd初始化
#img = sensor.snapshot().clear()
#mylcd = ziku(img)
#ziku.clear()#清屏
x_1,y_1=0,0
x_2,y_2=1,1
while(True):
    img = sensor.snapshot()
    mylcd = ziku(img)
    mylcd.draw_p6x8(x_1,y_1,'Sekiro')
    mylcd.draw_p8x16(x_2,y_2,'Rong',transparent=True)
    #img = sensor.snapshot()
    #img.binary([(0,255)])
    #img.invert()
    mylcd.display() # Take a picture and display the image.
    time.sleep_ms(100)
    #将图像显示在lcd中
    x_1=x_1+1
    y_2=y_2+1
    if x_1*6 > 127:
        x_1 = 0
    if y_2*16 > 159:
        y_2 = 1
    mylcd.clear()
