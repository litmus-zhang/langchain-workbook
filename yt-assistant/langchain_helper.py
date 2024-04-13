from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import openai
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.vectorstores import faiss
from langchain.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()


embeddings = OpenAIEmbeddings()

def create_vector_store(video_url: str) -> faiss.FAISS:
    loader = YoutubeLoader.from _youtube_url(video_url)
    