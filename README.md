# Running Python Script in the Background on Windows

## Overview

This guide explains how to schedule and run a Python script in the background on Windows using Task Scheduler.

## Steps

1. **Open Task Scheduler:**
    - Press `Win + S` to open the Windows Search.
    - Type "Task Scheduler" and press Enter to open it.

2. **Create a Basic Task:**
    - In the Actions pane on the right, click on "Create Basic Task..."
    - Follow the wizard to set a name and description for your task.

3. **Trigger:**
    - Choose the trigger that suits your schedule (e.g., daily, weekly, etc.).
    - Set the start date and time.

4. **Action:**
    - Choose "Start a program" as the action.
    - Browse and select the `pythonw.exe` executable as the program/script.
    - In the "Add arguments" field, add `main.py`.
    - In the "Start in" field, provide the directory where your script is located. For
      example: `C:\Path\To\Your\Main\Script\`

5. **Finish:**
    - Review your settings and click "Finish."

## Additional Considerations

- **Environment Variables:** Set up any required environment variables in the "Actions" tab where you edit the action
  that starts your Python script.

- **Permissions:** Ensure that the user account running the scheduled task has the necessary permissions to execute your
  Python script and access any required resources.

- **Logging:** Consider adding logging to your Python script to capture any errors or important information.

## Running Without Console Window

To run your Python script without displaying the command window, use `pythonw.exe` instead of `python.exe`. If you don't
have `pythonw.exe`, you can create a shortcut to `python.exe` and change the shortcut properties to run minimized.

Alternatively, you can use third-party tools like `pyinstaller` to convert your script into an executable that doesn't
show a console window.
