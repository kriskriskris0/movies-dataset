import pandas as pd
import streamlit as st

# Установка иконки и заголовка страницы
st.set_page_config(page_title="Данные пассажиров Титаника", page_icon="🚢")
st.title("🚢 Данные пассажиров Титаника")

# Описание приложения
st.write(
    """
    Это интерактивное приложение отображает данные о пассажирах Титаника.
    Выберите пункт посадки, чтобы увидеть количество спасенных и погибших.
    """
)

# Загрузка данных
@st.cache_data
def load_data():
    df = pd.read_csv("/mnt/data/titanic_train [tsKg9Q].csv")  # Загружаем твой файл с данными
    return df

df = load_data()

# Создание выпадающего списка для фильтрации по пункту посадки
embarked_option = st.selectbox(
    "Выберите пункт посадки (Embarked):",
    options=["Все", "C - Cherbourg", "Q - Queenstown", "S - Southampton"]
)

# Фильтрация данных по пункту посадки
if embarked_option == "C - Cherbourg":
    df_filtered = df[df['Embarked'] == 'C']
elif embarked_option == "Q - Queenstown":
    df_filtered = df[df['Embarked'] == 'Q']
elif embarked_option == "S - Southampton":
    df_filtered = df[df['Embarked'] == 'S']
else:
    df_filtered = df

# Подсчет спасенных и погибших
survived_count = df_filtered[df_filtered['Survived'] == 1].shape[0]
not_survived_count = df_filtered[df_filtered['Survived'] == 0].shape[0]

# Отображение результатов
st.write(f"Количество спасенных: {survived_count}")
st.write(f"Количество погибших: {not_survived_count}")

# Отображение таблицы с результатами
st.dataframe(df_filtered[['PassengerId', 'Pclass', 'Name', 'Survived', 'Embarked']], use_container_width=True)
