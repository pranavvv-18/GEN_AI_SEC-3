# GENERATIVE AI LAB – WEEK 6

**Experiment:** Golden Question Set Evaluation & Baseline Run — Release v0.1  
**Name:** V.Pranav  
**Roll Number:** 2520030207  
**Date:** 21/11/2026  
**Tool used:** Visual Studio Code  

---

### 1. Aim
To develop an automated LLM evaluation pipeline that tests a local language model (Llama 3.2 via Ollama) against a curated 30-question golden question set covering core Generative AI concepts, computes keyword-based coverage scores, evaluates response quality against threshold criteria (PASS ≥ 60% vs. REVIEW), automatically exports structured evaluation records to `baseline_results.csv`, and establishes the official benchmark as Release v0.1.

---

### 2. Software Used
Windows 11, Python 3.14, Visual Studio Code, Windows PowerShell / Terminal, Ollama runtime (v0.40.16), Llama 3.2 (3B parameter) local open-source LLM, and the Python `requests` library.

---

### 3. Procedure
1. Open PowerShell and verify the installed Ollama runtime version using `ollama --version`.
2. Check the local model repository and download/pull Llama 3.2 using `ollama pull llama3.2`.
3. Open Visual Studio Code and create the project directory structure under `PRACTICAL/WEEK-6`.
4. Create the required configuration and code files: `golden_set.json`, `requirements.txt`, and `main.py`.
5. Populate `golden_set.json` with 30 curated technical benchmark questions, each containing an identifier (`id`), question prompt (`question`), authoritative reference answer (`expected_answer`), key evaluation tokens (`keywords`), and source citation URL (`source`).
6. Specify dependencies in `requirements.txt` (`requests`) and install them using `pip install -r requirements.txt`.
7. Implement the evaluation engine in `main.py`:
   - Connect to Ollama's HTTP REST API endpoint (`http://localhost:11434/api/generate`).
   - Query the model deterministically with greedy decoding (`temperature: 0`) and non-streaming responses (`stream: False`).
   - Implement keyword-matching logic that converts text to lowercase and measures the presence of expected keywords.
   - Calculate keyword coverage score percentage:  
     $$\text{Score} = \left(\frac{\text{matched keywords}}{\text{total keywords}}\right) \times 100$$
   - Classify each question as `PASS` (score $\ge 60\%$) or `REVIEW` (score $< 60\%$).
   - Log detailed per-question output to the console.
   - Export all test records to a structured CSV file (`baseline_results.csv`).
   - Generate summary statistics for Release v0.1 (total questions, passed count, review count, average keyword coverage).
8. Run the program using `python main.py`, verify the generated `baseline_results.csv` output, and review the Release v0.1 baseline report.

---

### 4. Commands and Files

```powershell
# Step 1: Verify Ollama version
ollama --version

# Step 2: Pull local Llama 3.2 model
ollama pull llama3.2

# Step 3: Navigate to project directory
cd c:\Users\vaaka\OneDrive\Desktop\GEN-AI\PRACTICAL\WEEK-6

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Execute baseline evaluation run
python main.py
```

**Files in Project:**
- `golden_set.json`: Benchmark dataset with 30 questions, expected answers, keywords, and sources.
- `requirements.txt`: Python package dependencies (`requests`).
- `main.py`: Complete evaluation pipeline, scoring algorithm, and CSV generator.
- `baseline_results.csv`: Generated baseline results report for Release v0.1.

---

### 5. Program Logic

```
Load golden_set.json (30 questions)
  │
  ▼
Iterate through each question
  │
  ├──> Send HTTP POST to Ollama API (http://localhost:11434/api/generate)
  │    Parameters: model="llama3.2", temperature=0, stream=False
  │
  ├──> Receive generated LLM response text
  │
  ├──> Case-insensitive keyword matching against expected keywords list
  │
  ├──> Compute keyword coverage score: (len(matched) / len(expected)) * 100
  │
  ├──> Classify Status: PASS if score >= 60 else REVIEW
  │
  └──> Append record to results list
  │
  ▼
Export all evaluation records to baseline_results.csv
  │
  ▼
Compute and display Summary:
- Release Version: v0.1
- Total Questions, Passed Count, Review Count, Error Count
- Average Keyword Coverage Percentage
```

---

### 6. Result

The Python-based golden question set evaluation pipeline was created and executed successfully against the local Llama 3.2 model via Ollama. All 30 benchmark questions covering foundational Generative AI concepts—including tokenization algorithms (BPE, WordPiece, SentencePiece), token economics, context windows, autoregressive decoding, sampling parameters (temperature, top-k, top-p), token embeddings, and Transformer positional encodings (Sinusoidal, RoPE)—were evaluated. The baseline keyword coverage scores and classification results were recorded, exported to `baseline_results.csv`, and officially released as Release v0.1.

---

## SCREENSHOTS OF MY WORK – WEEK 6

### Screenshot: Golden Set Evaluation Code and Setup
*VS Code workspace displaying `PRACTICAL/WEEK-6` structure, `golden_set.json`, and `main.py` implementation.*

```text
+-- WEEK-6/
|   +-- golden_set.json       # 30 Curated benchmark questions & verification keywords
|   +-- main.py               # Evaluation engine & keyword scoring pipeline
|   +-- requirements.txt      # Project dependencies (requests)
|   +-- baseline_results.csv  # Generated Release v0.1 evaluation output
```

### Screenshot: Baseline Run Execution and Output
*Terminal output showing question-by-question evaluation, keyword matching, and summary statistics.*

```text
======================================
GOLDEN QUESTION SET
======================================
Total Questions: 30
Model: llama3.2

======================================
BASELINE RUN STARTED
======================================
--------------------------------------
Question 1: Q001
Question: What is tokenization in large language models?

LLM Answer:
Tokenization is the process of splitting input text into smaller units called tokens...

Expected Answer:
Tokenization is the process of splitting input text into smaller units called tokens.

Matched Keywords: ['splitting', 'text', 'tokens']
Missing Keywords: []
Score: 100.0 %
Status: PASS
...
======================================
BASELINE EVALUATION SUMMARY
======================================
Release Version: v0.1
Model: llama3.2
Total Questions: 30
Successful Responses: 30
...
Results saved to: baseline_results.csv

BASELINE RUN COMPLETED!
Release v0.1 created successfully.
```
