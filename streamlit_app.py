import pandas as pd
import streamlit as st

# Установка иконки и заголовка страницы
st.set_page_config(page_title="Данные пассажиров Титаника", page_icon="🚢")

# Добавление заголовка и описания
st.title("🚢 Данные пассажиров Титаника")
st.write(
    """
    Для просмотра данных только по спасенным или погибшим, выберите соответствующий пункт из списка:
    """
)

# Загрузка данных
@st.cache_data
def load_data():
    df = pd.read_csv("/mnt/data/titanic_train [tsKg9Q].csv")  # Подставляем правильный путь к загруженному файлу
    return df

df = load_data()

# Визуализация картинки (путь к изображению)
st.image("/mnt/data/image.png", caption="Титаник", use_column_width=True)

# Создание выпадающего списка для фильтрации по статусу выживания
survived_option = st.selectbox(
    "Значение поля Survived:",
    options=["Любое", "Спасены", "Погибшие"],
)

# Преобразование выбора в соответствующие числовые значения
if survived_option == "Спасены":
    df_filtered = df[df['Survived'] == 1]
elif survived_option == "Погибшие":
    df_filtered = df[df['Survived'] == 0]
else:
    df_filtered = df

# Подсчет среднего возраста по классу обслуживания
average_age_by_class = df_filtered.groupby('Pclass')['Age'].mean().reset_index()
average_age_by_class.columns = ['Класс обслуживания', 'Средний возраст']

# Отображение таблицы с результатами
st.write("Результаты по выбранному фильтру:")
st.dataframe(average_age_by_class, use_container_width=True)

# Вывод общей информации
st.write(f"Всего пассажиров: {len(df_filtered)}")
st.write(f"Спасено: {len(df[df['Survived'] == 1])}")
st.write(f"Погибло: {len(df[df['Survived'] == 0])}")
