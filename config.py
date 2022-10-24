import os

class Config(object):
	BOT_TOKEN = os.environ.get("5571503607:AAHvem3lFbtFpSG7AV6OEKslPDROhA64wpw")
	APP_ID = int(os.environ.get("7908729"))
	API_HASH = os.environ.get("2c4144e2797e81ccd415409c441ac2fb")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	SUDO_USERS = list(set(int(x) for x in ''.split()))
	SUDO_USERS.append(1215424881)
	SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "[🔔](https://i.imgur.com/SmqQApH.jpg) **FORCE SUBSCRIBE :**\n\nForce Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.",
        
        "[⚙](https://i.imgur.com/ItAdRVF.jpg) **SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n● Note: Only Creator Of The Group Can Setup Me.",
        
        "[⚙](https://i.imgur.com/LnOEiTK.jpg) **COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n● Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "[👨‍💻](https://telegra.ph/file/f2b08ba94ebd139d9da96.jpg) **DEVELOPED BY @**"
      ]

      START_MSG = "**Hey! [👋](https://i.imgur.com/SmqQApH.jpg) [{}](tg://user?id={})**\n\n● I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\n● Learn More At 👉 /help"
