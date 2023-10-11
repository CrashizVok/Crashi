import smtplib
import webbrowser, time

def banner():
    print("  _______     _______      _______     _______      _     _      _      _____ _                                            ")
    print(" |  _____|   |  ___  |    |  ___  |   | ______|    | |   | |    | |    |____  /                                               ")
    print(" | |         | |___| |    | |   | |   | |          | |   | |    | |        / /                                             ")
    print(" | |         |  _  __|    | |___| |   | |_____     | |___| |    | |       / /                                           ")
    print(" | |         | | \ \      |       |   |_____  |    |  ___  |    | |      / /                                                 ")
    print(" | |         | |  \ \     |  / \  |         | |    | |   | |    | |     / /                                         ")
    print(" | |_____    | |   \ \    | /   \ |    _____| |    | |   | |    | |    / /____                                             ")
    print(" |_______|   | |    \_\   |/     \|   |_______|    |_|   |_|    |_|   /_ _____|                                              ")
    print(f"BY Crashi                        Crashiz Ver 1.0 ")
    print("Email spammer[1] View bot[2] .........")

banner()
print()

x = int(input("Menyik feladat fusson le: "))
if x == 1:
    if x == 1:    
        toaddrs = input("Add meg az email címét akinek küldöd: ")
        fromaddrs = "nagykoldok@gmail.com"
        message = input("Add meg az üzenetet: ")
        szam = int(input("Add meg hogy hányszor küldje el: "))

        with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('nagykoldok@gmail.com',"fhidnucifyoishzb")
            for i in range(szam):
                smtpserver.sendmail(fromaddrs,toaddrs,message)
                print(i)
            print("Sikeres email küldés")    
            print("Vége a programnak")
if x == 2:
    #!usr/bin/env python
    #-*- coding:utf-8 -*-

    """
    @author: &! Tekky#1337 
    @file: main.py
    @time: 2024/07/29
    """

    import requests, time, json, urllib.parse, random, threading

    VIDEO = ""
    IID = ""
    DID = ""

    def view(video):
        try:
            
            version = random.choice(
                [247, 312, 322, 357, 358, 415, 422, 444, 466]
            )
            device = random.choice(
                ["SM-G9900", "sm-g950f", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B", "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B", "SM-A525F"]
            )
            
            host = random.choice(
                ["api16.tiktokv.com", "api.tiktokv.com", "api19.tiktokv.com", "api21.tiktokv.com"]
            )

            params = urllib.parse.urlencode(
                {
                    "app_language": "fr",
                    "iid": IID,
                    "device_id": DID,
                    "channel": "googleplay",
                    "device_type": device,
                    "ac": "wifi",
                    "os_version": random.randint(5, 11),
                    "version_code": version,
                    "app_name": "trill",
                    "device_brand": "samsung",
                    "ssmix": "a",
                    "device_platform": "android",
                    "aid": 1180,
                    "as": "a1iosdfgh",  # creds to @auut for params bypass
                    "cp": "androide1",
                }
            )

            response = requests.post(
                url = (
                    "https://"
                        + host
                        + "/aweme/v1/aweme/stats?"
                        + params
                ),
                data = (
                    f'&manifest_version_code={version}'
                        + f'&update_version_code={version}0'
                        + '&play_delta=1'
                        + f'&item_id={video}'
                        + f'&version_code={version}'
                        + '&aweme_type=0'
                ), 
                headers = {
                    "host": host,
                    "connection": "keep-alive",
                    "accept-encoding": "gzip",
                    "x-ss-req-ticket": str(int(time.time())),
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "user-agent": f"com.ss.android.ugc.trill/{version} (Linux; U; Android 11; fr_FR; {device}; Build/RP1A.200720.012; Cronet/58.0.2991.0)"
                },
                # proxies = {
                #     'http': 'http://xxx:zeff@geo.iproyal.com:12323',
                #     'https': 'http://xxx:zeff@geo.iproyal.com:12323',
                # }
            )

            print(response.json())
        except Exception as e:
            pass

    while True:
        if threading.active_count() < 10: # don't put too high lmao I warned you
            threading.Thread(
                target = view, 
                args = [
                    VIDEO
                ]
            ).start()
else:
    print("Valami nincs jól")