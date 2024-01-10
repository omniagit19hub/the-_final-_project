# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
 
df = pd.read_csv('sales_data.csv')
st.set_page_config(page_title='Bike store Dashboard', page_icon='https://vmn-bike-eu.imgix.net/2023/10/bike-europe-peugeot-cycles-new-ebikes.jpg?auto=compress%2Cformat&q=50')

Home = st.container()
TopRow = st.container()
MidRow= st.container()
CartRow = st.container()
Footer = st.container()

# Footer design
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer content
st.markdown(
    '<div class="footer">Made with ❤️ by Group C</div>',
    unsafe_allow_html=True
)

# sidebar
with st.sidebar:
    st.header('Welcome to Bike Store Sales Data Analysis!')
    st.markdown('Explore the realm of data analysis! Our extensive dataset encompasses global bike sales data, featuring information across multiple countries such as Australia, Canada, France, Germany, the UK, and the US. This dataset spans from 2011 to 2016, offering a comprehensive view of sales trends.')

# Home
with Home:
    st.image('https://user-images.githubusercontent.com/7065401/58563302-42466a80-8201-11e9-9948-b3e9f88a5662.jpg')
    st.title('Bike Store Sales Data Analysis')
    st.subheader('Click the button below to show the dataset:')
    btn = st.button('Click to Show Dataset')
    if btn:
        st.write(df)
def main():
    st.title('Visualizing Customer Age Data')
    

    mean_age = df['Customer_Age'].mean().round(2)
    st.markdown("### Mean Age of Customers:")
    st.markdown(f"<div style='border: 1px solid #ccc; padding: 10px;'>{mean_age}</div>", unsafe_allow_html=True)

    
    # Plot KDE plot with mean line
    st.write("### Customer Age Distribution")
    cust_age = sns.kdeplot(df['Customer_Age'], shade=True)
    mean_line = plt.axvline(mean_age, color='red', linestyle='--', label='Mean')
    plt.xlabel('Customer Age')
    plt.legend(handles=[mean_line])
    st.pyplot()  # Display the plot in Streamlit
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    # Plot box plot
    st.write("### Box Plot of Customer Age")
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.boxplot(x=df['Customer_Age'], orient='h', ax=ax)
    st.pyplot(fig)  # Display the box plot in Streamlit
    st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == "__main__":
    main()


def main():
    st.title('Order Quantity Visualization') 

    mean_order_quantity = df['Order_Quantity'].mean().round(2)
    st.markdown("### Mean Order Quantity:")
    st.markdown(f"<div style='border: 1px solid #ccc; padding: 10px;'>{mean_order_quantity}</div>", unsafe_allow_html=True)

 
    st.write("### Order Quantity Histogram:")
    plt.figure(figsize=(14, 6))
    plt.hist(df['Order_Quantity'])
    plt.xlabel('Order Quantity')
    plt.ylabel('Frequency')
    plt.title('Order Quantity Distribution')
    st.pyplot()


        
    st.write("### Order Quantity Box Plot:")
    order_quantity_box = df['Order_Quantity'].plot(kind='box', vert=False, figsize=(14, 6))
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)


if __name__ == "__main__":
    main()


def main():
    st.title('Sales Analysis')  
    st.write("### Sales per Year:")
    sales_per_year = df['Year'].value_counts()
    st.write(sales_per_year)
        
    st.write("### Sales per Year (Pie Chart):")
    sales_per_year.plot(kind='pie', autopct='%1.1f%%', figsize= (8,8))
    plt.legend()
    st.pyplot()
        
    st.write("### Sales per Month:")
    sales_per_month = df['Month'].value_counts()
    st.write(sales_per_month)
        
    st.write("### Sales per Month (Bar Chart):")
    sales_per_month.plot(kind='bar', figsize=(14, 6))
    plt.title('Sales Per Month')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    st.pyplot()
    

if __name__ == "__main__":
    main()


def main():
    st.title('Sales Analysis by Country')
        
    st.subheader("Sales per Country (Count)")
    sales_per_country = df['Country'].value_counts()
    st.write(sales_per_country)
        
    st.write("### Sales per Country (Bar Chart):")
    plt.figure(figsize=(12, 5))
    sales_per_country.plot(kind='bar')
    plt.title('Sales Per Country')
    plt.xlabel('Country')
    plt.ylabel('Sales')
    st.pyplot()

if __name__ == "__main__":
    main()


def main():    
        
    st.write("### List of Products Sold:")
    product_list = df['Product'].unique().tolist()
    selected_product = st.selectbox("",['select a product']+ product_list)

    st.write(f"Selected Product: {selected_product}")

