import csv
import requests

def call_customers():
    print("📢 Starting scheduled calls...")

    try:
        with open("customers.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["Name"]
                phone = row["Phone"].replace(" ", "").replace("+", "")
                print(f"📞 Calling {name} at {phone}")

                url = "https://api.exotel.com/v1/Accounts/jainalpahaar1/Calls/connect"
                payload = {
                    'From': '09513886363',
                    'To': phone,
                    'CallerId': '09513886363',
                    'Url': 'https://voice-xml-render.onrender.com/xml',  # Replace with your XML URL
                    'CallType': 'trans'
                }
                auth = ('jainalpahaar1', '99f12f11d042f057e05c526e0028215db14d2e0264977c22')

                response = requests.post(url, data=payload, auth=auth)
                print(f"✅ {name} call response: {response.status_code}, {response.text}")

    except Exception as e:
        print(f"❌ Error in call_customers(): {e}")
