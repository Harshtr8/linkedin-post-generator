# LinkedIn Post Generator

This project is part of the **Internship Assignment**.  
It is a **Streamlit-based web app** that generates **LinkedIn post drafts** using **Google’s Gemini 2.5 Pro model**.

---

## Live Demo
- Live App URL: [https://linkedin-postgenerator.streamlit.app/](https://linkedin-postgenerator.streamlit.app/)  
- Demo Video: [https://drive.google.com/file/d/1QdUdNgJaXl7FFK8qjs8yRRpKQJAQwlAo/view?usp=drive_link](https://drive.google.com/file/d/1QdUdNgJaXl7FFK8qjs8yRRpKQJAQwlAo/view?usp=drive_link)    

---

## Features
- Generate 3 or more LinkedIn posts from a given topic
- Input fields:
  - **Topic** (required)
  - **Tone** (Professional, Casual, Inspirational, Analytical, etc.)
  - **Target Audience**
  - **Optional Hashtags** (deduped & relevant)
  - **Optional Call-to-Action (CTA)**
  - **Word Count Control**
  - **Style Notes**
- Profanity/content guardrails
- Download posts as `.txt`
- Fully deployed on free hosting (Streamlit Cloud)

---

## Project Structure
```
linkedin-post-generator/
│── app.py            # Main Streamlit UI
│── agent.py          # AI logic (Gemini prompts + JSON parsing + filtering)
│── utils.py          # Helper functions (sanitization, hashtags, guardrails)
│── requirements.txt  # Dependencies
│── .env              # Local environment variables (ignored in git)
│── .gitignore        # Ignore venv, env, cache, pycache
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
- **Windows**: `.\.venv\Scripts\activate`
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

For **Streamlit Cloud deployment**, use `.streamlit/secrets.toml` instead:
```toml
GEMINI_API_KEY = "your_api_key_here"
BASE_URL = "https://generativelanguage.googleapis.com"
```

### 5. Run the App Locally
```bash
streamlit run app.py
```
The app will open at `http://localhost:8501`

---


### Deployment Notes:
- Add `GEMINI_API_KEY` and `BASE_URL` in **environment variables**
- `requirements.txt` is auto-installed by hosting service
- The app homepage `/` acts as a **200 OK health check**

---


## Requirements Coverage

1. **Public Web App**  
   - Deployed at a free live URL  
   - Topic input (required)  
   - Optional inputs (tone, audience, hashtags, CTA, style, word count)  
   - Generate button returns ≥3 LinkedIn-ready drafts  

2. **Agent Behavior**  
   - Gemini LLM used  
   - Style control (tone, persona)  
   - Audience targeting  
   - Hashtag extraction & CTA suggestions  
   - Guardrails (profanity + word count filter)  

3. **Output**  
   - Posts rendered clearly in cards  
   - Download option available   

4. **Deployment**  
   - Free hosting (Streamlit Cloud)  
   - Homepage = health check (200 OK)  
   - Secrets managed server-side  

5. **Other Requirements**  
   - Own work, with standard libraries and Gemini API  
   - Free tier API supported  
   - Sensitive content filter present  
---

## Tech Stack
- Python 3.10+
- Streamlit
- Google Generative AI (Gemini 2.5 Pro)
- python-dotenv
---

## Attribution & Disclaimer
- Built with **Streamlit** for UI, **Google Generative AI (Gemini)** for text generation, and **python-dotenv** for environment management.  
- The generated content is AI-created. Users are responsible for ensuring outputs comply with **LinkedIn policies, copyright, and sensitivity guidelines**.  
- API usage runs on **Gemini free tier**, ensuring no mandatory paid usage.  
---
