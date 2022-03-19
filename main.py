import win32api
import win32con
import time


win32api.SetCursorPos((500, 500))
time.sleep(2)
while(True):
    for i in range(100):
        win32api.keybd_event(40, 0, 0, 0)
        win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(10)

