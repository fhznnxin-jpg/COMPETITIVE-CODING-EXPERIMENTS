"""
Final Assignment Part 2 - Create Dashboard with Plotly and Dash

Tasks covered:
TASK 2.1: Create a Dash application and give it a meaningful title.
TASK 2.2: Add drop-down menus with appropriate titles and options.
TASK 2.3: Add a division for output display with appropriate id and className.
TASK 2.4: Create callbacks to update the input/year container and output container.
TASK 2.5: Create and display graphs for Recession Report Statistics.
TASK 2.6: Create and display graphs for Yearly Report Statistics.
"""

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# -------------------------------------------------------------------
# Sample automobile-sales data used by the dashboard
# -------------------------------------------------------------------
vehicle_types = [
    "ExecutiveCar",
    "MediumFamilyCar",
    "SmallFamilyCar",
    "Sports",
    "SuperMiniCar",
]

recession_vehicle_sales = pd.DataFrame({
    "Vehicle_Type": vehicle_types,
    "Automobile_Sales": [830, 1680, 1660, 810, 2010],
})

non_recession_vehicle_sales = pd.DataFrame({
    "Vehicle_Type": vehicle_types,
    "Automobile_Sales": [3330, 3850, 4020, 3430, 3750],
})

yearly_data = pd.DataFrame({
    "Year": [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989],
    "Automobile_Sales": [7500, 7200, 6100, 6800, 7900, 8300, 8100, 8700, 9200, 9600],
    "Advertising_Expenditure": [120, 135, 150, 165, 180, 195, 210, 230, 250, 275],
    "Unemployment_Rate": [7.2, 7.6, 9.7, 9.6, 7.5, 7.2, 7.0, 6.2, 5.5, 5.3],
})

# -------------------------------------------------------------------
# TASK 2.1: Create Dash application with meaningful title
# -------------------------------------------------------------------
app = Dash(__name__)
app.title = "Automobile Sales Statistics Dashboard"

# -------------------------------------------------------------------
# TASK 2.2 and TASK 2.3: Dashboard layout, dropdowns and output Div
# -------------------------------------------------------------------
app.layout = html.Div(
    children=[
        html.H1(
            "Automobile Sales Statistics Dashboard",
            className="header-title",
        ),

        html.Div(
            children=[
                html.Label(
                    "Select Statistics:",
                    className="dropdown-label",
                ),
                dcc.Dropdown(
                    id="statistics-dropdown",
                    options=[
                        {
                            "label": "Yearly Statistics",
                            "value": "Yearly Statistics",
                        },
                        {
                            "label": "Recession Period Statistics",
                            "value": "Recession Period Statistics",
                        },
                    ],
                    value="Yearly Statistics",
                    clearable=False,
                ),
            ],
            className="dropdown-container",
        ),

        # TASK 2.4: This input container is updated by the callback.
        html.Div(
            id="select-year-container",
            className="select-year-container",
        ),

        # TASK 2.3: Output display division with id and className.
        html.Div(
            id="output-container",
            className="output-container",
        ),
    ],
    className="main-container",
)

