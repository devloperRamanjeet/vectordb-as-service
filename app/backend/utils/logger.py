import logging
import os

def get_logger(name: str = "chromadb-backend") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers in case of re-imports
    if not logger.handlers:
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

        # Optional file logging (disabled by default)
        if os.getenv("ENABLE_FILE_LOGGING") == "1":
            file_handler = logging.FileHandler("backend.log")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger
