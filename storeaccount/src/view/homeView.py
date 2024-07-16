import flet as ft


class HomeView(ft.ExpansionPanelList):
    def __init__(self, db):
        super().__init__()
        self.__db=db
        self.controls=self.get_expansionPanel_list()

    def get_expansionPanel_list(self):
        expansionPanel_list = []
        dataYearly_list = self.__db.get_data("yearly")

        for dataYearly in dataYearly_list:
            dataRow_list = []
            dataMonthly_list = self.__db.get_data("monthly", "yearlyID", dataYearly[0])
            
            for dataMonthly in dataMonthly_list:
                dataRow_list.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(dataMonthly[1])),
                            ft.DataCell(ft.Text(dataMonthly[2])),
                            ft.DataCell(ft.Text(dataMonthly[3])),
                            ft.DataCell(ft.Text(dataMonthly[4])),
                            ft.DataCell(ft.Text(dataMonthly[5])),
                        ],
                    ),
                )

            expansionPanel = ft.ExpansionPanel(
                header=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(
                            ft.Text(f"{dataYearly[1]}"),
                            margin=ft.margin.symmetric(horizontal=20),
                        ),
                        ft.Container(
                            ft.Text(f"{dataYearly[5]}"),
                            margin=ft.margin.symmetric(horizontal=10),
                        ),
                    ]
                ),
                content=ft.ResponsiveRow([
                    ft.Container(
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("Mes")),
                                ft.DataColumn(ft.Text("Ventas")),
                                ft.DataColumn(ft.Text("Gastos Proveedores")),
                                ft.DataColumn(ft.Text("Gastos Generales")),
                                ft.DataColumn(ft.Text("Total")),
                            ],
                            rows=dataRow_list,
                        )
                    )
                ])
            )

            expansionPanel_list.append(expansionPanel)

        return expansionPanel_list
