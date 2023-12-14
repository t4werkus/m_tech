FROM jupyter/base-notebook

USER root

COPY M_tech.ipynb /home/jovyan/app/
COPY М.Тех_Данные_к_ТЗ_DS.csv /home/jovyan/app/

WORKDIR /home/jovyan/app

RUN chown -R jovyan:users /home/jovyan/app

USER jovyan

RUN pip install pandas scipy matplotlib

EXPOSE 8888

CMD ["start-notebook.sh", "--NotebookApp.token=''"]
