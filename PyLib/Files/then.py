import sh
import time as tm
while True:
    print('\n\n8888888b.           888      d8b 888      \n888   Y88b          888      Y8P 888      \n888    888          888          888      \n888   d88P 888  888 888      888 88888b.  \n8888888P"  888  888 888      888 888 "88b \n888        888  888 888      888 888  888 \n888        Y88b 888 888      888 888 d88P \n888         "Y88888 88888888 888 88888P"  \n                888                       \n           Y8b d88P                       \n            "Y88P"                        \n\n')
    print("\nPyLib bir python kütüphane kurucudur. İstediğiniz kategoriyi seçerek\nbaşlayabilirsiniz.\n\n!!!Not!!!\nBu dosyayı açmadan önce Start.sh doyasını açın.\nÇünkü o gerekli bağımlılıkları kuracaktır.\n")

    print("Python sürümünüz: ", sh.python3("-V"))

    print("1) Web için kütüphane\n")
    print("2) Masaüstü için kütüphane\n")
    print("3) Veri bilimi için kütüphane\n")

    kutuphane = int(input("Hangisi hakkında indirmek istiyorsun: "))

    if (kutuphane == 1):
        print(" 1) Django      5) Flask\n 2) Pyramid \n 3) Web2Py \n 4) Dash \n 99) Çıkış \n\n")
        web = int(input("Hangisini kurmak istersin."))
        if(web == 1):
            sh.pip3("install", "Django")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(web == 2):
            sh.pip3("install", "pyramid")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(web == 3):
            sh.pip3("install", "web2py")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(web == 4):
            sh.pip3("install", "dash")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(web == 5):
            sh.pip3("install", "Flask")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        else:continue
    elif (kutuphane == 2):
        print(" 1) PyQt5      5) Tkinter\n 2) Kivy      6) Flexx \n 3) Dabo      7) PyGUI\n 4) CEF python      8) Platform \n 99) Çıkış \n\n")
        desktop = int(input("Hangisini kurmak istersin? "))
        if (desktop == 1):
            sh.contrib.sudo.pip3("install", "PyQt5")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif (desktop == 2):
            sh.pip3("install", "Kivy")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif (desktop == 3):
            sh.pip3("install", "Dabo")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif (desktop == 4):
            sh.pip3("install", "cefpython3")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif (desktop == 5):
            print("\nÇok yakında!!")
        elif (desktop == 6):
            sh.pip3("install", "flexx")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif (desktop == 7):
            print("\nÇok yakında!!")
        elif (desktop == 8):
            sh.pip3("install", "platform-ai")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        else:continue
    elif (kutuphane == 3):
        print(" 1) SciPy      5) SciKit-Learn      9)Seaborn\n 2) Numpy      6) PyTorch      10)Bokeh\n 3) Pandas      7)Tensorflow      11)Pydot\n 4) Keras      8)Matplotlib      12)Plotly\n 99) Çık \n\n")
        veri = int(input("Hangisini kurmak istersin? "))
        if(veri==1):
            sh.pip3("install", "scipy")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==2):
            sh.pip3("install", "numpy")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==3):
            sh.pip3("install", "pandas")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==4):
            sh.pip3("install", "Keras")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==5):
            sh.pip3("install", "scikit-learn")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==6):
            sh.pip3("install", "pytorch")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==7):
            sh.pip3("install", "tensorflow")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==8):
            sh.pip3("install", "matplotlib")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==9):
            sh.pip3("install", "seaborn")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri==10):
            sh.pip3("install", "bokeh")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri == 11):
            sh.pip3("install", "pydot3")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        elif(veri == 12):
            sh.pip3("install", "plotly")
            print("Kütüphane yüklendi.")
            tm.sleep(3)
        else:continue
    else:continue