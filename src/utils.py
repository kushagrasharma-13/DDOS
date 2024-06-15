# src/utils.py
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

logger = setup_logging()

def send_alert(message):
    # Function to send alerts (e.g., via email or SMS)
    logger.info(f"Alert: {message}")