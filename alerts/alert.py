def tablepsace_alert(df):

    df["used %"] = df["used %"].astype(float)

    danger = df[df["used %"] >= 95]
    warning = df[(df["used %"] >= 85 & df["used %"] < 95)]

    return warning, danger