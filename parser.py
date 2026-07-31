from db.keywords import (
    TABLESPACE_KEYWORDS,
    DATAFILE_KEYWORDS,
    ADD_KEYWORDS,
    RESIZE_KEYWORDS
)

from db.tablespace_loader import load_tablespaces
tablespaces = load_tablespaces()

# Detect Keywords
def detect_keywords(command):

    command = command.upper()

    # Add Datafile
    if any(word in command for word in ADD_KEYWORDS):
        return "ADD_DATAFILE"

    # Resize Datafile
    if any(word in command for word in RESIZE_KEYWORDS):
        return "RESIZE_DATAFILE"

    # Tablespace Query
    if any(word in command for word in TABLESPACE_KEYWORDS):
        return "CHECK_TABLESPACE"

    # Datafile Query
    if any (word in command for word in DATAFILE_KEYWORDS):
        return "CHECK_DATAFILES"

    return None


# Detect Tablespace
def detect_tablespace(command):

    command = command.upper()

    for ts in tablespaces:

        if ts.upper() in command:
            return ts

    return None

# Main parser query
def parse_command(command):

    intent = detect_keywords(command)

    if intent is None:
        return None

    return{
        "type": "QUERY" if intent.startswith("CHECK") else "DDL_PREVIEW",
        "intent": intent,
        "tablespace": detect_tablespace(command),
        "original_command": command
    }