# -------------------------------------------------------------------
# TASK 2.4: Callback for input container and output container
# -------------------------------------------------------------------
@app.callback(
    Output("select-year-container", "children"),
    Output("output-container", "children"),
    Input("statistics-dropdown", "value"),
)
def update_dashboard(selected_statistics):
    """
    Update the year selector and dashboard graphs based on the
    selected statistics category.
    """

    # ---------------------------------------------------------------
    # TASK 2.5: Recession Report Statistics
    # ---------------------------------------------------------------
    if selected_statistics == "Recession Period Statistics":

        year_selector = html.Div(
            children=[
                html.P(
                    "Year selection is not required for Recession Period Statistics.",
                    className="info-text",
                )
            ]
        )

        # Vehicle-wise recession sales
        recession_fig = px.bar(
            recession_vehicle_sales,
            x="Vehicle_Type",
            y="Automobile_Sales",
            title="Average Automobile Sales by Vehicle Type During Recession",
        )

        # Advertising expenditure during recession
        recession_advertising = pd.DataFrame({
            "Vehicle_Type": vehicle_types,
            "Advertising_Expenditure": [420, 760, 700, 380, 900],
        })

        advertising_fig = px.pie(
            recession_advertising,
            names="Vehicle_Type",
            values="Advertising_Expenditure",
            title="Advertising Expenditure Distribution During Recession",
        )

        # Unemployment rate during recession
        unemployment_fig = px.bar(
            x=["Recession Period"],
            y=[9.7],
            labels={"x": "Economic Condition", "y": "Unemployment Rate (%)"},
            title="Unemployment Rate During Recession",
        )

        output = html.Div(
            children=[
                dcc.Graph(figure=recession_fig),
                dcc.Graph(figure=advertising_fig),
                dcc.Graph(figure=unemployment_fig),
            ],
            className="report-container",
        )

        return year_selector, output

    # ---------------------------------------------------------------
    # TASK 2.6: Yearly Report Statistics
    # ---------------------------------------------------------------
    year_selector = html.Div(
        children=[
            html.Label("Select Year:", className="dropdown-label"),
            dcc.Dropdown(
                id="year-dropdown",
                options=[
                    {"label": str(year), "value": int(year)}
                    for year in yearly_data["Year"]
                ],
                value=int(yearly_data["Year"].iloc[-1]),
                clearable=False,
            ),
        ]
    )

    # Default yearly view. A second callback below refreshes this
    # output when the user selects a specific year.
    selected_year = int(yearly_data["Year"].iloc[-1])
    row = yearly_data[yearly_data["Year"] == selected_year].iloc[0]

    sales_fig = px.bar(
        yearly_data,
        x="Year",
        y="Automobile_Sales",
        title="Average Annual Automobile Sales",
    )

    advertising_fig = px.scatter(
        yearly_data,
        x="Advertising_Expenditure",
        y="Automobile_Sales",
        trendline="ols",
        title="Advertising Expenditure vs Automobile Sales",
    )

    unemployment_fig = px.line(
        yearly_data,
        x="Year",
        y="Unemployment_Rate",
        markers=True,
        title="Unemployment Rate by Year",
    )

    output = html.Div(
        children=[
            html.H3(f"Yearly Statistics — Selected Year: {selected_year}"),
            html.P(
                f"Automobile Sales: {int(row['Automobile_Sales'])}"
            ),
            dcc.Graph(figure=sales_fig),
            dcc.Graph(figure=advertising_fig),
            dcc.Graph(figure=unemployment_fig),
        ],
        className="report-container",
    )

    return year_selector, output


# Additional callback: update the yearly report when a specific year
# is selected. The callback also demonstrates dynamic dashboard output.
@app.callback(
    Output("output-container", "children", allow_duplicate=True),
    Input("year-dropdown", "value"),
    prevent_initial_call=True,
)
def update_yearly_report(selected_year):
    """Create the Yearly Report Statistics for the selected year."""

    selected_year = int(selected_year)
    row = yearly_data[yearly_data["Year"] == selected_year].iloc[0]

    sales_fig = px.bar(
        yearly_data,
        x="Year",
        y="Automobile_Sales",
        title="Average Annual Automobile Sales",
    )

    advertising_fig = px.scatter(
        yearly_data,
        x="Advertising_Expenditure",
        y="Automobile_Sales",
        trendline="ols",
        title="Advertising Expenditure vs Automobile Sales",
    )

    unemployment_fig = px.line(
        yearly_data,
        x="Year",
        y="Unemployment_Rate",
        markers=True,
        title="Unemployment Rate by Year",
    )

    return html.Div(
        children=[
            html.H3(f"Yearly Statistics — Selected Year: {selected_year}"),
            html.P(
                f"Automobile Sales: {int(row['Automobile_Sales'])} | "
                f"Advertising Expenditure: {row['Advertising_Expenditure']}"
            ),
            dcc.Graph(figure=sales_fig),
            dcc.Graph(figure=advertising_fig),
            dcc.Graph(figure=unemployment_fig),
        ],
        className="report-container",
    )


if __name__ == "__main__":
    app.run(debug=True)
