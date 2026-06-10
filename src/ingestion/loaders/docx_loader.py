from docx import Document


class DOCXLoader:

    @staticmethod
    def load(file_path: str) -> str:

        doc = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )