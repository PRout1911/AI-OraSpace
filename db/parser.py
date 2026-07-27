from db.keywords import (
    TABLESPACE_KEYWORDS,
    DATAFILE_KEYWORDS,
    ADD_KEYWORDS,
    RESIZE_KEYWORDS
)

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
        return "CHECK_DATAFILE"

    return None

# Detect Tablespace
def detect_tablespace(command, tablespaces):

    command = command.upper()

    for ts in tablespaces:

        if ts.upper() in command:
            return ts

    return None

# Main parser query
def parse_command(command, tablespaces):

    keyword = detect_keywords(command)

    tablespace = detect_tablespace(command, tablespaces)

    if keyword is None:
        return None

    return{
        "type": "QUERY" if "CHECK" in keyword else "DDL_PREVIEW",
        "keyword": keyword,
        "tablespace": tablespace,
        "original_command": command
    }







































def comm_parse(comm: str):
    comm = comm.lower().strip()

    if comm == "check ts":
        return {
            "type": "QUERY",
            "action": "TABLESPACE"
    }

    if comm.startswith("check df files"):
        ts = comm.split()[-1].upper() #check df files users : it will split all according to spaces then will choose last word & uppercase it
        return {
            "type": "QUERY",
            "action": "DATAFILES",
            "tablespace": ts
        }

    if comm.startswith("add df"):
        return {
            "type": "DDL_PREVIEW",
            "sql": comm #since DDL command is dangerous, it will not auto run but ask for confirmation
        }

    if comm.startswith("resize"):
        return {
            "type": "DDL_PREVIEW",
            "sql": comm # same logic as add df, as altering anything should be confirmed once
        }
        
    return None #if user provides commands like hello, increae db, delete db tc...it would return nothing