import csv
import requests
import time

# Exotel credentials and config
EXOTEL_SID = "jainalpahaar1"
EXOTEL_TOKEN = "99f12f11d042f057e05c526e0028215db14d2e0264977c22"
EXOTEL_FROM = "09513886363"
FLOW_URL = "https://voiceapp-5sxo.onrender.com/voice"

CUSTOMERS_CSV = "customers.csv"

def make_call(to_number):
    url = f"https://{EXOTEL_SID}:{EXOTEL_TOKEN}@api.exotel.com/v1/Accounts/{EXOTEL_SID}/Calls/connect"

    data = {
        "From": EXOTEL_FROM,
        "To": to_number,
        "CallerId": EXOTEL_FROM,
        "Url": FLOW_URL,
        "CallType": "trans"
    }

    print(f"📞 Calling {to_number}...")
    response = requests.post(url, data=data)
    print("✅ Response:", response.status_code, response.text)

def schedule_calls():
    with open(CUSTOMERS_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            number = row['phone'].replace(" ", "").replace("+", "")
            print(f"Scheduling call for {name} ({number})...")
            make_call(number)
            time.sleep(3)  # avoid API rate limit

if __name__ == "__main__":
    print("📆 Starting call scheduler...")
    schedule_calls()
