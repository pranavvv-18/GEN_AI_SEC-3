# PRACTICAL LAB – Experiment 6: Golden Question Set Evaluation
## Automated LLM Benchmarking and First Baseline Run — Release v0.1

---

## 1. Problem Statement
When deploying Large Language Models (LLMs) into production applications, developers need a repeatable, deterministic method to verify that the model correctly understands domain concepts and provides factual answers. Without an empirical evaluation harness, prompts and model versions cannot be reliably compared. This practical lab implements an automated benchmarking pipeline using a curated **Golden Question Set** (30 technical questions on tokenization, token economics, decoding algorithms, embeddings, and Transformer architectures). The pipeline queries a local open-source model (**Llama 3.2** via **Ollama**) with zero temperature, calculates keyword coverage scores, classifies answers as `PASS` (≥ 60%) or `REVIEW`, exports a structured evaluation dataset to `baseline_results.csv`, and publishes the benchmark as **Release v0.1**.

---

## 2. Learning Objectives
- Design and structure a domain-specific **Golden Question Set** (`golden_set.json`) containing prompt questions, expected ground-truth answers, verification keywords, and authoritative documentation sources.
- Interface programmatically with a locally hosted LLM runtime (**Ollama**) via its REST API (`/api/generate`).
- Configure deterministic LLM inference using greedy decoding (`temperature: 0`) to ensure reproducibility.
- Implement automated **keyword-based evaluation scoring** to assess domain coverage and answer completeness.
- Classify outputs into actionable statuses (`PASS` vs. `REVIEW`) using defined benchmark thresholds.
- Export standardized evaluation metrics to CSV for version control and regression tracking across model releases.
- Establish the first evaluation baseline as **Release v0.1**.

---

## 3. Key Concepts & Definitions

| Term | Meaning |
| :--- | :--- |
| **Golden Question Set** | A curated, vetted collection of benchmark questions with ground-truth expected answers and validation keywords used as a standard testing suite for LLM evaluation. |
| **Baseline Run** | The initial recorded evaluation of an LLM against a benchmark set, providing a reference point against which future prompt modifications, fine-tuning, or model upgrades are measured. |
| **Ollama** | An open-source local LLM runner and management tool that exposes a lightweight REST API for querying models locally without third-party cloud API costs. |
| **Llama 3.2** | Meta's state-of-the-art compact open-weights language model (3B/1B parameters) optimized for edge and local execution with instruction-following capabilities. |
| **Greedy Decoding (`temperature: 0`)** | Decoding setting where the token with the highest predicted probability is selected at each step, yielding deterministic, repeatable model output. |
| **Keyword Coverage Score** | An automated lexical evaluation metric calculating the percentage of required reference keywords present in the model's generated answer. |
| **Release v0.1** | The official milestone designation given to the first baseline evaluation dataset, establishing the foundation for future iterative model comparisons. |

---

## 4. Evaluation Methodology and Formulas

Let:
- $N$ = Total number of benchmark questions in the golden dataset ($N = 30$)
- $K_i$ = Set of expected reference keywords for question $i$
- $M_i$ = Set of keywords from $K_i$ that appear in the model's generated answer (case-insensitive)
- $S_i$ = Keyword coverage score percentage for question $i$

$$\text{Score } S_i = \begin{cases} 0\% & \text{if } |K_i| = 0 \\ \left(\frac{|M_i|}{|K_i|}\right) \times 100 & \text{if } |K_i| > 0 \end{cases}$$

$$\text{Status}_i = \begin{cases} \text{PASS} & \text{if } S_i \ge 60\% \\ \text{REVIEW} & \text{if } S_i < 60\% \end{cases}$$

$$\text{Average Keyword Coverage} = \frac{1}{N_{successful}} \sum_{i=1}^{N_{successful}} S_i$$

---

## 5. Project Folder Structure

```
WEEK-6/
├── golden_set.json        # Curated 30-question benchmark with keywords & sources
├── requirements.txt       # Python dependencies (requests)
├── main.py                # Evaluation runner, Ollama client, scoring engine & CSV exporter
├── baseline_results.csv   # Generated Release v0.1 evaluation dataset
├── lab_output.txt         # Captured execution and summary logs
├── LAB_REPORT.md          # 2-Page Lab Report document format
└── README.md              # Complete technical documentation & Viva Q&A
```

---

## 6. Setup & Execution Guide

### 1. Verify Ollama Runtime
Ensure Ollama is installed and running on your system:
```powershell
ollama --version
```
Expected output:
```text
ollama version is 0.40.16 (or higher)
```

### 2. Pull the Llama 3.2 Model
Download the compact 3B instruction model locally:
```powershell
ollama pull llama3.2
```

### 3. Install Python Dependencies
From the `WEEK-6` directory, install the required HTTP library:
```powershell
cd c:\Users\vaaka\OneDrive\Desktop\GEN-AI\PRACTICAL\WEEK-6
pip install -r requirements.txt
```

### 4. Run the Baseline Evaluation
Execute the evaluation engine:
```powershell
python main.py
```

---

## 7. Golden Question Set Specification

The 30 questions are categorized across 8 core Generative AI foundational domains:

