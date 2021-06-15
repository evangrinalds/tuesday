"""Data visualization functions"""

from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

router = APIRouter()


@router.get('/map')
async def visual():
    # load in dataset
    DATA_PATH = 'https://raw.githubusercontent.com/evangrinalds/labs35-proofofconcept/main/data/viz.csv'
    df = pd.read_csv(DATA_PATH)

    fig = px.scatter_mapbox(df, lat="latitude", lon='longitude',
                            color="city",  # which column to use to set the color of markers
                            hover_name="zipcode",  # column added to hover information
                            size='counts',
                            zoom=4,
                            )

    fig.update_layout(mapbox_style="open-street-map")
    fig.show()

    return fig.to_json()