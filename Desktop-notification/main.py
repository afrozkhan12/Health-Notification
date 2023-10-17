#hey afroz its raafay here, i optimized someparts of the code and i stored notifications in python dictionaries
import time
from plyer import notification

def send_notification(title, message, app_icon, timeout):
    notification.notify(
        title=title,
        message=message,
        app_icon=app_icon,
        timeout=timeout
    )

if __name__ == "__main__":
    notifications = [
        {
            "title": "Please Drink Water Now!",
            "message": "Staying hydrated can help support physical performance, prevent headaches and constipation, you can more focus on your work and more.",
            "app_icon": "path/to/water.ico",
            "timeout": 5  # Adjust the duration as needed
        },
        {
            "title": "Please Correct your posture sit straight!",
            "message": "Good posture aligns and balances your muscles, decreasing joint compression and your risk of injury.",
            "app_icon": "path/to/sitting.ico",
            "timeout": 5  # Adjust the duration as needed
        }
    ]

    while True: #used while loop for execurion of sleep
        for notification_info in notifications:
            send_notification(**notification_info)
            time.sleep(60 * notification_info["timeout"])  # Convert timeout to seconds
