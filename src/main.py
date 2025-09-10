import flet as ft

def main(page: ft.Page):
    page.title = "calculator"
    page.window.width = 350
    page.window.height = 550
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.window.resizable = False

    light_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE,
            on_primary=ft.Colors.WHITE,
            surface=ft.Colors.WHITE,
            on_surface=ft.Colors.BLACK,
            background=ft.Colors.WHITE,
            on_background=ft.Colors.BLACK,
            inverse_surface=ft.Colors.BLACK,
            inverse_primary=ft.Colors.BLUE,
            shadow=ft.Colors.BLACK12,
        )
    )

    dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.DEEP_PURPLE_200,
            on_primary=ft.Colors.BLACK,
            surface="#363837",
            on_surface=ft.Colors.WHITE,
            background="#222222",
            on_background=ft.Colors.WHITE,
            inverse_surface=ft.Colors.WHITE,
            inverse_primary=ft.Colors.DEEP_PURPLE_200,
            shadow=ft.Colors.WHITE30,
        )
    )

    page.theme = light_theme
    page.dark_theme = dark_theme
    page.theme_mode = ft.ThemeMode.LIGHT

    all_values = ""

    result_text = ft.Text(value="0", size=28, color="black", text_align=ft.TextAlign.RIGHT)

    display = ft.Container(
        content=result_text,
        bgcolor="#eeeeee",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right,
    )

    number_style = {
        "height": 60,
        "bgcolor": "#ddd",
        "color": "black",
        "expand": 1,
    }
    operator_style = {
        "height": 60,
        "bgcolor": "#ff7043",
        "color": "white",
        "expand": 1,
    }

    def update_styles(theme="light"):
        if theme == "dark":
            result_text.color = "white"
            display.bgcolor = "#363837"
            number_style["bgcolor"] = "#4d4d4d"
            number_style["color"] = "white"
            operator_style["bgcolor"] = "#6b4444"
            operator_style["color"] = "white"
            for row in buttons:
                for btn in row.controls:
                    if btn.text.lower() == "тема":
                        btn.bgcolor = "#666"
                        btn.color = "white"
                    elif btn.text in ("C", "%", "/", "*", "-", "+", "=", ".", "R"):
                        btn.bgcolor = operator_style["bgcolor"]
                        btn.color = operator_style["color"]
                    else:
                        btn.bgcolor = number_style["bgcolor"]
                        btn.color = number_style["color"]
                    btn.update()
        else:
            result_text.color = "black"
            display.bgcolor = "#eeeeee"
            number_style["bgcolor"] = "#ddd"
            number_style["color"] = "black"
            operator_style["bgcolor"] = "#ff7043"
            operator_style["color"] = "white"
            for row in buttons:
                for btn in row.controls:
                    if btn.text.lower() == "тема":
                        btn.bgcolor = "#bbb"
                        btn.color = "black"
                    elif btn.text in ("C", "%", "/", "*", "-", "+", "=", ".", "R"):
                        btn.bgcolor = operator_style["bgcolor"]
                        btn.color = operator_style["color"]
                    else:
                        btn.bgcolor = number_style["bgcolor"]
                        btn.color = number_style["color"]
                    btn.update()
        page.update()

    def push_value(e):
        nonlocal all_values
        all_values += str(e.control.text)
        result_text.value = all_values
        page.update()

    def clear_value(e):
        nonlocal all_values
        all_values = ""
        result_text.value = "0"
        page.update()

    def remove_char(e):
        nonlocal all_values
        all_values = all_values[:-1]
        result_text.value = all_values if all_values else "0"
        page.update()

    def calculate(e):
        nonlocal all_values
        try:
            result_text.value = str(eval(all_values))
            all_values = result_text.value
        except:
            result_text.value = "Ошибка"
            all_values = ""
        page.update()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            update_styles(theme="dark")
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            update_styles(theme="light")
        page.update()

    theme_button = ft.ElevatedButton(text="тема", on_click=toggle_theme, bgcolor="#bbb", color="black", width=80)

    button_grid = [
        [
            ("C", operator_style, clear_value),
            ("%", operator_style, push_value),
            ("/", operator_style, push_value),
            ("*", operator_style, push_value),
        ],
        [
            ("7", number_style, push_value),
            ("8", number_style, push_value),
            ("9", number_style, push_value),
            ("-", operator_style, push_value),
        ],
        [
            ("4", number_style, push_value),
            ("5", number_style, push_value),
            ("6", number_style, push_value),
            ("+", operator_style, push_value),
        ],
        [
            ("1", number_style, push_value),
            ("2", number_style, push_value),
            ("3", number_style, push_value),
            ("=", operator_style, calculate),
        ],
        [
            ("0", {**number_style, "expand": 2}, push_value),
            (".", operator_style, push_value),
            ("R", operator_style, remove_char),
        ],
    ]

    buttons = []
    for row in button_grid:
        row_controls = []
        for text, style, handler in row:
            btn = ft.ElevatedButton(
                text=text,
                on_click=handler,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0,
                ),
            )
            row_controls.append(btn)
        buttons.append(ft.Row(row_controls, spacing=5))

    page.add(
        ft.Column(
            [
                ft.Container(content=ft.Row([theme_button], alignment=ft.MainAxisAlignment.CENTER), padding=ft.padding.all(10), height=50),
                display,
                ft.Column(buttons, spacing=5),
            ],
            spacing=15,
            expand=True,
        )
    )

    update_styles(theme="light")
    page.update()

ft.app(target=main)
