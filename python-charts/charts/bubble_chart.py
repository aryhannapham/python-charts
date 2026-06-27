import pandas as pd
import plotly.express as px
import flet as ft
from flet_charts import PlotlyChart

def create_bubble_chart():
    df = pd.read_csv("python-charts/data/student_budget_2026.csv")

    #documentation links: 
    #https://plotly.com/python/bubble-charts/
    #https://pandas.pydata.org/docs/user_guide/indexing.html
    df["total_expenses"] = (df["tuition"] + df["rent"] + df["food"] + df["transport"] + df["books_supplies"] + df["subscriptions"] + df["health_fitness"] + df["entertainment"])

    df["total_income"] = df["freelance_income"] + df["part_time_income"]

    df["net_cash_flow"] = df["total_income"] - df["total_expenses"]

    df["total_work_hours"] = df["study_hours"] + df["project_hours"]


    fig = px.scatter(
        df,
        x="total_income",
        y="total_expenses",
        size="total_work_hours",
        color="net_cash_flow",
        hover_name="month",
        title="Monthly Income vs. Expenses with Workload"
    )

    return fig

def main(page: ft.Page):
    page.title = "Monthly Income vs. Expenses with Workload"
    fig = create_bubble_chart()
    page.add(PlotlyChart(figure=fig, expand=True))

if __name__ == "__main__":
    ft.app(target=main)