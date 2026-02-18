import re
import pandas as pd


def preprocess(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def assign_to_predefined_cluster(description, cluster_dict):
    # words = set(description.split())
    # print(words)
    for cluster_name, keywords in cluster_dict.items():
        for keyword in keywords:
            if keyword in description:
                return cluster_name
        # for word in words:
        #     for keyword in keywords:
        #         if keyword.lower() in word.lower():  # Check if the keyword is a substring of the word
        #             return cluster_name  # Return the cluster name as soon as any match is found
    return 'Other'

