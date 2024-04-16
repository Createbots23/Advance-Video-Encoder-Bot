import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22672907")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "0ff15ae2153bd8e03b48cb293010bc6a") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7012772836:AAFBwKBA5S3s7ZmLTmWlMdf_U1NgC85z_vk") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002056115205') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://rani828719:sVyRWZOrUzIWNfHp@cluster0.zodktob.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6287591671")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002022119783')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg, https://graph.org/file/758ac2c9e68cb0ab7d47f.jpg, https://graph.org/file/701ff72fb43d85e073f03.jpg, https://graph.org/file/1cd7d4a6e8d57e9a3430f.jpg, https://graph.org/file/7f4a9dba475bb0e832ef9.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
