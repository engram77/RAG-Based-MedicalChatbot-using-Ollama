# RAG-Based-MedicalChatbot-using-Ollama

# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/engram77/RAG-Based-MedicalChatbot-using-Ollama.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

If conda asks you to accept Terms of Service, run:

```bash
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

If you face package compatibility issues, run:

```bash
pip install langchain==0.3.25 langchain-core==0.3.59 langchain-community==0.3.24 langchain-pinecone==0.2.8 langchain-ollama==0.3.2 python-dotenv flask
```

### STEP 03- Install Ollama and pull the model

Install Ollama on your laptop, then run:

```bash
ollama pull llama3.2
```

You can verify Ollama is working by running:

```bash
ollama run llama3.2
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Add your medical PDF file in the data folder

Example:

```bash
data/Medical_book.pdf
```

```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up localhost:
http://127.0.0.1:8080
```

### Techstack Used:

* Python
* LangChain
* Flask
* Pinecone
* Ollama
* HuggingFace Embeddings

# Notes

## 1. This project uses Ollama locally

So, no OpenAI API key is required in this version.

## 2. Pinecone is still required

This project uses Pinecone as the vector database for storing and retrieving document embeddings.

## 3. Make sure Ollama is installed and running

If Ollama is not installed or the model is not pulled, the chatbot will not generate responses.

## 4. Do not upload your `.env` file

Keep your Pinecone API key private.

## 5. If you face dependency issues

Use the compatible versions mentioned above.

# Common Errors and Fixes

## 1. `conda not recognized`

Install Miniconda or Anaconda and reopen the terminal.

## 2. `.env` not working

Make sure the file is named exactly `.env` and not `.env.txt`.

## 3. `ModuleNotFoundError`

Reinstall dependencies using the working package versions.

## 4. Ollama not responding

Run:

```bash
ollama pull llama3.2
```

## 5. Pinecone errors

Check:

* API key is correct
* index exists
* `store_index.py` ran successfully

# Disclaimer

This chatbot is for educational and demo purposes only.

It should not replace professional medical advice, diagnosis, or treatment.

Kindly consult a Doctor for medical decisions.



