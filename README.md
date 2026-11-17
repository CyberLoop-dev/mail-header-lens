<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=150&section=header&text=mail-header-lens&fontSize=34&fontColor=ffffff)
[![Typing](https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=14B8A6&center=true&vCenter=true&width=600&lines=mail-header-lens)](https://git.io/typing-svg)

[![MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![Python](https://img.shields.io/badge/language-Python-3776AB.svg)](https://python.org) [![Stars](https://img.shields.io/github/stars/CyberLoop-dev/mail-header-lens?style=social)](https://github.com/CyberLoop-dev/mail-header-lens/stargazers) [![Last Commit](https://img.shields.io/github/last-commit/CyberLoop-dev/mail-header-lens)](https://github.com/CyberLoop-dev/mail-header-lens/commits/main)

<img src="assets/mark.svg" width="110" alt="mail-header-lens icon">

**Inspect saved .eml headers for authentication results, routing hops, and sender/reply-to inconsistencies.**
</div>

## 🧭 Overview
A privacy-first .eml header inspector. It parses locally saved messages and highlights routing and authentication headers. It does not verify cryptographic signatures.

## ✨ Features
- ✨ Parse local .eml files
- ✨ Display Authentication-Results values
- ✨ Show Received routing hops
- ✨ Flag header claims that require independent verification

## 🎬 Demo
Run the CLI locally with your own .eml input. No hosted demo is provided.

## 🚀 Quick Start
~~~bash
git clone https://github.com/CyberLoop-dev/mail-header-lens.git
cd mail-header-lens
python main.py message.eml
~~~
Python 3.10+; standard library only.

## 🧰 Tech Stack
- 🐍 Python 3.10+
- 📦 email, argparse, json

## 🗂️ Folder Structure
~~~text
mail-header-lens/
├── main.py
├── assets/mark.svg
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
~~~

## 🗺️ Roadmap
- [x] 🧩 Header parsing
- [x] 🧭 Routing summary
- [ ] 🧪 Expand fixture coverage
- [ ] 📊 Export compact reports

## 🤝 Contributing
Issues and pull requests are welcome. Include test fixtures and document behavior changes.

## 📄 License
MIT © CyberLoop-dev. See [LICENSE](LICENSE).

<div align="center">
![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=90&section=footer)
</div>
