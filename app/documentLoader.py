from pathlib import Path

def load_document(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    return path.read_text(encoding='utf-8')

def split_into_chunks(text: str, chunk_size: int = 200, overlap: int = 40) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Overlap must be a non-negative integer less than chunk size.")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks