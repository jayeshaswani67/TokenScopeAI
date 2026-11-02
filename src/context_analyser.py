
def analyze_context(
    input_tokens: int,
    output_tokens: int,
    context_window: int
) -> dict:
    """
    Analyze token usage against a model's context window.

    Returns token usage, remaining capacity,
    utilization percentage, and status.
    """

    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("Token counts cannot be negative.")

    if context_window <= 0:
        raise ValueError("Context window must be positive.")

    total_tokens = input_tokens + output_tokens

    remaining_tokens = max(
        context_window - total_tokens,
        0
    )

    usage_percentage = (
        total_tokens / context_window
    ) * 100

    exceeds_limit = total_tokens > context_window

    if exceeds_limit:
        status = "Exceeded"
    elif usage_percentage >= 90:
        status = "Critical"
    elif usage_percentage >= 70:
        status = "High"
    else:
        status = "Normal"

    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "context_window": context_window,
        "remaining_tokens": remaining_tokens,
        "usage_percentage": round(usage_percentage, 2),
        "exceeds_limit": exceeds_limit,
        "status": status
    }
