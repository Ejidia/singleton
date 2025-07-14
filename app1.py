# app1.py
# Simulates one part of the system that logs data using the Singleton logger

from logger_singleton import LoggerSingleton

def process_data():
    # Get the singleton logger instance
    logger = LoggerSingleton()
    # Log a message
    logger.log("App1 is processing data...")
