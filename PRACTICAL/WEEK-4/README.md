# WEEK-4: Tokenizer Lab
## Comparison of BPE, WordPiece, and SentencePiece Tokenizers
**Languages Evaluated:** English • Telugu • Hindi

---

## 1. Aim
To implement and compare three subword tokenization approaches—**Byte Pair Encoding (BPE)**, **WordPiece**, and **SentencePiece**—using English, Telugu, and Hindi text, and observe how each tokenizer splits text into tokens and how many tokens are produced.

---

## 2. Learning Objectives
- Understand why tokenization is required before text is processed by a language model.
- Observe the difference between word-level and subword-level splitting.
- Run pretrained tokenizers representing BPE, WordPiece, and SentencePiece.
- Compare token pieces and token counts for English, Telugu, and Hindi.
- Explain why token counts differ across tokenizer vocabularies and training data.

---

## 3. Short Theory & Tokenizer Comparison

A tokenizer converts raw text into smaller units called **tokens**. A token may be a complete word, part of a word (subword), punctuation mark, or byte/character-related unit. The tokenizer maps these tokens to numeric token IDs that a language model can process.

| Tokenizer | Basic Idea | Model Used in this Lab |
| :--- | :--- | :--- |
| **BPE (Byte Pair Encoding)** | Builds subword units by repeatedly merging frequent adjacent symbol pairs. GPT-2 uses byte-level BPE. | `gpt2` |
| **WordPiece** | Uses a learned subword vocabulary; a word is split into pieces (prefixed with `##`) when the whole word is not in the vocabulary. | `bert-base-multilingual-cased` |
| **SentencePiece** | A language-independent framework that learns subword units directly from raw text (treats spaces as regular characters, e.g., `_`). XLM-R uses SentencePiece with a BPE model. | `xlm-roberta-base` |

> **Important Comparison Note:** This lab compares real pretrained tokenizers, not three algorithms trained on the same dataset with the same vocabulary size. GPT-2 is primarily English-trained, while multilingual BERT and XLM-R are multilingual. Therefore, token-count differences reflect both the tokenization method and each model's vocabulary and training data. XLM-R uses SentencePiece with BPE; SentencePiece is a framework, not one single algorithm.

---

## 4. Project Folder Structure

```
WEEK-4/
├── .venv/                   # Virtual environment with installed dependencies
├── .gitignore               # Git ignore configuration
├── requirements.txt         # Project dependencies (transformers, sentencepiece)
├── tokenizer_comparison.py  # Python script comparing BPE, WordPiece, SentencePiece
├── lab_output.txt           # Captured console output of the execution
└── README.md                # Full documentation, results analysis, and Viva Q&A
```

---

## 5. Setup & Execution

### 1. Activate the Virtual Environment
In PowerShell from the `WEEK-4` folder:
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Install Requirements (if setting up fresh)
```powershell
pip install -r requirements.txt
```

### 3. Run the Program
```powershell
python tokenizer_comparison.py
```

---

## 6. Experimental Results & Observations

### Summary Table of Token Counts

| Language | Input Text | BPE (GPT-2) | WordPiece (mBERT) | SentencePiece (XLM-R) |
| :--- | :--- | :---: | :---: | :---: |
| **English** | `Artificial intelligence is changing the world.` | **8** | 10 | 10 |
| **Telugu** | `కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.` | 112 | 18 | **14** |
| **Hindi** | `कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।` | 68 | 17 | **14** |

### Key Observations
1. **English Efficiency**: 
   - GPT-2 produces the fewest tokens (**8**) for English because it was trained almost exclusively on English web text and its vocabulary contains large, common English words as single tokens (e.g., `Ġintelligence`, `Ġchanging`).
   - mBERT and XLM-R add special tokens (`[CLS]`/`[SEP]` and `<s>`/`</s>`), bringing the English count to 10.
2. **Telugu & Hindi Disparity**:
   - GPT-2 inflates the token count dramatically (**112** for Telugu, **68** for Hindi). Because GPT-2 lacks Telugu and Hindi characters/subwords in its vocabulary, it falls back to raw UTF-8 bytes (`à°ķ...`), producing multiple tokens per Unicode character.
   - Multilingual BERT (`bert-base-multilingual-cased`) and XLM-RoBERTa (`xlm-roberta-base`) were explicitly trained on multilingual corpora including Indic scripts. They decompose words into meaningful native subwords (e.g., `##త్రి`, `##ాన్ని`, `కృత`, `బుద్ధి`), yielding drastically lower token counts (14–18 tokens).
   - SentencePiece XLM-R achieves the most compact representations (**14 tokens** for both Telugu and Hindi) due to its larger multilingual vocabulary (250,000 tokens) and raw-text subword optimization.

