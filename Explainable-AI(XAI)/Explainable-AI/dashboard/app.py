import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Sample comparison data
comp = pd.DataFrame({
    'Method': ['SHAP','LIME'],
    'BMI_Importance': [0.45, 0.40]
})

app = Dash(__name__)
app.layout = html.Div([
    html.H2('Explainable AI – BMI-based Diabetes Risk'),
    html.P('This demo shows BMI importance comparison between SHAP and LIME.'),
    dcc.Graph(figure=px.bar(comp, x='Method', y='BMI_Importance', title='BMI Importance (Sample)'))
])

if __name__ == '__main__':
    app.run_server(debug=True)
