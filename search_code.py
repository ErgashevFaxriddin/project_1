import os

search_terms = [
    "new dawn on education in uzbekistan",
    "Assalom ozbekiston mavzusida tadbir ;)"
]

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith((".py", ".html", ".txt", ".md")):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for term in search_terms:
                    if term in content:
                        print(f"Found '{term}' in: {path}")