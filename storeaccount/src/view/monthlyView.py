import flet as ft

# from src.components.form.home import HomeFrom
from src.components.paginator import Paginator

class MonthlyView(ft.View):
    def __init__(self, db, page):
        super().__init__()
        self.__db=db
        self.__page=page
        self.route="monthly"
        self.scroll=ft.ScrollMode.ADAPTIVE
        self.appbar=page.appbar
        self.controls=[
            ft.Container(
                Paginator(self.__db, self.__page, self.route),
                padding=ft.padding.symmetric(horizontal=20),
            )
        ]