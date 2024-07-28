import flet as ft

from src.components.form.home import HomeFrom
from src.components.table.home import HomeTable

class HomeView(ft.View):
    def __init__(self, db, page):
        super().__init__()
        self.__db=db
        self.__page=page
        self.route="/"
        self.scroll=ft.ScrollMode.ADAPTIVE
        self.appbar=page.appbar
        self.controls=[
            ft.Container(
                HomeFrom(self.__db, self.__page),
                padding=ft.padding.symmetric(vertical=30, horizontal=20),
            ),
            ft.Container(
                HomeTable(self.__db),
                padding=ft.padding.symmetric(horizontal=20),
            ),
        ]