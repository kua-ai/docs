import requests


def auth():
    url = "https://api-beta.kua.ai/core/api/v2/accounts/sessions/email"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "email": "alex@kua.ai",
        "password": "12345678"
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())


def import_product():
    url = "https://api-beta.kua.ai/weaver/api/v2/products/import/amazon"

    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrdWEuYWkiLCJpc3MiOiJrdWEuYWkiLCJpYXQiOjE3MjMwMjA3MTIsImV4cCI6MTcyMzYyNTUxMiwiYWNjIjoiYmZiNGZhN2ItZDgwMS00YzcyLWE4NjItNTQzYjcwZGU2NWNhIiwic2VzIjoiNzk0NjYzODA2OTM2MTIzMDMiLCJ3b3MiOiIzNjUwMjQ1MzE3OTY1NTIxMDYiLCJjdiI6IldPUktTUEFDRSIsIml2IjoiV09SS1NQQUNFIn0.1v9L7Dnp2L1p6aMRKwnr2jmGU4RbOHt11nBaDcHFY6k'

    payload = {
        "marketplace": "US",
        "asins": ["B0953SDCRG"]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.json())


def get_import():
    url = "https://api-beta.kua.ai/weaver/api/v2/products/import/583869576569603234"

    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrdWEuYWkiLCJpc3MiOiJrdWEuYWkiLCJpYXQiOjE3MjMwMjA3MTIsImV4cCI6MTcyMzYyNTUxMiwiYWNjIjoiYmZiNGZhN2ItZDgwMS00YzcyLWE4NjItNTQzYjcwZGU2NWNhIiwic2VzIjoiNzk0NjYzODA2OTM2MTIzMDMiLCJ3b3MiOiIzNjUwMjQ1MzE3OTY1NTIxMDYiLCJjdiI6IldPUktTUEFDRSIsIml2IjoiV09SS1NQQUNFIn0.1v9L7Dnp2L1p6aMRKwnr2jmGU4RbOHt11nBaDcHFY6k'

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.request("GET", url, headers=headers)
    print(response.json())


def create():
    url = "https://api-beta.kua.ai/weaver/api/v2/generations"

    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrdWEuYWkiLCJpc3MiOiJrdWEuYWkiLCJpYXQiOjE3MjMwMjA3MTIsImV4cCI6MTcyMzYyNTUxMiwiYWNjIjoiYmZiNGZhN2ItZDgwMS00YzcyLWE4NjItNTQzYjcwZGU2NWNhIiwic2VzIjoiNzk0NjYzODA2OTM2MTIzMDMiLCJ3b3MiOiIzNjUwMjQ1MzE3OTY1NTIxMDYiLCJjdiI6IldPUktTUEFDRSIsIml2IjoiV09SS1NQQUNFIn0.1v9L7Dnp2L1p6aMRKwnr2jmGU4RbOHt11nBaDcHFY6k'

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "applicationId": "295231319878644967",
        "inputs": {
            "Imageposition": "2nd",
            "Language": "American English",
            "Link": "https://kua.ai",
            "PrimaryKeyword": "Elon Musk",
            "Product": "{{_product['B0953SDCRG']}}"  # Replace B0787P86ZZ with your actual ASIN, {{_product['{ASIN}']}}
        }
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.json())


def get():
    url = "https://api-beta.kua.ai/weaver/api/v2/generations/295639361226721447"

    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrdWEuYWkiLCJpc3MiOiJrdWEuYWkiLCJpYXQiOjE3MjMwMjA3MTIsImV4cCI6MTcyMzYyNTUxMiwiYWNjIjoiYmZiNGZhN2ItZDgwMS00YzcyLWE4NjItNTQzYjcwZGU2NWNhIiwic2VzIjoiNzk0NjYzODA2OTM2MTIzMDMiLCJ3b3MiOiIzNjUwMjQ1MzE3OTY1NTIxMDYiLCJjdiI6IldPUktTUEFDRSIsIml2IjoiV09SS1NQQUNFIn0.1v9L7Dnp2L1p6aMRKwnr2jmGU4RbOHt11nBaDcHFY6k'

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.json())
    if response.json()["status"] == "SUCCESS":
        print("Generation completed")
        print(response.json()["result"])


if __name__ == '__main__':
    get()
