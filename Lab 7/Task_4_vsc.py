def compute_ratios(values):
    results =[]
    for i in range(len(values)):
        for j in range(i , len(values)):
            denominator = values[j] - values[i]
            if denominator == 0:
                ratio = None  # or you can use 'float('inf')' or a custom message
            else:
                ratio = values[i] / denominator
            results.append((i,j,ratio))
    return results
nums = [5,10,15,20,25]
print(compute_ratios(nums))