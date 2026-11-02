# TokenScope AI 🔍

**Analyze tokens. Estimate costs. Optimize AI usage.**

TokenScope AI is a Python-based tool that helps developers analyze text token usage, estimate LLM API costs, and monitor context-window consumption across different AI models.

It provides a simple interactive dashboard built with Streamlit, making it easier to understand how much a prompt may cost before sending it to an AI model.

## 🚀 Features

- **Token Counter:** Count tokens in text using `tiktoken`.
- **Word & Character Analysis:** Get detailed text statistics.
- **Cost Estimator:** Estimate input and output costs based on model pricing.
- **Context Window Analyzer:** Monitor context usage and remaining capacity.
- **Interactive Dashboard:** Explore token and cost breakdowns through charts.
- **CSV Export:** Download analysis results for further review.
- **Multiple Model Support:** Compare token usage and estimated costs across supported models.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Tiktoken | Tokenization |
| Pandas | Data processing |
| Plotly | Interactive visualizations |
| JSON | Model pricing configuration |

## 📁 Project Structure

```text
TokenScopeAI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── tokenizer.py
│   ├── cost_calculator.py
│   └── context_analyser.py
│
├── data/
│   └── model_pricing.json
│
├── tests/
│   ├── __init__.py
│   └── test_tokenizer.py
│
└── results/
    └── .gitkeep
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/jayeshaswani67/TokenScopeAI.git
cd TokenScopeAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows CMD:**

```cmd
.venv\Scripts\activate
```

**PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL:

```text
http://localhost:8501
```

## 📊 How It Works

1. Enter your prompt or text into the application.
2. Select an AI model.
3. Specify the expected output token count.
4. Click **Analyze Prompt**.
5. Review token counts, estimated API costs, and context-window usage.
6. Export your analysis as a CSV file.

## 🧪 Run Tests

Run the tokenizer unit tests:

```bash
python -m unittest tests.test_tokenizer -v
```



## ⚠️ Important Notes

- Token counts are based on the selected tokenizer encoding and may not exactly match complete API request usage.
- Actual API usage can include additional tokens from system messages, chat formatting, tools, images, and other inputs.
- API prices and context-window limits can change. Verify current official model pricing before relying on cost estimates.
- Cost estimates are informational and do not represent actual API billing.

## 🔮 Future Improvements

- [ ] Add more LLM providers and models.
- [ ] Integrate official model pricing data.
- [ ] Add prompt optimization suggestions.
- [ ] Add token usage history and analytics.
- [ ] Support API-based token usage tracking.
- [ ] Add side-by-side model cost comparisons.
- [ ] Introduce team dashboards and usage reports.

## 🤝 Contributing

Contributions, ideas, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 👨‍💻 Author

**Jayesh Aswani**

- GitHub: [@jayeshaswani67](https://github.com/jayeshaswani67)

---

⭐ If you find TokenScope AI useful, consider giving the repository a star!

**TokenScope AI — Understand your tokens before you spend them.**