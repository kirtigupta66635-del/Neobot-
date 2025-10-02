
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "29308061"))
API_HASH = getenv("API_HASH", "462de3dfc98fd938ef9c6ee31a72d099")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7959513360:AAE9H03DtBa8Mrbs9H9XLNDFB_s8XjibaHs")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://alyabots636:6dvpdXmakQrZSnJ0@vampireking.qqfnpan.mongodb.net/?retryWrites=true&w=majority&appName=VAMPIREKING")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1003070925721))

OWNER_ID = int(getenv("OWNER_ID", 8410426172))

OWNER = int(getenv("OWNER", 8410426172))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-AAC-IRkPcu7dxXBXyYINt4D6-K0yThQkytnKsoGulhvg_____wJzXQYI1Ay1")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/kirtigupta66635-del/Neobot-.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = "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"
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/promoters_botse")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/promoters_botse")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = '7f92897a59464ddbbf00f06cd6bda7fc'
YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY", None)
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION","BQCMd7sAUyS8TU__bNfG-ukzZa_TLqttrBYU-kVpSqfbflFs-IaEnrhYIx_tll_-TTHfUVBo24xiBbPvXV4rp0wr1cukUTC-MkLOanbOlCN7WuKbXNsOVLqoouMTae7QVIQprhUVEyJdAk-dc2mTu2okxoypX5R7UWjHyiLkGnbyNEbygjlcHhZcOAwRaHtlbc6jtOXyn9e374AYuN4iqRQAp0-zTJXDLhu_DjeZqL3OniFTPYSeqXpcPJsmQcN2xuVM7v-DC-LPEswQXg5COwfhpipYGIq87QUQqU1kmndwKrwlFjQrbPAsceJMtgk9X7bcqLq_tsJCFBNpsCWbV1r9KjKmugAAAAHlB_nMAA")
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
