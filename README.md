# 🔍 AI Content Fact Checker

An AI-powered **Content Fact Checker** built using **Streamlit** and **n8n** to analyze articles, posts, and other written content for potentially misleading or inaccurate claims.

The application provides a simple Streamlit interface where users can paste content and submit it for automated fact-checking. The text is sent to an n8n workflow through a webhook, which processes the content and returns a structured fact-checking report.

## ✨ Features

* 📝 Paste articles, posts, or other textual content
* 🔗 Automated processing through an n8n workflow
* 📊 Summary of the fact-checking analysis
* 🔢 Displays the number of claims checked
* 🚩 Identifies flagged claims that need attention
* ✅ **Likely True** verdict
* ❌ **Likely False** verdict
* ⚠️ **Needs Context** verdict
* ❔ **Unverifiable** verdict
* 🎯 Confidence level for each claim
* 💡 Reasoning behind each verdict
* 📋 Expandable view for individual claims
* ⚡ Simple and interactive Streamlit interface

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Frontend interface
* **n8n** – Workflow automation and AI processing
* **Requests** – Communication between Streamlit and the n8n webhook

## 🔄 How It Works

```text
User enters content
        ↓
Streamlit Application
        ↓
n8n Webhook
        ↓
AI Fact-Checking Workflow
        ↓
Claims Analysis
        ↓
Verdicts + Confidence + Reasoning
        ↓
Fact-Checking Report
        ↓
Streamlit Dashboard
```

The Streamlit application sends the submitted text as JSON to the n8n webhook and processes the returned JSON response.

## 📊 Output

The application generates:

* **Overall Summary**
* **Number of Claims Checked**
* **Number of Claims Flagged**
* **Individual Claims**
* **Verdict**
* **Confidence**
* **Reasoning**
* **Claims Requiring Attention**

The interface displays the results dynamically and highlights flagged claims separately for easier review.

## 🎯 Use Cases

This project can be useful for:

* Fact-checking online articles
* Reviewing social media posts
* Identifying potentially misleading claims
* Content verification workflows
* AI-assisted research
* Media literacy and information analysis

## 🚀 Future Improvements

* Add source/reference links for individual claims
* Support URLs directly instead of only pasted text
* Add PDF and document upload support
* Improve claim extraction and verification
* Add fact-checking history
* Export reports as PDF/CSV
* Add multiple AI models for cross-verification
* Deploy the application publicly

> **Note:** AI-generated fact-checking results should be treated as an assistive analysis and independently verified before being used as authoritative information.
