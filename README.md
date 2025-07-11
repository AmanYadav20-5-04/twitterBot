# 🚀 Internet Speed Twitter Bot

A Python automation bot that checks your internet speed using [Speedtest.net](https://www.speedtest.net/) and tweets at your Internet Service Provider (ISP) on [Twitter (X.com)](https://x.com) if the speed is below what you're paying for.

This is a fun and practical project using **Selenium** for browser automation and **.env** for secure credential management.

---

## 📌 Features

- ✅ Automatically runs an internet speed test
- ✅ Compares actual speed with promised speed
- ✅ Logs into Twitter and tweets a complaint if speed is too low
- ✅ Uses `.env` to protect sensitive login information
- ✅ Modular, clean, and easy to customize
- ✅ Optional headless mode and configurable wait times

---

## 📁 Project Structure

```
internet-speed-twitter-bot/
├── main.py                 # Main runner script
├── Speedtwitterbot.py      # Bot class for speed test & Twitter actions
├── .env                    # Stores credentials (not pushed to GitHub)
├── .gitignore              # Prevents uploading sensitive/junk files
├── requirements.txt        # Python dependencies
└── README.md               # Project guide (this file)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/internet-speed-twitter-bot.git
cd internet-speed-twitter-bot
```

### 2. Install Dependencies

Make sure you have Python 3.7+ and pip installed, then:

```bash
pip install -r requirements.txt
```

### 3. Set Up `.env` File

Create a `.env` file in the project directory with your Twitter credentials:

```env
USERNAME=your_twitter_email
PASSWORD=your_twitter_password
```

⚠️ **Never share or commit this file. It contains sensitive login info.**

### 4. Run the Bot

```bash
python main.py
```

The bot will:

- Open [speedtest.net](https://speedtest.net)
- Run a speed test
- If the speed is lower than expected, it will:

  - Open [x.com](https://x.com)
  - Log in with your credentials
  - Tweet a complaint to your ISP

---

## 🔧 Configuration

Configuration is now handled through environment variables loaded from your
`.env` file. In addition to `USERNAME` and `PASSWORD`, you can set:

- `PROMISED_DOWN` – expected download speed (default: `1000` Mbps)
- `PROMISED_UP` – expected upload speed (default: `1000` Mbps)
- `HEADLESS` – set to `true` to run Chrome without a visible window
- `WAIT_TIMEOUT` – custom Selenium wait time in seconds

Example `.env` snippet:

```env
USERNAME=your_twitter_email
PASSWORD=your_twitter_password
PROMISED_DOWN=100
PROMISED_UP=20
HEADLESS=true
```

---

## 📦 Dependencies

- `selenium` – browser automation
- `python-dotenv` – loads `.env` environment variables

Install them via:

```bash
pip install selenium python-dotenv
```

---

## 🛡️ Disclaimer

This project is for educational purposes only.

- **Twitter may block or restrict automated activity**.
- **Use a test account** if you're experimenting.
- **Respect website terms of service** when using automation tools.

---
