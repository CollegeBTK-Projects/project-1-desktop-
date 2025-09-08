import flet as ft 


def main(page: ft.Page):
    #Add theme styles (light/dark) !!!
    page.title = "Calculator"
    page.window.width = 350
    page.window.height = 550
    page.padding = 10
    page.window.alignment = ft.alignment.center
    page.window.resizable = False 

    all_values = ""
    
    page.vertical_alignment = ft.MainAxisAlignment.END

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
        result_text.value = all_values
        page.update()
    def calculate(e): #считывает
        nonlocal all_values
        try:
            result_text.value = str(eval(all_values))
            all_value = result_text.value
        except:
            result_text.value = "Error"
            all_values = ""
        page.update()
    
    
    result_text = ft.Text(value='0', size=28, color='white', text_align='right') 
    
    cont_safe = ft.Container(expand=1) #Ильюха, этот контейнер и создает пустое место сверху, можешь с ним работатью.
    
    display = ft.Container( #display = область за result_text
        content=result_text,
        bgcolor='#363837',
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
             cont_safe, #Контейнер отвечат за свободное место сверху.
             display,   
             ft.Column(buttons, spacing=5)
             
            ],
            spacing=15,
            expand=True
        )
        
    )
    
    page.update()
ft.app(target=main)