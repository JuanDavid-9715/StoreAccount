import flet as ft


class YearTable(ft.DataTable):
    def __init__(self, db, paginator):
        self.__db=db
        self.paginator=paginator
        columns=self.create_column()
        rows=self.get_data_row_year()
        super().__init__(columns=columns, rows=rows)

    def get_data_row_year(self):
        data_rows = []

        data_list = self.__db.get_data(
            "yearly",
            column="yearly.id, yearly.year, yearly.sales, yearly.supplierExpenses, yearly.overheads, yearly.total",
            join=True,
            order_by="yearly.year DESC",
            limit=self.paginator,
        )

        for dato in data_list:
            data_rows.append(self.create_data_row(dato))

        return data_rows

    def create_column(self):
        return [
            ft.DataColumn(ft.Text("año")),
            ft.DataColumn(ft.Text("Ventas")),
            ft.DataColumn(ft.Text("Gastos Proveedores")),
            ft.DataColumn(ft.Text("Gastos Generales")),
            ft.DataColumn(ft.Text("Total")),
        ]

    def create_data_row(self, dato):
        return ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(dato[1])),
                    ft.DataCell(ft.Text(dato[2])),
                    ft.DataCell(ft.Text(dato[3])),
                    ft.DataCell(ft.Text(dato[4])),
                    ft.DataCell(ft.Text(dato[5])),
                ],
            )