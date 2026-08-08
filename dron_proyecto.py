import numpy as np
import plotly.graph_objects as go

# =====================================================
# TERRENO (CAMPO ESCALAR)
# =====================================================

x = np.linspace(0, 120, 180)
y = np.linspace(0, 120, 180)

X, Y = np.meshgrid(x, y)

Z = (
    28*np.exp(-((X-20)**2+(Y-20)**2)/140)
    + 35*np.exp(-((X-55)**2+(Y-85)**2)/180)
    + 30*np.exp(-((X-95)**2+(Y-70)**2)/180)
    + 22*np.exp(-((X-75)**2+(Y-25)**2)/130)
    + 18*np.exp(-((X-110)**2+(Y-35)**2)/80)
)

# =====================================================
# FUNCIÓN DEL TERRENO
# =====================================================

def terreno(xp, yp):
    return (
        28*np.exp(-((xp-20)**2+(yp-20)**2)/140)
        + 35*np.exp(-((xp-55)**2+(yp-85)**2)/180)
        + 30*np.exp(-((xp-95)**2+(yp-70)**2)/180)
        + 22*np.exp(-((xp-75)**2+(yp-25)**2)/130)
        + 18*np.exp(-((xp-110)**2+(yp-35)**2)/80)
    )

# =====================================================
# RUTA ÓPTIMA (BLANCA)
# =====================================================

t = np.linspace(0, 1, 250)

x_opt = 10 + 108*t

y_opt = (
    95
    - 20*t
    + 12*np.sin(2*np.pi*t)
    + 5*np.sin(6*np.pi*t)
)

# siempre por encima del terreno

z_opt = terreno(x_opt, y_opt) + 8

# =====================================================
# RUTA NO ÓPTIMA (ROJA)
# =====================================================

x_bad = np.linspace(10,118,250)

y_bad = (
    95
    - 60*t
    + 18*np.sin(4*np.pi*t)
)

z_bad = terreno(x_bad,y_bad) + 3

# =====================================================
# FIGURA
# =====================================================

fig = go.Figure()

# =====================================================
# TERRENO
# =====================================================

fig.add_trace(
    go.Surface(
        x=X,
        y=Y,
        z=Z,
        colorscale='Turbo',
        opacity=1,
        showscale=True,
        colorbar=dict(
            title="Costo"
        )
    )
)

# =====================================================
# CILINDROS ROJOS
# =====================================================

def agregar_cilindro(cx, cy, radio, altura):

    theta = np.linspace(0, 2*np.pi, 50)
    z = np.linspace(0, altura, 30)

    Theta, Zc = np.meshgrid(theta, z)

    Xc = cx + radio*np.cos(Theta)
    Yc = cy + radio*np.sin(Theta)

    fig.add_trace(
        go.Surface(
            x=Xc,
            y=Yc,
            z=Zc,
            opacity=0.35,
            showscale=False,
            colorscale=[[0,'red'],[1,'red']]
        )
    )

agregar_cilindro(55,55,8,28)
agregar_cilindro(85,88,8,40)
agregar_cilindro(100,40,8,22)

# =====================================================
# RUTA ÓPTIMA
# =====================================================

fig.add_trace(
    go.Scatter3d(
        x=x_opt,
        y=y_opt,
        z=z_opt,
        mode='lines',
        line=dict(
            color='white',
            width=10
        ),
        name='Ruta óptima'
    )
)

# puntos verdes

idx = np.arange(0, len(x_opt), 25)

fig.add_trace(
    go.Scatter3d(
        x=x_opt[idx],
        y=y_opt[idx],
        z=z_opt[idx],
        mode='markers',
        marker=dict(
            size=7,
            color='lime',
            line=dict(
                color='white',
                width=2
            )
        ),
        name='Waypoints'
    )
)

# =====================================================
# RUTA NO ÓPTIMA
# =====================================================

fig.add_trace(
    go.Scatter3d(
        x=x_bad,
        y=y_bad,
        z=z_bad,
        mode='lines',
        line=dict(
            color='red',
            width=7,
            dash='dash'
        ),
        name='Ruta no óptima'
    )
)

# =====================================================
# INICIO
# =====================================================

fig.add_trace(
    go.Scatter3d(
        x=[x_opt[0]],
        y=[y_opt[0]],
        z=[z_opt[0]],
        mode='markers+text',
        marker=dict(
            size=12,
            color='lime'
        ),
        text=['A'],
        textposition='top center',
        textfont=dict(
        color='yellow',
        size=18
        ),
        name='A: Inicio'
    )
)

# =====================================================
# DESTINO
# =====================================================

fig.add_trace(
    go.Scatter3d(
        x=[x_opt[-1]],
        y=[y_opt[-1]],
        z=[z_opt[-1]],
        mode='markers+text',
        marker=dict(
            size=12,
            color='blue'
        ),
        text=['B'],
        textposition='top center',
        textfont=dict(
        color='yellow',
        size=18
        ),
        name='B: Destino'
    )
)

# =====================================================
# DISEÑO
# =====================================================

fig.update_layout(

    title='Optimización de Trayectoria de Dron',

    paper_bgcolor='#E7E6E5',

    scene=dict(

    bgcolor='#E7E6E5',

    xaxis=dict(
        title='X (m)',
        showbackground=True,
        backgroundcolor='black',
        gridcolor='white',
        zerolinecolor='white'
    ),

    yaxis=dict(
        title='Y (m)',
        showbackground=True,
        backgroundcolor='black',
        gridcolor='white',
        zerolinecolor='white'
    ),

    zaxis=dict(
        title='Altitud (m)',
        showbackground=True,
        backgroundcolor='black',
        gridcolor='white',
        zerolinecolor='white'
    ),

    camera=dict(
        eye=dict(
            x=1.6,
            y=1.4,
            z=0.9
        )
    )
),

    legend=dict(
        x=0.01,
        y=0.98
    )
)

fig.show()