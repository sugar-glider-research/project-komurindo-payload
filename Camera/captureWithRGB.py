import time
import picamera
from PIL import Image

def capture_bmp():
    with picamera.PiCamera() as camera:
        camera.resolution = (2000, 2000)
        #camera.start_preview()
        # Camera warm-up time
        time.sleep(1)
        camera.capture('payload_surv.bmp', resize=(200,200))

#=========================================================================#

def retrieve_rgb():
    time.sleep(1)
    image = Image.open("payload_surv.bmp")
    pixel = image.load()

    #Declaration of RGB Array
    arrayOfRGB = [[[0 for x in range(3)]for x in range(200)]for x in range(200)]

    j = 0
    while j < 200:
        k = 0
        while k < 200:
            RGB = str(pixel[j,k])
            #print("RGB Data [" + str(j) + "," + str(k) + "] = " + RGB)

            # Number of RGB Data String (For While Iteration)
            numberOfArray = len(RGB)        

            i = 0 # iteration parameter
            stringTemp = "" # Variable to store number before ','
            l = 0
            while i < numberOfArray:
                if RGB[i].isdigit():
                    stringTemp += RGB[i]
                elif RGB[i] == ',' or RGB[i] == ')':
                    arrayOfRGB[j][k][l] = stringTemp
                    if(l == 0){
                            print ("R = " + arrayOfRGB[j][k][l])
                    } elif(l == 1){
                            print ("G = " + arrayOfRGB[j][k][l])
                    } elif(l == 2){
                            print ("B = " + arrayOfRGB[j][k][l])
                    }
                    stringTemp = ""
                    l = l + 1
                i = i + 1
            k = k + 1        
        j = j + 1
    return arrayOfRGB

#j = 0
#while j < 200:
#    k = 0
#    while k < 200:
#        RGB = str(pixel[j,k])
#        print("RGB Data [" + str(j) + "," + str(k) + "] = " + RGB)
#        i = 0
#        while i < 3:
#            print ("R = " + arrayOfRGB[j][k][i])
#            i = i + 1
#            print ("G = " + arrayOfRGB[j][k][i])
#            i = i + 1
#            print ("B = " + arrayOfRGB[j][k][i])
#            i = i + 1
#        k = k + 1
#    j = j + 1
