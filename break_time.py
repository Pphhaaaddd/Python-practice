import webbrowser
import time

print ("Hi, this program should give breaks if you are sitting on your PC for long")
t0 = time.time()
print(t0)

for i in range(3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=ozv4q2ov3Mk")
    print(round(time.time()-t0,3))
