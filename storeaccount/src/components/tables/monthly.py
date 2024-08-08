import flet as ft

from src.utilities.utilities import get_month

class MonthlyTable(ft.DataTable):
    def __init__(self, db, paginator):
        self.__db=db
        self.paginator=paginator
        columns=self.create_column()
        rows=self.get_data_row_year()
        super().__init__(columns=columns, rows=rows)

    def get_data_row_year(self):
        data_rows = []

        data_list = self.__db.get_data(
            "monthly",
            column="monthly.id, monthly.month, yearly.year, monthly.sales, monthly.supplierExpenses, monthly.overheads, monthly.total",
            join=True,
            order_by="yearly.year DESC, monthly.month DESC",
            limit=self.paginator,
        )

        for data in data_list:
            month = get_month(data[1])
            data_rows.append(self.create_data_row(data, month))

        return data_rows

    def create_column(self):
        return [
            ft.DataColumn(ft.Text("mes")),
            ft.DataColumn(ft.Text("año")),
            ft.DataColumn(ft.Text("Ventas")),
            ft.DataColumn(ft.Text("Gastos Proveedores")),
            ft.DataColumn(ft.Text("Gastos Generales")),
            ft.DataColumn(ft.Text("Total")),
        ]

    def create_data_row(self, data, month):
        return ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(month)),
                    ft.DataCell(ft.Text(data[2])),
                    ft.DataCell(ft.Text(data[3])),
                    ft.DataCell(ft.Text(data[4])),
                    ft.DataCell(ft.Text(data[5])),
                    ft.DataCell(ft.Text(data[6])),
                ],
            )