| Category | Question IDs | Topics Covered | Reference Sources |
| :--- | :--- | :--- | :--- |
| **Tokenization Fundamentals** | Q001 – Q002 | Tokenization definition, tokens, subwords, characters | Hugging Face Transformers Docs |
| **Tokenization Algorithms** | Q003 – Q006 | BPE, WordPiece, SentencePiece, BPE vs. WordPiece differences | Hugging Face / Google SentencePiece |
| **Multilingual & Token Ratios** | Q007 – Q008 | Language vocabulary representation, Telugu vs. English ratios | Hugging Face Transformers Docs |
| **Token Economics & Pricing** | Q009 – Q014 | Input/output tokens, cost formulas, context windows, rate limits | Google Gemini API Docs |
| **Autoregressive Generation** | Q015 – Q018 | Next-token prediction, probability distributions, greedy decoding | Hugging Face Generation Docs |
| **Sampling & Decoding Hyperparameters** | Q019 – Q022 | Sampling, temperature, top-k sampling, top-p (nucleus) sampling | Hugging Face Generation Docs |
| **Embeddings & Representations** | Q023 – Q025 | Vector embeddings, token IDs, semantic vector spaces | Hugging Face Embeddings Docs |
| **Positional Encodings & Transformers** | Q026 – Q030 | Positional encoding necessity, Sinusoidal encodings, RoPE, Transformer role | Vaswani et al. (2017), Su et al. (2021) |

---

## 8. Baseline Evaluation Output & Results

### Sample Question Output
```text
--------------------------------------
Question 1: Q001
Question: What is tokenization in large language models?

LLM Answer:
Tokenization is the process of splitting input text into smaller units called tokens.
Tokens can be words, subwords, or even characters, depending on the specific model
and its architecture...

Expected Answer:
Tokenization is the process of splitting input text into smaller units called tokens.

Matched Keywords: ['splitting', 'text', 'tokens']
Missing Keywords: []
Score: 100.0 %
Status: PASS
```

### Release v0.1 Summary Table
- **Release Version:** `v0.1`
- **Model:** `llama3.2` (3B parameters)
- **Decoding Method:** Greedy (`temperature: 0`)
- **Total Questions Evaluated:** `30`
- **Output Artifact:** `baseline_results.csv`

---

## 9. CSV Output Schema

The evaluation script generates `baseline_results.csv` with the following 11 columns:

| Column | Description |
| :--- | :--- |
| `Question_ID` | Unique question identifier (`Q001` to `Q030`) |
| `Question` | Full prompt question text submitted to the model |
| `Expected_Answer` | Gold-standard reference answer |
| `LLM_Answer` | Raw generated answer from Llama 3.2 |
| `Matched_Keywords` | Comma-separated list of reference keywords found in the answer |
| `Missing_Keywords` | Comma-separated list of reference keywords not found in the answer |
| `Score` | Keyword coverage percentage ($0.00\%$ to $100.00\%$) |
| `Status` | `PASS` ($\ge 60\%$) or `REVIEW` ($< 60\%$) |
| `Source` | Documentation source URL validating the ground truth |
| `Model` | Evaluated LLM model identifier (`llama3.2`) |
| `Release` | Dataset release tag (`v0.1`) |

---

## 10. Viva & Practice Questions

### Q1. What is a "Golden Dataset" in LLM application development?
**Answer:** A Golden Dataset is an authoritative, human-curated benchmark collection of representative test questions paired with verified ground-truth expected answers, validation criteria, and source references. It acts as an immutable regression test suite to measure accuracy, catch hallucinations, and benchmark model upgrades or prompt changes.

### Q2. Why is greedy decoding (`temperature = 0`) necessary for baseline evaluation?
**Answer:** Non-zero temperature values introduce stochastic sampling, meaning the model can produce different word choices and syntactic variations across successive runs for the exact same prompt. Setting `temperature = 0` enforces deterministic greedy decoding, ensuring that the benchmark evaluation is fully reproducible across repeated runs.

### Q3. What are the advantages and limitations of keyword-based LLM scoring?
**Answer:**  
- **Advantages:** Fast, deterministic, computationally inexpensive, requires no external judge model or API costs, and directly verifies whether essential technical terminology is present in the response.  
- **Limitations:** Cannot detect semantic equivalence (synonyms or paraphrased explanations), does not penalize verbosity or hallucinations, and may award full credit if keywords are mentioned even in an incorrect logical context. Modern evaluation pipelines often combine keyword checks with LLM-as-a-judge or semantic embedding similarity.

### Q4. What is the difference between BPE, WordPiece, and SentencePiece tokenization?
**Answer:**  
- **BPE (Byte Pair Encoding):** Bottom-up subword algorithm that starts with single characters and iteratively merges the most frequent adjacent character/token pairs based on frequency.  
- **WordPiece:** Similar to BPE, but selects symbol pairs that maximize the likelihood of the training data according to an unigram language model rather than pure frequency.  
- **SentencePiece:** Treats the input as a raw byte stream including whitespace characters (replacing space with `_`), allowing language-independent tokenization without language-specific pre-tokenizers.

### Q5. Why does modern LLM architecture favor Rotary Positional Embeddings (RoPE) over Sinusoidal encodings?
**Answer:** While original sinusoidal encodings add absolute positional vectors to input embeddings at the bottom of the Transformer, Rotary Position Embedding (RoPE) encodes positional information by multiplying the query and key representations by a rotation matrix in the complex plane. This naturally captures relative distances between tokens, improves length extrapolation to longer context windows, and preserves positional decay properties across self-attention layers.
