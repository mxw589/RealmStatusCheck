# Checking a WoW Realm status on a schedule

## Overview

If you want to be informed when a WoW realm doesn't have a particular status, then the following steps will create a
windows task to inform you when it has changed

## Steps

1. **Create WoW API Account:**
    - Follow instructions at https://develop.battle.net/access/clients to create client credentials. Keep your secret
      safe!

2. **Open Task Scheduler:**
    - Press `Win + S` to open the Windows Search.
    - Type "Task Scheduler" and press Enter to open it.

3. **Create a Basic Task:**
    - In the Actions pane on the right, click on "Create Basic Task..."
    - Follow the wizard to set a name and description for your task.

4. **Trigger:**
    - Choose the trigger that suits your schedule (e.g., daily, weekly, etc.).
    - Set the start date and time.

5. **Action:**
    - Choose "Start a program" as the action.
    - Browse and select the `pythonw.exe` executable as the program/script.
    - In the "Add arguments" field, add `main.py`.
    - In the "Start in" field, provide the directory where your script is located. For
      example: `C:\Path\To\Your\Main\Script\`

6. **Finish:**
    - Review your settings and click "Finish."
    - You probably will want to edit your trigger schedule to run more regularly than was possible when creating a basic
      task using the wizard, so edit this now. For example: https://i.imgur.com/vXVGoI0.png

## Additional Considerations

- **Environment Variables:** Set up any required environment variables in the "Actions" tab where you edit the action
  that starts your Python script. The environment variables required by this project are:
-

| Variable Name | Variable Value                                             | Example                        |
|---------------|------------------------------------------------------------|--------------------------------|
| BASE_URL      | The URL of the Blizzard Game Data API                      | https://eu.api.blizzard.com    |
| TOKEN_URL     | The URL of the Blizzard Token API                          | https://oauth.battle.net/token |
| CLIENT_ID     | The id of your client credentials you made in step one     | -                              |
| CLIENT_SECRET | The secret of your client credentials you made in step one | -                              |
| REALM_NAME    | The realm you're checking for                              | "Crusader Strike"              |
| ENEMY_STATUS  | The status you're hoping the realm does not have           | LOCKED                         |
        


