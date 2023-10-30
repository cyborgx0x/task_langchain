from langchain.document_loaders import WebBaseLoader


def retriever(url):
    loader = WebBaseLoader(url)
    return loader.load()
