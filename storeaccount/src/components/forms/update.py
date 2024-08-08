import flet as ft
import datetime

from src.components.form import Form

class DiaryUpdate(ft.IconButton, Form):
    def __init__(self, db, page, data, size=18):
        ft.IconButton.__init__(self, icon=ft.icons.UPDATE, icon_color=ft.colors.LIGHT_BLUE_600, icon_size=size,)
        Form.__init__(self)
        self._db=db
        self._page=page
        self.date=datetime.date(int(data[3]), int(data[2]), int(data[1]))
        self.on_click=self.open_update
        self.data=data
        self.button_date=ft.ElevatedButton(
            "Fecha",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=self.open_date,
        )
        self.datePicker=ft.DatePicker(
            value=self.date,
            first_date=datetime.datetime(year=2020, month=1, day=1),
            last_date=datetime.datetime(year=2050, month=12, day=31),
            on_change=self.get_date,
        )
        self.text_date=ft.Text(value=f"Fecha: {self.date.strftime('%d %B %Y')}")
        self.form_panel=ft.AlertDialog(
            title=ft.Text("Actualizar Dia"),
            content=ft.Container(
                ft.Column(
                    controls=[
                        self.button_date,
                        self.text_date,
                        self.tf_sales,
                        self.tf_supplier_expenses,
                        self.tf_overheads,
                    ]
                ),
                width=300,
                height=250,
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=self.close_update),
                ft.TextButton("Guardar", on_click=self.update_form),
            ],
        )

    def open_date(self, e):
        self._page.open(self.datePicker)

    def get_date(self, e):
        self.date = self.datePicker.value.date()
        self.text_date.value=f"Fecha: {self.date.strftime('%d %B %Y')}"
        self._page.update()

    def open_update(self, e):
        self.tf_sales.value=self.data[4]
        self.tf_supplier_expenses.value=self.data[5]
        self.tf_overheads.value=self.data[6]
        
        self._page.open(self.form_panel)

    def close_update(self, e):
        self._page.close(self.form_panel)
