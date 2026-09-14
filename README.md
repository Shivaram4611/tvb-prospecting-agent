# TVB Autonomous Startup Prospecting Engine

An autonomous venture-intelligence agent engineered for **The Venture Build (TVB)**. It discovers, qualifies, and enriches non-US technology platforms matching TVB's venture catalyst investment and expansion criteria.

## Target Profile & Constraints
- **Funding / Revenue:** $1M – $5M USD (or European equivalent; Seed to Series A stage)
- **Sector Focus:** Tech-enabled platforms (AI, SaaS, Cybersecurity, Fintech, Digital Twin)
- **Geographic HQ:** Outside the United States (Europe, India, UK, Southeast Asia, Middle East)
- **Decision Makers:** CEO or Co-founder attribution
- **Data Integrity:** Strict DNS MX email verification; unverified fields remain intentionally blank

## Pipeline Architecture
1. **Autonomous Discovery:** Dynamic search generation across venture registries and news desks (EU-Startups, TechInAsia, Inc42).
2. **Deterministic Evaluation:** Gemini model processes announcements against TVB parameters.
3. **Executive Contact Resolution:** Generates and validates founder email addresses via DNS MX records.
4. **Interactive Dashboard:** Self-serve Streamlit application featuring live trigger controls and CSV export.

## Live Link
[Live Demo in streamlit](https://tvb-prospecting-agent.streamlit.app/)

## Deployment Setup
```bash
git clone https://github.com/Shivaram4611/tvb-prospecting-agent.git
cd tvb-prospecting-agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
