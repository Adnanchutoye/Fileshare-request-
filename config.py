#(©)Code-society




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7702677441:AAFiPlXVnCGAq8iXRq86gMC1ElUlgz4gJEE")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20718334"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002255147559"))

CHANNEL_ONE = int(os.environ.get("CHANNEL_ONE", "-1002255147559"))
CHANNEL_TWO = int(os.environ.get("CHANNEL_TWO", "-1002323979383"))
CHANNEL_THREE = int(os.environ.get("CHANNEL_THREE", "-1002232203073"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2024483729"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://solo_bot:solo2319p@cluster0.wiqnf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ!! {mention} ⚡,\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ : <a href=https://t.me/Anime_Hindi_Sub_Industry>ᴀɴɪᴍᴇ ɪɴᴅᴜsᴛʀʏ</a></b>",)
try:
    ADMINS=[5585016974]
    for x in (os.environ.get("ADMINS", "2024483729 6231961680 5585016974").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ!! {mention},\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ : <a href=https://t.me/Anime_Hindi_Sub_Industry>ᴀɴɪᴍᴇ ɪɴᴅᴜsᴛʀʏ</a></b>",)

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!» ᴍʏ ᴏᴡɴᴇʀ : <a href=https://t.me/Anime_Hindi_Sub_Industry>ᴀɴɪᴍᴇ ɪɴᴅᴜsᴛʀʏ</a></b>",

ADMINS.append(5585016974)
ADMINS.append(2024483729)

LOG_FILE_NAME = "logs.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
