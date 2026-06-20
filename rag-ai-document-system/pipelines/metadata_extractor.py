def extract_metadata(file_name, file_path, text):
    return {
        "doc_id": file_name.split(".")[0],
        "file_name": file_name,
        "file_path": file_path,
        "department": infer_department(file_path),
        "classification": "internal",
        "length": len(text)
    }

def infer_department(path):
    if "hr" in path:
        return "HR"
    if "security" in path:
        return "SECURITY"
    return "ENGINEERING"
