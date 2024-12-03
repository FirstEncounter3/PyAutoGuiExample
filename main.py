import os
import time
import pyautogui

BUTTON_IMAGES = {
    "one": "one.png",
    "two": "two.png",
    "plus": "plus.png",
    "seven": "seven.png",
    "equals": "eq.png",
}

CONFIDENCE_LEVEL = 0.9

BASE_PATH = os.path.join(os.getcwd(), "buttons")


def open_calculator() -> None:
    """Open the calculator application."""
    pyautogui.hotkey("win", "r")
    pyautogui.typewrite("calc")
    pyautogui.press("enter")
    retryes = 0

    while True:
        try:
            print("Check if calculator is open...")
            pyautogui.locateOnScreen(
                os.path.join(BASE_PATH, "one.png"), confidence=CONFIDENCE_LEVEL
            )
            break
        except pyautogui.ImageNotFoundException:
            retryes += 1
            print(f"Maybe calculator is not open. Retrying ({retryes}) ...")
            time.sleep(1)
            if retryes >= 3:
                print("calculator can't be opened or something went wrong. Exiting...")
                exit(1)

    print("Calculator is open.")


def find_button_coordinates() -> dict:
    """Find the coordinates of calculator buttons."""
    open_calculator()
    coordinates = {}

    for name, image in BUTTON_IMAGES.items():
        button_location = pyautogui.locateOnScreen(
            os.path.join(BASE_PATH, image), confidence=CONFIDENCE_LEVEL
        )
        if button_location is not None:
            coordinates[name] = button_location
            print(f"Coordinates for button {name}: {button_location}")
        else:
            print(f"Button {name} not found on screen.")

    return coordinates


def perform_calculation(button_coordinates) -> None:
    """Perform the calculation using the found button coordinates."""
    print("Performing calculation...")
    try:
        pyautogui.click(button_coordinates["one"])
        pyautogui.click(button_coordinates["two"])
        pyautogui.click(button_coordinates["plus"])
        pyautogui.click(button_coordinates["seven"])
        pyautogui.click(button_coordinates["equals"])
    except KeyError as e:
        print(
            f"Error: Missing button coordinate for {e}. Calculation cannot be performed."
        )


def calculator_call() -> None:
    """Main function to execute the calculator operation."""
    button_coordinates = find_button_coordinates()
    if button_coordinates:
        perform_calculation(button_coordinates)


if __name__ == "__main__":
    print("Starting calculator automation...")
    calculator_call()
    print("Done!")
