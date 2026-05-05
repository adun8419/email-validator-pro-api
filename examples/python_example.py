import requests

# Email Validator Pro
# Free API key: https://rapidapi.com/adunaev8419/api/email-validator-pro11

API_KEY = "YOUR_RAPIDAPI_KEY"
BASE_URL = "https://email-validator-pro11.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "Content-Type": "application/json"}

def validate_email(email):
    r = requests.post(f"{BASE_URL}/validate", json={"email": email}, headers=headers)
    return r.json()

def validate_batch(emails):
    r = requests.post(f"{BASE_URL}/batch", json={"emails": emails}, headers=headers)
    return r.json()

if __name__ == "__main__":
    print(validate_email("user@gmail.com"))
    print(validate_email("fake@mailinator.com"))
    print(validate_batch(["user@gmail.com", "test@mailinator.com"]))