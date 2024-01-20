from dotenv import load_dotenv

from check.RealmCheckService import check_realm_status

# Load environment variables from the .env file
load_dotenv()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_realm_status()
