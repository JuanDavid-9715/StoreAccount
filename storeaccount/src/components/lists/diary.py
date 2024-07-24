import flet as ft

from src.components.utilities import get_month

class DiaryList(ft.DataTable):
    def __init__(self, db):
        self.__db=db
        columns=self.create_column()
        rows=self.get_data_row_year()
        super().__init__(columns=columns, rows=rows)

    def update_click(self, e):
        print("Se presiono el boton update")
        print(f"e.data: {e.control.data}")
        diary = self.__db.get_data("diary", condition=f"id='{e.control.data}'")
        print(diary)

    def delete_click(self, e):
        print("Se presiono el boton delete")
        print(f"e.data: {e.control.data}")
        diary = self.__db.get_data("diary", condition=f"id='{e.control.data}'")
        print(diary)

    def get_data_row_year(self):
        data_rows = []

        yearly_data = self.__fetch_yearly_data()

        for yearly in yearly_data:
            monthly_data = self.__fetch_monthly_data(yearly[0])
            for monthly in monthly_data:
                diary_data = self.__fetch_diary_data(monthly[0])
                for diary in diary_data:
                    month = get_month(monthly[1])
                    data_rows.append(self.create_data_row(diary, month, yearly[1]))

        return data_rows

    def __fetch_yearly_data(self):
        return self.__db.get_data_orderBy(
            "yearly", 
            "year", 
            column="id, year", 
            address="DESC"
        )

    def __fetch_monthly_data(self, yearly_id):
        return self.__db.get_data_orderBy(
            "monthly",
            "month",
            column="id, month",
            condition=f"yearlyID='{yearly_id}'",
            address="DESC"
        )

    def __fetch_diary_data(self, monthly_id):
        return self.__db.get_data_orderBy(
            "diary",
            "day",
            condition=f"monthlyID='{monthly_id}'",
            address="DESC"
        )

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

    def create_data_row(self, diary, monthly, yearly):
        return ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(diary[1])),
                    ft.DataCell(ft.Text(monthly)),
                    ft.DataCell(ft.Text(yearly)),
                    ft.DataCell(ft.Text(diary[2])),
                    ft.DataCell(ft.Text(diary[3])),
                    ft.DataCell(ft.Text(diary[4])),
                    ft.DataCell(ft.Text(diary[5])),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.icons.UPDATE,
                            icon_color=ft.colors.LIGHT_BLUE_600,
                            icon_size=30,
                            on_click=self.update_click, 
                            data=diary[0],
                        ),
                    ),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.icons.DELETE_FOREVER_ROUNDED,
                            icon_color=ft.colors.PINK_600,
                            icon_size=30,
                            on_click=self.delete_click,
                            data=diary[0],
                        ),
                    ),
                ],
            )