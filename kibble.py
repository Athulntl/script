import requests,datetime
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable insecure request warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ti = ["7454287947", "1086441183", "6737423619", "6796696313"]
tn = ["cryptoboy", "Athul G", "Swa Am", "Akkku A"]
no = ["31", "77", "79", "99"]
num=[0]

while True:
    for i, j, n in zip(ti, tn, no):
        

        proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}

        headers = {
    'Host': 'api-game.kibble.exchange',
    # 'Content-Length': '73',
    'Sec-Ch-Ua': '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Sec-Ch-Ua-Mobile': '?1',
    'Authorization': "''",
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; ASUS_I005DA Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.186 Mobile Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Android"',
    'Origin': 'https://clicker.kibble.exchange',
    'X-Requested-With': 'org.telegram.messenger',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://clicker.kibble.exchange/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en,en-US;q=0.9',
    'Priority': 'u=1, i',
}

        json_data1 = {
            'telegram_id': i,
            'telegram_name': j,
            'referral_code': '',
        }

        response = requests.post('https://api-game.kibble.exchange/auth/connect-telegram', headers=headers, json=json_data1, verify=False)
        
        if response.status_code == 200:
            try:
                token = response.json()['token']
                print("try")
            except (ValueError, KeyError) as e:
                print(f"Error parsing token response for {j}: {e}")
                print("except")
                continue
        else:
            print(f"{n} Failed to get token for {j}: {response.status_code} - {response.text}")
            print("else")
             
            continue

        headers1 = {
    'Host': 'api-game.kibble.exchange',
    # 'Content-Length': '106',
    'Sec-Ch-Ua': '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Sec-Ch-Ua-Mobile': '?1',
    'Authorization': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; ASUS_I005DA Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.186 Mobile Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Android"',
    'Origin': 'https://clicker.kibble.exchange',
    'X-Requested-With': 'org.telegram.messenger',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://clicker.kibble.exchange/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en,en-US;q=0.9',
    'Priority': 'u=1, i',
}

        json_data=[
    {
    'points': 840,
    'taps': 7,
    'signature': 'c78a0694e91f26e27b8f579fb9b0815dadcdb99d11f8c5365c4e7c7f202f7377',
}
]


        response = requests.get('https://api-game.kibble.exchange/users/statistic', headers=headers1, verify=False)
        
        if response.status_code == 200:
            try:
                for a in num:
                 user_stats = response.json()
                 print("check")
                 if user_stats['energy'] >= 7:
                    response1 = requests.post('https://api-game.kibble.exchange/points/click', headers=headers1, json=json_data[a], verify=False)
                    respons2 = requests.get('https://api-game.kibble.exchange/tasks/daily-quest', headers=headers1, verify=False)
                    respons3 = requests.get('https://api-game.kibble.exchange/tasks/daily-quest/me', headers=headers1, verify=False)
                    response4 = requests.get('https://api-game.kibble.exchange/users/statistic', headers=headers1, verify=False)
                    print(n, "balance", user_stats['points'], "energy", user_stats['energy'],datetime.datetime.now().time())
            except ValueError as e:
                print(f"Error parsing user stats response for {j}: {e}")
        else:
            print(f"{n} Failed to get user stats for {j}: {response.status_code} - {response.text}")
       
