from air_control.logger import get_logger
from air_control.service import Service

SERVICE_NAME = "air_control"
logger = get_logger(SERVICE_NAME)

if __name__ == "__main__":
    logger.info(f"Starting Service {SERVICE_NAME}")

    s = Service(SERVICE_NAME, logger)
    s.start()
