import pandas as pd
from sqlalchemy import create_engine

# Database credentials
user = "postgres"
password = "demoteste"
host = "localhost"
port = "5432"
database = "E-SHOP"

#Database connection
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

#csv files list
#add here all csv files names
files_list = ['itens_pedido', 'pedidos']

#Function to read all csv and save then in the database
def etl_data():
    for file in files_list:
        df = pd.read_csv(f"csv_files/{file}.csv")
        df.to_sql(f'{file}', con=engine, schema='public', if_exists='replace', index=False)
        print(f'Table {file} saved!')

etl_data()