if __name__ == "__main__":
    main()


def main():
    st.title('Best Selling Products')
        
    st.write("### Best Selling Products (Top 10):")
    best_sellers = df['Product'].value_counts().head(10)
    plt.figure(figsize=(12, 5))
    best_sellers.plot(kind='bar')
    plt.title('Best Seller')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    st.pyplot()

if __name__ == "__main__":
    main()

def main():
    st.title('Relationship Analysis')
    
    st.write("### Relationship between Unit Cost and Unit Price:")
    plt.figure(figsize=(12, 5))
    plt.scatter(df['Unit_Cost'], df['Unit_Price'])
    plt.title('Relation between Unit Cost & Unit Price')
    plt.xlabel('Unit Cost')
    plt.ylabel('Unit Price')
    st.pyplot()
        
    st.write("### Relationship between Order Quantity and Profit:")
    plt.figure(figsize=(16, 8))
    plt.scatter(df['Order_Quantity'], df['Profit'])
    plt.title('Relation between Order Quantity and Profit')
    plt.xlabel('Order Quantity')
    plt.ylabel('Profit')
    st.pyplot()

if __name__ == "__main__":
    main()

def main():
    st.title('Relationship Analysis by Country') 
        
    st.write("### Profit per Country:")
    plt.figure(figsize=(12, 9))
    df[['Profit', 'Country']].boxplot(by='Country', figsize=(12, 9))
    plt.title('Profit by Country')
    plt.xlabel('Country')
    plt.ylabel('Profit')
    st.pyplot()
        
    st.write("### Customer Age per Country:")
    plt.figure(figsize=(12, 9))
    df[['Customer_Age', 'Country']].boxplot(by='Country', figsize=(12, 9))
    plt.title('Customer Age by Country')
    plt.xlabel('Country')
    plt.ylabel('Customer Age')
    st.pyplot()

if __name__ == "__main__":
    main()


df['Calculated_Date'] = df[['Year', 'Month', 'Day']].apply(lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)

df['Calculated_Date']= pd.to_datetime(df['Calculated_Date'])

def main():
    st.title('Sales Evolution Through The Years')
        
    st.write("### Sales Evolution Through The Years:")
    plt.figure(figsize=(16, 8))
    df['Calculated_Date'].value_counts().sort_index().plot(kind='line')
    plt.title('Sales Evolution Through The Years')
    plt.xlabel('Calculated Date')
    plt.ylabel('Sales')
    plt.legend()
    st.pyplot()

if __name__ == "__main__":
    main()


#Increase 50 U$S revenue to every sale
df['Revenue']+50


def main():
    st.title('Order Analysis')

    orders_canada_france = df.loc[(df['Country'] == 'Canada') | (df['Country'] == 'France')].shape[0]
    bike_racks_canada = df.loc[(df['Country'] == 'Canada') & (df['Sub_Category'] == 'Bike Racks')].shape[0]

    st.markdown("""
    <ul>
    <li>Number of orders made in Canada or France: <strong>{}</strong></li>
    <li>Number of Bike Racks orders made from Canada: <strong>{}</strong></li>
    </ul>
    """.format(orders_canada_france, bike_racks_canada), unsafe_allow_html=True)

if __name__ == "__main__":
    main()


def main():
    st.title('Orders in Each Region (State) of France')


    France_states = df.loc[df['Country'] == 'France', 'State'].value_counts()

    st.write("### Orders in Each Region (State) of France:")
    st.write(France_states)

    st.write("### Orders in Each state of France (Bar Chart):")
    plt.figure(figsize=(14, 6))
    France_states.plot(kind='bar')
    plt.title('Orders in Each state of France')
    plt.xlabel('States')
    plt.ylabel('Number Of Orders')
    plt.legend()
    st.pyplot()

if __name__ == "__main__":
    main()


def main():
    st.title('Sales Analysis')

    st.write("### Sales per Category:")
    sales_per_category = df['Product_Category'].value_counts()
    st.write(sales_per_category)

    st.write("### Sales Per Category (Pie Chart):")
    plt.figure(figsize=(8, 8))
    sales_per_category.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Sales Per Category')
    plt.legend()
    st.pyplot()

    st.write("### Orders per Accessory Sub-Categories:")
    accessories = df.loc[df['Product_Category'] == 'Accessories', 'Sub_Category'].value_counts()
    st.write(accessories)
    st.write("### Orders Per Accessory Sub-Categories (Bar Chart):")
    plt.figure(figsize=(14, 6))
    accessories.plot(kind='bar')
    plt.title('Numbers Of Orders Per Accessory Sub-Categories')
    plt.xlabel('Accessory Sub Category')
    plt.ylabel('Number of orders')
    plt.legend()
    st.pyplot()

    st.write("### Orders per Bike Sub-Categories:")
    bikes = df.loc[df['Product_Category'] == 'Bikes', 'Sub_Category'].value_counts()
    st.write(bikes)

    st.write("### Orders Per Bike Sub-Categories (Pie Chart):")
    plt.figure(figsize=(8, 8))
    bikes.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Orders Per Bike Sub_Category')
    plt.legend()
    st.pyplot()
