import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from scipy.stats import ttest_ind, levene

file_path = st.file_uploader("Загрузите файл CSV", type=["csv"])
if file_path is not None:
    data = pd.read_csv(file_path)
    data.columns = ["sick_days", "age", "gender"]

    work_days_threshold = st.slider("Выберите порог пропущенных рабочих дней:", min_value=0, max_value=10, value=2)
    filtered_data = data[data['sick_days'] > work_days_threshold]

    mens = filtered_data[filtered_data['gender'] == "М"]
    women = filtered_data[filtered_data['gender'] == "Ж"]

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(filtered_data, x='sick_days', kde=True, hue='gender', element='step', stat='density',
                 common_norm=False, ax=ax, palette={'М': 'blue', 'Ж': 'pink'})

    ax.set_title('Распределение количества пропущенных дней по полу')
    ax.set_xlabel('Количество пропущенных дней')
    ax.set_ylabel('Плотность')
    st.pyplot(fig)

    statistic, p_value_levene = levene(mens['sick_days'], women['sick_days'])

    if p_value_levene > 0.05:
        # Равенство дисперсий не отвергается, можно использовать equal_var=True
        t_statistic, p_value_ttest = ttest_ind(mens['sick_days'], women['sick_days'], equal_var=True)
    else:
        # Равенство дисперсий отвергается, использовать equal_var=False
        t_statistic, p_value_ttest = ttest_ind(mens['sick_days'], women['sick_days'], equal_var=False)
    st.write(
        "Предположим, что гипотеза H0 - Мужчины пропускают в течение года более 2 рабочих дней по болезни столько же сколько и женщины.\n"
        "H1 - кол-во пропусков у мужчин значительно больше, чем у женщин.\n"
        "Воспользуемся t-тестом для независимых выборок и если p-value < 0.05, то гипотезу H0 отвергаем.")
    st.write("Результат проверки гипотезы 1:")
    st.write(f"p-value: {round(p_value_ttest, 4)}, t-статистика: {round(t_statistic, 4)}")
    st.write("Гипотеза отвергается" if p_value_ttest < 0.05 else "Гипотеза не отвергается")
    st.write("\n")
    st.write("\n")
    
    age_threshold = st.slider("Выберите возрастной порог:", min_value=20, max_value=60, value=35)
    work_days_threshold_1 = st.slider("Выберите порог пропущенных рабочих дней для 2 гипотезы:", min_value=0, max_value=10, value=2)

    # Фильтрация данных для первого способа визуализации
    younger = data[(data['age'] > age_threshold) & (data['sick_days'] > work_days_threshold_1)]
    older = data[(data['age'] <= age_threshold) & (data['sick_days'] > work_days_threshold_1)]

    # Визуализация данных для фильтра
    st.title('Гистограмма больничных')

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    sns.histplot(older['sick_days'], bins=20, kde=False, ax=axes[0])
    axes[0].set_title(f'Старше {age_threshold} лет')
    sns.histplot(younger['sick_days'], bins=20, kde=False, ax=axes[1])
    axes[1].set_title(f'Моложе {age_threshold} лет')

    fig.text(0.5, 0.04, 'Больничные', ha='center', va='center')
    fig.text(0.04, 0.5, 'Частота', ha='center', va='center', rotation='vertical')

    plt.tight_layout()
    st.pyplot(fig)

    statistic, p_value_levene = levene(older['sick_days'], younger['sick_days'])

    if p_value_levene > 0.05:
        # Равенство дисперсий не отвергается, можно использовать equal_var=True
        t_statistic, p_value_ttest = ttest_ind(older['sick_days'], younger['sick_days'], equal_var=True)
    else:
        # Равенство дисперсий отвергается, использовать equal_var=False
        t_statistic, p_value_ttest = ttest_ind(older['sick_days'], younger['sick_days'], equal_var=False)
    st.write(f"Предположим, что гипотеза H0 - Работники старше {age_threshold} лет пропускают в течение года более 2 рабочих дне по болезни столько же как и коллеги помоложе.")
    st.write("H1 - кол-во пропусков у этих старшей группы значительно больше.")
    st.write("Воспользуемся t-тестом для независимых выборок и если p-value < 0.05, то гипотезу H0 отвергаем.")
    st.write(f"Результат проверки гипотезы 2:")
    st.write(f"p-value: {round(p_value_ttest, 4)}, t-статистика: {round(t_statistic, 4)}")
    st.write("Гипотеза отвергается" if p_value_ttest < 0.05 else "Гипотеза не отвергается")
