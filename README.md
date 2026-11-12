# Groq API Call (Python)

A small Python example of calling a hosted language model through the [Groq API](https://console.groq.com/). It uses the [Groq Python SDK](https://github.com/groq/groq-python) with `llama-3.1-8b-instant`.

**Note:** Groq (the API provider used here) is different from Grok (the xAI assistant).

## Prerequisites

- Python 3.10 or later
- A Groq API key from the [Groq Console](https://console.groq.com/keys)

## Install

Clone this repository, then create and activate a virtual environment:

```bash
git clone https://github.com/kakarot987/grok-api-call.git
cd grok-api-call
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configure the API key

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
# Windows PowerShell: Copy-Item .env.example .env
```

Edit `.env` and set `GROQ_API_KEY` to your actual API key. The `.env` file is ignored by Git; **never commit an actual API key**. You can also set the environment variable directly in your shell.

## Run

```bash
python main.py
```

The script sends one prompt and prints the model's response. A key and network connection are required. Model availability and usage limits are controlled by Groq and may change.

For an interactive example, open `groq_jupyter.ipynb` in Jupyter using the same Python environment and API key.

## Test

Unit tests use the standard-library `unittest` framework and **mock the Groq client**; no live API requests or API keys are required.

```bash
python -m unittest discover -s tests -v
```

GitHub Actions also runs these tests on pull requests and pushes to `main`.

## Project files

- `main.py` — minimal Groq API example
- `groq_jupyter.ipynb` — notebook example
- `requirements.txt` — Python dependencies
- `.env.example` — API key configuration template
- `tests/` — offline unit tests
