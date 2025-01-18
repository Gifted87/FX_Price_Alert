from telegram_bot import send_telegram_message
alerts = []
alert_id_counter = 1  # To assign unique IDs to alerts

def add_alert(instrument, target_price, alert_type):
    """Adds a new alert to the list of active alerts."""
    global alert_id_counter
    alert = {
        "id": alert_id_counter,
        "instrument": instrument,
        "target_price": float(target_price),
        "alert_type": alert_type,  # "above" or "below"
        "triggered": False
    }
    alerts.append(alert)
    print(f"Alert added: {alert}")
    alert_id_counter += 1

def get_all_alerts():
    """Returns a list of all alerts."""
    return alerts

def delete_alert(alert_id):
    """Deletes an alert with the given ID."""
    global alerts
    alerts = [alert for alert in alerts if alert["id"] != alert_id]
    print(f"Alert with ID {alert_id} deleted.")

def get_active_alerts():
    """Returns a list of all active alerts (not triggered)."""
    return [alert for alert in alerts if not alert["triggered"]]

def check_alerts(current_prices, telegram_bot):
    """
    Checks if any alert conditions are met and sends Telegram notifications.

    Args:
        current_prices (dict): A dictionary of current prices, where keys are instrument symbols
                               and values are their current prices.
        telegram_bot: The telegram_bot module for sending messages.
    """
    for alert in get_active_alerts():
        instrument = alert["instrument"]
        target_price = alert["target_price"]
        alert_type = alert["alert_type"]

        if instrument in current_prices:
            current_price = current_prices[instrument]

            if alert_type == "above" and current_price >= target_price:
                message = f"Alert triggered! {instrument} price ({current_price:.2f}) crossed above {target_price:.2f}"
                send_telegram_message("7575529318", message) # Replace with your actual chat ID
                alert["triggered"] = True
            elif alert_type == "below" and current_price <= target_price:
                message = f"Alert triggered! {instrument} price ({current_price:.2f}) crossed below {target_price:.2f}"
                send_telegram_message("7575529318", message) # Replace with your actual chat ID
                alert["triggered"] = True

if __name__ == '__main__':
    # Example usage
    add_alert("AAPL", 170.0, "above")
    add_alert("BTC-USD", 30000.0, "above")
    add_alert("EURUSD=X", 1.10, "below")

    print("Active Alerts:", get_active_alerts())

    # Example current prices (replace with actual fetched prices)
    current_prices_data = {
        "AAPL": 175.50,
        "BTC-USD": 31000.0,
        "EURUSD=X": 1.09
    }

    # Mock telegram_bot module for testing
    # class MockTelegramBot:
    #     def send_telegram_message(self, chat_id, message):
    #         print(f"[Mock Telegram] Sending to {chat_id}: {message}")

    # mock_telegram_bot = MockTelegramBot()

    check_alerts(current_prices_data)
    print("Active Alerts after check:", get_active_alerts())