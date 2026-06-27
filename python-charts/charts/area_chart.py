import pandas as pd
import plotly.express as px
import flet as ft
from flet_charts import PlotlyChart

def create_area_chart():
    df = pd.read_csv("python-charts/data/student_budget_2026.csv")

    #documentation links: 
    #https://plotly.com/python/filled-area-plots/
    #https://pandas.pydata.org/docs/reference/api/pandas.melt.html
    long_df = df.melt(
        id_vars="month",
        value_vars=["tuition", "rent", "food", "transport", "books_supplies", "subscriptions", "health_fitness", "entertainment"],
        var_name="category",
        value_name="amount"
    )

    fig = px.area(
        long_df,
        x="month",
        y="amount",
        color="category",
        title="Monthly Student Spending by Category"
    )

    return fig

def main(page: ft.Page):
    page.title = "Monthly Student Spending by Category"
    fig = create_area_chart()
    page.add(PlotlyChart(figure=fig, expand=True))

if __name__ == "__main__":
    ft.app(target=main)