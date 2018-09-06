def minha_funcao(a, b):
    """
    >>> minha_funcao(1, 2)
    4
    """
    return a + b 

if __name__ == '__main__':
    import doctest
    doctest.testmod()