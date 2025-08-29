# LinkedIn Post Generator

This project is part of the **Internship Assignment**.  
It is a **Streamlit-based web app** that generates **LinkedIn post drafts** using **Google’s Gemini 2.5 Pro model**.

---

## Features
- Generate 5+ LinkedIn posts from a given topic
- Select tone (Professional, Casual, Inspirational, Analytical, etc.)
- Define a target audience (e.g., HR leaders, Founders, Students)
- Add hashtags (optional, deduped & relevant)
- Add a Call-to-Action (optional)
- Control maximum word count
- Download posts as `.txt`
- Includes content filtering, word limit enforcement, and style consistency

---

## Project Structure
```
linkedin-post-generator/
│── app.py            # Main Streamlit UI
│── agent.py          # AI logic (Gemini prompts + JSON parsing)
│── utils.py          # Helper functions (sanitization, hashtags, etc.)
│── requirements.txt  # Dependencies
│── .env              # API key (not pushed to repo)
│── .gitignore        # Ignore venv, env, cache
│── README.md         # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

Activate:
- **Windows**: `.\.venv\Scriptsctivate`  
- **Mac/Linux**: `source .venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_api_key_here
BASE_URL=https://generativelanguage.googleapis.com
```

### 5. Run the App
```bash
streamlit run app.py
```

The app will open at:  
`http://localhost:8501`

---

### Deployment Notes:
- Add `GEMINI_API_KEY` and `BASE_URL` in **project settings → environment variables**  
- Ensure `requirements.txt` is installed automatically by the host  
---

## Deliverables
- Live app link: [https://linkedin-postgenerator.streamlit.app/](https://linkedin-postgenerator.streamlit.app/)  
- GitHub repo link: (https://github.com/Harshtr8/linkedin-post-generator)  
- Demo video:    

---

## Requirements Coverage

- Public Web App → Implemented  
- Inputs (topic, tone, audience, hashtags, CTA, length, style) → Implemented  
- Agent Behavior (planning, style control, filtering) → Implemented  
- Output (≥3 posts, JSON-parsed, cards in UI, download option) → Implemented  
- Deployment → Completed (Streamlit Cloud)  
- Deliverables → Repo and Demo video required  

---

## Tech Stack
- Python 3.10+  
- Streamlit  
- Google Generative AI (Gemini 2.5 Pro)  
- python-dotenv  

---