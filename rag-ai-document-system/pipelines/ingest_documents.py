from utils.pdf_loader import extract_pdf_text
from utils.docx_loader import extract_docx_text
from utils.text_cleaner import clean_text

cleaned_text = clean_text(text

)import os

def ingest_documents(folder_path="documents/"):
    docs = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)

            if file.endswith(".pdf"):
                text = extract_pdf_text(full_path)

            elif file.endswith(".docx"):
                text = extract_docx_text(full_path)

            docs.append({
                "file_name": file,
                "file_path": full_path,
                "text": text
            })

    return docs
