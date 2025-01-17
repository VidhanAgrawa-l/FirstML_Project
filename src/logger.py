import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

# if __name__== "__main__":
#     logging.info("logging has started")


# You're baking a cake and want to keep track of everything happening so you can remember what went well or what went wrong.

# You write notes in a notebook:
# "Started mixing ingredients at 10 AM."
# "Oops, spilled some flour!"
# "Cake is in the oven at 10:15 AM."
# "Finished baking at 11 AM. Tastes great!"
# These notes help you see:

# What steps you followed.
# Where mistakes happened (spilling flour).
# The overall process timeline.

# In programming, this notebook is called "Logging".

# What is logger.py?
# It’s like your notebook setup:

# You decide where to write your notes (console, file, or both).
# You organize the notes by importance:
# DEBUG: Small details for developers.
# INFO: General progress updates.
# WARNING: Something unusual but not broken.
# ERROR: A problem happened, but the program can continue.
# CRITICAL: Big problem! Something serious happened.


# What Happens When You Run It?
# Console Output:

# 2025-01-17 12:00:00 - INFO - Starting the tea-making process.
# 2025-01-17 12:00:01 - DEBUG - Boiling water...
# 2025-01-17 12:00:02 - INFO - Water boiled successfully.
# 2025-01-17 12:00:03 - DEBUG - Adding tea leaves...
# 2025-01-17 12:00:04 - ERROR - An error occurred: No tea leaves left!
