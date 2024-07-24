from dotenv import load_dotenv
import flet as ft
import os

from config.database import DataBase

from src.components.navbar import Navbar

from src.view.homeView import HomeView
from src.view.diaryView import DiaryView
from src.view.monthlyView import MonthlyView
from src.view.yearView import YearView

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

        page.appbar = Navbar(page)

        def route_change(e):
            page.views.clear()
            match page.route:
                case "/":
                    page.views.append(HomeView(db, page))
                case "/diary":
                    page.views.append(DiaryView(db, page))
                case "/monthly":
                    page.views.append(MonthlyView(db, page))
                case "/yearly":
                    page.views.append(YearView(db, page))
            page.update()

        def view_pop(self, e):    
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)

    ft.app(target=main)