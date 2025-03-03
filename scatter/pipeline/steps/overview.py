"""Create summaries for the clusters."""
# 追加
import dotenv
dotenv.load_dotenv()
# 追加終わり
from tqdm import tqdm
import os
from typing import List
import numpy as np
import pandas as pd
from langchain_openai import AzureChatOpenAI
from utils import messages, update_progress


def overview(config):
    dataset = config['output_dir']
    path = f"outputs/{dataset}/overview.txt"

    takeaways = pd.read_csv(f"outputs/{dataset}/takeaways.csv")
    labels = pd.read_csv(f"outputs/{dataset}/labels.csv")

    prompt = config['overview']['prompt']
    model = config['overview']['model']

    ids = labels['cluster-id'].to_list()
    takeaways.set_index('cluster-id', inplace=True)
    labels.set_index('cluster-id', inplace=True)

    input = ''
    for i, id in enumerate(ids):
        input += f"# Cluster {i}/{len(ids)}: {labels.loc[id]['label']}\n\n"
        input += takeaways.loc[id]['takeaways'] + '\n\n'

    #    llm = ChatOpenAI(model_name=model, temperature=0.0)
    #追加
    llm = AzureChatOpenAI(
    model_name=model, 
    temperature=0.0,
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"))
    #追加終わり
    response = llm(messages=messages(prompt, input)).content.strip()

    with open(path, 'w') as file:
        file.write(response)
