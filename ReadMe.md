# IAM AI Agent

# Overview

The IAM AI Agent is an AI-driven Identity and Access Management system that combines:

- RAG-based policy retrieval
- Multi-turn memory
- Adaptive behavior
- Security anomaly detection
- Tool orchestration
- Runtime logging and tracing
- Docker deployment support

The system supports the following personas:

- End User
- IAM Decision Agent
- IAM Security Agent

---

# Features

- Access request evaluation
- Security anomaly detection
- Context-aware multi-turn conversations
- Short-term and long-term memory
- Adaptive behavior using feedback
- Tool execution workflows
- Logging and tracing
- Runtime failure handling
- Dockerized deployment
- Streamlit UI support

---

# Project Structure

```text
IAMAgent/
│
├── agent/
│   ├── rag_agent.py
│   ├── memory.py
│   ├── feedback.py
│
├── rag/
│   ├── retriever.py
│   ├── build_index.py
│   └── faiss_index/
│
├── data/
│   └── feedback.json  
|   └── memory_store.json
│   └── policies.json
|
├── logs/
│   └── agent.log
│
├── ui/
│   └── app.py
│
├── docs/
│   ├── ProblemStatement.md
│   ├── Evaluation And Engineering Review.md
│   ├── DemoScript.md
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env.example
└── README.md
```

---

# Prerequisites

Ensure the following are installed:

| Requirement | Version |
|---|---|
| Python | 3.11+ |
| Docker | Latest |
| Git | Latest |

---

# Environment Configuration

Create a `.env` file in the project root.

Example:

```text
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=https://api.openai.com/v1
```

Important:

- Do NOT include quotes
- Do NOT commit `.env` to GitHub

---

# Installation

## Create Virtual Environment

### Windows

```bash
python -m venv IAMAgent
IAMAgent\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Agent from Terminal

## Start Terminal-Based IAM Agent

From the project root directory:

```bash
python agent/rag_agent.py
```

---

## Example Interaction

```text
IAM RAG Agent (type 'exit' to quit)

Enter request: QA need write access to production DB
```

---

## Example Response

```json
{
  "decision": "escalate",
  "risk": "high",
  "tool": "request_approval"
}
```

---

# Running the Streamlit UI

## Start Streamlit Application

```bash
streamlit run ui/app.py
```

---

## Access UI

Open browser:

```text
http://localhost:8501
```

---

# Docker Deployment

# Build Docker Image

```bash
docker build --no-cache -t iam-agent .
```

---

# Run Docker Container

```bash
docker run --env-file .env -p 8501:8501 iam-agent
```

---

# Access Streamlit UI in Docker

Open browser:

```text
http://localhost:8501
```

---

# Docker Port Mapping

| Host Port | Container Port | Purpose |
|---|---|---|
| 8501 | 8501 | Streamlit UI |

---

# Dockerfile Overview

The Docker container performs the following:

- Copies project files
- Installs dependencies
- Configures runtime environment
- Exposes Streamlit port
- Starts Streamlit automatically

---

# Logging

Logs are stored in:

```text
logs/agent.log
```

Example log:

```text
INFO | Decision: approve | Risk: low | Latency: 6.2s
```

Security violation example:

```text
ERROR | SECURITY VIOLATION DETECTED
```

---

# Supported Capabilities

| Capability | Supported |
|---|---|
| Access request evaluation | ✔ |
| Anomaly detection | ✔ |
| Adaptive behavior | ✔ |
| Memory retention | ✔ |
| Security escalation | ✔ |
| Docker deployment | ✔ |
| Logging and tracing | ✔ |

---

# Memory Features

The IAM agent supports:

- Short-term memory
- Long-term memory
- Context-aware reasoning
- Multi-turn conversations
- Explicit memory reset

Reset memory using:

```text
reset
```

---

# Adaptive Behavior

Feedback can be stored using:

```text
feedback: qa write access test_db should be approved
```

The agent uses stored feedback to adapt future decisions.

---

# Documentation

| Document | Description |
|---|---|
| Phase 6 | Planning, Memory & Context |
| Phase 7 | Adaptive Behavior |
| Phase 8 | Deployment Readiness |
| Phase 9 | Evaluation & Engineering Review |
| Demo Script | Forced interaction walkthrough |

---

# Deployment Assumptions

The deployment assumes:

- Internet connectivity exists
- OpenAI API access is available
- FAISS index is already generated
- Docker runtime is installed

---

# Known Limitations

| Limitation | Description |
|---|---|
| Local deployment only | No cloud orchestration |
| Single-user memory | No session isolation |
| Rule-based adaptation | No autonomous learning |
| Local JSON persistence | Limited scalability |

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core implementation |
| LangChain | LLM orchestration |
| OpenAI | LLM + embeddings |
| FAISS | Vector retrieval |
| Streamlit | UI |
| Docker | Containerization |

---

# Final Outcome

The IAM AI Agent demonstrates:

- AI-driven IAM reasoning
- Multi-turn contextual interaction
- Adaptive behavior
- Security-focused escalation
- Deployment readiness
- Runtime observability

The system combines RAG, memory, security workflows, and deployment engineering into a production-oriented IAM solution.
