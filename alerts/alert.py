def tablepsace_alert(df):

    df["used %"] = df["used %"].astype(float)

    threshold = df[df["used %"] >= 95]