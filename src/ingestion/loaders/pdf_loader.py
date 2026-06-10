from pypdf import PdfReader


class PDFLoader:

    @staticmethod
    def load(file_path: str) -> str:

        reader = PdfReader(file_path)

        content = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                content.append(text)

        return "\n".join(content)