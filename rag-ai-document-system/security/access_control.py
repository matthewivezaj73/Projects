def filter_by_role(docs, user_role):
    if user_role != "HR":
        return [d for d in docs if "HR" not in d["file_path"]]

    return docs
