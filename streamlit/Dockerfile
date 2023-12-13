FROM python:3.11

RUN pip install pandas matplotlib seaborn streamlit scipy

COPY m_tech.py /app/m_tech.py
COPY М.Тех_Данные_к_ТЗ_DS.csv /app/М.Тех_Данные_к_ТЗ_DS.csv

WORKDIR /app

EXPOSE 8501

CMD ["streamlit", "run", "m_tech.py"]
