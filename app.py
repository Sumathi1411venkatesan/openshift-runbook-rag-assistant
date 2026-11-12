import ollama
import streamlit as st
from qdrant_client import QdrantClient

COLLECTION = "openshift_runbooks"
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2:latest"

client = QdrantClient(url="http://localhost:6333")

st.set_page_config(page_title="OpenShift Runbook Assistant")
st.title("OpenShift Runbook Assistant")
st.caption("Ask about an OpenShift issue. Answers come from your runbooks.")

question = st.chat_input("e.g. My pod is in CrashLoopBackOff, what should I check?")

if question:
    st.chat_message("user").write(question)

    vec = ollama.embed(model=EMBED_MODEL, input=question)["embeddings"][0]
    hits = client.query_points(COLLECTION, query=vec, limit=3).points
    context = "\n\n".join(f"[{h.payload['source']}]\n{h.payload['text']}" for h in hits)

    system = ("You are an OpenShift support assistant. Answer ONLY from the context. "
              "Give clear numbered steps with oc commands. "
              "If the answer is not in the context, say you don't know.")
    user = f"Context:\n{context}\n\nQuestion: {question}"

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            resp = ollama.chat(model=LLM_MODEL, messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user}])
        st.write(resp["message"]["content"])
        sources = sorted({h.payload["source"] for h in hits})
        st.caption("Sources: " + ", ".join(sources))