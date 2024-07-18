from dotenv import load_dotenv
import flet as ft
import os

from config.database import DataBase

from src.components.navbar import Navbar

from src.view.homeView import HomeView

load_dotenv()

BASE_DIR = os.path.dirname(__file__)

db_access = {
    'host':os.getenv('HOST'),
    'user':os.getenv('USER'),
    'password':os.getenv('PASSWORD'),
    'database':os.getenv('DATABASE')
}

if __name__ == '__main__':
    db = DataBase(**db_access)

    def main(page: ft.Page):
        page.title = "CuentasTienda"
        page.padding = 0
        page.bgcolor = ft.colors.BLUE_GREY_200

        page.appbar = Navbar(page)

        def route_change(e):
            page.views.clear()
            page.views.append(
                ft.View(
                    route="/",
                    scroll=ft.ScrollMode.ADAPTIVE,
                    appbar=page.appbar,
                    controls=[
                        ft.Container(
                            HomeView(db),
                            padding=ft.padding.symmetric(horizontal=20)
                        )
                    ],
                )
            )
            match page.route:
                case "/diary":
                    page.views.append(
                        ft.View(
                            "/diary",
                            [
                                page.appbar,
                                ft.Text("diary"),
                            ],
                        )
                    )
                case "/monthly":
                    page.views.append(
                        ft.View(
                            "/monthly",
                            [
                                page.appbar,
                                ft.Text("monthly"),
                            ],
                        )
                    )
                case "/yearly":
                    page.views.append(
                        ft.View(
                            "/yearly",
                            [
                                page.appbar,
                                ft.Text("yearly"),
                            ],
                        )
                    )
            page.update()

        def view_pop(self, e):    
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)

    ft.app(target=main)

    """ 
    db.post_data(
        "diary", 
        {
            "sales": 3000000.0,
            "supplierExpenses": 3000000.0,
            "overheads": 3000000.0,
            "total": 3000000.0,
            "monthlyID": 1,
        }
    ) 
    """

    # db.delete_data("diary", "id = 11")

    # db.update_data("diary", "sales = '2000000'", "id = 8")

    # db.get_column("diary")
    # db.get_column("monthly")
    # db.get_column("yearly")

    # db.get_data("diary")
    # db.get_data("monthly")
    # db.get_data("yearly")

    # db.backup_db(BASE_DIR)