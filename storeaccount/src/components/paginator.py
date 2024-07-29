import flet as ft

from src.components.tables.diary import DiaryTable
from src.components.tables.monthly import MonthlyTable
from src.components.tables.yearly import YearTable


class Paginator(ft.Column):
    def __init__(self, db, page, route):
        super().__init__()
        self.__db=db
        self.__page=page
        self.route=route
        self.length=self.__find_length(self.route)
        self.paginator_init=0
        self.paginator_step=10
        self.responsiveRow=ft.ResponsiveRow()
        self.paginator=self.update_paginator()
        self.button_size=30
        self.first_button=ft.IconButton(
            icon=ft.icons.KEYBOARD_DOUBLE_ARROW_LEFT_ROUNDED,
            icon_color=ft.colors.WHITE12,
            icon_size=self.button_size,
            on_click=self.first_click,
        )
        self.previous_button=ft.IconButton(
            icon=ft.icons.KEYBOARD_ARROW_LEFT_ROUNDED,
            icon_color=ft.colors.WHITE12,
            icon_size=self.button_size,
            on_click=self.previous_click,
        )
        self.next_button=ft.IconButton(
            icon=ft.icons.KEYBOARD_ARROW_RIGHT_ROUNDED,
            icon_color=ft.colors.WHITE12,
            icon_size=self.button_size,
            on_click=self.next_click,
        )
        self.last_button=ft.IconButton(
            icon=ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED,
            icon_color=ft.colors.WHITE12,
            icon_size=self.button_size,
            on_click=self.last_click,
        )
        self.controls=[
            ft.Container(
                self.responsiveRow,
                padding=ft.padding.symmetric(horizontal=20),
            ),
            ft.Container(
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.first_button,
                        self.previous_button,
                        self.next_button,
                        self.last_button
                    ]
                ),
                padding=ft.padding.symmetric(horizontal=20),
            )
        ]

    def first_click(self, e):
        self.paginator_init = 0
        self.update_paginator()

    def previous_click(self, e):
        if self.paginator_init > 10:
            self.paginator_init -= 10
            self.update_paginator()

    def next_click(self, e):
        if self.paginator_init < int(self.length/10)*10:
            self.paginator_init += 10
            self.update_paginator()

    def last_click(self, e):
        self.paginator_init = int(self.length/10)*10
        self.update_paginator()

    def __find_length(self, table):
        length_db = self.__db.get_length(table)
        return length_db[0][0]

    def update_paginator(self):
        self.paginator = f"{self.paginator_init},{self.paginator_step}"
        print(self.paginator)
        self.responsiveRow.controls = []

        match self.route:
            case "diary":
                self.responsiveRow.controls.append(DiaryTable(self.__db, self.paginator))
            case "monthly":
                self.responsiveRow.controls.append(MonthlyTable(self.__db, self.paginator))
            case "yearly":
                self.responsiveRow.controls.append(YearTable(self.__db, self.paginator))

        self.__page.update()
