import flet as ft

from src.components.form.diary import DiaryFrom
from src.components.paginator import Paginator

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
                Paginator(self.__db, self.__page, self.route),
                padding=ft.padding.symmetric(horizontal=20),
            )
        ]