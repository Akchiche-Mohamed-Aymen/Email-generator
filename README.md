# AI Email Generator

An intelligent email generation tool powered by Google's Gemini AI, LangChain, and Streamlit. Simply provide your context and requirements, and let AI craft professional emails for you.

## 🎯 Overview

This tool uses advanced AI to generate customized emails based on your input. Whether you need a formal business email, a friendly follow-up, or any other type of communication, the AI handles the writing for you.

## ✨ Benefits

- **No More Writer's Block**: Don't worry about what to write or how to start
- **Automatic Tone Matching**: No need to think about achieving the right tone for different email types (formal, casual, persuasive, etc.)
- **Time-Saving**: Generate well-structured emails in seconds
- **Consistent Quality**: Maintain professional communication standards effortlessly
- **Focus on Content**: Provide your key points and let AI handle the composition

## 🚀 Features

- User-friendly Streamlit interface
- Powered by Google Gemini AI
- LangChain integration for enhanced AI capabilities
- Custom data input for personalized email generation
- Instant email generation

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Akchiche-Mohamed-Aymen/Email-generator
```
2. Go to the project folder
```bash
cd ai-email-generator
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API key:
   - Create a `keys.py` file in the project root
   - Add your Gemini API key:
```python
key = "your-gemini-api-key-here"
```

## 📁 Project Structure
```
ai-email-generator/
│
├── ui.py                 # Streamlit user interface
├── generator.py          # Email generation logic with LangChain and Gemini
├── requirements.txt      # Project dependencies
├── keys.py              # API key storage (not tracked in git)
└── README.md            # Project documentation
```

## 🎮 Usage

1. Run the Streamlit app:
```bash
streamlit run ui.py
```

2. Open your browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter your custom data and requirements in the interface

4. Click the generate button to create your email

5. Copy and use the generated email as needed

## 🎥 Demo

[https://private-user-images.githubusercontent.com/170353978/531619635-1215e98e-02c5-49dd-9d93-218b1527bc50.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc0NDA1NTIsIm5iZiI6MTc2NzQ0MDI1MiwicGF0aCI6Ii8xNzAzNTM5NzgvNTMxNjE5NjM1LTEyMTVlOThlLTAyYzUtNDlkZC05ZDkzLTIxOGIxNTI3YmM1MC5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwM1QxMTM3MzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wZjcwNmI0NzJkZjMyNjU3ZWFiMWU3OWMyZDE3Nzg1MDE3NTFkMWI3NjBmNzA2ZDBlYWM0ODYxZWMzNjg0NjQ5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.aXzzlC8tYgc9yOSj1G24sIWBV8ysh_o9RTpjoeulpvU]

## 🔧 Technologies Used

- **Streamlit**: Web application framework
- **LangChain**: Framework for developing applications with LLMs
- **Google Gemini AI**: Advanced language model for email generation
- **Python**: Core programming language



## 📝 Getting Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `keys.py` file

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.


## 👤 Author

Akchiche Mohamed Aymen
- Email: [@myEmail](akchiche.mohamedaymen@gmail.com)

## 🙏 Acknowledgments

- Google Gemini AI for providing the language model
- LangChain for the AI framework
- Streamlit for the web interface framework

---

**Note**: This is a tool, not an autonomous agent. It performs the specific task of generating emails based on user input without autonomous decision-making or multi-step planning.