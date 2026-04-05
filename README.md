# 🧠 DocuMind: Enterprise-Grade AI PDF SaaS

**[🚀 View Live Production Demo](http://44.200.194.133)**

DocuMind is a full-stack AI platform that transforms static PDFs into interactive conversation partners. By leveraging **Retrieval-Augmented Generation (RAG)**, the system allows users to "chat" with massive documents in real-time while maintaining 100% data context and minimizing LLM costs.

-----

## 🏗️ System Architecture & Infrastructure

This project is built for scale, using a professional-grade DevOps stack to ensure high availability and security.

  * **Cloud Hosting:** Deployed on **Amazon EC2 (Ubuntu 24.04 LTS)**.
  * **Containerization:** Fully orchestrated with **Docker & Docker Compose** to ensure parity between local and production environments.
  * **Web Server:** **Nginx** acting as a high-performance reverse proxy.
  * **Application Server:** **Gunicorn** handling concurrent Python workers.
  * **CI/CD Pipeline:** Automated deployment via **GitHub Actions** for seamless, zero-downtime updates.

-----

## ✨ Core Features

### 🤖 True RAG Pipeline

Unlike basic "context-stuffing," DocuMind uses a sophisticated **LangChain** and **FAISS** pipeline. It chunks documents, converts them into high-dimensional vectors, and retrieves only the most relevant text fragments for the OpenAI API—drastically reducing token usage.

### 🔐 Secure User Vault

A comprehensive authentication system allowing users to manage their personal document library. Includes secure uploads, file renaming, and a custom "file bouncer" to prevent oversized uploads.

### 💳 "Freemium" Business Logic

A built-in database tracker enforces a **Daily Query Limit** (5 questions per 24 hours), demonstrating how the app can be scaled into a profitable business model.

### 📱 Responsive UI/UX

A modern, light-themed interface built with **Bootstrap 5**, featuring dynamic loading states, real-time chat bubbles, and mobile-responsive document management.

-----

## 🛠️ Tech Stack

  * **Backend:** Python, Django, SQLite
  * **AI Architecture:** LangChain, FAISS (Vector Store), PyPDF
  * **LLM & Embeddings:** OpenAI API (gpt-3.5-turbo & text-embedding-ada-002)
  * **Infrastructure:** Docker, Nginx, AWS
  * **Frontend:** HTML5, CSS3, Vanilla JavaScript, Bootstrap 5

-----

## 🚀 Quick Start (Local Development)

To run this project locally, you must have Docker installed.

1.  **Clone the Repo**
    ```bash
    git clone https://github.com/Altay911/documind-saas.git
    cd documind-saas
    ```
2.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```env
    SECRET_KEY=your_secret_key
    OPENAI_API_KEY=your_openai_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```
3.  **Launch**
    ```bash
    docker compose up --build
    ```

-----

🗺️ Product Roadmap & Upcoming Features
DocuMind is evolving from a technical demo into a production-ready SaaS. The following features are currently in development:

☁️ Persistent Cloud Storage (AWS S3): Transitioning from local Docker volumes to Amazon S3 for indestructible, encrypted PDF storage.

💳 Subscription Tiers (Stripe Integration): Implementing a multi-tier billing system to allow users to upgrade for unlimited daily queries and larger file uploads.

📂 Multi-File Support: Adding the ability to chat with multiple documents simultaneously, allowing the AI to draw connections across an entire project library.

📊 Usage Analytics Dashboard: A private admin view to track API costs, popular query topics, and user growth.

🔒 Enhanced Privacy: Adding "Self-Destruct" modes for sensitive documents where data is wiped from the Vector DB immediately after the session ends.