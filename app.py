from flask import Flask, render_template, request, redirect, url_for, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from alerts import add_alert, get_all_alerts, delete_alert, get_active_alerts, check_alerts
from price_fetcher import PriceFetcher
from telegram_bot import send_telegram_message

template_dir = r'C:\Users\USER\Downloads\price_alert_bot\templates'

# Initialize Flask app with the custom template directory
app = Flask(__name__, template_folder=template_dir)

INSTRUMENT_OPTIONS = {
     "major_pairs": [
        "EURUSD=X", "USDJPY=X", "GBPUSD=X", "AUDUSD=X", "USDCAD=X", "USDCHF=X", "NZDUSD=X"
    ],
    "minor_pairs": [
        "EURGBP=X", "EURJPY=X", "EURCHF=X", "EURAUD=X", "EURCAD=X", "EURNZD=X", "GBPJPY=X",
        "GBPCHF=X", "GBPAUD=X", "GBPCAD=X", "GBPNZD=X", "AUDJPY=X", "AUDCHF=X", "AUDCAD=X",
        "AUDNZD=X", "CADJPY=X", "CADCHF=X", "CHFJPY=X", "NZDJPY=X", "NZDCHF=X", "NZDCAD=X", "GC=F", "SI=F", "PL=F", "PA=F", "HG=F", "CL=F", "BZ=F", "NG=F", "HO=F", "RB=F", "ZC=F", "ZW=F", "ZS=F", "KC=F", "CT=F", "OJ=F", "SB=F"
    ],
    "crypto_pairs": [
        "BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "ADA-USD", "SOL-USD", "DOGE-USD",
        "DOT-USD", "AVAX-USD", "SHIB-USD", "MATIC-USD", "LTC-USD", "UNI-USD", "LINK-USD",
        "BCH-USD", "ATOM-USD", "XLM-USD", "ETC-USD", "ALGO-USD", "XMR-USD"
    ]
}

price_fetcher = PriceFetcher()
alerts_triggered_state = {} # To store whether an alert has triggered and to notify front-end


def fetch_prices_and_check_alerts():
    print("Checking Alerts")
    """Fetches current prices for all instruments in active alerts and checks for triggers."""
    global alerts_triggered_state
    active_alerts = get_active_alerts()
    if not active_alerts:
        print("No active alerts to check.")
        return

    current_prices = {}
    for alert in active_alerts:
        instrument = alert["instrument"]
        price = price_fetcher.get_current_price(instrument)
        if price is not None:
            current_prices[instrument] = price

    check_alerts(current_prices, send_telegram_message) # Pass the function directly
    alerts_triggered_state = {alert["id"]: alert["triggered"] for alert in get_all_alerts()}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        instrument = request.form['instrument']
        target_price = request.form['target_price']
        alert_type = request.form['alert_type']
        add_alert(instrument, target_price, alert_type)
        return redirect(url_for('index'))
    alerts = get_all_alerts()
    return render_template('add_alert.html', **INSTRUMENT_OPTIONS, alerts=alerts, alerts_triggered_state=alerts_triggered_state)

@app.route('/delete_alert/<int:alert_id>', methods=['DELETE'])
def delete_alert_route(alert_id):
    delete_alert(alert_id)
    return jsonify({'success': True, 'message': f'Alert with ID {alert_id} deleted'})

@app.route('/alerts')
def get_alerts():
    """Endpoint to fetch the current list of alerts as JSON."""
    global alerts_triggered_state
    alerts = get_all_alerts()
    return jsonify(
        {"alerts": alerts,
         "alerts_triggered_state": alerts_triggered_state
         }
    )
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_prices_and_check_alerts, 'interval', minutes=1)
    scheduler.start()

    app.run(debug=True, use_reloader=False, host='0.0.0.0')