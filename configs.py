# (c) @AbirHasan2005

import os


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("STRING_SESSION")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = "-1001384761806"
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = "-1001405478529"
    # Your User ID
    USER_ID = "1722532247"
