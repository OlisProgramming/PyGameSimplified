from WorkingDir.testWindow import *
if __name__ == '__main__':
    greeting = 3.1414592653589795
    print(str(greeting))
    hwnd = TestWindow()
    hwnd.display()
    print(str(hwnd.hello))
