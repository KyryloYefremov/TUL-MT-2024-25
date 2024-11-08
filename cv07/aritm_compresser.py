from collections import Counter


def code_arithmetically(data: list[str]) -> tuple[float, dict[str: tuple[float ,float]]]:
    # Init
    frequency = Counter(data)
    data_len = len(data)

    # Count probability for every symbol
    symbols_probs = {symbol: freq/data_len for symbol, freq in frequency.items()}
    # print(symbols_probs)

    # Count cumulative probs and set probability interval for every symbol
    probs_intervals = dict()
    low_boundary = 0
    for symbol, prob in symbols_probs.items():
        high_boundary = low_boundary + prob
        probs_intervals[symbol] = (low_boundary, high_boundary)
        low_boundary = high_boundary
    # print(probs_intervals)

    # Build new interval from known symbols' intervals IZ = [ZL, HL)
    interval = (0, 1)  # I = [L, H)
    for symbol in data:
        # Count LB and HB of new interval
        low_boundary = interval[0] + probs_intervals[symbol][0] * (interval[1] - interval[0])   # NL = L + ZL * (H - L)
        high_boundary = interval[0] + probs_intervals[symbol][1] * (interval[1] - interval[0])  # NH = L + ZH * (H - L)
        interval = (low_boundary, high_boundary)  # IN = (NL, NH)

    # Find the decimal place in float nums to which these numbers are the same
    # Copmute their difference, convert result to exp. form (ex. 2.642e-05) and extract the degree of 'ten'
    float_position = int(str(interval[1]-interval[0])[-2:])
    shortest_number = round(interval[0], float_position)

    print(f"RESULT INTERVAL: {interval}")
    
    return shortest_number, probs_intervals


def decode_arithmetically(coding_result: float, probs_intervals: dict[tuple[float, float]], data_len: int) -> list[str]:
    # Init
    decoded_data = []

    interval = (0, 1)  # I = [L, H)
    # for symbol, (low_boundary, high_boundary) in probs_intervals.items():
    for _ in range(data_len):
        L, H = interval
        code = (coding_result - L) / (H - L)  # K = (C - L) / (H - L)

        # Find corresponding symbol as ZL <= K < ZH
        for symbol, (low_boundary, high_boundary) in probs_intervals.items(): 
            if low_boundary <= code < high_boundary:
                decoded_symbol = symbol
        decoded_data.append(decoded_symbol)
        
        # Compute new intevarl boundaries
        low_boundary = L + probability_intervals[decoded_symbol][0] * (H - L)   # L + ZL * (H - L)
        high_boundary = L + probability_intervals[decoded_symbol][1] * (H - L)  # L + ZH * (H - L)
        interval = [low_boundary, high_boundary]

    return decoded_data


if __name__ == "__main__":
    """
    Print interval.
    Print the shortest num that was chosen.
    """
    data = 'CBAABCADAC'
    print(f"Original data: {data}\n")
    coding_result, probability_intervals = code_arithmetically(data)
    print(f"Result of coding: {coding_result}")
    print(f"Probs intervals: {probability_intervals}")
    decoded_data = decode_arithmetically(coding_result, probability_intervals, len(data))
    print(f"\nDecoded data: {''.join(decoded_data)}")

