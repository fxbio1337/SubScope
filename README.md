# SubScope - Subdomain Scanner

🕵️‍♂️ A clean and extendable subdomain scanner written in Python for ethical hacking and penetration testing.

---

## ⚠️ Legal Notice

> **This tool is intended solely for authorized penetration testing, research, and educational purposes.**
> Do **not** use SubScope against systems you do not own or do not have **explicit permission** to test.
> Unauthorized scanning or probing of systems may be **illegal**.
> The developer assumes **no liability** for misuse or damage caused by this tool.

---

## 🔧 Features

* 🔍 Passive subdomain enumeration using:

  * `crt.sh` (Certificate Transparency logs)
  * `hackertarget.com` (DNS API)
* 🚀 Active DNS brute-force using your own wordlist
* 📦 Modular code structure (easily extendable)
* 🧠 CLI interface for flexible usage
* 💻 Compatible with **Windows & Linux**
* 📝 Saves results to `.txt` file automatically

---

## 🛠️ Installation

### 🔁 Clone the Repository

```bash
git clone https://github.com/yourusername/SubScope.git
cd SubScope
```

### 📦 Install Python dependencies

```bash
pip install -r requirements.txt
```
---

## 🚀 Quick Start

```bash
python subscope.py example.com --all -w wordlists/small.txt
```

---

## 📘 Usage Examples

### Passive Subdomain Enumeration

```bash
python subscope.py example.com --passive
```

### Active DNS Brute-Force

```bash
python subscope.py example.com --active --wordlist wordlists/small.txt
```

### Combined (Passive + Active)

```bash
python subscope.py example.com --all --wordlist wordlists/medium.txt
```

### Short Options

```bash
python subscope.py example.com -a -w wordlists/top1000.txt
python subscope.py example.com -p
```

---

## 💡 CLI Options

| Option              | Short | Description                             |
| ------------------- | ----- | --------------------------------------- |
| `--passive`         | `-p`  | Perform only passive reconnaissance     |
| `--active`          | `-a`  | Perform DNS brute-force with a wordlist |
| `--all`             | –     | Run both passive and active enumeration |
| `--wordlist <file>` | `-w`  | Path to wordlist for active scans       |
| `--help`            | `-h`  | Show all available options              |

---

## 📂 Wordlists

Place your wordlists inside the `wordlists/` directory:

```
wordlists/
├── small.txt
├── medium.txt
└── top1000.txt
```

> 🔑 Tip: You can also use your own custom wordlists.

---

## 📁 Project Structure

```
SubScope/
├── subscope.py
├── README.md
├── LICENSE
├── requirements.txt
└── wordlists/
    ├── small.txt
    ├── medium.txt
    └── top1000.txt
```

---

## 🧪 Disclaimer

This tool is intended strictly for authorized security testing, research, and educational use only.
Unauthorized use against systems you do not own or have explicit permission to test is **illegal**.
The author takes **no responsibility** for any misuse or damage.

---

## 📜 License

SubScope is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 fxbio1337

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.
```

---

## 🔗 Tags

`python` `recon` `subdomain-scanner` `dns` `pentesting` `bugbounty` `ethical-hacking` `osint`
