import cv2
cam=int(raw_input("Enter Camera number: "))
cap=cv2.VideoCapture(cam)
font = cv2.FONT_HERSHEY_SIMPLEX
success = True
count = 0
fps = int(cap.get(cv2.CAP_PROP_FPS))

while success:
    success,image = cap.read()
    cv2.rectangle(image,(310,100),(700,300),(255,0,0),3) # bounding box which captures ASL sign to be detected by the system
    img1=image[100:310,300:700]
    cv2.imshow('frame',img1)
    #print('Read a new frame: ', success)
    if count%(5*fps) == 0 :
        cv2.imwrite("temp/frame%d.jpg" % count, img1)      
        print('successfully written 5th frame')
    
    count += 1
