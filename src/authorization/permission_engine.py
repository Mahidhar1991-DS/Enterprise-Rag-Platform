from src.constants.access_levels import (
    AccessLevel
)


class PermissionEngine:

    def has_access(
        self,
        chunk: dict,
        request
    ) -> bool:

        access_level = chunk.get(
            "access_level",
            AccessLevel.PUBLIC
        )

        if access_level == AccessLevel.PUBLIC:

            return True

        return False