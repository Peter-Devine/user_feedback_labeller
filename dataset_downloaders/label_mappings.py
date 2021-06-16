from dataset_downloaders.chen_2014 import download_chen
from dataset_downloaders.ciurumelea_2017 import download_ciurumelea
from dataset_downloaders.di_sorbo_2016 import download_di_sorbo
from dataset_downloaders.guzman_2015 import download_guzman
from dataset_downloaders.maalej_2016 import download_maalej
from dataset_downloaders.scalabrino_2017 import download_scalabrino
from dataset_downloaders.tizard_2019 import download_tizard
from dataset_downloaders.williams_2017 import download_williams

dataset_downloaders = {
    "chen_2014": download_chen,
    "ciurumelea_2017": download_ciurumelea,
    "di_sorbo_2016": download_di_sorbo,
    "guzman_2015": download_guzman,
    "maalej_2016": download_maalej,
    "scalabrino_2017": download_scalabrino,
    "tizard_2019": download_tizard,
    "williams_2017": download_williams,
}

relevance_dataset_mappings = {
    "chen_2014": {
        "relevant": ["informative"],
        "irrelevant": ["non-informative"]
    },
    "ciurumelea_2017": {
        "relevant": ["COMPATIBILITY", "PROTECTION", "RESSOURCES"],
        "irrelevant": ["OTHER", "PRICING", "USAGE"]
    },
    "di_sorbo_2016": {
        "relevant": ["[BUG]", "[REQUEST]"],
        "irrelevant": ["[INFO]", "[QUESTION]"]
    },
    "guzman_2015": {
        "relevant": ["Bug report", "Feature shortcoming", "Feature strength", 'User request'],
        "irrelevant": ["Complaint", "Noise", "Praise", "Usage scenario"]
    },
    "maalej_2016": {
        "relevant": ["Bug", "Feature"],
        "irrelevant": ["Rating", "UserExperience"]
    },
    "scalabrino_2017": {
        "relevant": ["BUG", "FEATURE"],
        "irrelevant": ["ENERGY","PERFORMANCE","SECURITY","USABILITY"]
    },
    # FIX THIS AT SOME POINT!! Some labels that are called relevant in the paper are not relevant imo (E.g. dispraise for application)
    "tizard_2019": {
        "relevant": ["acknowledgement of problem resolution", "agreeing with the feature request", "agreeing with the problem", "apparent bug", "application guidance", "application usage", "attempted solution", "dispraise for application", "feature request", "limitation confirmation", "malfunction confirmation", "praise for application", "question on application", "question on background", "user setup"],
        "irrelevant": ["non-informative", "requesting more information", "help seeking"]
    },
    "williams_2017": {
        "relevant": ["bug", "fea"],
        "irrelevant": ["oth"]
    },
}



bfo_dataset_mappings = {
    "di_sorbo_2016": {
        "bug": ["[BUG]"],
        "feature": ["[REQUEST]"],
        "other": ["[INFO]", "[QUESTION]"]
    },
    "guzman_2015": {
        "bug": ["Bug report"],
        "feature": ["Feature shortcoming", 'User request'],
        "other": ["Complaint", "Noise", "Praise", "Usage scenario", "Feature strength"]
    },
    "scalabrino_2017": {
        "bug": ["BUG"],
        "feature": ["FEATURE"],
        "other": ["ENERGY","PERFORMANCE","SECURITY","USABILITY"]
    },
    "maalej_2016": {
        "bug": ["Bug"],
        "feature": ["Feature"],
        "other": ["Rating", "UserExperience"]
    },
    "tizard_2019": {
        "bug": ["apparent bug"],
        "feature": ["feature request"],
        "other": ["acknowledgement of problem resolution", "agreeing with the feature request", "agreeing with the problem", "application guidance", "application usage", "attempted solution", "dispraise for application", "limitation confirmation", "malfunction confirmation", "praise for application", "question on application", "question on background", "user setup", "non-informative", "requesting more information", "help seeking"]
    },
    "williams_2017": {
        "bug": ["bug"],
        "feature": ["fea"],
        "other": ["oth"]
    },
}