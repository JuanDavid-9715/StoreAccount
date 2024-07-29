import flet as ft
import datetime

from src.components.form import Form

class HomeFrom(ft.AutofillGroup, Form):
    def __init__(self, db, page):
        super().__init__()
        self._db=db
        self._page=page
        self.date=datetime.date.today()
        self.content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                self.tf_sales,
                self.tf_supplier_expenses,
                self.tf_overheads,
                ft.ElevatedButton(
                    text="Guardar", 
                    on_click=self.submit_form,
                )
            ]
        )

    
