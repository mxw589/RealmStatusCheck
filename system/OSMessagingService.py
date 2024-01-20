import ctypes


# Function to display a system message
def display_system_message(message, title="MAKE A CHARACTER!!!"):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)
