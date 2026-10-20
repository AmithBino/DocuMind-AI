from app.documentLoader import load_document

def split_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Splits the input text into chunks of specified size with optional overlap.

    Args:
        text (str): The input text to be split.
        chunk_size (int): The size of each chunk. Default is 500 characters.
        overlap (int): The number of overlapping characters between chunks. Default is 50 characters.

    Returns:
        list[str]: A list of text chunks.
    """
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer.")

    if overlap < 0 :
        raise ValueError("Overlap must be a non-negative integer.")

    if overlap >= chunk_size:
        raise ValueError("Overlap must be a smaller than chunk size.")

    words = text.split()
    chunks = []

    step = chunk_size - overlap

    for start in range(0, len(words), step):
        chunk_words = words[start:start + chunk_size]
        chunks.append(" ".join(chunk_words))

        if start + chunk_size >= len(words):
            break

    return chunks


def main():
    file_path = "documents/sample.txt"

    # Load the document using our existing loader
    text = load_document(file_path)

    # Split the loaded text into chunks
    chunks = split_text(text, chunk_size=100, overlap=20)

    print(f"Total chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {index} ---")
        print(chunk)


if __name__ == "__main__":
    main()