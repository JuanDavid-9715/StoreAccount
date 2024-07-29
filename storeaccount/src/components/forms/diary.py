import flet as ft
import datetime

from src.components.form import Form

class DiaryFrom(ft.Row, Form):
    def __init__(self, db, page):
        super().__init__()
        self._db=db
        self._page=page
        self.date=datetime.date.today()
        self.alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        self.controls=[
            ft.Text(
                "Diario"
            ),
            ft.FilledButton(
                text="Agregar", 
                icon="add",
                on_click=self.open_add
            ),
        ]
        self.button_date=ft.ElevatedButton(
            "Fecha",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=self.open_date,
        )
        self.datePicker=ft.DatePicker(
            first_date=datetime.datetime(year=2020, month=1, day=1),
            last_date=datetime.datetime(year=2050, month=12, day=31),
            on_change=self.get_date,
        )
        self.text_date=ft.Text(value=f"Fecha: {self.date.strftime('%d %B %Y')}")
        self.form_panel=ft.AlertDialog(
            title=ft.Text("Formulario Dia"),
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
                ft.TextButton("Cancelar", on_click=self.close_add),
                ft.TextButton("Guardar", on_click=self.submit_form),
            ],
        )

    def open_date(self, e):
        self.page.open(self.datePicker)

    def get_date(self, e):
        self.date = self.datePicker.value.date()
        self.text_date.value=f"Fecha: {self.date.strftime('%d %B %Y')}"
        self.page.update()

    def open_add(self, e):
        self.page.open(self.form_panel)

    def close_add(self, e):
        self.page.close(self.form_panel)
