El País Opinion Scraper Automation

An automated Selenium-based scraping solution that extracts Opinion articles from El País, translates titles into English, downloads article images, and performs word frequency analysis.

Built with scalability in mind and compatible with BrowserStack for parallel cloud execution.


- Scrapes 5 latest Opinion articles from El País
- Extracts:
  - Spanish Title
  - Spanish Article Content
  - Cover Image (downloaded locally)
- Translates titles to English via RapidAPI
- Performs repeated word analysis (words appearing > 2 times)
- Robust handling of dynamic content and multiple DOM structures
- Designed for BrowserStack parallel execution


 Tech Stack

- Python 3.10+
- Selenium
- WebDriver Manager
- Requests
- RapidAPI (Google Translate API)
- BrowserStack (for cloud execution)

---

 Project Structure
BrowserStackProject/
│
├── scraper.py
├── translator.py
├── analyzer.py
├── main.py
├── requirements.txt
└── images/


 Setup Instructions

 1️⃣ Clone the Repository
git clone https://github.com/your-username/elpais-opinion-scraper.git

cd elpais-opinion-scraper


 2️⃣ Create Virtual Environment



python -m venv .venv
.venv\Scripts\activate (Windows)


 3️⃣ Install Dependencies



pip install -r requirements.txt


 4️⃣ Set RapidAPI Key

Set your environment variable:

Go to translator.py and replace your API key


Restart terminal after setting.

---

 ▶️ Run Locally



python main.py


Output:
- 5 Spanish titles
- 5 English translated titles
- Article content preview
- Images saved inside `/images`
- Word frequency analysis

---

 BrowserStack Execution

This project supports parallel execution on BrowserStack using Selenium Grid capabilities.

To run on BrowserStack:

- Configure BrowserStack credentials
- Update WebDriver capabilities
- Run parallel sessions

---

 Sample Output



Title (Spanish): Perú necesita estabilidad
Translated Title: Peru needs stability

--- Repeated Words (>2 times) ---
spain : 3




