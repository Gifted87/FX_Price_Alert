## Alertify: Real-Time Price Alert Bot


This project implements a real-time price alert bot that monitors financial instruments (forex, cryptocurrencies, and stocks) and sends notifications via Telegram when user-defined price targets are reached.  The application uses `yfinance` to fetch price data, Flask for the web interface, APScheduler for background tasks, and the Telegram Bot API for notifications.

### 1. Table of Contents

- [Alertify: Real-Time Price Alert Bot](#alertify-real-time-price-alert-bot)
  - [1. Table of Contents](#1-table-of-contents)
  - [2. Description](#2-description)
  - [3. Features](#3-features)
  - [4. Getting Started](#4-getting-started)
    - [4.1 Prerequisites](#41-prerequisites)
    - [4.2 Installation](#42-installation)
    - [4.3 Configuration](#43-configuration)
  - [5. Usage](#5-usage)
    - [5.1 Adding Alerts](#51-adding-alerts)
    - [5.2 Viewing and Managing Alerts](#52-viewing-and-managing-alerts)
    - [5.3 Dark Mode](#53-dark-mode)
  - [6. Project Structure](#6-project-structure)
  - [7. Technologies Used](#7-technologies-used)

### 2. Description

Alertify provides a user-friendly web interface for setting price alerts on various financial instruments. The bot continuously monitors the market prices in the background and triggers alerts when predefined conditions are met.  Users receive instant notifications via Telegram, enabling them to react promptly to market changes.  The system is designed to be flexible and easily extendable to support additional instruments or notification channels.

### 3. Features

- **Real-time price monitoring:**  Fetches the latest price data at regular intervals (currently set to 1 minute).
- **Customizable alerts:**  Set price targets and alert types (above or below).
- **Multiple instrument support:**  Monitor forex pairs, cryptocurrencies, and stocks.
- **Telegram notifications:**  Receive instant alerts via Telegram messenger.
- **User-friendly web interface:**  Easily manage and delete alerts through a clean web dashboard.
- **Dark/Light Mode:** Toggle between light and dark themes for optimal viewing experience.
- **Persistent alerts:** Alerts are stored and loaded on application startup.

### 4. Getting Started

#### 4.1 Prerequisites

- **Python 3.7+:** Ensure you have a compatible Python version installed.
- **Required Libraries:** Install the necessary Python packages using:
```bash
pip install -r requirements.txt
```
  This will install `Flask`, `yfinance`, `APScheduler`, `python-dotenv`, `requests`, and `select2`.
- **Telegram Bot:**  Create a Telegram bot using BotFather and obtain your bot token.
- **.env file:** Create a `.env` file in the project root directory and add your Telegram bot token:
```
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

#### 4.2 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/alertify.git  # Replace with your repository URL
```
2. Navigate to the project directory:
```bash
cd alertify
```
3. Install the required libraries (see Prerequisites).

#### 4.3 Configuration

- **Telegram Chat ID:** Update the `chat_id` parameter in the `send_telegram_message` function in `alerts.py` and `telegram_bot.py` with your Telegram chat ID. You can find your chat ID using a bot like @userinfobot.
- **Template Directory:** The path to the `templates` directory is hardcoded in `app.py`.  Ensure the path is correct for your system, or modify it accordingly.


### 5. Usage

#### 5.1 Adding Alerts

1. Run the Flask application:
```bash
python app.py
```
2. Open the web interface in your browser (typically http://127.0.0.1:5000/).
3. Select the instrument, enter the target price, choose the alert type (above or below), and click "Add Alert".

#### 5.2 Viewing and Managing Alerts

- The "Current Alerts" section on the web interface displays all active and triggered alerts.
- Click the "Delete" button to remove an alert.
- Triggered alerts are highlighted visually.

#### 5.3 Dark Mode

- Click the sun/moon icon in the top right corner to toggle between dark and light mode. The preference is saved locally in your browser.



**Page 2 of 2**

### 6. Project Structure

```
alertify/
├── app.py             # Main Flask application file
├── alerts.py          # Alert management logic
├── config.py         # Configuration variables (Telegram bot token)
├── price_fetcher.py  # Fetches price data using yfinance
├── telegram_bot.py   # Sends Telegram notifications
├── templates/        # HTML templates for the web interface
│   └── add_alert.html
├── requirements.txt   # Project dependencies
└── .env              # Environment variables (Telegram bot token) 
```

### 7. Technologies Used

- **Flask:** A lightweight web framework for creating the user interface and handling HTTP requests.
- **yfinance:**  A Python library for downloading market data from Yahoo Finance.
- **APScheduler:**  A powerful task scheduling library for running background processes, such as fetching prices and checking alerts.
- **Telegram Bot API:**  Used for sending real-time notifications to users.
- **Requests:**  A library for making HTTP requests.
- **python-dotenv:**  For managing environment variables.
- **Select2:**  A jQuery library for enhanced select boxes in the web interface.
- **HTML, CSS, JavaScript:**  Used for building the front-end interface.



### 8. Contributing

Contributions are welcome!  If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

### 9. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 10. Acknowledgments

- Thanks to the developers of the libraries used in this project.
- Inspiration drawn from various open-source projects and online resources.


### 11. Contact

For any questions or feedback, feel free to contact Gifted Braimah at braimahgifted@gmail.com.


### 12. Disclaimer

This project is for educational and informational purposes only and should not be considered financial advice.  Use at your own risk.  The accuracy and reliability of the price data are not guaranteed. Always consult with a qualified financial advisor before making any investment decisions.
