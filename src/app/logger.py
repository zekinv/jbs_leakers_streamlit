import logging
import logging.handlers
import os

#: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
LEVEL = os.getenv("LOGGER")

rfh = logging.handlers.RotatingFileHandler(
    filename='logs', 
    mode='a',
    maxBytes=100*1024*1024,
    backupCount=2,
    encoding=None,
    delay=0
)

logging.basicConfig(
    # level=logging.DEBUG,
    level = logging.__dict__.get(LEVEL),
    format="%(asctime)s %(message)s",
    datefmt='%d %m %Y %H:%M:%S',
    handlers=[
        rfh
    ]
)