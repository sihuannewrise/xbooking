from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"

def read_doc(filename: str) -> str:
    return (DOCS_DIR / filename).read_text(encoding="utf-8")

XBOOKING_DESC = read_doc("xbooking.md")
