### **Building a Student Budget Dashboard with Flet, Plotly, and Quarto**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **The Project**

This project is a student budget dashboard using Python, Flet, and Plotly. The dashboard visualizes a full year of student financial data, including monthly spending across categories like tuition, rent, food, and entertainment, as well as income from freelance and part time work. It was built as part of an internship with Oppkey during the summer of 2026, with the goal of practicing: loading CSV data with pandas, building interactive charts with Plotly, and rendering them inside a Flet app. The project includes three charts: a stacked area chart showing monthly spending trends, a donut chart showing the annual spending breakdown, and a bubble scatter chart comparing income, expenses, and workload across the year.  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **The Data**

The dashboard uses a CSV file called student\_budget\_2026.csv with 12 rows (one per month) and 12 columns:

* Expenses: tuition, rent, food, transport, books\_supplies, subscriptions, health\_fitness, entertainment  
* Income: freelance\_income, part\_time\_income  
* Workload: study\_hours, project\_hours

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Chart 1: Monthly Spending Trend**

\[Insert screenshot here\]

Explanation of Chart: This chart is a stacked area chart showing how spending across eight categories: tuition, rent, food, transport, books and supplies, subscriptions, health and fitness, and entertainment, changed month by month over the year. Each colored layer represents one category, and the total height of the chart at any given month represents total spending for that month. It makes it easy to see that rent and tuition dominate the budget.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Chart 2: Annual Spending Breakdown**

\[Insert screenshot here\]

Explanation of Chart: This chart is a donut chart showing the percentage of total annual spending by category. Instead of showing month-by-month changes, it answers the question of where the money went over the full year. Tuition and rent together make up the majority of the total, while smaller categories like subscriptions and health and fitness are easy to underestimate month to month but still add up significantly over 12 months.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Chart 3: Income vs. Expenses with Workload**

\[Insert screenshot here\]

Explanation of Chart: This chart is a bubble scatter chart that combines financial and workload data in one view. Each bubble represents one month. The x-axis shows total income, the y-axis shows total expenses, the size of the bubble represents total work and study hours, and the color represents net cash flow. It shows that expenses consistently outpace income every month, but summer months like July and August have slightly better cash flow and higher workload.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Using Plotly with Flet**

To use Plotly charts inside a Flet app, I needed to install:

uv pip install plotly kaleido flet flet-charts

Getting Plotly working inside Flet took some trial and error. The issue was that pandas and plotly were being installed to the system Python instead of the virtual environment, which meant the packages installed successfully but the script still threw ModuleNotFoundError. The fix was to use uv pip install instead of pip3 install, which installed packages correctly into the venv.  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **What I Would Improve**

In a future version I would add the following:

* A dropdown or toggle so the user can switch between charts without running separate files.  
* A summary section showing total annual income, total annual expenses, and net cash flow as numbers alongside the charts.  
* The ability to upload a different CSV file and have the charts update automatically.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### **Conclusion**

This project was a great introduction to building data dashboards with Python, covering the full workflow from loading CSV data with pandas to rendering interactive Plotly charts inside a Flet app. It showed how to combine multiple tools together and gave real experience debugging package installation, import errors, and chart configuration along the way.