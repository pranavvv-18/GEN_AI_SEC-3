# Week 1 Lab: First LLM API Call

## Prerequisites
1. **Python 3.14+** installed.
2. Virtual environment configured (`.venv`).
3. An API key from either:
   - **OpenAI Platform** (`OPENAI_API_KEY`)
   - **Google AI Studio / Gemini Platform** (`GEMINI_API_KEY`)

## Quick Start

### 1. Activate Environment
In PowerShell from `week1-llm-call`:
```powershell
.\.venv\Scripts\Activate.ps1
```
or if using parent environment:
```powershell
..\.venv\Scripts\Activate.ps1
```

### 2. Configure `.env`
Open `.env` and paste your API key:
```env
OPENAI_API_KEY=your_actual_key_here
# or
GEMINI_API_KEY=your_actual_key_here
```

### 3. Run the script
```powershell
python main.py
```

