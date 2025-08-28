def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            # Skip when i == j to avoid division by zero
            if i == j:
                continue
            # Check if denominator is zero
            denominator = values[j] - values[i]
            if denominator == 0:
                continue
            ratio = values[i] / denominator
            results.append((i, j, ratio))
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))