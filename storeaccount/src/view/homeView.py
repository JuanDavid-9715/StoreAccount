import flet as ft

from src.components.homeList import HomeList

class HomeView(ft.View):
    def __init__(self, db, page):
        super().__init__()
        self.__db=db
        self.route="/"
        self.scroll=ft.ScrollMode.ADAPTIVE
        self.appbar=page.appbar
        self.controls=[
            ft.Container(
                HomeList(self.__db),
                padding=ft.padding.symmetric(horizontal=20),
            ),
        ]