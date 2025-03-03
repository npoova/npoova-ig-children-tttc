import os
#追加
from langchain_openai import AzureOpenAIEmbeddings
#追加終わり
import pandas as pd
from tqdm import tqdm


def embedding(config):
    dataset = config['output_dir']
    path = f"outputs/{dataset}/embeddings.pkl"
    arguments = pd.read_csv(f"outputs/{dataset}/args.csv")
    embeddings = []
    for i in tqdm(range(0, len(arguments), 1000)):
        args = arguments["argument"].tolist()[i: i + 1000]
        # embeds = OpenAIEmbeddings().embed_documents(args)
        #追加
        embeds = AzureOpenAIEmbeddings(
        model="text-embedding-3-large",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), 
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION_EMBEDDING")
        ).embed_documents(args)
        #追加終わり
        embeddings.extend(embeds)
    df = pd.DataFrame(
        [
            {"arg-id": arguments.iloc[i]["arg-id"], "embedding": e}
            for i, e in enumerate(embeddings)
        ]
    )
    df.to_pickle(path)
