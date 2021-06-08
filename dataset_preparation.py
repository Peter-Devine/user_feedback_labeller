import torch
import os
from transformers import AutoTokenizer
import pandas as pd

class FeedbackDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

def get_splits(dataset_name, training_type):
    df = pd.read_csv(os.path.join("./data", f"{dataset_name}_{training_type}.csv"))
    df = df.dropna()
    
    train_val_df = df.sample(frac=0.7)
    train_df = train_val_df.sample(frac=0.7)
    val_df = train_val_df.drop(train_df.index)
    test_df = df.drop(train_val_df.index)
    
    return train_df, val_df, test_df

def get_dataset(df, tokenizer):
    tokenized_text = tokenizer(text = df.text.tolist(), padding=True, truncation=True, max_length=256, return_tensors="np")
    binary_labels = df.drop("text", axis=1).values
    return FeedbackDataset(tokenized_text, binary_labels)
    

def prepare_datasets(dataset_list, training_type, model_name):
    train_data = []
    val_data = []
    test_data = []
    
    for dataset_name in dataset_list:
        tr, va, te = get_splits(dataset_name, training_type)
        train_data.append(tr)
        val_data.append(va)
        test_data.append(te)
        
    train_df = pd.concat(train_data)
    val_df = pd.concat(val_data)
    test_df = pd.concat(test_data)
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    train_dataset = get_dataset(train_df, tokenizer)
    val_dataset = get_dataset(val_df, tokenizer)
    test_dataset = get_dataset(test_df, tokenizer)
    
    return train_dataset, val_dataset, test_dataset, train_df.columns