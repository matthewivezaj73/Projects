import docx

def extract_docx_text(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])
