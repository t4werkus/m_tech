FROM jupyter/base-notebook

COPY M_tech.ipynb /work/

WORKDIR /home/jovyan/app

RUN pip install pandas scipy matplotlib

EXPOSE 8888

CMD ["start-notebook.sh", "--NotebookApp.token=''"]

