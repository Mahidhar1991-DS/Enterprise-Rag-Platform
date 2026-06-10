import uuid

from src.sync.hash_generator import HashGenerator
from src.versioning.version_manager import VersionManager


def main():

    manager = VersionManager()

    document_id = str(uuid.uuid4())

    content_v1 = """
    Leave Policy Version 1
    """

    hash_v1 = HashGenerator.generate(
        content_v1
    )

    manager.create_new_version(
        document_id=document_id,
        file_hash=hash_v1,
        file_size=len(content_v1)
    )

    content_v2 = """
    Leave Policy Version 2 Updated
    """

    hash_v2 = HashGenerator.generate(
        content_v2
    )

    manager.create_new_version(
        document_id=document_id,
        file_hash=hash_v2,
        file_size=len(content_v2)
    )

    print(
        "Versioning test completed."
    )


if __name__ == "__main__":
    main()