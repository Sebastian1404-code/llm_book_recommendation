# Book Recommendation Chatbot

This project is an AI-powered chatbot that recommends books based on user queries about themes, genres, or keywords. It uses OpenAI for embeddings and language generation, stores book summaries in a Chroma vector database, and provides a conversational interface via Gradio.

---

## Features

- Semantic search over book summaries using vector embeddings
- Conversational book recommendations powered by OpenAI GPT
- Easy-to-use web interface (Gradio)
- Modular and extensible codebase

---

## Requirements

- Python 3.8+
- OpenAI API key
- The following Python packages:
  - pandas
  - chromadb
  - langchain
  - openai
  - gradio
  - python-dotenv

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sebastian1404-code/llm_book_recommendation.git
   cd llm_book_recommendation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your environment variables:**
   - Create a `.env` file in the project root with:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     GROQ_API_KEY=your_groq_api_key_here  # (optional)
     ```

4. **Add your book summaries:**
   - Place your `book_summaries.xlsx` file in the project directory.
   - Ensure it has columns: `title` and `resume`.

---

## Running the App

You can launch the chatbot using the notebook or as a script:

### Option 1: Run from Jupyter Notebook

1. Open `assignment.ipynb` in VS Code or Jupyter.
2. Run all cells.

### Option 2: Run as a Python Script

If you convert the notebook to a script (e.g., `assignment.py`), run:
```bash
python assignment.py
```

---

## Usage

- Open the Gradio web interface (the link will appear in your terminal).
- Enter a query such as:
  - "I want a story about friendship and adventure"
  - "Suggest a mystery novel"
  - "Looking for a book about overcoming adversity"
- The chatbot will recommend a book and provide a summary.

---
