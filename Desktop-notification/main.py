import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water Now!... ",
            message="""Staying hydrated can help support physical performance, prevent headaches and constipation, 
                    you can more focus on your work and more.""",
            app_icon="E:/py-practice/New folder/Projects/Desktop-notification/water.ico.ico",
            timeout=2   #Here you can specify duration in second for how long you want the notification to be shown on screen.
        )
        time.sleep(2*3)    #Here You can set the duration in seconds after which this message appears on your desktop notification.

        notification.notify(
            title="Please Correct your posture sit straight!... ",
            message="""Good posture aligns and balances your muscles, decreasing joint compression and your risk of injury. """,
            app_icon="E:/py-practice/New folder/Projects/Desktop-notification/sitting.ico",
            timeout=2   #Here you can specify duration in second for how long you want the notification to be shown.
        )
        time.sleep(2*5)   #Here You can set the duration in seconds after which this message appears on your desktop notification.

#For running this program in background 
#run this command in terminal 'pythonw .\filename.py' OR pythonw.exe .\filename.py