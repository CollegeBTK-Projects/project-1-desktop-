def calculate(expression: str) -> str:
    try:
	return str(eval(expression))
    except Exception:
	return "Ошибка"
