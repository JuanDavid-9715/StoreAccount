import flet as ft

# from src.components.form.home import HomeFrom
from src.components.lists.monthly import MonthlyList

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
                ft.ResponsiveRow([
                    MonthlyList(self.__db),
                ]),
                padding=ft.padding.symmetric(horizontal=20),
            ),
        ]