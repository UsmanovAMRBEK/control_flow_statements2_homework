def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    max=n%10
    n=n//10
    if n%10>max:
        max=n%10
        index=1
    n=n//10
    if n%10>max:
        max=n%10
        index=2
    n=n//10
    if n%10>max:
        max=n%10
        index=3
    n=n//10
    if n%10>max:
        max=n%10
        index=4
    n=n//10
    if n%10>max:
        max=n%10
        index=5
    
    return index