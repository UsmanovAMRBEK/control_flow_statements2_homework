from operator import index


def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.  # 57643
    """
    max=n//10000
    index=5
    if n//1000%10>max:
        max=n//1000%10
        index=4
    if n//100%10>max:
        max=n//100%10
        index=3
    if n//10%10>max:
        max=n//10%10
        index=2
    if n%10>max:
        max=n%10
        index=1
    return index