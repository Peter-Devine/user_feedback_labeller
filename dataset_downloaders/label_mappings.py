from dataset_downloaders.guzman_2015 import download_guzman
from dataset_downloaders.maalej_2016 import download_maalej
from dataset_downloaders.williams_2017 import download_williams

dataset_downloaders = {
    "guzman_2015": download_guzman,
    "maalej_2016": download_maalej,
    "williams_2017": download_williams,
}

relevance_dataset_mappings = {
    "guzman_2015": {
        "relevant": ["Bug report", "Feature shortcoming", "Feature strength", 'User request'],
        "irrelevant": ["Complaint", "Noise", "Praise", "Usage scenario"]
    },
    "maalej_2016": {
        "relevant": ["Bug", "Feature"],
        "irrelevant": ["Rating", "UserExperience"]
    },
    "williams_2017": {
        "relevant": ["bug", "fea"],
        "irrelevant": ["oth"]
    },
}

bfo_dataset_mappings = {
    "guzman_2015": {
        "bug": ["Bug report"],
        "feature": ["Feature shortcoming", 'User request'],
        "other": ["Complaint", "Noise", "Praise", "Usage scenario", "Feature strength"]
    },
    "maalej_2016": {
        "bug": ["Bug"],
        "feature": ["Feature"],
        "other": ["Rating", "UserExperience"]
    },
    "williams_2017": {
        "bug": ["bug"],
        "feature": ["fea"],
        "other": ["oth"]
    },
}