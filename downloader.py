from dataset_downloaders.label_mappings import dataset_downloaders, relevance_dataset_mappings, bfo_dataset_mappings
import os
import argparse

def save_data(download_fn, save_path, dataset_mapping):
    df = download_fn()
    
    df = df[df.text.apply(type) == str]
    
    if dataset_mapping is not None:
        # Apply a mapped label if the original label is in the original label mapping
        df.label = df.label.apply(lambda x: [mapped_label for mapped_label, orig_label in dataset_mapping.items() if x in orig_label])
        assert (df.label.str.len() == 1).all(), f"Unmapped data. \n\n{df.label[df.label.str.len() != 1]}"
        df.label = df.label.str[0]
    
    #Collate dataframe to include all labels for a given piece of feedback
    df = df.groupby("text")["label"].apply(list).apply(lambda x: ",".join(x)).reset_index(drop=False)
    
    bins_df = df.label.str.get_dummies(sep=",")
    bins_df["text"] = df["text"].str.replace("\n", ". ").str.replace("\t", "    ")
    
    bins_df = bins_df[sorted(bins_df.columns)]

    bins_df.to_csv(save_path, index=False)

def download_datasets(dataset_list, label_granularity="raw"):
    
    supported_granularities = ["requirements_relevance", "bug_feature_other", "raw"]
    
    assert label_granularity in supported_granularities, f"{label_granularity} not in supported label granularities ({str(supported_granularities)})"
    
    base_save_dir = os.path.join("./data")
    os.makedirs(base_save_dir, exist_ok = True)
    
    if label_granularity == "requirements_relevance":
        dataset_mappings = relevance_dataset_mappings
    elif label_granularity == "bug_feature_other":
        dataset_mappings = bfo_dataset_mappings
    elif label_granularity == "raw":
        dataset_mappings = None
        
    for dataset_name in dataset_list:
        print(f"Downloading {dataset_name}")
        dataset_downloader = dataset_downloaders[dataset_name]
        dataset_mapping = dataset_mappings[dataset_name] if dataset_mappings is not None else None
        dataset_path = os.path.join(base_save_dir, f"{dataset_name}_{label_granularity}.csv")
        save_data(dataset_downloader, dataset_path, dataset_mapping)