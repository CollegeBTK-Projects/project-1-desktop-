# Калькулятор
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Flet?style=flat&color=orange)
![Flet](https://img.shields.io/badge/Flet-0.28.3-orange?style=flat&logoColor=orange)
![GitHub License](https://img.shields.io/github/license/CollegeBTK-Projects/project-1-desktop-)
![GitHub last commit](https://img.shields.io/github/last-commit/CollegeBTK-Projects/project-1-desktop-?style=flat)
![GitHub Repo stars](https://img.shields.io/github/stars/CollegeBTK-Projects/project-1-desktop-?style=flat)

Функциональный калькулятор с современным дизайном.
Создан для обеспечения простоты и удобства в повседневных вычислениях.

## Содержание
- [Установка](#установка)
- [Функционал](#функционал)
- [Технологии](#технологии)

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/CollegeBTK-Projects/project-1-desktop-.git
   cd project-1-desktop-
   ```
2. Создайте и активируйте виртуальное окружение:
   ```sh
   # Для Windows
   python -m venv venv
   venv\Scripts\activate

   # Для macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```
4. Запустите приложение:
   ```sh
   flet run src/main.py
   ```

## Функционал
- Сложение, вычитание, умножение, деление
- Очистка поля ввода
- Удаление последнего символа

## Технологии
- [Python](https://www.python.org/)
- [Flet](https://flet.dev/)