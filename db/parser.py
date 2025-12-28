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