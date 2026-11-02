
import tiktoken


def count_tokens(
    text: str,
    model: str = "gpt-4o"
) -> int:

    try:

        encoding = tiktoken.encoding_for_model(
            model
        )

    except KeyError:

        encoding = tiktoken.get_encoding(
            "o200k_base"
        )

    tokens = encoding.encode(text)

    return len(tokens)


def analyze_text(text: str) -> dict:

    return {
        "characters": len(text),
        "words": len(text.split()),
        "tokens": count_tokens(text)
    }
