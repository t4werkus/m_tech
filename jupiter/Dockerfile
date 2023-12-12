FROM jupyter/base-notebook

COPY m_tech.ipynd /home/jovyan/work/

RUN pip install pandas scipy matplotlib

EXPOSE 8888

CMD ["start-notebook.sh", "--NotebookApp.token=''"]

