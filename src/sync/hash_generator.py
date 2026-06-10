import hashlib


class HashGenerator:

    @staticmethod
    def generate(content: str) -> str:
        """Generates a SHA-256 hash for the given content."""
        return hashlib.sha256(
            content.encode("utf-8")
        ).hexdigest()