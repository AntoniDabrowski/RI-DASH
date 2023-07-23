"""
    The following code is under CC-BY-NC-SA 4.0 license (more in root/LICENSE.txt)
            Free to use and redistribute for any non-commercial purpose
"""

import os
import openai
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from tqdm import tqdm

from utils.pages.genomic_analysis.myVectorstoreIndexCreator import VectorstoreIndexCreator


load_dotenv('.env')

if not os.environ.get('OPENAI_API_KEY'):
    raise ValueError("You have to provide valid OpenAI API key in '.env' file in the root of the repository.")
openai.api_key = os.environ['OPENAI_API_KEY']

persist_directory = 'database'


def initialize_database(document_paths: list[str]):
    assert document_paths, ValueError("You have to provide at least one document path.")

    documents = []
    for path in tqdm(document_paths):
        loader = TextLoader(path, encoding='UTF-8')
        documents.extend(loader.load())
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, length_function=len,
                                          separator=" ")
    docs = text_splitter.split_documents(documents)

    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=persist_directory)
    vectordb.persist()


def extend_database(document_paths: list[str]):
    assert document_paths, ValueError("You have to provide at least one document path.")
    raise NotImplementedError("This function is not implemented yet.")


def answer_question(query: str, context: str, db: Chroma):
    db.similarity_search(query, filter={'source': context})


def initialize_databases(document_paths: list[str]):
    assert document_paths, ValueError("You have to provide at least one document path.")

    for path in tqdm(document_paths):
        current_directory = os.path.join(persist_directory, path.split('/')[-1].split('.')[0])

        loader = TextLoader(path, encoding='UTF-8')
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, length_function=len,
                                              separator=" ")
        docs = text_splitter.split_documents(documents)

        embedding = OpenAIEmbeddings()
        vectordb = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=current_directory)
        vectordb.persist()


def context_chatbot(context: str):
    current_directory = os.path.join(persist_directory, context.split('/')[-1].split('.')[0])
    return VectorstoreIndexCreator().from_persistent_index(path=current_directory)


if __name__ == "__main__":
    all_files = ['./../../../publications/TXTs/' + f'{i}.txt'.zfill(10) for i in range(25)]
    initialize_databases(all_files)