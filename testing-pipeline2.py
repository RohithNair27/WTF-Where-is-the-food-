import requests

API_URL = "https://yelp-pipeline-2.onrender.com/analyze-business"

def main():
    print("\n=== Yelp Pipeline 2 API Tester ===\n")
    yelp_url = input("Paste a Yelp business URL: ").strip()

    if not yelp_url:
        print("No URL entered.")
        return

    try:
        response = requests.post(
            API_URL,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            json={"business_url": yelp_url}
        )

        print("\n--- Status Code:", response.status_code)
        print("\n--- Raw Response ---")
        print(response.text)

        if response.status_code == 200:
            print("\n--- Parsed JSON ---")
            data = response.json()
            print(f"\nP (Positive):\n{data.get('P','N/A')}\n")
            print(f"N (Negative):\n{data.get('N','N/A')}\n")
            print(f"J (Judge Verdict):\n{data.get('J','N/A')}\n")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()