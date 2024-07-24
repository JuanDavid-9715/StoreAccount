import flet as ft

#from src.components.form.home import HomeFrom
from src.components.lists.year import YearList

class YearView(ft.View):
    def __init__(self, db, page):
        super().__init__()
        self.__db=db
        self.__page=page
        self.route="year"
        self.scroll=ft.ScrollMode.ADAPTIVE
        self.appbar=page.appbar
        self.controls=[
            ft.Container(
                ft.ResponsiveRow([
                    YearList(self.__db),
                ]),
                padding=ft.padding.symmetric(horizontal=20),
            ),
        ]