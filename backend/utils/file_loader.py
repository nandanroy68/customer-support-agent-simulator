import os
import io
from typing import Iterable, Tuple
from unstructured.partition.auto import partition

def load_to_text(raw_bytes: bytes, filename: str) -> str:
    elements = partition(file=io.BytesIO(raw_bytes), metadata_filename=filename)
    return "\n".join([str(e) for e in elements])

def load_path_to_texts(root: str) -> Iterable[Tuple[str, str]]:
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith((".pdf", ".txt", ".docx", ".md", ".html", ".htm")):
                fpath = os.path.join(dirpath, fn)
                with open(fpath, "rb") as f:
                    txt = load_to_text(f.read(), filename=fn)
                yield fpath, txt


