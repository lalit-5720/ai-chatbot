# Local Streamlit AI Chatbot

A Python + Streamlit chatbot that uses a local language model through Ollama. No OpenAI API key or OpenAI API credits are needed.

## 1. Install Ollama
Download and install Ollama for Windows: https://ollama.com/download/windows

## 2. Download and run a model
Open PowerShell or Command Prompt and run:

```powershell
ollama run llama3.2
```

The first run downloads the model and may take some time. Wait until the model prompt appears. You can test it there, then enter `/bye` to exit the model chat. Ollama should remain running in the background.

## 3. Set up the Streamlit app
Open a second terminal in this project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`, then install the requirements and start Streamlit.

Open the local URL shown, usually http://localhost:8501.

## Troubleshooting
- **Cannot connect:** Start Ollama from the Start menu or run `ollama run llama3.2`.
- **Model not found:** Run `ollama run llama3.2` once to download it.
- **Slow response:** Speed depends on your computer's RAM/CPU/GPU.
- **No OpenAI API key is needed.**

This local setup is for your own computer. It will not automatically work on a public Streamlit host because that host cannot access Ollama running on your PC.
