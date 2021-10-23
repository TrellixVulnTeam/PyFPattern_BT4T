def blas(name, ndarray):
    'Helper for getting BLAS function, used :func:`scipy.linalg.get_blas_funcs`.\n\n    Parameters\n    ----------\n    name : str\n        Name(s) of BLAS functions without type prefix.\n    ndarray : numpy.ndarray\n        Arrays can be given to determine optimal prefix of BLAS routines.\n\n    Returns\n    -------\n    fortran object\n        Fortran function for needed operation.\n\n    '
    return scipy.linalg.get_blas_funcs((name,), (ndarray,))[0]