# 🔍 Subtheme Sentiment Analysis using BERT

This project focuses on performing **multi-label subtheme sentiment analysis** using **BERT (Bidirectional Encoder Representations from Transformers)**. Each input text (e.g., a customer review) is analyzed to detect multiple subthemes (like *garage service*, *ease of booking*, *value for money*, etc.) and their corresponding **sentiments (positive/negative)**.

---

## 📌 Project Goals

- Classify multiple subtheme-sentiment labels per review
- Fine-tune `bert-base-uncased` for multi-label text classification
- Prepare the model for deployment or reuse in other projects

---



## 🧪 Dataset

- The input is a structured CSV file where:
  - Column `text` contains customer reviews
  - Other columns are binary labels (0/1) representing sentiment for each subtheme.

### Example:

| text                                         | garage_service_positive | ease_of_booking_positive | value_for_money_positive |
|----------------------------------------------|--------------------------|---------------------------|---------------------------|
| "Tyres delivered quickly, smooth experience" | 1                        | 1                         | 0                         |

---

## ⚙️ Model Used

- `bert-base-uncased` from HuggingFace
- Fine-tuned for `multi_label_classification`
- Uses sigmoid activation and binary cross-entropy loss

---

## 🚀 Quickstart

### ✅ 1. Clone Repository

```bash
git clone https://github.com/Aswin-Cheerngodan/Subtheme-Sentiment-Analysis.git
cd subtheme-sentiment-analysis
```
### ✅ 2. Install Dependencies
```bash
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```
### ✅ 2. run streamlit app
```bash
streamlit run src/main.py
```
### 🌐 Access the App
subtheme-sentiment-analyzer: http://localhost:8501

### 🧪 Example Usage
- Type a customer review related to the garage.
- It finds the subthemes along withe their sentiment.  
- Optionally you can view scores of all subthemes.

### 📬 Contact
Questions or contributions? Open an issue or reach out at aachu8966@gmail.com

