import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import calendar

def generate_timesheet_report(timesheet_path: str, output_html: str = "summary.html"):
    df = pd.read_csv(timesheet_path)
    df['Month'] = df['Month'].apply(lambda x: calendar.month_name[x])
    month_order = list(calendar.month_name)[1:]
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

    grouped_data = df.groupby(['Month'])['Hours'].sum().reset_index()
    grouped_data = df.groupby("Month", as_index=False).agg({"Hours": "sum", "Available_Hours": "sum"})
    
    grouped_data["hours_label"] = grouped_data.apply(lambda row: f"{row['Hours']}", axis=1)
    colors = ["#636EFA"] * len(grouped_data)
    # project_hours = df.groupby('Project')['Hours'].sum().reset_index()
    client_hours = df.groupby("Client_Name", as_index=False)["Hours"].sum()
    no_of_clients = df['Client_Name'].nunique()
    tot_available_hours = df['Available_Hours'].sum()
    total_no_of_hours = df['Hours'].sum()
    billed_percentage = (total_no_of_hours / tot_available_hours) * 100 if tot_available_hours > 0 else 0

    fig = make_subplots(rows=1, cols=2, column_widths=[0.75, 0.45], 
                        specs=[[{"type": "bar"}, {"type": "pie"}]])

    colors = ["green" if i % 2 == 0 else "blue" for i in range(len(grouped_data))]
    fig.add_trace(
        go.Bar(
            x=grouped_data['Month'], 
            y=grouped_data['Hours'], 
            marker_color=colors, 
            text=grouped_data["hours_label"],
            textposition='inside', 
            textangle=0,
            # hovertemplate="<b>Month:</b> %{x}<br><b>Hours:</b> %{y}",
            hovertemplate="<b>Month:</b> %{x}<br><b>Utilized Hours:</b> %{y}<br><b>Available Hours:</b> %{customdata}",
            customdata=grouped_data["Available_Hours"], 
            name="",
            showlegend=False,
        ),
        row=1, col=1
    )
    
    fig.update_layout(
        xaxis_title="<b>Month</b>", 
        yaxis_title="<b>Utilized Hours</b>",
        font = dict(
            family="Arial, sans-serif",
            size=12,
            color="black",
        ),
        bargap=0.1,
        bargroupgap=0.1,
    )

    fig.add_trace(
        go.Pie(
            labels=client_hours['Client_Name'], 
            values=client_hours['Hours'],  
            textinfo='percent', 
            hovertemplate="<b>Client:</b> %{label}<br><b>Total Hours:</b> %{value}<br><b>Percentage:</b> %{percent}",
            domain={'x': [0.65, 0.95]},
            name="",
            showlegend=True,
            hole=0.5,
        ),
        row=1, col=2
    )

    # Generate HTML Div for Plotly Graph
    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    #  <link rel="stylesheet" type="text/css" href="styles.css"> //to link external css
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Timesheet Report</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                width: 90%;
                margin: auto;
                background: white;
                padding: 20px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            }}
            h1 {{
                color: #333;
            }}
            
            .summary-container {{
                display: flex;
                justify-content: space-around;
                align-items: center;
                margin-bottom: 20px;
                width: 100%;
            }}
            
            .summary-box {{
                background-color: #84cbdb;
                border-radius: 15px 0px 15px 0px;
                font-weight: bold;
                padding: 15px;
                width: 15%; 
                text-align: center;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }}
            
            .summary-box .billed-hours {{
                font-size: 17px; 
                font-weight: bold;
            }}

            .summary-box .utilization {{
                font-size: 13px; 
                font-weight: normal;
                margin-top: 5px;
            }}
        
        </style>
    </head>
    <body>
        <div class="container">
            <h1 style="color: blue;">Timesheet Report</h1>
            <div class="summary-container">
                <div class="summary-box">
                    <span class="billed-hours">Billed Hours : {total_no_of_hours}</span><br>
                    <span class="utilization">Available Hours : {tot_available_hours}</span><br>
                    <span class="utilization">Utilization : {billed_percentage:.2f}%</span>
                </div>
            
                <div class="summary-box">
                    <span>Clients : {no_of_clients}</span>
                </div>
            </div>
            {plot_html}
        </div>
    </body>
    </html>
    """


    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Custom HTML report saved successfully as '{output_html}'")

generate_timesheet_report('D:/timesheet_data_week7.csv', 'summary.html')
