# app1.py
# Simulates one part of the system that logs data using the Singleton logger

from logger_singleton import LoggerSingleton

def process_data():
    # Get the singleton logger instance
    logger = LoggerSingleton()
    # Log a message
    logger.log("App1 is processing data...")


# app2.py
# Simulates another part of the system that also uses the Singleton logger


def save_results():
    # Get the singleton logger instance
    logger = LoggerSingleton()
    # Log a different message
    logger.log("App2 is saving results...")


def monitor_performance():
    # Get the singleton logger instance
    logger = LoggerSingleton()
    # Log a performance monitoring message
    logger.log("Monitoring system performance...")