if __name__ == "__main__":
    main()

 

def main():
    st.title('Sales Analysis by Gender')

    st.write("### Sales by Gender:")
    sales_by_gender = df['Customer_Gender'].value_counts()
    st.write(sales_by_gender)
    st.write("### Sales by Gender (Bar Chart):")
    plt.figure(figsize=(10, 4))
    sales_by_gender.plot(kind='bar')
    plt.title('Sales by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Number of Sales')
    st.pyplot()

    st.write("### Sales with Revenue > $500 by Men:")
    sales_over_500_by_men = df.loc[(df['Customer_Gender'] == 'M') & (df['Revenue'] > 500)].shape[0]
    st.write(f"Number of sales with revenue > $500 made by men: {sales_over_500_by_men}")

if __name__ == "__main__":
    main()

def main():
    st.title('Top Sales Analysis')

    st.write("### Top-5 Sales with Highest Revenue:")
    top_5_sales = df.sort_values(['Revenue'], ascending=False).head(5)
    st.write(top_5_sales)

    st.write("### Sale with the Highest Revenue:")
    highest_revenue = df['Revenue'].max()
    sale_highest_revenue = df[df['Revenue'] == highest_revenue]
    st.write(sale_highest_revenue)

if __name__ == "__main__":
    main()


def main():
    st.title('Order Quantity Analysis by Revenue')

    mean_order_quantity_greater_10k = df.loc[df['Revenue'] > 10000, 'Order_Quantity'].mean().round(2)
    mean_order_quantity_less_10k = df.loc[df['Revenue'] < 10000, 'Order_Quantity'].mean().round(2)

    st.markdown("### Mean Order Quantity for Orders with Revenue > $10,000:")
    st.markdown(f"<div style='border: 1px solid #ccc; padding: 10px;'>{mean_order_quantity_greater_10k}</div>", unsafe_allow_html=True)

    st.markdown("### Mean Order Quantity for Orders with Revenue < $10,000:")
    st.markdown(f"<div style='border: 1px solid #ccc; padding: 10px;'>{mean_order_quantity_less_10k}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()



def main():
    st.title('Order Analysis and Profit Visualization')


    orders_may_2016 = df.loc[(df['Year'] == 2016) & (df['Month'] == 'May')].shape[0]
    orders_may_to_july_2016 = df.loc[(df['Year'] == 2016) & (df['Month'].isin(['May', 'June', 'July']))].shape[0]

    st.markdown("### Orders Made in May 2016:")
    st.markdown(f"<div style='border: 1px solid #ccc; padding: 10px;'>{orders_may_2016}</div>", unsafe_allow_html=True)

    st.markdown("### Orders Made between May and July 2016:")
    st.markdown(f"<div style='border: 1px solid #ccc; padding: 10px;'>{orders_may_to_july_2016}</div>", unsafe_allow_html=True)


    st.write("### Grouped Box Plot of Profit Values per Month in 2016:")
    profit_2016 = df.loc[df["Year"] == 2016, ['Profit', "Month"]]
    plt.figure(figsize=(14, 6))
    profit_2016.boxplot(by="Month")
    plt.title('Grouped Box Plot of Profit Values per Month in 2016')
    plt.xlabel('Month')
    plt.ylabel('Profit')
    st.pyplot()

if __name__ == "__main__":
    main()





def apply_tax_on_sales(df):
    # Applying 7.2% tax to Unit_Price for sales within the United States
    df.loc[df["Country"] == "United States", 'Unit_Price'] *= 1.072
    return df

def main():
    st.title('Applying Tax on Sales')

    st.write("### Original Data (United States):")
    # Filtering data for the United States
    us_data = df[df['Country'] == 'United States']
    st.write(us_data)  # Displaying data for the United States

    st.write("### Applying 7.2% Tax on Sales within the United States:")
    modified_data = apply_tax_on_sales(us_data.copy())  # Applying tax on US sales
    st.write(modified_data)  # Displaying modified data with tax applied

if __name__ == "__main__":
    main()




























