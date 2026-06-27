import pandas as pd
import plotly.express as px
import flet as ft
from flet_charts import PlotlyChart

def create_donut_chart():
    df = pd.read_csv("python-charts/data/student_budget_2026.csv")

    #documentation links: 
    #https://plotly.com/python/pie-charts/
    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html
    expense_cols = ["tuition", "rent", "food", "transport", "books_supplies", "subscriptions", "health_fitness", "entertainment"]
    category_totals = df[expense_cols].sum().reset_index()
    category_totals.columns = ["category", "total"]

    fig = px.pie(
        category_totals,
        names="category",
        values="total",
        hole=0.4,
        title="Annual Student Spending Breakdown"
    )

    return fig

def main(page: ft.Page):
    page.title = "Annual Student Spending Breakdown"
    fig = create_donut_chart()
    page.add(PlotlyChart(figure=fig, expand=True))

if __name__ == "__main__":
    ft.app(target=main)