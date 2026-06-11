import flet as ft
from datetime import datetime

def main_page(page: ft.Page):

    page.add(
        ft.TextField(label="Введите имя и нажмите ENTER", on_submit=lambda e: page.add(ft.Text(f"{datetime.now().strftime('%Y:%m:%d - %H:%M:%S')} - Привет!{e.control.value}!")))
    )


ft.run(main_page)