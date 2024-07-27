import flet as ft

from src.components.form.diary import DiaryFrom
from src.components.lists.diary import DiaryList

class DiaryView(ft.View):
    def __init__(self, db, page):
        super().__init__()
        self.__db=db
        self.__page=page
        self.route="diary"
        self.scroll=ft.ScrollMode.ADAPTIVE
        self.appbar=page.appbar
        self.controls=[
            ft.Container(
                DiaryFrom(self.__db, self.__page),
                padding=ft.padding.only(left=20, top=20, right=20),
            ),
            ft.Container(
                ft.ResponsiveRow([
                    DiaryList(self.__db),
                ]),
                padding=ft.padding.symmetric(horizontal=20),
            ),
        ]