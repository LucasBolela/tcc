import io
import requests
from pypdf import PdfReader
import docx2txt

from eagle.helpers.validators.reader.file_type_validate import file_type_validate


def read_document_content(isFile: bool, path: str, file) -> str:
    """
    Read an online document and return the content.
    Parameters:
        path: link from web to document
    Returns: string with the content
    """

    if isFile:
        f = file
        typeFile = file_type_validate(f.name)
    else:
        typeFile = file_type_validate(path)
        if typeFile == "":
            typeFile = "word"
        r = requests.get(path, stream=True)
        f = io.BytesIO(r.content)

    text = ""
    if typeFile == "pdf":
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    elif typeFile == "word":
        text = docx2txt.process(f)

    return text
