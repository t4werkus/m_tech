# Используем базовый образ Python
FROM python:3.11

# Устанавливаем зависимости
RUN pip install pandas matplotlib seaborn streamlit scipy

# Создаем директорию для приложения внутри контейнера
WORKDIR /app

# Копируем файлы внутрь контейнера
COPY m_tech.py /app/m_tech.py
COPY М.Тех_Данные_к_ТЗ_DS.csv /app/М.Тех_Данные_к_ТЗ_DS.csv

# Экспонируем порт, который будет использоваться приложением Streamlit
EXPOSE 8501

# Команда, которая будет выполнена при запуске контейнера
CMD ["streamlit", "run", "m_tech.py"]

