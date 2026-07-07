import plotly.express as px

def revenue_chart(df):

    fig = px.line(

        df,

        x="Month",

        y="Revenue",

        markers=True,

        title="📈 Monthly Revenue Trend"

    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.02,

        height=450,

        hovermode="x unified"

    )

    return fig
def payment_donut(df):

    import plotly.express as px

    fig = px.pie(
        df,
        names="payment_type",
        values="Revenue",
        hole=0.6,
        title="🍩 Payment Method Distribution"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig

import plotly.express as px

def state_chart(df):

    fig = px.bar(

        df,

        x="Total_Orders",

        y="customer_state",

        orientation="h",

        title="🌍 Orders by State"

    )

    fig.update_layout(

        template="plotly_white",

        height=450,

        yaxis=dict(categoryorder="total ascending")

    )

    return fig

def product_chart(df):

    fig = px.bar(

        df,

        x="Total_Sales",

        y="product_category_name",

        orientation="h",

        title="🏆 Top Product Categories"

    )

    fig.update_layout(

        template="plotly_white",

        height=450,

        yaxis=dict(categoryorder="total ascending")

    )

    return fig