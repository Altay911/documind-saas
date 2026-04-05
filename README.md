# 🧠 DocuMind SaaS

DocuMind is an AI-powered SaaS platform that allows users to securely upload PDF documents and extract insights by chatting directly with their data. Built with Django and the OpenAI API, it features a complete user authentication system, a document management vault, and a built-in "Freemium" daily limit model to protect API costs.

## ✨ Key Features

* **True RAG Architecture (Retrieval-Augmented Generation):** Replaces basic context-stuffing with a highly efficient LangChain and FAISS Vector Database pipeline. The system chunks massive PDFs, embeds them mathematically, and only retrieves highly relevant paragraphs to drastically reduce API costs and improve AI accuracy.
* **Secure Authentication:** Full login/registration system with password visibility toggles and secure session management.
* **Smart Document Vault:** Users can upload, view, rename, and safely delete PDFs. (Includes a custom file size bouncer).
* **Freemium Business Model:** Custom database tracking limits users to 5 free questions per day to prevent API abuse.
* **Modern UI/UX:** Built with Bootstrap 5 featuring dynamic empty states, responsive grids, and error handling.
* **Production Security:** Hidden `.env` architecture to protect Django secret keys and OpenAI API credentials.

## 🛠️ Tech Stack

* **Backend:** Python, Django, SQLite
* **AI Architecture:** LangChain, FAISS (Vector Store), PyPDF
* **LLM & Embeddings:** OpenAI API (gpt-3.5-turbo & text-embedding-ada-002)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Bootstrap 5, Bootstrap Icons
* **Security:** python-dotenv

## 🚀 Local Setup Instructions

Want to run DocuMind on your own machine? Follow these steps:

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/documind-saas.git](https://github.com/YOUR_USERNAME/documind-saas.git)
   cd documind-saas