# 🧠 AI Search & Research Assistant (Ongoing Project)

An AI-powered web application that helps users collect, analyze, and summarize information from the web into structured research reports. The application combines web search, generative AI, and automated PDF generation to improve research efficiency and productivity.

This project is currently under active development.

---

##  Features

- 🔍 **Web Search Integration:** Retrieves relevant web search results using the Tavily API.
- 🤖 **AI-Based Research:** Uses Google's Gemini API to generate structured research reports from search results.
- 📝 **Automated Report Generation:** Organizes research findings into an executive summary, key findings, insights, advantages and disadvantages, and a conclusion.
- 📄 **PDF Report Generation:** Generates downloadable PDF reports using ReportLab.
- 🖼️ **Related Image Search:** Retrieves related image results through the Tavily API.
- 🧩 **Modular Agent-Based Architecture:**
  - Search Agent
  - Research Agent
  - Report Agent
  - Image Agent
- 📊 **Research Statistics:** Displays source count, report word count, and generation time.
- 📚 **Session-Based Research History:** Tracks searched topics during the current Streamlit session.
- ⚙️ **Report Length Options:** Allows users to select Short, Medium, or Detailed reports.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web application interface |
| Google Gemini API | AI-based research and report generation |
| Tavily API | Web search and image search integration |
| Requests | HTTP requests and API communication |
| python-dotenv | Loading environment variables for local development |
| ReportLab | PDF report generation |

---

## 🏗️ Application Workflow

1. **User Input:** The user enters a research topic in the Streamlit interface.
2. **Web Search:** The Search Agent retrieves relevant results using Tavily.
3. **Content Preparation:** The Report Agent combines search result titles, content, and source URLs.
4. **AI Research:** The Research Agent sends the topic and collected content to Gemini to generate a structured report.
5. **Image Search:** The Image Agent requests related image results from Tavily.
6. **Report Display:** The application displays the report, source count, word count, and generation time.
7. **PDF Export:** The PDF utility creates a downloadable research report.
8. **Source References:** The application displays links to the retrieved web sources.

---

## 📁 Project Structure

```text
ai-search-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── research_report.pdf
│
├── agents/
│   ├── search_agent.py
│   ├── research_agent.py
│   ├── report_agent.py
│   └── image_agent.py
│
└── utils/
    └── pdf_utils.py
```

- `app.py` — Main Streamlit application and research workflow.
- `requirements.txt` — Lists the Python dependencies.
- `agents/search_agent.py` — Retrieves web search results using Tavily.
- `agents/research_agent.py` — Generates research reports using Gemini.
- `agents/report_agent.py` — Prepares content from search results.
- `agents/image_agent.py` — Retrieves related image results using Tavily.
- `utils/pdf_utils.py` — Creates PDF reports using ReportLab.
- `research_report.pdf` — A PDF report file included in the repository.
- `.gitignore` — Specifies files and folders Git should ignore.

Local files such as `.env` and the virtual environment should not be committed to the repository.

---

## ⚙️ Installation and Setup

### Prerequisites

- Python installed on your system
- A Tavily API key
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/anshikasrivastavbst-a11y/ai-search-assistant.git
cd ai-search-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root for local development:

```env
TAVILY_API_KEY=your_tavily_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder values with your own API keys. Never publish real credentials in source code or GitHub commits.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

---

## ☁️ Deployment

The application is deployed on **Streamlit Community Cloud**.

**Live Demo:** [AI Search & Research Assistant](https://ai-search-assistant-wfh6kvc5wuvdvocpcqqw9p.streamlit.app/)

The deployed application uses API credentials configured through Streamlit Community Cloud Secrets.

To deploy your own copy:

1. Push the project to a GitHub repository.
2. Connect the repository to Streamlit Community Cloud.
3. Select `app.py` as the application entry point.
4. Configure the required API credentials in the app's Secrets settings.
5. Deploy the application and review the logs if errors occur.

Successful deployment does not guarantee continuous availability of third-party APIs or their usage quotas.

---

## 🚧 Current Project Status

- ✔ Streamlit application implemented.
- ✔ Tavily web search integration implemented.
- ✔ Modular agent-based architecture implemented.
- ✔ Gemini-based research report generation integrated.
- ✔ PDF report generation functionality implemented.
- ✔ Related image search integration implemented.
- ✔ Application deployed on Streamlit Community Cloud.
- 🔄 UI improvements and additional features remain ongoing.

**API limitation:** Gemini report generation has encountered a free-tier quota error during deployment testing. The feature may be temporarily unavailable until quota becomes available.

---

## 🔐 Security Note

- API keys are loaded through environment variables during local development.
- Streamlit Community Cloud Secrets are used to configure deployment credentials.
- `.env` and local virtual environment folders should be excluded through `.gitignore`.
- Never commit API keys or other credentials to GitHub.
- If an API key is exposed, revoke it and generate a replacement.

---

## 📌 Future Improvements

- Improve the Streamlit interface and user experience.
- Optimize AI response time and API usage.
- Add multi-document research and summarization.
- Support additional report export formats.
- Improve error handling for API failures and quota limits.
- Enhance source attribution and research traceability.
- Add automated testing and performance improvements.

---

## 🎯 Learning Outcomes

This project provides practical experience with:

- Integrating external APIs into a Python application.
- Building an interactive web application using Streamlit.
- Designing modular agent-based components.
- Using generative AI for research and summarization.
- Generating downloadable PDF reports.
- Managing API credentials and cloud deployment.
- Handling third-party API errors and usage limitations.

---

## 👩‍💻 Author

**Anshika Srivastav**

GitHub: [anshikasrivastavbst-a11y](https://github.com/anshikasrivastavbst-a11y)

---

*This project is under active development. Feature availability depends on successful API responses and service quotas.*
