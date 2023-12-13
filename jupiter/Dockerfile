FROM jupyter/base-notebook

COPY M_tech.ipynb /app/
COPY М.Тех_Данные_к_ТЗ_DS.csv /app/М.Тех_Данные_к_ТЗ_DS.csv

WORKDIR /home/jovyan/app

RUN pip install pandas scipy matplotlib

EXPOSE 8888

CMD ["start-notebook.sh", "--NotebookApp.token=''"]

