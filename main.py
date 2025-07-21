import time
import datetime
from pynput import mouse, keyboard
import pyautogui

# --- Globals ---
kb = keyboard.Controller()
process_active = False


# --- Logging Function ---
def log(message):
    """Prints a message with a timestamp."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}")


# --- Core Functions ---
def check_template(template_code, confidence=0.95):
    """
    Searches the screen for a given template image.
    """
    try:
        template_path = f"{template_code}_template.png"
        found = pyautogui.locateOnScreen(template_path, confidence=confidence)
        return found
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        log(f"Error during searching for template '{template_code}': {e}")
        exit(1)


def soul_search():
    """
    Main loop to search for the 'soul' by interacting with 'arcana' packs.
    """
    restart_count = 0
    arcana_count = 0

    while True:
        restart_count += 1
        log("=" * 10 + f" Restart no. {restart_count} " + "=" * 10)

        kb.press('r')
        time.sleep(4)
        kb.release('r')

        template = check_template("arcana")
        if template:
            arcana_count += 1
            if template.left > 800:
                log("Arcana pack found - second skip")
                click_x_1 = template.left + template.width - 250
                click_y_1 = template.top - 30

                pyautogui.moveTo(click_x_1, click_y_1)
                pyautogui.click()

                time.sleep(1)

                click_x_2 = template.left + template.width + 50

                pyautogui.moveTo(click_x_2, click_y_1)
                pyautogui.click()
            else:
                log("Arcana pack found - first skip")
                click_x = template.left + template.width + 50
                click_y = template.top + template.height // 2
                pyautogui.moveTo(click_x, click_y)
                pyautogui.click()

            pyautogui.moveTo(1, 1)
            time.sleep(4)

            if not check_template('soul', 0.5):
                log("Soul not found, continuing search")
                continue
            else:
                log("Soul found, exiting loop")
                break
        else:
            log("Arcana pack not found")

    log(f"Restart count: {restart_count}")
    log(f"Arcana count: {arcana_count}")


def on_click(x, y, button, pressed):
    """
    Handles mouse clicks to start the search process.
    """
    global process_active
    try:
        if button == mouse.Button.x1 and pressed and not process_active:
            process_active = True
            log("Process started by X1 button.")
            soul_search()
            log("Process finished.")
            process_active = False
    except Exception as e:
        log(f"Error in on_click: {e}")
        process_active = False


# --- Main Execution ---
if __name__ == "__main__":
    with mouse.Listener(on_click=on_click) as listener:
        log("Press the X1 mouse button to start searching...")
        listener.join()
