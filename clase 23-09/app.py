import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
#importamos el frontend
from frontend.main import layout
import math
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
                
app.layout = layout


@app.callback(
    Output('salidaCirculo', 'children'),
    Input('entradaCirculo', 'value'),
)
def areaCirculo(entradaCirculo):
    areaCirculo = math.pi * (entradaCirculo**2)
    return 'El área del circulo es: ' + str(areaCirculo)

if __name__ == '__main__' :
    app.run_server(debug=True)
                
                
                