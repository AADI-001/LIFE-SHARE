#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello  {first} 🖤"
 "Welcome To [TIF] Links Bot __________________________________________________________________"
"📌Join our other Channels @TIF_TvSeries1 🌹 @TIF_WebSeries  @TIF_Moviez 🌹 @TIF_Anime _________________________________________________________"
  
"📌Our Discussion Group @TIFDiscuss 🌹 @TIF_OTs 🌹 @TIFRequests  "
"__________________________________________________________________"
"📌Our Store @TIF_Shoppie 🌹 @TIF_Vouches  __________________________________________________________________"

"📌 Follow us on Instagram  https://instagram.com/tif_network?igshid=YmMyMTA2M2Y= __________________________________________________________________")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1014734769 989451380 878419316 692926828 1066681358 1626129666 359751388 1428191214 858310812 1059440698 1842073219 1362429856 2092914085 1264027502 1988210787 838912777 1170258624 724516516 1545262687 1141611406 772094614 1365187878 992923461 846915783 1399513864 994884531").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first} "
"____________________________________________________________________"
"To use me, You need to join "
"K-Drama [TIF]   https://t.me/+zMyGDIqisi1hNGI1 " 
"____________________________________________________________________"
"There are no Ads or Link Shortners"
"____________________________________________________________________"
"I am not an Auto Filter Bot, I can't send files if u send me names here, you have to click on the links in our channels"
"____________________________________________________________________"
"Join the Channel and click on the Link again to get files 😉")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1407122915)

LOG_FILE_NAME = "filesharingbot.txt"

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
