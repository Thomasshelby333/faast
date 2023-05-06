# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '14505719'))
    API_HASH = str(getenv('API_HASH', '620f0a2aa2cd1474a4953619b3e3643d'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', 'BOT_TOKEN'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'rxmoviesdaa'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001660274107'))
    PORT = int(getenv('PORT', 8080))
    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "BOTTOM")
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5296610774").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    SHORTENER_API = str(getenv('SHORTENER_API', 'b6aace46d40c605fff8e0cafbcd8fbe416851f4d'))
    SHORTENER_WEBSITE = str(getenv('SHORTENER_WEBSITE', 'tnlink.in'))
    FDQN = str(getenv('FDQN', 'https://rxmoviesdaa.onrender.com'))

    APP_NAME = None
    OWNER_USERNAME = str(getenv('JonSnow11'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', 'Rxmovies'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "DATABASE_URI"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "@RolexMoviesOXO"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
