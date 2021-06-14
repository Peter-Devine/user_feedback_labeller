import pandas as pd

def download_scalabrino():

    df = pd.read_csv("https://dibt.unimol.it/reports/clap/downloads/rq3-manually-classified-implemented-reviews.csv")

    df = df.rename(columns = {"body": "text", "category": "label"})
    df["app"] = df["App-name"]
    df["sublabel"] = df["rating"]

    return df
