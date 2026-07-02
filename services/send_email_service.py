from utils.logger import logger


class EmailService:

    def send_email(self,recipient,subject,body):

        logger.info("=" * 60)
        logger.info(f"To      : {recipient}")
        logger.info(f"Subject : {subject}")
        logger.info("\n%s", body)
        logger.info("=" * 60)

        return True