import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

izquierdo = dbc.Container(
    [
        html.H1('Nuevo Sondeo'),
        html.Hr(),
        html.Div([
        html.Label('Area del circulo'),
        dcc.Input(id = 'entradaCirculo', value = 5, type = 'number'),
        html.Label(id = 'salidaCirculo'),
        ]),

        html.Div([
                html.H2('Categoría del proyecto'),
                html.Label('Niveles de construcción '),
                dcc.Slider(
                    id='Niveles de construcción',
                    min=1,
                    max=30,
                    value=5,
                    step=1,
                    marks={i: str(i) for i in range(0, 30, 1)}
                ),
                html.Label('Tipo servicio de construcción'),
                dcc.Slider(
                    id='Tipo servicio de construcción',
                    min=1,
                    max=5,
                    value=3,
                    step=1,
                    marks={i: str(i) for i in range(0, 5, 1)}
                ),

                
                
            ]
        ),




        

    ],
    style={'background-color':'orange'}
)

