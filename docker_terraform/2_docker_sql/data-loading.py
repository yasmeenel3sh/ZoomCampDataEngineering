

# get_ipython().system('pip install --only-binary=:all: pyarrow')




import pandas as pd
import pyarrow.parquet as pq
from time import time
from sqlalchemy import create_engine
import argparse,os

def main(params):
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    database=params.database
    tb=params.tb
    url=params.url

    # Get the name of the file from url
    file_name = url.rsplit('/', 1)[-1].strip()
    print(f'Downloading {file_name} ...')
    # Download file from url
    os.system(f'curl {url.strip()} -o {file_name}')
    print('\n')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')


    #read file and check schema
    file= pq.ParquetFile(file_name)
    df = next(file.iter_batches(batch_size=10)).to_pandas()
    df_iter = file.iter_batches(batch_size=100000)

    #Create table
    df.head(0).to_sql(name=tb, con=engine, if_exists='replace')





    t_start=time()
    count=0
    for batch in df_iter:
        count+=1
        batch_df= batch.to_pandas()
        print(f'inserting batch {count}')
        b_start=time()
        batch_df.to_sql(name=tb,con=engine,if_exists='append')
        b_end= time()
        print(f'inserted and time taken is {b_end-b_start:10.3f} seconds.\n')
    t_end=time()
    print(f'completed in {t_end-t_start:10.3f} seconds for {count} batches.')



if __name__=='__main__':
    parser= argparse.ArgumentParser(description='Loading data from parquet file to a postgres database.')

    parser.add_argument('--user',help='Username for Postgres.')
    parser.add_argument('--password', help='Password to the username for Postgres.')
    parser.add_argument('--host', help='Hostname for Postgres.')
    parser.add_argument('--port', help='Port for Postgres connection.')
    parser.add_argument('--database', help='Databse name for Postgres')
    parser.add_argument('--tb', help='Destination table name for Postgres.')
    parser.add_argument('--url', help='URL for .paraquet file.')

    args = parser.parse_args()
    main(args)


