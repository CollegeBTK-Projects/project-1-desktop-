def calculate(expr: str) -> str:
    try:
        return str(eval(expr))
    except:
        return "Ошибка"
