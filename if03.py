def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a>c:
        if b>c:
            return b
        else:
            return c
    elif b>a and b>c:
        if a>c:
            return a
        else:
            return c
    else:
        if a>b:
            return a
        else:
            return b