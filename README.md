\# OpenShift Runbook RAG Assistant



An AI assistant that answers OpenShift troubleshooting questions from runbooks, with sources. Runs fully local: no data leaves the machine.



\## Architecture



```mermaid

flowchart LR

&#x20;   A\[Runbooks: md / pdf] --> B\[ingest.py: chunk + embed]

&#x20;   B -->|nomic-embed-text via Ollama| C\[(Qdrant vector DB)]

&#x20;   U\[User question] --> D\[Streamlit app]

&#x20;   D -->|embed question| C

&#x20;   C -->|top 3 chunks| D

&#x20;   D -->|context + question| E\[Llama 3.2 3B via Ollama]

&#x20;   E -->|answer + sources| D

```



\## Tech stack



\- Python, Streamlit

\- Qdrant (vector database)

\- Ollama: llama3.2 (3B) for answers, nomic-embed-text for embeddings

\- Docker



\## How to run



```

docker run -d -p 6333:6333 qdrant/qdrant

docker run -d -p 11434:11434 --name ollama ollama/ollama

docker exec ollama ollama pull nomic-embed-text

docker exec ollama ollama pull llama3.2:3b

pip install -r requirements.txt

python ingest.py

streamlit run app.py

```



\## Example



Q: My pod keeps restarting, what should I check?

A: Steps from the CrashLoopBackOff runbook, with sources listed.



\## Lessons learned



\- Small 3B models can hallucinate commands not in the runbook. Strict prompts and evaluation are needed.



\## Next steps



\- Evaluation set of 20 questions with accuracy score

\- Stricter grounding prompt

\- Deploy on OpenShift with vLLM / KServe (Project 2)

