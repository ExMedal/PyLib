import sh
import time as tm
while True:
    print('\n\n8888888b.           888      d8b 888      \n888   Y88b          888      Y8P 888      \n888    888          888          888      \n888   d88P 888  888 888      888 88888b.  \n8888888P"  888  888 888      888 888 "88b \n888        888  888 888      888 888  888 \n888        Y88b 888 888      888 888 d88P \n888         "Y88888 88888888 888 88888P"  \n                888                       \n           Y8b d88P                       \n            "Y88P"                        \n\n')
    print("\nPyLib is a python library builder. You can \n start by selecting the category you want. \n \n !!! Note !!! \nOpen the Start.sh file before opening this file. \nBecause it will install the necessary dependencies.\n")

    print("Python version: ", sh.python3("-V"))

    print("1) Lib for Web develop\n")
    print("2) Lib for Desktop GUI\n")
    print("3) Lib for Data Science\n")

    kutuphane = int(input("Which one do you want to download about: "))

    if (kutuphane == 1):
        print(" 1) Django      5) Flask\n 2) Pyramid \n 3) Web2Py \n 4) Dash \n 99) Quit \n\n")
        web = int(input("Which one would you like to install? "))
        if(web == 1):
            sh.pip3("install", "Django")
            print("The library is loaded.")
            tm.sleep(3)
        elif(web == 2):
            sh.pip3("install", "pyramid")
            print("The library is loaded.")
            tm.sleep(3)
        elif(web == 3):
            sh.pip3("install", "web2py")
            print("The library is loaded.")
            tm.sleep(3)
        elif(web == 4):
            sh.pip3("install", "dash")
            print("The library is loaded.")
            tm.sleep(3)
        elif(web == 5):
            sh.pip3("install", "Flask")
            print("The library is loaded.")
            tm.sleep(3)
        else:continue
    elif (kutuphane == 2):
        print(" 1) PyQt5           5) Tkinter\n 2) Kivy            6) Flexx \n 3) Dabo            7) PyGUI\n 4) CEF python      8) Platform \n 99) Quit \n\n")
        desktop = int(input("Which one would you like to install? "))
        if (desktop == 1):
            sh.contrib.sudo.pip3("install", "PyQt5")
            print("The library is loaded.")
            tm.sleep(3)
        elif (desktop == 2):
            sh.pip3("install", "Kivy")
            print("The library is loaded.")
            tm.sleep(3)
        elif (desktop == 3):
            sh.pip3("install", "Dabo")
            print("The library is loaded.")
            tm.sleep(3)
        elif (desktop == 4):
            sh.pip3("install", "cefpython3")
            print("The library is loaded.")
            tm.sleep(3)
        elif (desktop == 5):
            print("\nÇok yakında!!")
        elif (desktop == 6):
            sh.pip3("install", "flexx")
            print("The library is loaded.")
            tm.sleep(3)
        elif (desktop == 7):
            print("\nÇok yakında!!")
        elif (desktop == 8):
            sh.pip3("install", "platform-ai")
            print("The library is loaded.")
            tm.sleep(3)
        else:continue
    elif (kutuphane == 3):
        print(" 1) SciPy      5) SciKit-Learn   9)Seaborn\n 2) Numpy      6) PyTorch        10)Bokeh\n 3) Pandas     7)Tensorflow      11)Pydot\n 4) Keras      8)Matplotlib      12)Plotly\n 99) Quit \n\n")
        veri = int(input("Which one would you like to install? "))
        if(veri==1):
            sh.pip3("install", "scipy")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri==2):
            sh.pip3("install", "numpy")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri==3):
            sh.pip3("install", "pandas")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri==4):
            sh.pip3("install", "Keras")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri==5):
            sh.pip3("install", "scikit-learn")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri==6):
            sh.pip3("install", "pytorch")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri==7):
            sh.pip3("install", "tensorflow")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri==8):
            sh.pip3("install", "matplotlib")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==9):
            sh.pip3("install", "seaborn")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri==10):
            sh.pip3("install", "bokeh")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri == 11):
            sh.pip3("install", "pydot3")
            print("The library is loaded.")
            tm.sleep(3)
        elif(veri == 12):
            sh.pip3("install", "plotly")
            print("The library is loaded.")
            tm.sleep(3)
        else:continue
    else:continue
