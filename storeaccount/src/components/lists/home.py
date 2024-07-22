import flet as ft


class HomeList(ft.ExpansionPanelList):
    def __init__(self, db):
        super().__init__()
        self.__db=db
        self.controls = self.get_expansion_panel_list()

    def get_expansion_panel_list(self):
        yearly_data = self.__db.get_data("yearly")
        return [self.create_expansion_panel(data) for data in yearly_data]

    def create_expansion_panel(self, yearly_data):
        monthly_data = self.__db.get_data("monthly", condition=f"yearlyID = '{yearly_data[0]}'")
        data_rows = self.create_data_rows(monthly_data)

        return ft.ExpansionPanel(
            header=self.create_panel_header(yearly_data),
            content=self.create_panel_content(data_rows)
        )

    def create_panel_header(self, yearly_data):
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(
                    ft.Text(f"{yearly_data[1]}"),
                    margin=ft.margin.symmetric(horizontal=20),
                ),
                ft.Container(
                    ft.Text(f"{yearly_data[5]}"),
                    margin=ft.margin.symmetric(horizontal=10),
                ),
            ]
        )

    def create_panel_content(self, data_rows):
        return ft.ResponsiveRow([
            ft.Container(
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Mes")),
                        ft.DataColumn(ft.Text("Ventas")),
                        ft.DataColumn(ft.Text("Gastos Proveedores")),
                        ft.DataColumn(ft.Text("Gastos Generales")),
                        ft.DataColumn(ft.Text("Total")),
                    ],
                    rows=data_rows,
                )
            )
        ])

    def create_data_rows(self, monthly_data):
        return [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(month[1])),
                    ft.DataCell(ft.Text(month[2])),
                    ft.DataCell(ft.Text(month[3])),
                    ft.DataCell(ft.Text(month[4])),
                    ft.DataCell(ft.Text(month[5])),
                ],
            )
            for month in monthly_data
        ]