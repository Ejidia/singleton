# app2.py
# Simulates another part of the system that also uses the Singleton logger

from logger_singleton import LoggerSingleton

def save_results():
    # Get the singleton logger instance
    logger = LoggerSingleton()
    # Log a different message
    logger.log("App2 is saving results...")
