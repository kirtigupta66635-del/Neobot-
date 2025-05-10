
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "29308061"))
API_HASH = getenv("API_HASH", "462de3dfc98fd938ef9c6ee31a72d099")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7937199110:AAHpT7xYewYZ0D7So8I60Qrd3_Bjx1eadc4")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://alyabots636:6dvpdXmakQrZSnJ0@vampireking.qqfnpan.mongodb.net/?retryWrites=true&w=majority&appName=VAMPIREKING")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-100264978111))

OWNER_ID = int(getenv("OWNER_ID", 8174329380))

OWNER = int(getenv("OWNER", 8084276864))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-7bb233ff-bef9-4ef8-85d9-46df858d1d23")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/MR-KILLER-OP/KILLER-OP-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = "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"
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DPZ_WORLD_OP")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/DPZ_WORLD_OP")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = '7f92897a59464ddbbf00f06cd6bda7fc'
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION","BQExqCAAnuUaGo528FVSuZRr5pp8smkP_kyp9P1xfi_jerVTyFKibmVRyEZg6HStlqsmizbdSjMcKiiHlm-r3jpC0_2V306v27_iaL6mAYE9GzHVMQFoxYZBEmseEjen07ALz4GQatXyyWPaTlF1M_XApcPEqtINcjLBmnngKdQ6JfbRTyZ3gfXaOlu_cAbYvi8pLjbq1uy2uLYWz-YgXY-RJGJlMBTxI9iXCkQoPZ3PImmzMt6MGrbhPn92jrjwr4VJsPcp9kiUuB9piWhmfX5w1pxppzoouBozw2LzQ9eytONvNOItL-wKpOOMZxTVj7EvK9uEH2vnB-FkrS0eH15vdtdCcQAAAAHV7lwgAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/geixdw.jpg")
PING_IMG_URL = "https://files.catbox.moe/1wntxh.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/wcd3us.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://files.catbox.moe/hvb582.jpg")
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/geixdw.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/zun19v.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/jmo3i7.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/jmo3i7.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
