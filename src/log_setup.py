import logging

def setup_logging(log_level="DEBUG", log_file="app.log"):
    """Set up logging for the application"""
    # Set up logger
    logger = logging.getLogger()
    logger.setLevel(log_level.upper())

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level.upper())
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
