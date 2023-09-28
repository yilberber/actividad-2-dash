import dash
import dash_bootstrap_components as dbc
from dash import html

derecho = dbc.Container([
     
        html.H2('Niveles de construcción'),
        dbc.Row([
        dbc.Col(["Relacione la cantidad de niveles o plantas con la que contará su edificación"],md=12,style={'background-color':'silver'}),
        html.H2('Tipo servicio de construcción'),
        dbc.Col(["Grupo 1: Edificaciones esenciales"],md=11,style={'background-color':'silver'}),
        dbc.Col(["Grupo 2: Edificaciones riesgosas"],md=11,style={'background-color':'silver'}),
        dbc.Col(["Grupo 3: Edificaciones ocupación especial"],md=11,style={'background-color':'silver'}),
        dbc.Col(["Grupo 4: Edificaciones ocupación normal"],md=11,style={'background-color':'silver'}),
        dbc.Col(["Grupo 5: Otras edificaciones"],md=11,style={'background-color':'silver'}),
        html.Hr(),

        html.H2('Datos del proyecto'),
        html.Hr(),
        html.Label('Nombre:'),
        dbc.Input(value="Nombre"),
        html.Label('Localización:'),
        dbc.Input(value="Localización"),
        html.Label('Fecha Inicio:'),
        dbc.Input(value="Fecha", type="date"),
        html.Label('Fecha Fin:'),
        dbc.Input(value="Fecha", type="date"),

    ])
    
])