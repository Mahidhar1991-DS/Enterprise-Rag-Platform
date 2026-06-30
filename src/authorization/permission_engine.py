class PermissionEngine:

    def has_access(
        self,
        chunk: dict,
        request
    ) -> bool:

        access_level = chunk.get(
            "access_level",
            "PUBLIC"
        )

        if access_level == "PUBLIC":

            return True

        return False