def clean_data_with_split(data):
    clean = []
    for i in data:
        new = i.strip().split(",")
        clean.append(new)
    return clean


def clean_data_without_split(data):
    clean = []
    for i in data:
        new = i.strip()
        clean.append(new)
    return clean