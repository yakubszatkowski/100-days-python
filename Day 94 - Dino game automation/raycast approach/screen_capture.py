import numpy as np, win32gui, win32ui, win32con
from ctypes import windll
from threading import Thread, Lock

class WindowCaputre():

    screenshot = None

    def __init__(self, window_name):
        self.lock = Lock()
        self.hwnd = win32gui.FindWindow(None, window_name)
        self.left, self.top, self.right, self.bottom = win32gui.GetWindowRect(self.hwnd)
        self.w = self.right
        self.h = self.bottom


    def screen_capture(self):
        hwndDC = win32gui.GetWindowDC(self.hwnd)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, self.w, self.h)
        saveDC.SelectObject(saveBitMap)    
        windll.user32.PrintWindow(self.hwnd, saveDC.GetSafeHdc(), 2)
        bmpstr = saveBitMap.GetBitmapBits(True)

        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwndDC)

        img = np.frombuffer(bmpstr, dtype='uint8')
        img.shape = (self.h, self.w, 4)
        img = img[...,:3]
        img = img[710:711, 250:550]

        return img  # [0]
    

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()


    def stop(self):
        self.stopped = True


    def run(self):
        while not self.stopped:
            screenshot = self.screen_capture()
            self.lock.acquire()
            self.screenshot = screenshot
            self.lock.release()