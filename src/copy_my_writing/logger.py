import logging
import logging.handlers


class AppLogger:
    def __init__(self, log_file="logs/app.log"):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Check if the logger already has handlers to prevent adding multiple handlers
        if not self.logger.handlers:
            file_handler = logging.handlers.RotatingFileHandler(
                log_file, maxBytes=5 * 1024 * 1024, backupCount=3
            )
            file_handler.setLevel(logging.DEBUG)

            file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(file_format)

            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
