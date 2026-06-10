class ChangeDetector:

    @staticmethod
    def has_changed(
        old_hash: str,
        new_hash: str
    ) -> bool:

        return old_hash != new_hash