def verificar_edad(valor):

    """
    Verifica si el valor proporcionado es un numero entero positivo mayor o igual a 12.

    Parametros:
    - valor: Valor a verificar.

    Lanza:
    - ValueError: Si el valor no es un numero entero positivo mayor o igual a 12.

    """

    if not valor.isdigit() or int(valor) < 12:
        raise ValueError(f"'{valor}' no es un valor valido o es menor a 12.")