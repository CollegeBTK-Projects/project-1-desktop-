import flet as ft 


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Calculator"
    page.window.width = 350
    page.window.height = 550
    page.padding = 10
    page.window.alignment = ft.alignment.center
    page.window.resizable = False

    light_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
        primary=ft.colors.BLUE,
        on_primary=ft.colors.WHITE,
        surface=ft.colors.WHITE,
        on_surface=ft.colors.BLACK,
        background=ft.colors.WHITE,
        on_background=ft.colors.BLACK,
        inverse_surface=ft.colors.BLACK,
        inverse_primary=ft.colors.BLUE,
        shadow=ft.colors.BLACK12
      )
    )
    dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
        primary=ft.colors.DEEP_PURPLE_200,
        on_primary=ft.colors.BLACK,
        surface="#363837",
        on_surface=ft.colors.WHITE,
        background="#222222",
        on_background=ft.colors.WHITE,
        inverse_surface=ft.colors.WHITE,
        inverse_primary=ft.colors.DEEP_PURPLE_200,
        shadow=ft.colors.WHITE30
      )
    )
    page.theme = light_theme
    page.dark_theme = dark_theme
    page.theme_mode = ft.ThemeMode.LIGHT 

    all_values = ""
    
    page.vertical_alignment = ft.MainAxisAlignment.END

    def update_styles(theme="light"):
        if theme == "dark":
            result_text.color = "white"
            display.bgcolor = "#363837"
            number_style['bgcolor'] = "#4d4d4d"
            number_style['color'] = "white"
            operator_style['bgcolor'] = "#6b4444"
            operator_style['color'] = "white"
            for row in buttons:
                for btn in row.controls:
                    if btn.text == "Тема":
                        btn.bgcolor = "#666"
                        btn.color = "white"
                    elif btn.text in ("C", "%", "/", "*", "-", "+", "=", ".", "R"):
                        btn.bgcolor = operator_style['bgcolor']
                        btn.color = operator_style['color']
                    else:
                        btn.bgcolor = number_style['bgcolor']
                        btn.color = number_style['color']
        else:
            result_text.color = "black"
            display.bgcolor = "#eeeeee"
            number_style['bgcolor'] = "#ddd"
            number_style['color'] = "black"
            operator_style['bgcolor'] = "#ff7043"
            operator_style['color'] = "white"
            for row in buttons:
                for btn in row.controls:
                    if btn.text == "Тема":
                        btn.bgcolor = "#bbb"
                        btn.color = "black"
                    elif btn.text in ("C", "%", "/", "*", "-", "+", "=", ".", "R"):
                        btn.bgcolor = operator_style['bgcolor']
                        btn.color = operator_style['color']
                    else:
                        btn.bgcolor = number_style['bgcolor']
                        btn.color = number_style['color']
        page.update()

    def pushvalue(e): #добавляет значения в конт
        nonlocal all_values
        all_values += str(e.control.text)
        result_text.value = all_values
        page.update()

    def clearvalue(e): #убирает значения "C" в конт
        nonlocal all_values
        all_values = ""
        result_text.value = "0"
        page.update()

    def remc(e): # -1 "R"
        nonlocal all_values
        all_values = all_values[:-1]
        result_text.value = all_values if all_values else "0"
        page.update()

    def calculate(e): #считывает
        nonlocal all_values
        try:
            result_text.value = str(eval(all_values))
            all_values = result_text.value
        except:
            result_text.value = "Error"
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
    
    
    result_text = ft.Text(value='0', size=28, color='white', text_align='right') 
     
    theme_button = ft.ElevatedButton(text="тема", on_click=toggle_theme, bgcolor="#444", color="White", width=80)
    cont_safe = ft.Container(
	content=ft.Row([theme_button], alignment=ft.MainAxisAlignment.CENTER),
	padding=ft.padding.all(10),
	bgcolor=None,
	expand=0,
	height=50)
	 
    display = ft.Container( #display = область за result_text
        content=result_text,
        bgcolor='#eeeeee',
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right
        )
    
    number_style = {
        'height': 60,
        'bgcolor': "#4d4d4d",
        'color': "white",
        'expand': 1,
    }
    operator_style = {
        'height': 60,
        'bgcolor': "#6b4444",
        'color': "white",
        'expand': 1,
    }
    
    button_grid = [
        [
            ("C", operator_style, clearvalue),
            ("%", operator_style, pushvalue),
            ("/", operator_style, pushvalue),
            ("*", operator_style, pushvalue),
        ],
        [
            ("7", number_style, pushvalue),
            ("8", number_style, pushvalue),
            ("9", number_style, pushvalue),
            ("-", operator_style, pushvalue),
        ],
        [
            ("4", number_style, pushvalue),
            ("5", number_style, pushvalue),
            ("6", number_style, pushvalue),
            ("+", operator_style, pushvalue)
        ],
        [
            ("1", number_style, pushvalue),
            ("2", number_style, pushvalue),
            ("3", number_style, pushvalue),
            ("=", operator_style, calculate),
        ],
        [
            ("0", {**number_style, 'expand': 2}, pushvalue),
            (".", operator_style, pushvalue),
            ("R", operator_style, remc),
        ]
    ]
    
    buttons = []
    for row in button_grid:
        row_controls = []
        for text, style, handler in row:
            btn = ft.ElevatedButton(
                text=text,
                on_click = handler,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0
                    )
                )  
            
            row_controls.append(btn)
        buttons.append(ft.Row(row_controls, spacing=5))
               
    page.add(
        
        ft.Column(
            [ 
             cont_safe, #конопка перекючения темы
             display,   
             ft.Column(buttons, spacing=5)
             
            ],
            spacing=15,
            expand=True
        )
        
    )
    update_styles(theme="light")
    page.update()
ft.app(target=main)
