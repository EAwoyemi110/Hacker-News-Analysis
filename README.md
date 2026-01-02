## 📊 Hacker News Engagement Analysis

### 🔍 Project Overview
- Analyzed Hacker News data using Python to understand what drives post engagement.
- Processed **20,000+ posts** using the `csv` and `datetime` modules.
- Compared **“Ask HN” vs. “Show HN”** performance.
- Examined how **submission time** affects comment volume.
- Goal: identify the optimal timing for reaching the tech community.

### ❓ Key Questions
- Do **“Ask HN”** or **“Show HN”** posts receive more comments on average?
- Does the **time of day** affect post engagement?

### 🗂 Dataset
- Source: **Y Combinator’s Hacker News**
- Size: approximately **20,000 rows**

### 🛠 Technologies Used
- **Language:** Python 3.x
- **Modules:**
  - `csv` – data parsing
  - `datetime` – time-series analysis
  - `matplotlib` – data visualization

### 📈 Key Findings
- “Ask HN” posts submitted at **15:00 (3 PM EST)** receive the **highest average number of comments**.

### ▶️ How to Run
- Run the script from the command line:
  ```bash
  python hacker_news.py
