# Monthly College Spending Dashboard

A Python data visualization app that displays monthly college spending data using flet-charts.

## Live Site
[View the live app](https://aryhannapham.github.io/python-charts/)

> Note: may take a minute to load the first time due to the entire app and Pyodide being loaded.

## What it shows
- Monthly Tuition payments vs Living Expenses
- Bar chart comparison across 12 months
- Total spending summary

## How to run locally
Clone the repo and install dependencies:
uv sync
uv run main.py

## How to run tests
uv run pytest

## Built with
- Python
- Flet
- flet-charts

## Data
Uses a simple CSV file (data.csv) with monthly tuition and living expense data.
Data can be swapped out by editing data.csv directly.