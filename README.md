# Alertify - Real-Time Price Alert Bot

Alertify is a real-time price alert bot that allows users to set alerts for financial instruments (cryptocurrencies, forex pairs, etc.). It fetches real-time prices using the `yfinance` library and sends notifications via Telegram when the specified conditions are met. The application is built using Flask for the web interface and `yfinance` for price data.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [File Structure](#file-structure)
7. [Technologies Used](#technologies-used)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgements](#acknowledgements)

---

## Features
- **Set Price Alerts**: Users can set alerts for financial instruments (e.g., `AAPL`, `BTC-USD`) with conditions like:
  - Price goes **above** a target price.
  - Price goes **below** a target price.
  - Price breaks **Bollinger Bands** (upper or lower).
- **Real-Time Price Fetching**: Fetches real-time prices using the `yfinance` library.
- **Telegram Notifications**: Sends notifications via Telegram when an alert is triggered.
- **Web Interface**: A user-friendly web interface to add, view, and delete alerts.
- **Background Task Scheduler**: Periodically checks for alert conditions using `APScheduler`.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- A Telegram bot token (create one using [BotFather](https://core.telegram.org/bots#botfather))

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/alertify.git
   cd alertify
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory and add your Telegram bot token:
     ```plaintext
     TELEGRAM_BOT_TOKEN=your-telegram-bot-token
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Web Interface**:
   - Open your browser and go to `http://localhost:5000`.

---

## Configuration

### Environment Variables
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token (required).
- `TELEGRAM_CHAT_ID`: The chat ID where notifications will be sent (optional, defaults to a hardcoded value).

### Customizing Instruments
You can customize the list of financial instruments in `app.py` under the `INSTRUMENT_OPTIONS` dictionary. The categories include:
- **Major Forex Pairs** (e.g., `EURUSD=X`)
- **Minor Forex Pairs** (e.g., `EURGBP=X`)
- **Cryptocurrency Pairs** (e.g., `BTC-USD`)

---

## Usage

### Adding an Alert
1. Go to the web interface (`http://localhost:5000`).
2. Select an instrument from the dropdown menu.
3. Choose the alert type:
   - **Above**: Notify when the price goes above a target price.
   - **Below**: Notify when the price goes below a target price.
   - **Bollinger Bands**: Notify when the price breaks the upper or lower Bollinger Band.
4. Enter the target price (if applicable) and click **Add Alert**.

### Viewing Alerts
- The **Current Alerts** section displays all active alerts.
- Alerts that have been triggered are highlighted.

### Deleting an Alert
- Click the **Delete** button next to an alert to remove it.

### Telegram Notifications
- When an alert is triggered, a notification is sent to the specified Telegram chat ID.

---

## API Endpoints

### Web Interface
- **GET `/`**: Renders the main web interface for adding and managing alerts.
- **POST `/`**: Adds a new alert.

### API
- **GET `/alerts`**: Returns a JSON list of all alerts and their triggered states.
- **DELETE `/delete_alert/<int:alert_id>`**: Deletes an alert with the specified ID.

---

## File Structure

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

---

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Web framework for serving the web interface.
- **yfinance**: Library for fetching real-time and historical price data.
- **APScheduler**: Background task scheduler for checking alerts.
- **Telegram Bot API**: Sends notifications via Telegram.
- **HTML/CSS/JavaScript**: Frontend for the web interface.
- **Select2**: JavaScript library for dropdown menus.

---

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements
- **yfinance**: For providing real-time and historical price data.
- **Flask**: For making it easy to build the web interface.
- **Telegram**: For providing the Bot API for notifications.

---

## Support
If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/your-username/alertify/issues).

---

Enjoy using Alertify! 🚀
