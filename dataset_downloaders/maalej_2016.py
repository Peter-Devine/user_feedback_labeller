import requests
import zipfile
import json
import os
import io
import shutil

import pandas as pd

def download_maalej():
    task_data_path = os.path.join(".", "temp_data", "maalej_2016_temp")
    os.makedirs(task_data_path, exist_ok = True)

    # from https://mast.informatik.uni-hamburg.de/wp-content/uploads/2015/06/review_classification_preprint.pdf
    # Bug Report, Feature Request, or Simply Praise? On Automatically Classifying App Reviews
    r = requests.get("https://mast.informatik.uni-hamburg.de/wp-content/uploads/2014/03/REJ_data.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path = task_data_path)


    json_path = os.path.join(task_data_path, "REJ_data", "all.json")

    with open(json_path) as json_file:
        data = json.load(json_file)

    shutil.rmtree(task_data_path)
    
    df_data = [ ]
    
    for datum in data:
        text = datum["comment"] if datum["title"] is None else datum["title"] + ". " + datum["comment"]
        
        df_data.append({"title": datum["title"],
                "text": text,
                "rating": datum["rating"],
                "label": datum["label"],
                "reviewer": datum["reviewer"],
                "app": datum["appId"],
                "dataSource": datum["dataSource"],
                "date": datum["date"]})

    df = pd.DataFrame(df_data)

    return df
