import subprocess as sub
import pychromecast
import time
chromecasts = pychromecast.get_chromecasts()
t = False
#    cast = pychromecast.get_chromecasts()[0] #todo maybe this will use the first cast in the array making it portable 


while True:
    while t == False: 
        p = sub.Popen(('tcpdump', '-i', 'eno1', '-l', 'port 53'), stdout=sub.PIPE)
        for row in iter(p.stdout.readline, b''):
            print (row.rstrip())   # process here
            if ("porn")  in str(row.rstrip()):
                print ("ladies and gentlemen we got him")
                cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Basement TV")
                mc = cast.media_controller
                cast.set_volume(1)
                mc.play_media("http://172.16.99.170:80/fbi.mp4", content_type = "video/mp4")
                mc.play_media("http://172.16.99.170:80/fbi.mp4", content_type = "video/mp4") 
                mc.block_until_active()
                mc.play()
                t = True
                break
            if "anime" in str(row.rstrip()):
                print ("ladies and gentlemen we got him")
                cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Basement TV")
                mc = cast.media_controller
                cast.set_volume(1)
                mc.play_media("http://172.16.99.170:80/fbi.mp4", content_type = "video/mp4")    
                mc.play_media("http://172.16.99.170:80/fbi.mp4", content_type = "video/mp4")
                mc.block_until_active()
                mc.play()
                t = True
                break
    while t == True:
        time.sleep(1)
        t = False