import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

def create_macro_chart(goal):
    """Creates a pie chart for target macro distribution based on goal."""
    if goal == "Gain Muscle":
        values = [30, 45, 25] # Protein, Carb, Fat
    elif goal == "Lose Weight":
        values = [40, 30, 30]
    else:
        values = [25, 50, 25]
    
    labels = ['Protein 🥩', 'Carbs 🍚', 'Fats 🥑']
    colors = ['#00F2FE', '#4FACFE', '#717171']
    
    fig = px.pie(
        names=labels, 
        values=values, 
        hole=0.4,
        color_discrete_sequence=colors,
        title="Target Macro Distribution"
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='#F1F5F9',
        margin=dict(t=40, b=0, l=0, r=0),
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )
    return fig

def create_intensity_gauge(level):
    """Creates a gauge for workout intensity."""
    levels = {"Beginner": 40, "Intermediate": 70, "Advanced": 90}
    val = levels.get(level, 50)
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = val,
        title = {'text': "Training Intensity Index 🔥"},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#00F2FE"},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.1)",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(79, 172, 254, 0.2)'},
                {'range': [50, 80], 'color': 'rgba(79, 172, 254, 0.4)'},
                {'range': [80, 100], 'color': 'rgba(79, 172, 254, 0.6)'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': val}}))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#F1F5F9',
        height=250,
        margin=dict(t=50, b=0, l=20, r=20)
    )
    return fig

def create_burn_radar(age, weight, goal):
    """Creates a radar chart for metabolic drivers."""
    # Dummy logic for radar visualization
    categories = ['Metabolism', 'Activity', 'Muscle Mass', 'Consistency', 'Sleep']
    
    if goal == "Gain Muscle":
        r = [80, 70, 90, 85, 95]
    elif goal == "Lose Weight":
        r = [90, 95, 60, 90, 80]
    else:
        r = [75, 75, 75, 75, 75]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=r,
        theta=categories,
        fill='toself',
        line_color='#00F2FE',
        name='Physical Profile'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="rgba(255,255,255,0.1)"),
            angularaxis=dict(gridcolor="rgba(255,255,255,0.1)"),
            bgcolor="rgba(0,0,0,0)"
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#F1F5F9',
        margin=dict(t=30, b=30, l=30, r=30)
    )
    return fig

def create_meal_timeline(tdee, meals):
    """Creates a bar chart showing caloric distribution over meals."""
    meal_names = [f"Meal {i+1}" for i in range(meals)]
    calories = [tdee / meals] * meals
    
    df = pd.DataFrame({'Meal': meal_names, 'Calories': calories})
    
    fig = px.bar(df, x='Meal', y='Calories', 
                 title="Optimal Caloric Distribution",
                 color_discrete_sequence=['#4FACFE'])
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='#F1F5F9',
        xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
        margin=dict(t=50, b=20, l=20, r=20)
    )
    return fig

def create_pain_gauge(val):
    """Creates a gauge for injury pain level."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = val,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Injury Pain Level ⚡"},
        gauge = {
            'axis': {'range': [None, 10], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#FF007A"}, # Vibrant pink/red for pain
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.1)",
            'steps': [
                {'range': [0, 3], 'color': 'rgba(0, 242, 254, 0.2)'},
                {'range': [3, 7], 'color': 'rgba(255, 165, 0, 0.3)'},
                {'range': [7, 10], 'color': 'rgba(255, 0, 0, 0.4)'}],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': val}}))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#FFFFFF',
        height=250,
        margin=dict(t=50, b=0, l=20, r=20)
    )
    return fig
