# PDFAssist 📃✍⚡

PDFAssist is an innovative tool designed to empower users from all walks of life—researchers, students, and everyday individuals—by providing them with a seamless way to interact with their PDF documents. Whether you're conducting in-depth research, studying for exams, or simply need quick access to information within a PDF, PDFAssist offers an intuitive platform where you can ask questions about the content and receive accurate, context-aware answers. By leveraging advanced technology, PDFAssist transforms static documents into dynamic, interactive resources, making it easier than ever to extract valuable insights from your PDFs.

![PDFAssist](https://github.com/harshd23/PDFAssist/blob/main/pdfassist.png)

## Technologies Used:-

- Langchain + LLM(Google Gemini Pro)
- Streamlit: UI
- Text Embeddings: Google Text Embeddings
- FAISS: Vector database

## Features:-

- Users can ask questions about the content within their PDFs and receive accurate, context-aware answers.
- Designed for all users, from researchers to students to the general public, making it easy to navigate and extract information.
- Ideal for various needs, including academic research, study assistance, and everyday information retrieval.

## Project Structure:-

- app.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
- index.pkl: A pickle file to store the FAISS index.
- .env: Configuration file for storing your Google API key.

## Steps to run the project:-

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/harshd23/PDFAssist.git
```

2.Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```

3.Set up your Google API key by creating a .env file in the project root and adding your API

```bash
  GOOGLE_API_KEY = "put_your_google_api_key_here"
```

## Usage of the project:-

1.Run the Streamlit app by executing:

```bash
streamlit run app.py
```

2.The web app will open in your browser:

- On the left of the screen, you can upload your multiple PDFs directly.
- Initiate the data loading and processing by clicking "Submit & Process"
- Observe the system as it performs text splitting, generates embedding vectors, and efficiently indexes them using FAISS.
- The embeddings will be stored and indexed using FAISS, enhancing retrieval speed.
- The FAISS index will be saved in a local file path in pickle format for future use.
- One can now ask a question and get the answer from your own PDFs.
