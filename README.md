# 🌍 AI-Powered Travel Assistant Agent (RAG-Enabled)

An intelligent conversational travel agent built on **Google Cloud Platform (GCP)** using **Vertex AI Agent Builder** and **Retrieval-Augmented Generation (RAG)** to provide grounded, context-aware travel recommendations.

---

## 🚀 Project Overview
Standard Large Language Models (LLMs) often rely solely on pre-trained memory and can hallucinate facts about fictional or niche locations. This project solves that limitation by implementing a **RAG architecture**. 

The agent connects directly to a custom unstructured data store containing domain-specific documents (e.g., custom travel itineraries and destination guidelines), ensuring all suggestions are accurate, grounded, and contextually relevant.

---

## 🛠️ Tech Stack & Architecture
* **Cloud Platform:** Google Cloud Platform (GCP)
* **Core Service:** Vertex AI Agent Builder / Dialogflow CX
* **AI Model:** Gemini 3.5 Flash / Gemini Pro
* **Data Grounding:** Vertex AI Search & Conversation (Unstructured Data Store)
* **Security & Operations:** Google Cloud IAM (Identity and Access Management), Agent Runtime Deployment

---

## ⚙️ Key Features & Implementation
1. **Custom Data Grounding:** Configured a Vertex AI Search data store to ingest custom text files (such as destination guidelines and itineraries), preventing generic LLM hallucinations.
2. **Agentic Behavior & Instructions:** Designed custom system instructions and persona parameters to control tone, greetings, and multi-turn conversational flow.
3. **Advanced Testing & Validation:** Tested the agent using real-world edge cases (e.g., querying fictional locations like Wakanda) to verify successful retrieval from the custom data store.
4. **Cloud Deployment:** Deployed the agent to an Agent Runtime instance with proper IAM role configurations (`Service Usage Viewer`) for verification and secure operations.

---

## 💡 What I Learned
* Building production-ready conversational agents using Google Cloud's modern Agent Builder console.
* Implementing Retrieval-Augmented Generation (RAG) to anchor AI responses in private/custom data stores.
* Managing Google Cloud project resources, runtime instances, and IAM security permissions.
