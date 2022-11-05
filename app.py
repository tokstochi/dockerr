#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import os
import psycopg2
import psycopg2.extras as extras


# In[6]:


pwd


# In[22]:


df = pd.read_csv(r"C:\Users\tokst\Downloads\orders.csv")


# In[23]:


df.head()


# In[24]:


df


# In[19]:


database='postgres'
user='postgres'
password='mysecretpassword'
host='localhost'
port='5432'


# In[20]:


def create_server_connection():
    connection = None
    try:

        connection = psycopg2.connect(
            database = database,
            user = user,
            password = password,
            host = host,
            port = port
        )
        
        print("PostgreSql Database connection successful")
    except Error:
        print(f"Error")

    return connection


# In[25]:


conn = create_server_connection()


# In[29]:


def load_df_to_warehouse(conn, df, table):

    tuples = [list(row) for row in df.itertuples(index=False)]

    cols = ','.join(list(df.columns))
    
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)                   
    cursor = conn.cursor()
    
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
      
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    except psycopg2.InterfaceError:
        pass
    print("the dataframe is inserted")
    cursor.close()


# In[30]:


load_df_to_warehouse(conn, df, 'public.orders')

