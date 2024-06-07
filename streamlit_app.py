import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def main():
    url = "https://raw.githubusercontent.com/meule/names/master/names.csv"

    df = pd.read_csv(url)

    df['num'] = df['num'] / df['total']*100

    df.drop('total', axis=1, inplace=True)

    df_female = df[df['sex'] == 'Ж'].copy()

    # Создание DataFrame для мужчин
    df_male = df[df['sex'] == 'М'].copy()

    df_female.drop('sex', axis=1, inplace=True)
    df_male.drop('sex', axis=1, inplace=True)
    df_w = pd.read_excel('w.xlsx')
    df_m = pd.read_excel('m.xlsx')
    df_w = df_w.drop(index=0).reset_index(drop=True)
    df_m = df_m.drop(index=0).reset_index(drop=True)

    df_w["NumberOfPersons"] = pd.to_numeric(df_w["NumberOfPersons"], errors='coerce').fillna(0).astype(int)

    # Найдем количество имен для каждого года
    names_per_year = df_w.groupby("Year")["NumberOfPersons"].sum().reset_index()
    names_per_year.columns = ["year", "count_names"]

    # Группируем данные по имени и году, затем считаем сумму NumberOfPersons для каждой группы
    df_sumf = df_w.groupby(["Name", "Year"])["NumberOfPersons"].sum().reset_index()
    df_sumf.columns = ['name', 'year', 'num']

    # Объединяем с данными о количестве имен в каждом году
    df_sumf = pd.merge(df_sumf, names_per_year, on='year')

    # Делим значение num на количество имен в этом году
    df_sumf['num'] = df_sumf['num'] / df_sumf['count_names']*100

    # Удаляем временный столбец count_names
    df_sumf.drop('count_names', axis=1, inplace=True)

    df_m["NumberOfPersons"] = pd.to_numeric(df_m["NumberOfPersons"], errors='coerce').fillna(0).astype(int)
    # Найдем количество имен для каждого года
    names_per_year = df_m.groupby("Year")["NumberOfPersons"].sum().reset_index()
    names_per_year.columns = ["year", "count_names"]

    # Группируем данные по имени и году, затем считаем сумму NumberOfPersons для каждой группы
    df_summ = df_m.groupby(["Name", "Year"])["NumberOfPersons"].sum().reset_index()
    df_summ.columns = ['name', 'year', 'num']

    # Объединяем с данными о количестве имен в каждом году
    df_summ = pd.merge(df_summ, names_per_year, on='year')

    # Делим значение num на количество имен в этом году
    df_summ['num'] = df_summ['num'] / df_summ['count_names']*100

    # Удаляем временный столбец count_names
    df_summ.drop('count_names', axis=1, inplace=True)
    merged_df_female = pd.concat([df_female, df_sumf], ignore_index=True)
    merged_df_female['name'] = merged_df_female['name'].apply(lambda x: x.capitalize() if x.isupper() else x.lower().capitalize())
    merged_df_female['name'] = merged_df_female['name'].replace('София, софья', 'София')
    merged_df_female['name'] = merged_df_female['name'].replace('Софья', 'София')
    merged_df_female = merged_df_female.groupby(['name', 'year'], as_index=False).agg({'num': 'sum'})

    merged_df_male = pd.concat([df_male, df_summ], ignore_index=True)
    merged_df_male['name'] = merged_df_male['name'].apply(lambda x: x.capitalize() if x.isupper() else x.lower().capitalize())
    merged_df_male['name'] = merged_df_male['name'].replace('Аарон', 'Арон')
    merged_df_male = merged_df_male.groupby(['name', 'year'], as_index=False).agg({'num': 'sum'})

    # Streamlit interface
    st.title('Процент имени по годам')

    # Выбор имени для женщин
    name_female = st.selectbox('Выберите имя для женщин', merged_df_female['name'].unique())

    # Фильтрация данных по имени для женщин
    df_name_female = merged_df_female[merged_df_female['name'] == name_female]
    df_name_female.loc[:, 'year'] = df_name_female['year'].astype(int)  # Преобразуем годы в числовой формат
    df_name_female = df_name_female.sort_values(by='year')  # Сортируем по году

    # Построение графика для женщин
    fig_female, ax_female = plt.subplots(figsize=(12, 8))
    ax_female.plot(df_name_female['year'], df_name_female['num'], linestyle='-', label=name_female)
    ax_female.set_xlabel('Год')
    ax_female.set_ylabel('Процент')
    ax_female.set_title('Процент имени по годам (Женщины)')
    ax_female.legend()

    name_male = st.selectbox('Выберите имя для мужчин', merged_df_male['name'].unique())

    # Фильтрация данных по имени для мужчин
    df_name_male = merged_df_male[merged_df_male['name'] == name_male]
    df_name_male.loc[:, 'year'] = df_name_male['year'].astype(int)  # Преобразуем годы в числовой формат
    df_name_male = df_name_male.sort_values(by='year')  # Сортируем по году

    # Построение графика для мужчин
    fig_male, ax_male = plt.subplots(figsize=(12, 8))
    ax_male.plot(df_name_male['year'], df_name_male['num'], linestyle='-', label=name_male)
    ax_male.set_xlabel('Год')
    ax_male.set_ylabel('Процент')
    ax_male.set_title('Процент имени по годам (Мужчины)')
    ax_male.legend()

    # Отображение графиков в Streamlit
    st.pyplot(fig_female)
    st.pyplot(fig_male)

if __name__ == "__main__":
    main()
