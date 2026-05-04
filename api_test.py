import requests

print("🚀 Starting API tests...")

apis = [
    "https://blockstream.info/api/blocks/tip/height",
    "https://api.blockcypher.com/v1/btc/main",
    "https://mempool.space/api/blocks/tip/height"
]

for api in apis:
    print("\n---------------------")
    print("Testing:", api)

    try:
        r = requests.get(api, timeout=10)
        print("Status:", r.status_code)
        print("Response:", r.text[:120])
    except Exception as e:
        print("Error:", e)

print("\n✅ Done")
