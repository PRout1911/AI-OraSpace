def comm_parse(comm: str):
    comm = comm.lower().strip()

    if comm == "check ts":
        return {
            "type": "QUERY",
            "action": "TABLESPACE"
    }