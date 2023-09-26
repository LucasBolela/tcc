def file_type_validate(name: str) -> str:
    """
    Verify the extension of files by his name or path
    - parameters:
        - name: file complete name or the online path
    - return: file type -> str
    """
    if name.lower().endswith(".pdf"):
        return "pdf"
    elif name.lower().endswith((".doc", ".docx")):
        return "word"
    else:
        return ""
