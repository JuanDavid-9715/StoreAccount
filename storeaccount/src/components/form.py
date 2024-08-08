import flet as ft

from src.utilities.utilities import get_month

class Form():
    def __init__(self):
        self.tf_sales=ft.TextField(
            label="Ventas",
            autofocus=True,
        )
        self.tf_supplier_expenses=ft.TextField(
            label="Gastos Proveedores",
        )
        self.tf_overheads=ft.TextField(
            label="Gastos Generales",
        )

    def submit_form(self, e):
        try:
            month, year = self.__validate()

            day = self.__validate_day(self.date.day, month[0])
            if not day:
                return
            else:
                self._page.open(ft.AlertDialog(
                    title=ft.Text("Este dia ya fue registrado en la base de datos"),
                    content=ft.Text(day),
                ))

            self._page.update()
        except Exception as e:
            self._page.open(ft.AlertDialog(
                title=ft.Text("Ocurrió un error al enviar el formulario"),
            ))
            print(f"Error: {e}")

    def update_form(self, e):
        try:
            month, year = self.__validate()

            day = self.__validate_day(self.date.day, month[0], update=True)
            print(day)
            if not day:
                return
            else:
                print(year)
                print(month)
                print(day)
                self._page.open(ft.AlertDialog(
                    title=ft.Text(f"Se actualizaron los datos del dia {day[1]}-{get_month(month[1])}-{year[1]}"),
                    content=ft.Text(day),
                ))
        except Exception as e:
            self._page.open(ft.AlertDialog(
                title=ft.Text("Ocurrió un error al enviar el formulario"),
            ))
            print(f"Error: {e}")

    def __validate(self):
        try:
            if not self.date:
                return 

            flag = self.__validate_inputs()
            if not flag:
                return

            year = self.__validate_year(self.date.year)
            if not year:
                return

            month = self.__validate_month(self.date.month, year[0])
            if not month:
                return

            return month, year
        except:
            self._page.open(ft.AlertDialog(
                title=ft.Text("Ocurrió un error al validar datos"),
            ))
            print(f"Error: {e}")

    def __validate_inputs(self):
        try:
            self.sales = int(self.tf_sales.value)
            self.supplier_expenses = int(self.tf_supplier_expenses.value)
            self.overheads = int(self.tf_overheads.value)
            self.total = self.sales - self.supplier_expenses - self.overheads

            return True
        except ValueError as e:
            self._page.open(ft.AlertDialog(
                title=ft.Text("Valores inválidos ingresados."),
            ))
            print(f"Error: {e}")
            return False

    def __validate_year(self, year):
        try:
            year_data = self._db.get_data("yearly", condition=f"year='{year}'")
            if not year_data:
                flag = self.__create_year(year)
                if not flag:
                    return None
                return self.__validate_year(year)
            return year_data[0]
        except Exception as e:
            self.page.open(ft.AlertDialog(
                title=ft.Text("El año no existe en la base de datos"),
            ))
            print(f"Error: {e}")
            return None

    def __validate_month(self, month, year_id):
        try:
            month_data = self._db.get_data("monthly", condition=f"month='{month}' AND yearlyID='{year_id}'")
            if not month_data:
                flag = self.__create_month(month, year_id)
                if not flag:
                    return None
                return self.__validate_month(month, year_id)
            return month_data[0]
        except Exception as e:
            self._page.open(ft.AlertDialog(
                title=ft.Text("El mes no existe en la base de datos"),
            ))
            print(f"Error: {e}")
            return None

    def __validate_day(self, day, month_id, update=False, exist=True):
        try:
            day_data = self._db.get_data("diary", condition=f"day='{day}' AND monthlyID='{month_id}'")
            if not day_data:
                flag = self.__create_data(day, self.sales, self.supplier_expenses, self.overheads, self.total, month_id)
                if not flag:
                    return None

                self.clear_fields()

                self._page.open(ft.AlertDialog(
                    title=ft.Text("Se han cargado exitosamente los datos en la base de datos"),
                ))
                return self.__validate_day(day, month_id, exist=False)

            if update:
                flag = self.__update_data(day_data[0][0], day, self.sales, self.supplier_expenses, self.overheads, self.total, month_id)
                if not flag:
                    return None

                self.clear_fields()

                return self.__validate_day(day, month_id)

            if not exist:
                return None
            return day_data[0]
        except Exception as e:
            self._page.open(ft.AlertDialog(
                title=ft.Text("El dia no existe en la base de datos"),
            ))
            print(f"Error: {e}")
            return None

    def __create_year(self, year):
        try:
            data = {
                "year": str(year),
            }
            print(f"post_data: {data}")
            self._db.post_data("yearly", data)

            return True
        except Exception as e:
            self.page.open(ft.AlertDialog(
                title=ft.Text("No se pudo crear el año en la base de datos"),
            ))
            print(f"Error: {e}")
            return False

    def __create_month(self, month, year_id):
        try:
            data = {
                "month": str(month),
                "yearlyID": str(year_id),
            }
            print(f"post_data: {data}")
            self._db.post_data("monthly", data)
            
            return True
        except Exception as e:
            self.page.open(ft.AlertDialog(
                title=ft.Text("No se pudo crear el mes en la base de datos"),
            ))
            print(f"Error: {e}")
            return False

    def __create_data(self, day, sales, supplier_expenses, overheads, total, month_id):
        try:
            data = {
                "day": str(day),
                "sales": str(sales),
                "supplierExpenses": str(supplier_expenses),
                "overheads": str(overheads),
                "total": str(total),
                "monthlyID": str(month_id)
            }
            print(f"post_data: {data}")
            self._db.post_data("diary", data)

            return True
        except Exception as e:
            self.page.open(ft.AlertDialog(
                title=ft.Text("No se pudo crear el dia en la base de datos"),
            ))
            print(f"Error: {e}")
            return False

    def __update_data(self, id, day, sales, supplier_expenses, overheads, total, month_id):
        try:
            data = {
                "day": str(day),
                "sales": sales,
                "supplierExpenses": supplier_expenses,
                "overheads": overheads,
                "total": total,
                "monthlyID": month_id
            }
            print(f"update_data: {data}")
            self._db.update_data(
                "diary", 
                data, 
                condition=f"id = {id}",
            )
            return True
        except Exception as e:
            self.page.open(ft.AlertDialog(
                title=ft.Text("No se pudo crear el dia en la base de datos"),
            ))
            print(f"Error: {e}")
            return False

    def clear_fields(self):
        self.tf_sales.value = ""
        self.tf_supplier_expenses.value = ""
        self.tf_overheads.value = ""
    