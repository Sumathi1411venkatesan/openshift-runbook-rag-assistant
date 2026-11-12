import os, glob, uuid
import ollama
from pypdf import PdfReader
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

COLLECTION = "openshift_runbooks"
EMBED_MODEL = "nomic-embed-text"

def read_file(path):
    if path.endswith(".pdf"):
        return "\n".join(p.extract_text() or "" for p in PdfReader(path).pages)
    with open(path, encoding="utf-8") as f:
        return f.read()

def chunk(text, size=800, overlap=100):
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks

client = QdrantClient(url="http://localhost:6333")
if client.collection_exists(COLLECTION):
    client.delete_collection(COLLECTION)
client.create_collection(COLLECTION, vectors_config=VectorParams(size=768, distance=Distance.COSINE))

points = []
for path in glob.glob("docs/*"):
    for i, c in enumerate(chunk(read_file(path))):
        vec = ollama.embed(model=EMBED_MODEL, input=c)["embeddings"][0]
        points.append(PointStruct(id=str(uuid.uuid4()), vector=vec,
                                  payload={"text": c, "source": os.path.basename(path), "chunk": i}))
        print(f"Embedded {os.path.basename(path)} chunk {i}")

client.upsert(COLLECTION, points=points)
print(f"Done. {len(points)} chunks stored in '{COLLECTION}'.")