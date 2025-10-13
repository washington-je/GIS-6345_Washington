#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: Week 4 Homework.ipynb
Conversion Date: 2025-10-13T02:54:32.541Z
"""

# ## Welcome to your notebook.
# 


# #### Run this cell to connect to your GIS and get started:


from arcgis.gis import GIS
gis = GIS("home")

# #### Now you are ready to start!


map1 = gis.map("Seattle, WA")

map1



# Item Added From Toolbar
# Title: USA Storm Reports | Type: Feature Service | Owner: esri_livefeeds2
item = gis.content.get("e109e8fd9c5a495c813b5cbaee9c7d9b")
item

map1.add_layer(item)