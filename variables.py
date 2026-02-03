# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 28733143  # Get this value from my.telegram.org/apps
    API_HASH = "f7bbd29cf8ba336237046dbecfeab519"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgresql://postgres:hCBSVxkbSbQQKQQgWrOVJQzDxyptYevI@nozomi.proxy.rlwy.net:51342/railway"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1003814371676
    MESSAGE_DUMP = -1003814371676

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://neonman242:neonman.123@game0.sqfzcd4.mongodb.net/MikoDB?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "AdvanceBot_support"
    SUPPORT_ID = -1003814371676

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "8312882882:AAGJR4EhsOcqZI9w5cfTqGAV9_oVZpsTYsU"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 7066124462
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
