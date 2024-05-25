import win32gui, win32ui, numpy as np, cv2
from ctypes import windll


def get_game_screen(hwnd, region):
    left, top, right, bottom = region
    w, h = win32gui.GetWindowRect(hwnd)[2:]
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)    
    windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 2)
    bmpstr = saveBitMap.GetBitmapBits(True)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    img = np.frombuffer(bmpstr, dtype='uint8')
    img.shape = (h, w, 4)
    img = img[...,:3]
    game_screen_array = img[top:bottom, left:right]
    game_contigous_array = np.ascontiguousarray(game_screen_array) 

    return cv2.cvtColor(game_contigous_array, cv2.COLOR_BGR2GRAY)