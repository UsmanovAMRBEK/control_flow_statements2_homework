def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    max=a
    if b>max:
        max=b
    elif c>max:
        max=c
    return max