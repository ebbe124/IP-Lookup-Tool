print ("")
print ("")
print ("|_ _| |  _ \    | |       ___     ___   | | __  _   _   _ __     | __ )   _   _    | ____| | |__   | __ )    ___   _| || |_   / _ \   / _ \   / _ \   / _ \ ")
print ("| |  | |_) |   | |      / _ \   / _ \  | |/ / | | | | | '_ \    |  _ \  | | | |   |  _|   | '_ \  |  _ \   / _ \ |_  ..  _| | (_) | | (_) | | (_) | | (_) |")
print ("| |  |  __/    | |___  | (_) | | (_) | |   <  | |_| | | |_) |   | |_) | | |_| |   | |___  | |_) | | |_) | |  __/ |_      _|  \__, |  \__, |  \__, |  \__, |")
print ("|___| |_|       |_____|  \___/   \___/  |_|\_\  \__,_| | .__/    |____/   \__, |   |_____| |_.__/  |____/   \___|  |_||_|      /_/     /_/     /_/     /_/ ")
print ("                                                       |_|                |___/                                                                        ")     

print ("Only you Are Responsable For Your Actions")
print ("Support Me")
print ("PayPal: www.paypal.me/hgdhgd0011")
print ("Discord Server: discord.ggDEQDmnVrbQ")
import requests
while True:
    try:
        ip = input("Enter Ip: ")  
        Get = requests.get(f"http://ip-api.com/json/{ip}?fields=66842623")
        Get_values = Get.json()
        if Get_values['status'] == "fail":
            wowowow = Get_values['message']
            print(f"Operation failed. Reason: {wowowow}")
        else:
            for i in Get_values:
                x = Get_values[i]
                while len(i) < 13: # this is only for like space injection
                    i = " " + i
                if x == "":
                    x = "Undefined"
                print(i,":", x)
    except:
        wowowow = "Connection issue, check internet"
        print(f"Operation failed. Reason: {wowowow}")
