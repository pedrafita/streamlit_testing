#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:58:18 2024

@author: manu
"""

# streamlit_app.py
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

df2 = st.data_editor(df)

df2 = conn.update(worksheet="Conference",data=df2)
