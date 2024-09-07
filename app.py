import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go

# Load dataset
dataset = pd.read_csv(r'C:\Users\hp\Documents\datasets\heart.csv')

# Title and description
st.title('Heart Disease Dashboard')
st.markdown("## Interactive Dashboard for Healthcare Data (Heart Disease)")

# Sidebar filters
st.sidebar.header("Filters")
age_filter = st.sidebar.slider('Select Age Range', int(dataset['age'].min()), int(dataset['age'].max()), (30, 60))
sex_filter = st.sidebar.selectbox('Select Gender', options=['Both', 'Male', 'Female'], index=0)

# Apply filters
filtered_data = dataset[(dataset['age'] >= age_filter[0]) & (dataset['age'] <= age_filter[1])]
if sex_filter != 'Both':
    filtered_data = filtered_data[filtered_data['sex'] == (1 if sex_filter == 'Male' else 0)]

# Show data statistics
st.write("### Key Statistics")
st.metric(label="Total Cases", value=len(dataset))
st.metric(label="Average Cholesterol", value=round(dataset['chol'].mean(), 2))

# Show dataset
st.write("### Filtered Data")
st.write(filtered_data.head())

# Basic charts
st.write("## Basic Charts")

# Bar Chart
st.write("### Bar Chart: Disease Outcome Count")
bar_fig = px.bar(filtered_data, x='num', title='Disease Outcome Distribution')
st.plotly_chart(bar_fig)
st.write("Observation: The bar chart shows the distribution of heart disease outcomes.")

# Pie Chart
st.write("### Pie Chart: Gender Distribution")
pie_fig = px.pie(filtered_data, names='sex', title='Gender Distribution', labels={'sex': 'Gender'}, 
                 color_discrete_map={1: 'blue', 0: 'red'}, hole=0.3)
st.plotly_chart(pie_fig)
st.write("Observation: This pie chart shows the gender distribution of patients.")

# Histogram
st.write("### Histogram: Age Distribution")
hist_fig = px.histogram(filtered_data, x='age', title='Age Distribution')
st.plotly_chart(hist_fig)
st.write("Observation: The histogram indicates the distribution of ages in the filtered data.")

# Scatter Plot
st.write("### Scatter Plot: Age vs Cholesterol")
scatter_fig = px.scatter(filtered_data, x='age', y='chol', color='num', title='Age vs Cholesterol')
st.plotly_chart(scatter_fig)
st.write("Observation: This scatter plot shows the relationship between age and cholesterol levels.")

# Filter out rows with NaN values in 'trestbps'
filtered_data_no_nan = filtered_data.dropna(subset=['trestbps'])

# Bubble Plot: Age vs Cholesterol with Resting Blood Pressure
st.write("### Bubble Plot: Age vs Cholesterol with Resting Blood Pressure")
bubble_fig = px.scatter(
    filtered_data_no_nan, 
    x='age', 
    y='chol', 
    size='trestbps', 
    color='num', 
    title='Age vs Cholesterol with Blood Pressure'
)
st.plotly_chart(bubble_fig)


# Advanced charts
st.write("## Advanced Charts")

# Box and Whisker Plot
st.write("### Box Plot: Cholesterol Distribution by Disease Outcome")
box_fig = px.box(filtered_data, x='num', y='chol', title='Cholesterol Distribution by Outcome')
st.plotly_chart(box_fig)
st.write("Observation: The box plot shows the spread and outliers in cholesterol levels by disease outcome.")

# Violin Plot
fig, ax = plt.subplots()
st.write("### Violin Plot: Age Distribution by Disease Outcome")
sns.violinplot(x='num', y='age', data=filtered_data)
st.pyplot(fig)
st.write("Observation: The violin plot visualizes the age distribution for patients with and without heart disease.")

# Linear Regression Plot
st.write("### Linear Regression Plot: Age vs Cholesterol")
sns.regplot(x='age', y='chol', data=filtered_data, scatter_kws={'color':'blue'}, line_kws={'color':'red'})
st.pyplot(fig)
st.write("Observation: This linear regression plot indicates the linear relationship between age and cholesterol.")

# 3D Plot
st.write("### 3D Plot: Age, Cholesterol, and Resting Blood Pressure")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(filtered_data['age'], filtered_data['chol'], filtered_data['trestbps'], c='r', marker='o')
ax.set_xlabel('Age')
ax.set_ylabel('Cholesterol')
ax.set_zlabel('Resting Blood Pressure')
st.pyplot(fig)
st.write("Observation: The 3D chart helps visualize the relationship between age, cholesterol, and blood pressure.")

# Waterfall Chart
st.write("### Waterfall Chart: Age, Cholesterol, and Blood Pressure Contributions")
waterfall_fig = go.Figure(go.Waterfall(
    x = ["Age", "Cholesterol", "Blood Pressure"],
    y = [30, 50, -20],
    connector = {"line":{"color":"rgb(63, 63, 63)"}}
))
waterfall_fig.update_layout(title="Waterfall Chart: Health Risk Factors")
st.plotly_chart(waterfall_fig)
st.write("Observation: The waterfall chart visualizes the cumulative effect of age, cholesterol, and blood pressure.")

# Treemap
st.write("### Treemap: Disease Outcome by Gender")
treemap_fig = px.treemap(filtered_data, path=['sex', 'num'], values='age', title='Treemap: Disease Outcome by Gender')
st.plotly_chart(treemap_fig)
st.write("Observation: This treemap highlights disease outcomes for different gender groups.")

# Funnel Chart
st.write("### Funnel Chart: Cholesterol Across Age Groups")
funnel_fig = px.funnel(filtered_data, x='age', y='chol', title='Funnel Chart: Cholesterol Across Age Groups')
st.plotly_chart(funnel_fig)
st.write("Observation: The funnel chart depicts the reduction of cholesterol levels across different age groups.")

# Run the Streamlit app
if __name__ == '__main__':
    st.write("## Dashboard Completed.")
