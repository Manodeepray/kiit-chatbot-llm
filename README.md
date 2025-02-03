# 📚 KIIT LLM Chatbot with RAG: Multi-File Data Query System

Welcome to the **KIIT LLM Chatbot**, an AI-powered system designed to retrieve and generate relevant information from **PDFs, CSVs, and DOCs** using **Retrieval-Augmented Generation (RAG)**. This project leverages the power of **Streamlit** for the UI, providing an interactive experience for users to query documents with ease.

## 🌟 Features

- **Multi-Source Document Support**: Integrates **PDFs, CSVs, and DOC** files, allowing users to query across multiple file types.
- **Advanced RAG Model**: Combines **retrieval** and **generation** techniques for highly relevant and accurate answers.
- **Streamlit Interface**: Simple, user-friendly UI for easy interaction with the system.
- **Scalable Design**: Built to handle a wide variety of document types and queries.
- **Customizable LLM Options**: Users can choose between **Gemini 1.5 Flash**, **Hugging Face models (via serverless inference endpoint)**, or **Ollama on-device models**.
- **Ensemble Retriever**: Combines **PDF**, **CSV**, and **TXT** retrievers using LangChain's **EnsembleRetriever** with equal weights (0.33 each).
- **History-Aware Retrieval**: Implements LangChain's **create_history_aware_retriever** for context-aware querying.

## 🛠️ Technologies Used

- **Python**: Core language for the system.
- **LangChain**: Framework used for managing retrieval and generation.
- **Streamlit**: Provides the interactive frontend for users.
- **FAISS**: Vector store for efficient document retrieval.
- **Gemini API / Hugging Face Models**: To handle the LLM-based query generation.
- **PyPDF2**, **pandas**, **docx2txt**: Used to parse PDFs, CSVs, and DOC files.

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- Required packages (found in `requirements.txt`)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Manodeepray/kiit-chatbot-llm.git
   cd kiit-chatbot-llm
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your documents in the data folder**:

4. **Create the vectorstores**:

   ```bash
   python vector_db.py
   ```

5. **Run the application**:

   ```bash
   streamlit run app.py
   ```

### File Structure

```
📂 kiit-llm-rag-chatbot/
│
├── 📁 src/
|   |
|   ├──📁 data/
│       ├── example.pdf
│       ├── example.csv
│       └── example.txt
│
├── app.py              # Main Streamlit app
├── main_rag.py         # RAG logic and document processing
├── requirements.txt    # Python package requirements
├── README.md           # Project documentation
└── LICENSE
```

## ⚙️ How It Works

1. **Upload Documents**: Users can upload PDFs, CSVs, and TXT files to the interface.
2. **Query the System**: After the files are processed, users can input their queries.
3. **Retrieval & Generation**:
   - The system uses an **Ensemble Retriever** to fetch information from PDFs, CSVs, and TXT files.
   - Retrieval incorporates **history awareness** for more contextually relevant results.
4. **Response Generation**: The RAG system retrieves relevant information and generates a coherent, human-like response using the selected LLM.
5. **Display Answers**: Answers are displayed interactively within the Streamlit app.

## 📝 Example Query

Once the system is running, upload your documents and enter a query such as:

```
"What are the key highlights from the meeting notes in the uploaded TXT file?"
```

The system will return a detailed response based on the contents of the uploaded TXT file.

## 📈 Future Improvements

- **Multi-Language Support**: Expand capabilities to support document querying in multiple languages.
- **Real-Time Document Updating**: Allow dynamic updates when documents are added or modified.
- **Improved Performance**: Further optimize the RAG pipeline for faster responses.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## 🙌 Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## 📧 Contact

For any inquiries or questions, feel free to reach out at:  
**Manodeep Ray**  
Email: [Manodeep](mailto:manodeepray1@gmail.com)

---

_Happy Querying!_

---
