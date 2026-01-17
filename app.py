import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Title
st.title("Application Web Interactive avec Streamlit et DuckDB")

# File upload
uploaded_file = st.file_uploader("Téléversez un fichier CSV contenant des données de ventes", type="csv")

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :")
    st.dataframe(df.head())

    # Assume columns: date, region, product, sales_amount
    # You may need to adjust based on actual CSV

    # Connect to DuckDB
    con = duckdb.connect(database='sales.db', read_only=False)

    # Create table
    con.execute("CREATE OR REPLACE TABLE sales AS SELECT * FROM df")

    # Filters
    st.sidebar.header("Filtres")

    # Date filter - assume date column is 'date'
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        min_date = df['date'].min()
        max_date = df['date'].max()
        date_range = st.sidebar.date_input("Sélectionnez la période", [min_date, max_date])
        if len(date_range) == 2:
            start_date, end_date = date_range
            filter_query = f"WHERE date >= '{start_date}' AND date <= '{end_date}'"
        else:
            filter_query = ""
    else:
        filter_query = ""

    # Region filter
    if 'region' in df.columns:
        regions = con.execute(f"SELECT DISTINCT region FROM sales {filter_query}").fetchall()
        regions = [r[0] for r in regions]
        selected_regions = st.sidebar.multiselect("Régions", regions, default=regions)
        if selected_regions:
            region_filter = "AND region IN (" + ",".join(f"'{r}'" for r in selected_regions) + ")"
        else:
            region_filter = ""
    else:
        region_filter = ""

    # Product filter
    if 'product' in df.columns:
        products = con.execute(f"SELECT DISTINCT product FROM sales {filter_query} {region_filter}").fetchall()
        products = [p[0] for p in products]
        selected_products = st.sidebar.multiselect("Produits", products, default=products)
        if selected_products:
            product_filter = "AND product IN (" + ",".join(f"'{p}'" for p in selected_products) + ")"
        else:
            product_filter = ""
    else:
        product_filter = ""

    full_filter = filter_query + " " + region_filter + " " + product_filter

    # KPIs
    st.header("Indicateurs Clés de Performance")

    # KPI 1: Total Sales
    total_sales = con.execute(f"SELECT SUM(sales_amount) as total FROM sales {full_filter}").fetchone()[0]
    st.metric("Ventes Totales", f"${total_sales:,.2f}")

    # KPI 2: Average Sales per Transaction
    avg_sales = con.execute(f"SELECT AVG(sales_amount) as avg FROM sales {full_filter}").fetchone()[0]
    st.metric("Ventes Moyennes par Transaction", f"${avg_sales:,.2f}")

    # KPI 3: Number of Transactions
    num_transactions = con.execute(f"SELECT COUNT(*) as count FROM sales {full_filter}").fetchone()[0]
    st.metric("Nombre de Transactions", num_transactions)

    # KPI 4: Top Region
    if 'region' in df.columns:
        top_region = con.execute(f"SELECT region, SUM(sales_amount) as total FROM sales {full_filter} GROUP BY region ORDER BY total DESC LIMIT 1").fetchone()
        st.metric("Région avec les Plus Hautes Ventes", f"{top_region[0]}: ${top_region[1]:,.2f}")

    # Visualizations
    st.header("Visualisations")

    col1, col2 = st.columns(2)

    with col1:
        # Visualization 1: Sales over time
        if 'date' in df.columns:
            sales_over_time = con.execute(f"SELECT date, SUM(sales_amount) as total FROM sales {full_filter} GROUP BY date ORDER BY date").fetchall()
            sales_df = pd.DataFrame(sales_over_time, columns=['date', 'total'])
            fig1 = px.line(sales_df, x='date', y='total', title="Évolution des Ventes dans le Temps")
            st.plotly_chart(fig1)

        # Visualization 2: Sales by Region
        if 'region' in df.columns:
            sales_by_region = con.execute(f"SELECT region, SUM(sales_amount) as total FROM sales {full_filter} GROUP BY region").fetchall()
            region_df = pd.DataFrame(sales_by_region, columns=['region', 'total'])
            fig2 = px.bar(region_df, x='region', y='total', title="Ventes par Région")
            st.plotly_chart(fig2)

    with col2:
        # Visualization 3: Sales by Product
        if 'product' in df.columns:
            sales_by_product = con.execute(f"SELECT product, SUM(sales_amount) as total FROM sales {full_filter} GROUP BY product ORDER BY total DESC LIMIT 10").fetchall()
            product_df = pd.DataFrame(sales_by_product, columns=['product', 'total'])
            fig3 = px.bar(product_df, x='product', y='total', title="Top 10 Produits par Ventes")
            st.plotly_chart(fig3)

        # Visualization 4: Sales Distribution
        sales_dist = con.execute(f"SELECT sales_amount FROM sales {full_filter}").fetchall()
        sales_list = [s[0] for s in sales_dist]
        fig4 = px.histogram(sales_list, title="Distribution des Montants de Ventes")
        st.plotly_chart(fig4)

    con.close()
else:
    st.write("Veuillez téléverser un fichier CSV pour commencer.")