from WorkingDir.testWindow import *
if __name__ == '__main__':
    howdy = "Howdy! "
    greeting = howdy + howdy
    print(str(greeting))
    hwnd = TestWindow()
    hwnd.display()
    print(str(hwnd.hello))
