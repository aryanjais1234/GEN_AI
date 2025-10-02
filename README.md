# 🤖 GenAI Learning Hub

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT-green.svg)](https://openai.com)
[![Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)](https://ai.google.dev)

> 🚀 **A comprehensive collection of Generative AI examples and prompt engineering techniques**

Welcome to the **GenAI Learning Hub** - your one-stop destination for exploring the fascinating world of Generative AI! This repository contains practical examples, prompt engineering techniques, and hands-on implementations to help you master AI interactions.

---

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [🏗️ Project Structure](#️-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🧠 Prompt Engineering Techniques](#-prompt-engineering-techniques)
- [📁 File Descriptions](#-file-descriptions)
- [⚙️ Setup & Installation](#️-setup--installation)
- [🎮 Usage Examples](#-usage-examples)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🎯 Overview

This repository demonstrates various **prompt engineering techniques** and **AI interaction patterns** using popular AI models like Google's Gemini. Perfect for students, developers, and AI enthusiasts looking to understand:

- 🎪 **Zero-Shot Prompting** - Direct task execution without examples
- 🎭 **Few-Shot Prompting** - Learning from examples
- 🧩 **Chain-of-Thought (CoT)** - Step-by-step reasoning
- 📝 **Prompt Formatting Styles** - Different prompt structures

---

## 🏗️ Project Structure

```
📦 GenAI_Udemy/
├── 📄 README.md                    # This amazing documentation
├── 🌍 hello_world/
│   └── 🐍 main.py                  # Basic AI interaction example
└── 💭 prompts/
    ├── 🎯 zero.py                   # Zero-shot prompting examples
    ├── 🎭 few.py                    # Few-shot prompting techniques
    ├── 🧩 cot.py                    # Chain-of-thought reasoning
    └── 📝 prompt_styles.md          # Various prompt formatting styles
```

---

## 🚀 Getting Started

### Prerequisites

- 🐍 Python 3.8 or higher
- 🔑 Google Gemini API Key
- 📦 OpenAI Python package

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/aryanjais1234/GEN_AI.git
   cd GEN_AI
   ```

2. **Set up virtual environment**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**

   ```bash
   pip install openai
   ```

4. **Run your first example**
   ```bash
   cd hello_world
   python main.py
   ```

---

## 🧠 Prompt Engineering Techniques

### 🎯 Zero-Shot Prompting

> Direct task execution without providing examples

**File:** `prompts/zero.py`

- ✨ **What it does:** Asks the AI to perform tasks based solely on its training
- 🎪 **Use case:** Quick responses for well-understood tasks
- 💡 **Example:** "Write Python code to translate Hindi to English"

### 🎭 Few-Shot Prompting

> Provide examples to guide the model's response

**File:** `prompts/few.py`

- ✨ **What it does:** Shows the AI examples before asking for output
- 🎪 **Use case:** Complex tasks requiring specific format or style
- 💡 **Example:** Structured JSON responses with examples

### 🧩 Chain-of-Thought (CoT) Prompting

> Step-by-step reasoning process

**File:** `prompts/cot.py`

- ✨ **What it does:** Breaks down complex problems into logical steps
- 🎪 **Use case:** Mathematical problems, complex reasoning tasks
- 💡 **Example:** Solving math equations with BODMAS method
- 🔄 **Interactive:** Real-time step-by-step problem solving

---

## 📁 File Descriptions

### 🌍 `hello_world/main.py`

Your first AI interaction! A simple math tutor that:

- 🧮 Specializes in mathematics questions only
- 🚫 Politely declines non-math queries
- 💬 Demonstrates basic AI conversation flow

### 🎯 `prompts/zero.py`

Zero-shot prompting demonstration:

- 🤖 Creates "Alexa" - a coding assistant
- 💻 Answers only programming-related questions
- 🔒 Implements strict query filtering

### 🎭 `prompts/few.py`

Few-shot learning with examples:

- 📊 Returns structured JSON responses
- 💼 Provides code examples when appropriate
- 🎯 Distinguishes between coding and non-coding questions

### 🧩 `prompts/cot.py`

Interactive Chain-of-Thought reasoning:

- 🔄 **START** → **PLAN** → **OUTPUT** workflow
- 🧠 Shows step-by-step thinking process
- 💡 Perfect for complex problem solving
- 🎮 Interactive command-line interface

### 📝 `prompts/prompt_styles.md`

Reference guide for different prompt formats:

- 🦙 **Alpaca Prompt** format
- 💬 **ChatML** structure
- 🎯 **INST** prompting style

---

## ⚙️ Setup & Installation

### 🔧 Environment Setup

1. **Create virtual environment:**

   ```powershell
   python -m venv venv
   ```

2. **Activate environment:**

   ```powershell
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1

   # Windows Command Prompt
   .\venv\Scripts\activate.bat

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   _Or install individually:_

   ```bash
   pip install openai python-dotenv
   ```

### 🔑 API Configuration

**🔒 IMPORTANT: Secure API Configuration**

This project uses environment variables to keep your API keys secure and prevent them from being accidentally committed to version control.

1. **Create a `.env` file in the root directory:**

   ```bash
   # Copy the example and add your API key
   cp .env.example .env
   ```

2. **Add your Gemini API key to `.env`:**

   ```env
   # Environment Variables for GenAI Project
   # DO NOT COMMIT THIS FILE TO VERSION CONTROL

   # Google Gemini API Configuration
   GEMINI_API_KEY=your_actual_api_key_here
   GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/

   # Other Configuration
   MODEL_NAME=gemini-2.5-flash
   ```

3. **Get your Gemini API key:**
   - Visit [Google AI Studio](https://makersuite.google.com/)
   - Create an account and generate an API key
   - Replace `your_actual_api_key_here` with your actual API key

**🛡️ Security Features:**

- ✅ `.env` file is in `.gitignore` - won't be committed to GitHub
- ✅ API keys loaded from environment variables
- ✅ No hardcoded secrets in source code

---

## 🎮 Usage Examples

### 🧮 Math Tutor (Hello World)

```bash
cd hello_world
python main.py
```

**Output:** Explains mathematical formulas like (a+b)²

### 🤖 Coding Assistant (Zero-Shot)

```bash
cd prompts
python zero.py
```

**Output:** Provides Python code for translation tasks

### 📊 Structured Responses (Few-Shot)

```bash
cd prompts
python few.py
```

**Output:** JSON formatted responses with code examples

### 🧠 Interactive Problem Solver (CoT)

```bash
cd prompts
python cot.py
```

**Interactive Experience:**

```
👉 Can you solve 15 + 3 * 4?

🧠 Looking at this math problem, I need to use BODMAS
🧠 First, I'll multiply 3 * 4 = 12
🧠 Then, I'll add 15 + 12 = 27
💡 So the final answer is 27
```

---

## 🛠️ Troubleshooting

### Common Issues

1. **❌ API Key Error**

   - Ensure your Gemini API key is valid
   - Check the base URL is correct

2. **❌ Import Error**

   - Make sure virtual environment is activated
   - Run `pip install openai`

3. **❌ Model Not Found**
   - Verify model name: `gemini-2.5-flash`
   - Check API endpoint availability

---

## 🎯 Learning Objectives

After exploring this repository, you'll understand:

- ✅ Different prompt engineering techniques
- ✅ How to structure AI conversations
- ✅ When to use each prompting method
- ✅ How to implement AI assistants with specific roles
- ✅ Interactive AI application development

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔀 Open a Pull Request

### 💡 Ideas for contributions:

- 🆕 New prompt engineering techniques
- 🐛 Bug fixes and improvements
- 📚 Additional documentation
- 🎨 UI improvements for interactive scripts

---

## 📖 Additional Resources

- 📚 [OpenAI Documentation](https://platform.openai.com/docs)
- 🌟 [Google AI Studio](https://makersuite.google.com/)
- 🎓 [Prompt Engineering Guide](https://www.promptingguide.ai/)
- 💬 [AI Community Discord](https://discord.gg/ai)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Aryan Jaiswal** - [@aryanjais1234](https://github.com/aryanjais1234)

---

<div align="center">

### 🎉 Happy Coding with AI! 🎉

If you found this repository helpful, please give it a ⭐️!

**Made with ❤️ and lots of ☕**

[⬆️ Back to Top](#-genai-learning-hub)

</div>
