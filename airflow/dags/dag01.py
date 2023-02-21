from airflow import DAG
from airflow.operators.empty import EmptyOperator
import datetime as dt


with DAG(
    dag_id="Sumar numeritos",
    start_date="Primer DAG",
    start_date=dt.datetime(2023,2,20),
    schedule_interval="@once") as dag:

    t1 = 