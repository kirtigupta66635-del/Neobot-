import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "26399631"))
API_HASH = getenv("API_HASH", "16b94384632645b5c23ee23ac1b0c8af")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7913305235:AAG_ee32FXN5yqwAH74zcUdq-XUnefGP_H4")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://musicbotxd:musicbotxd@cluster0.6thyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002392274240))

OWNER_ID = int(getenv("OWNER_ID", 6018803920))

OWNER = int(getenv("OWNER", 6018803920))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Zfini/Adonis",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = "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"
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MBT_UPDATES")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+EK-lvu4shmBkNmZl")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = '7f92897a59464ddbbf00f06cd6bda7fc'
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION","BAFUizgAhmo99RhQr_NxjtRUn25XZQKU1PEh1Jf3lYhN3nA2Pd-BplowpZWJDdYGbSW5B9sk3cGwwZm55UNgdyRG_0gsoDtwxwSSOr_i0JlqOguvYwKrfD3ALFMQhR34F30ZxrYBuZFMESx_ekMvPeFp5XxO9EoBuRYliHvMVqFVjwWnmE5ON3bsbG2P3kKN_trOZrmg5bw5QhUVVIZ4RbHhc7MzK9Zuse31TbckT4vPInEA_rOH-cec61A47EdP0N3pjZlhUPEFgyUrky3wgLc9XdZFGq9kyc6c66VIYlcLSQKvSTRF_LArOmvjUa1H1XEh3udbS4nyrsf6QezsHJDvu5zaqQAAAAGXpY4PAA")
STRING2 = getenv("STRING_SESSION2","BQGMDg4AEb3cgtWM_a8lK9eg2y2z4GSZYeiAkX-l1mKuBwXo8VLo8UTlPFmIKiwBzpfdI8P6nQQ7-IJzgCAnER4SkqiKT87DGzAUYzLyHP3DjO9CmQkoZwQr-DRLoKEIio-OVlq2qATXIzIEY24d4IYPrWH4lvZ8r_coJAFVE0P6zxrPaFaF2asSo8CrSN0BElg9ew3qbUCT8Hni7AL0VSKPN8-P2g8BFsg-ce7dN2I9m3J7NOYm4SyGjPp6-hko_Zi8WucYcqEk_kVgzA0W6fPLvFW5GsKEX-div-2wmsH597MTzAca_M6IA611DcJ5jSaeBt82HkxhKRKzHjZxTUrQNFVasAAAAAHXGk-qAA")
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
