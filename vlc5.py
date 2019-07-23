import vlc
import cv2
v=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
player=vlc.MediaPlayer(r'C:\Users\hp\Downloads/song.mp3')
flag=0
while(1):
    try:
        r,i=v.read()
        j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        f=fd.detectMultiScale(j,1.3,5)
        #print(len(f))
        
        if(len(f)>0):
            (x,y,w,h)=f[0]
            cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),5)
            player.play()
            flag=1
        elif(flag==1):
            player.pause()
            flag=0
        k=cv2.waitKey(5)
        cv2.imshow('camera',i)
        if(k==ord('q')):
           cv2.destroyAllWindows()
           break
    except IndexError as e:
        print(e)
v.release()    
