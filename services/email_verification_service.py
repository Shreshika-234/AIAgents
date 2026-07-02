from email_validator import validate_email, EmailNotValidError


class VerificationService:

    def verify_email(self, email):

        try:
            validate_email(email)

            return {
                "verified": True,
                "status": "valid",
                "score": 100
            }

        except EmailNotValidError:

            return {
                "verified": False,
                "status": "invalid",
                "score": 0
            }