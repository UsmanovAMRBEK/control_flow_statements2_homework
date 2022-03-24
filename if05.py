def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    max=n%10
    n=n//10
    if n%10>max:
        max=n%10
    n=n//10
    if n%10>max:
        max=n%10
    n=n//10
    if n%10>max:
        max=n%10
    n=n//10
    if n%10>max:
        max=n%10
    return max