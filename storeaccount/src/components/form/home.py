import flet as ft
import datetime

class HomeFrom(ft.AutofillGroup):
    def __init__(self, db, page):
        super().__init__()
        self.__db=db
        self.__page=page
        self.sales=ft.TextField(
            label="Ventas",
            autofocus=True,
        )
        self.supplier_expenses=ft.TextField(
            label="Gastos Proveedores",
        )
        self.overheads=ft.TextField(
            label="Gastos Generales",
        )
        self.submit=ft.ElevatedButton(text="Guardar", on_click=self.submit_form)
        self.content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                self.sales,
                self.supplier_expenses,
                self.overheads,
                self.submit,
            ]
        )

    def submit_form(self, e):
        try:
            date = datetime.date.today()

            sales = self.sales.value
            supplier_expenses = self.supplier_expenses.value
            overheads = self.overheads.value

            if not self.validate_inputs(sales, supplier_expenses, overheads):
                self.page.open(ft.AlertDialog(
                    title=ft.Text("Valores inválidos ingresados."),
                ))
                return

            total = int(sales) - int(supplier_expenses) - int(overheads)

            year_id = self.__db.get_data("yearly", column="id", condition=f"year='{date.year}'")
            if not year_id:
                self.page.open(ft.AlertDialog(
                    title=ft.Text("El año no existe en la base de datos"),
                ))
                return

            month_id = self.__db.get_data("monthly", column="id", condition=f"month='{date.month}' AND yearlyID='{year_id[0][0]}'")
            if not month_id:
                self.page.open(ft.AlertDialog(
                    title=ft.Text("El mes no existe en la base de datos"),
                ))
                return

            day = self.__db.get_data("diary", condition=f"day='{date.day}' AND monthlyID='{month_id[0][0]}'")
            if not day:
                self.save_data(date.day, sales, supplier_expenses, overheads, total, month_id[0][0])

                self.clear_fields()

                self.page.open(ft.AlertDialog(
                    title=ft.Text("Se han cargado exitosamente los datos en la base de datos"),
                ))
            else:
                self.page.open(ft.AlertDialog(
                    title=ft.Text("Este dia ya fue registrado en la base de datos"),
                    content=ft.Text(day),
                ))
                print(f'day_id: {day}')
            self.page.update()
        except Exception as e:
            self.page.open(ft.AlertDialog(
                title=ft.Text("Ocurrió un error al enviar el formulario"),
            ))
            print(e)

    def validate_inputs(self, sales, supplier_expenses, overheads):
        try:
            int(sales)
            int(supplier_expenses)
            int(overheads)

            return True
        except ValueError:
            return False

    def save_data(self, day, sales, supplier_expenses, overheads, total, month_id):
        data = {
            "day": str(day),
            "sales": str(sales),
            "supplierExpenses": str(supplier_expenses),
            "overheads": str(overheads),
            "total": str(total),
            "monthlyID": str(month_id)
        }
        print(f"post_data: {data}")
        self.__db.post_data("diary", data)

    def clear_fields(self):
        self.sales.value = ""
        self.supplier_expenses.value = ""
        self.overheads.value = ""