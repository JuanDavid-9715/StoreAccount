import flet as ft

from src.utilities.utilities import get_month

class DiaryTable(ft.DataTable):
    def __init__(self, db, paginator):
        self.__db=db
        self.paginator=paginator
        self.icon_size=18
        columns=self.create_column()
        rows=self.get_data()
        super().__init__(columns=columns, rows=rows)

    def update_click(self, e):
        print("Se presiono el botón update")
        print(f"e.data: {e.control.data}")
        diary = self.__db.get_data("diary", condition=f"id='{e.control.data}'")
        print(diary)

    def delete_click(self, e):
        print("Se presiono el botón delete")
        print(f"e.data: {e.control.data}")
        diary = self.__db.get_data("diary", condition=f"id='{e.control.data}'")
        print(diary)

    def get_data(self):
        data_rows = []
        
        data_list = self.__db.get_data(
            "diary",
            column="diary.id, diary.day, monthly.month, yearly.year, diary.sales, diary.supplierExpenses, diary.overheads, diary.total",
            join=True,
            order_by="yearly.year DESC, monthly.month DESC, diary.day DESC",
            limit=self.paginator,
        )

        for data in data_list:
            month = get_month(data[2])
            data_rows.append(self.create_data_row(data, month))

        return data_rows

    def create_column(self):
        return [
            ft.DataColumn(ft.Text("dia")),
            ft.DataColumn(ft.Text("mes")),
            ft.DataColumn(ft.Text("año")),
            ft.DataColumn(ft.Text("Ventas")),
            ft.DataColumn(ft.Text("Gastos Proveedores")),
            ft.DataColumn(ft.Text("Gastos Generales")),
            ft.DataColumn(ft.Text("Total")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
        ]

    def create_data_row(self, data, month):
        return ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(data[1])),
                    ft.DataCell(ft.Text(month)),
                    ft.DataCell(ft.Text(data[3])),
                    ft.DataCell(ft.Text(data[4])),
                    ft.DataCell(ft.Text(data[5])),
                    ft.DataCell(ft.Text(data[6])),
                    ft.DataCell(ft.Text(data[7])),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.icons.UPDATE,
                            icon_color=ft.colors.LIGHT_BLUE_600,
                            icon_size=self.icon_size,
                            on_click=self.update_click, 
                            data=data[0],
                        ),
                    ),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.icons.DELETE_FOREVER_ROUNDED,
                            icon_color=ft.colors.PINK_600,
                            icon_size=self.icon_size,
                            on_click=self.delete_click,
                            data=data[0],
                        ),
                    ),
                ],
            )