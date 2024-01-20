import ctypes


# Function to display a system message
def display_system_message(message, title="System Message", style=0, topmost=True, beep=True):
    """
    Display a system message using a custom dialog box.

    Parameters:
    - message (str): The message text to be displayed.
    - title (str): The title of the message box.
    - style (int): The style of the message box (default is 0).
                  0 - OK button
                  1 - OK and Cancel buttons
                  2 - Abort, Retry, and Ignore buttons
                  3 - Yes, No, and Cancel buttons
                  4 - Yes and No buttons
                  5 - Retry and Cancel buttons
    - topmost (bool): Whether to set the message box as topmost (default is True).
    - beep (bool): Whether to make a beep sound (default is True).

    Reference: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messagebox
    """
    if topmost:
        style |= 0x40  # Set the TOPMOST flag

    result = ctypes.windll.user32.MessageBoxW(0, message, title, style)

    if beep:
        ctypes.windll.user32.MessageBeep(0xFFFFFFFF)  # Beep sound

    return result