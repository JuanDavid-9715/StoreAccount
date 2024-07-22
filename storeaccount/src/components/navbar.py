import flet as ft


class Navbar(ft.AppBar):
    def __init__(self, page):
        super().__init__()
        self.leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED)
        self.leading_width=100
        self.title=ft.Text(
            f"Cuantas Tienda", 
            font_family="Pacifico", 
            size=32, 
            text_align="start"
        )
        self.center_title=False
        self.toolbar_height=60
        self.bgcolor=ft.colors.PURPLE_400
        self.actions=[
            ft.TextButton(text="home", on_click=lambda e:page.go("/")),
            ft.TextButton(text="diario", on_click=lambda e:page.go("/diary")),
            ft.TextButton(text="mensual", on_click=lambda e:page.go("/monthly")),
            ft.TextButton(text="anual", on_click=lambda e:page.go("/yearly")),
        ]