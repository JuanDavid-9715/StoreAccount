import flet as ft


class YearList(ft.DataTable):
    def __init__(self, db):
        self.__db=db
        columns=self.create_column()
        rows=self.get_data_row_year()
        super().__init__(columns=columns, rows=rows)

    def update_click(self, e):
        print("Se presiono el boton update")
        print(f"e.data: {e.control.data}")
        yearly = self.__db.get_data("yearly", condition=f"id='{e.control.data}'")
        print(yearly)

    def delete_click(self, e):
        print("Se presiono el boton delete")
        print(f"e.data: {e.control.data}")
        yearly = self.__db.get_data("yearly", condition=f"id='{e.control.data}'")
        print(yearly)

    def get_data_row_year(self):
        data_rows = []

        yearly_data = self.__fetch_yearly_data()

        for yearly in yearly_data:
            data_rows.append(self.create_data_row(yearly))

        return data_rows

    def __fetch_yearly_data(self):
        return self.__db.get_data_orderBy(
            "yearly", 
            "year", 
            address="DESC"
        )

    def create_column(self):
        return [
            ft.DataColumn(ft.Text("año")),
            ft.DataColumn(ft.Text("Ventas")),
            ft.DataColumn(ft.Text("Gastos Proveedores")),
            ft.DataColumn(ft.Text("Gastos Generales")),
            ft.DataColumn(ft.Text("Total")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
        ]

    def create_data_row(self, yearly):
        return ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(yearly[1])),
                    ft.DataCell(ft.Text(yearly[2])),
                    ft.DataCell(ft.Text(yearly[3])),
                    ft.DataCell(ft.Text(yearly[4])),
                    ft.DataCell(ft.Text(yearly[5])),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.icons.UPDATE,
                            icon_color=ft.colors.LIGHT_BLUE_600,
                            icon_size=30,
                            on_click=self.update_click, 
                            data=yearly[0],
                        ),
                    ),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.icons.DELETE_FOREVER_ROUNDED,
                            icon_color=ft.colors.PINK_600,
                            icon_size=30,
                            on_click=self.delete_click,
                            data=yearly[0],
                        ),
                    ),
                ],
            )