---

## 7. Questions for Practice / Viva

### Q1. What is tokenization, and why do language models need it?
**Answer:** Tokenization is the process of breaking down raw, continuous text into smaller discrete semantic units called tokens (words, subwords, or characters) and mapping them to unique numerical identifiers (Token IDs). Language models cannot directly process raw characters or strings; their underlying neural network architectures perform mathematical operations (matrix multiplications, attention mechanisms, embeddings) on numeric tensors. Tokenization bridges human language and machine representation.

### Q2. What is the difference between a word and a subword token?
**Answer:** 
- A **word token** treats each whitespace-delimited word as a discrete atomic unit. This leads to massive vocabulary sizes and fails when encountering out-of-vocabulary (OOV) words or morphological variations (e.g., `running`, `unfriendly`).
- A **subword token** breaks words down into smaller meaningful units, syllables, morphemes, or character combinations (e.g., `un-`, `friend`, `##ly`). Subword tokenization balances vocabulary size and coverage, effectively handling rare or unseen words without OOV errors.

### Q3. Explain the basic idea of Byte Pair Encoding (BPE).
**Answer:** BPE is a data compression algorithm adapted for NLP tokenization. It begins with a base vocabulary of individual characters (or bytes in byte-level BPE). The algorithm iteratively identifies the most frequently co-occurring adjacent pair of symbols across the training corpus and merges them into a single new subword token. This process repeats until the desired vocabulary size is reached.

### Q4. How does WordPiece split an unknown or rare word?
**Answer:** WordPiece checks if the complete word exists in its vocabulary. If not, it splits the word greedily from left to right into the longest subword segments present in its vocabulary. Non-initial subword pieces are marked with a special prefix (such as `##` in BERT) to indicate that they attach to the preceding token rather than starting a new word.

### Q5. What is SentencePiece? Does SentencePiece always mean the Unigram algorithm?
**Answer:** SentencePiece is an unsupervised, language-independent text tokenizer and detokenizer framework designed primarily for Neural Machine Translation. Unlike traditional tokenizers, it does not rely on language-specific pre-tokenizers or whitespace rules; it treats the entire input as a continuous stream of characters and replaces whitespace with a special symbol (like `_` or ` ` U+2581). SentencePiece does **not** always mean the Unigram algorithm: it supports both **BPE** and **Unigram** models (for instance, XLM-RoBERTa uses SentencePiece with a BPE model).

### Q6. Why might GPT-2 split Telugu or Hindi text into more tokens than a multilingual tokenizer?
**Answer:** GPT-2 was predominantly trained on an English-dominated corpus (WebText). As a result, its vocabulary of 50,257 tokens rarely contains multi-character Indic subwords or morphemes for Telugu or Hindi. Consequently, GPT-2 falls back to byte-level representations, breaking individual Telugu and Hindi Unicode characters into multiple byte tokens (UTF-8 bytes). In contrast, multilingual tokenizers like `bert-base-multilingual-cased` and `xlm-roberta-base` were trained on corpora covering 100+ languages and include native Telugu and Hindi characters and subwords in their vocabularies.

### Q7. Does a lower token count always mean that a tokenizer is better? Give a reason.
**Answer:** No. A lower token count simply indicates longer subwords or full words matched in the vocabulary. Having larger subwords requires a much larger vocabulary size, which significantly increases the model's embedding layer parameter count, memory footprint, and training data requirements. Furthermore, if a tokenizer fails to decompose morphologically complex words into shared stems, it may impair generalization. An optimal tokenizer balances token sequence length with vocabulary size and semantic granularity.

### Q8. What are token IDs, and where are they used?
**Answer:** Token IDs are integer indexes that uniquely correspond to each token in a tokenizer's vocabulary. They are used as lookups in the model's initial embedding matrix to retrieve continuous vector representations (dense embeddings) that are passed into the transformer layers.

### Q9. Why should we compare tokenizers using the same input sentences?
**Answer:** Comparing tokenizers on the exact same input sentences ensures controlled evaluation. It allows us to directly observe differences in segmentation granularity, handling of whitespace and punctuation, handling of non-Latin scripts, and relative compression efficiency (sequence length) without confounding factors from different sentence lengths or domains.

### Q10. What is the difference between token count and the number of characters in a sentence?
**Answer:** The character count is the total number of raw typographic symbols (letters, spaces, punctuation marks, combining diacritics/accents) in a string. The token count is the number of discrete units into which the tokenizer segments that sentence. Because subword tokens typically represent multiple characters (or conversely, non-Latin Unicode characters can be split into multiple byte tokens in byte-level BPE), the token count is usually lower than the character count for supported languages, but may exceed the character count for low-resource languages in byte-level models.
