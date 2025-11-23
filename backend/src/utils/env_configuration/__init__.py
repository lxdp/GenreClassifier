import os

from dotenv import load_dotenv
load_dotenv()

MODE = os.getenv("MODE")


# Find a way to access cuda for development and production instead of cpu.
if MODE == "local":
    from .local import *
elif MODE == "production":
    from .production import *
elif MODE == "development":
    from .development import *
else:
    raise ValueError("Not a valid mode.")