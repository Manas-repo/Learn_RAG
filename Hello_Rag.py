import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Load api key from environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Load the document
loader = TextLoader('zelthar.txt')
docs = loader.load()

print(f"Number of documents loaded: {len(docs)}")
print(f"First document content:\n{docs[0].page_content[:500]}...")  # Print first 500 characters