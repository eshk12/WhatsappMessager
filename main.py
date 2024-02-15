import time
import pyautogui
import clipboard


def open_whatsapp():
    # Adjust the position of the WhatsApp Desktop icon according to your screen resolution
    pyautogui.click(x=2427, y=1413, clicks=1, interval=0.25)

def close_whatsapp():
    # Adjust the position of the WhatsApp Desktop icon according to your screen resolution
    pyautogui.rightClick(x=2427, y=1413)
    time.sleep(1)
    pyautogui.click(x=2427, y=1373, clicks=1, interval=0.25)

def send_message(contact_name, message):
    print("Starting to send message")
    clipboard.copy(contact_name)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    print("Pasting contact name:", contact_name)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    clipboard.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    print("Pasting message:", message)
    time.sleep(1)
    pyautogui.press("enter")
    close_whatsapp()

if __name__ == "__main__":
    contactsNames = ["person1", "person2", "person3"]
    for contactsName in contactsNames:
        open_whatsapp()
        time.sleep(2)  # Adjust as necessary to allow WhatsApp Desktop to open
        send_message(contactsName, "Hello, this is an automated message.")
