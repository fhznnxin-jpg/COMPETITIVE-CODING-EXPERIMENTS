import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the data (falls back to the local copy if the URL is unreachable)
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
try:
    data = pd.read_csv(URL)
except Exception:
    data = pd.read_csv("historical_automobile_sales.csv")

app = dash.Dash(__name__)
app.title = "Automobile Statistics Dashboard"

dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
year_list = [i for i in range(1980, 2024, 1)]

# TASK 2.1: Layout
app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard",
            style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(id='dropdown-statistics', options=dropdown_options,
                     value='Select Statistics', placeholder='Select a report type',
                     style={'width': '80%', 'padding': '3px', 'font-size': '20px',
                            'textAlignLast': 'center'})
    ]),
    html.Div(dcc.Dropdown(id='select-year',
                          options=[{'label': i, 'value': i} for i in year_list],
                          placeholder='Select-year', value='Select-year',
                          style={'width': '80%', 'padding': '3px', 'font-size': '20px',
                                 'textAlignLast': 'center'})),
    html.Div([html.Div(id='output-container', className='chart-grid',
                       style={'display': 'flex', 'flexWrap': 'wrap'})])
])

# TASK 2.2: enable/disable the year dropdown
@app.callback(Output('select-year', 'disabled'),
              Input('dropdown-statistics', 'value'))
def update_input_container(selected_statistics):
    return selected_statistics != 'Yearly Statistics'

# TASK 2.4: Callback for the charts
@app.callback(Output('output-container', 'children'),
              [Input('dropdown-statistics', 'value'), Input('select-year', 'value')])
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]

        # Plot 1: average automobile sales per year during recessions
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(figure=px.line(yearly_rec, x='Year', y='Automobile_Sales',
            title="Average Automobile Sales fluctuation over Recession Period"))

        # Plot 2: average vehicles sold by vehicle type
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(figure=px.bar(average_sales, x='Vehicle_Type', y='Automobile_Sales',
            title="Average Number of Vehicles Sold by Vehicle Type during Recession"))

        # Plot 3: pie of total advertising expenditure by vehicle type
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(figure=px.pie(exp_rec, values='Advertising_Expenditure', names='Vehicle_Type',
            title="Total Advertising Expenditure Share by Vehicle Type during Recession"))

        # Plot 4: effect of unemployment rate on vehicle type and sales
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(figure=px.bar(unemp_data, x='unemployment_rate', y='Automobile_Sales',
            color='Vehicle_Type',
            labels={'unemployment_rate': 'Unemployment Rate', 'Automobile_Sales': 'Average Automobile Sales'},
            title='Effect of Unemployment Rate on Vehicle Type and Sales'))

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)],
                     style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)],
                     style={'display': 'flex'})
        ]

    elif input_year and selected_statistics == 'Yearly Statistics':
        yearly_data = data[data['Year'] == input_year]

        # Plot 1: yearly automobile sales for the whole period
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas, x='Year', y='Automobile_Sales',
            title='Yearly Automobile Sales'))

        # Plot 2: total monthly automobile sales for the selected year
        mas = yearly_data.groupby('Month', sort=False)['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(mas, x='Month', y='Automobile_Sales',
            title='Total Monthly Automobile Sales'))

        # Plot 3: average vehicles sold by vehicle type in the selected year
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata, x='Vehicle_Type', y='Automobile_Sales',
            title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

        # Plot 4: total advertisement expenditure for each vehicle type
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(exp_data, values='Advertising_Expenditure', names='Vehicle_Type',
            title='Total Advertisement Expenditure for Each Vehicle Type'))

        return [
            html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart2)],
                     style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=Y_chart3), html.Div(children=Y_chart4)],
                     style={'display': 'flex'})
        ]
    else:
        return None

if __name__ == '__main__':
    app.run(debug=False, port=8050)
