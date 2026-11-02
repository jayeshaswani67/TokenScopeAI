
def calculate_cost(
    input_tokens: int,
    output_tokens: int,
    input_price: float,
    output_price: float
) -> dict:

    input_cost = (
        input_tokens / 1_000_000
    ) * input_price

    output_cost = (
        output_tokens / 1_000_000
    ) * output_price

    total_cost = input_cost + output_cost

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": total_cost
    }
