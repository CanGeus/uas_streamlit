import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image


def list_hero():
    df = pd.read_csv('mlbb_hero.csv')

    # Filter pengurutan
    sorting_options = ['Name', 'HP', 'Mana', 'Primary_Role']
    selected_sorting = st.selectbox('Sort Heroes By:', sorting_options)

    # Membagi layar menjadi 4 kolom
    col1, col2, col3, col4 = st.columns(4)

    # Urutkan DataFrame berdasarkan pilihan pengguna
    if selected_sorting == 'Name':
        df = df.sort_values(by='Name')
    elif selected_sorting == 'HP':
        df = df.sort_values(by='Hp', ascending=False)
    elif selected_sorting == 'Mana':
        df = df.sort_values(by='Mana', ascending=False)
    elif selected_sorting == 'Primary_Role':
        df = df.sort_values(by='Primary_Role')

    # Tampilkan data dari file CSV dalam 4 kolom
    for index, row in df.iterrows():
        if index % 4 == 0:
            col1.image(row["Link"], caption=row["Name"], use_column_width=True)
        elif index % 4 == 1:
            col2.image(row["Link"], caption=row["Name"], use_column_width=True)
        elif index % 4 == 2:
            col3.image(row["Link"], caption=row["Name"], use_column_width=True)
        else:
            col4.image(row["Link"], caption=row["Name"], use_column_width=True)

def hero_lane():
    # Load the CSV data
    data = pd.read_csv('mlbb_hero.csv')

    # Create a multiselect box to choose a lane
    selected_lanes = st.multiselect("Select Lanes:", data['Lane'].unique())

    # Filter the data for the selected lanes
    filtered_data = data[data['Lane'].isin(selected_lanes)]

    # Display the selected lanes' data
    if not filtered_data.empty:
        # Create a Streamlit column to organize elements
        col1, col2 = st.columns(2)  # Set column widths

        best_hero = None
        best_score = 0  # Inisialisasi skor terbaik

        # Create a chart for each selected hero
        for hero_name in filtered_data['Name'].unique():
            hero_data = filtered_data[filtered_data['Name'] == hero_name]
            stats = hero_data[[
                "Hp", "Hp_Regen", "Mana", "Mana_Regen",
                "Phy_Damage", "Mag_Damage", "Phy_Defence", "Mag_Defence", "Mov_Speed"
            ]].iloc[0]

            # Menghitung skor berdasarkan semua statistik
            score = stats.sum()

            chart_data = pd.DataFrame({
                'Stat': stats.index,
                'Value': stats.values
            })

            chart = alt.Chart(chart_data).mark_bar().encode(
                x=alt.X('Value:Q', title=''),
                y=alt.Y('Stat:N', title='')
            ).properties(
                width=700,
                height=380
            )

            # Menentukan hero terbaik berdasarkan skor
            if score > best_score:
                best_hero = hero_name
                best_score = score

            # Add the labels and images for each selected hero with CSS for alignment
            with col1:
                st.markdown(
                    f'<div style="display: flex; align-items: center; text-align: center;">'
                    f'<div style="flex: 1;">'
                    f'<h2>{hero_name}</h2>'
                    f'<img src="{hero_data["Link"].values[0]}" style="max-width: 100%;" />'
                    f'</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )

            # Display the comparison chart for each hero
            with col2:
                st.altair_chart(chart, use_container_width=True)

        # Tampilan kesimpulan dengan tampilan menarik
        # st.markdown(
        #     f'<div style="background-color: #007BFF; color: white; padding: 20px; border-radius: 10px; text-align: center;">'
        #     f'<h2>Best Hero based on Total Score</h2>'
        #     f'<h3>{best_hero} with a total score of {best_score}</h3>'
        #     f'</div>',
        #     unsafe_allow_html=True
        # )

    else:
        st.warning("No data found for the selected lanes.")

def hero_stat():
    import streamlit as st
    import pandas as pd
    import altair as alt

    # Load the CSV data
    data = pd.read_csv('mlbb_hero.csv')


    # Create a multiselect box to choose multiple heroes
    selected_heroes = st.multiselect("Select Heroes:", data['Name'].unique())

    # Filter the data for the selected heroes
    filtered_data = data[data['Name'].isin(selected_heroes)]

    # Display the selected heroes' data
    if not filtered_data.empty:
        st.markdown(
            f'<div style="text-align:center"><h1>Statistics Comparison</h1></div>',
            unsafe_allow_html=True
        )

        # Create a Streamlit column to organize elements
        col1, col2 = st.columns(2)  # Set column widths

        best_hero = None
        best_score = 0  # Inisialisasi skor terbaik

        # Create a chart for each selected hero
        for hero_name in selected_heroes:
            hero_data = filtered_data[filtered_data['Name'] == hero_name]
            stats = hero_data[[
                "Hp", "Hp_Regen", "Mana", "Mana_Regen",
                "Phy_Damage", "Mag_Damage", "Phy_Defence", "Mag_Defence", "Mov_Speed"
            ]].iloc[0]

            # Menghitung skor berdasarkan semua statistik
            score = stats.sum()

            chart_data = pd.DataFrame({
                'Stat': stats.index,
                'Value': stats.values
            })

            chart = alt.Chart(chart_data).mark_bar().encode(
                x=alt.X('Value:Q', title=''),
                y=alt.Y('Stat:N', title='')
            ).properties(
                width=700,
                height=380
            )

            # Menentukan hero terbaik berdasarkan skor
            if score > best_score:
                best_hero = hero_name
                best_score = score

            # Add the labels and images for each selected hero with CSS for alignment
            with col1:
                st.markdown(
                    f'<div style="display: flex; align-items: center; text-align: center;">'
                    f'<div style="flex: 1;">'
                    f'<h2>{hero_name}</h2>'
                    f'<img src="{hero_data["Link"].values[0]}" style="max-width: 100%;" />'
                    f'</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )

            # Display the comparison chart for each hero
            with col2:
                st.altair_chart(chart, use_container_width=True)

        # Tampilan kesimpulan dengan tampilan menarik
        st.markdown(
            f'<div style="background-color: #007BFF; color: white; padding: 20px; border-radius: 10px; text-align: center;">'
            f'<h2>Best Hero based on Total Score</h2>'
            f'<h3>{best_hero} with a total score of {best_score}</h3>'
            f'</div>',
            unsafe_allow_html=True
        )

    else:
        st.warning("No data found for the selected heroes.")


def hero_data():
    # Load the CSV data
    data = pd.read_csv('mlbb_hero.csv')
    # Define a Streamlit app
    st.title("Data Mobile Legends: Bang Bang Heroes Data")

    # Create a select box to choose a hero
    selected_hero = st.selectbox("Select a Hero:", data['Name'].unique())

    # Filter the data for the selected hero
    filtered_data = data[data['Name'] == selected_hero]

    # Display the selected hero's data
    if not filtered_data.empty:
        st.markdown(
            f'<div style="text-align:center"><h1>Statistik {selected_hero}</h1></div>',
            unsafe_allow_html=True
        )
        # List of statistics to display
        stats = ["Hp", "Hp_Regen", "Mana", "Mana_Regen", "Phy_Damage", "Mag_Damage", "Phy_Defence", "Mag_Defence",
                 "Mov_Speed"]

        # Create a horizontal bar chart for each statistic
        chart_data = pd.DataFrame({
            'Stat': stats,
            'Value': [filtered_data[stat].values[0] for stat in stats]
        })

        chart = alt.Chart(chart_data).mark_bar().encode(
            x=alt.X('Value:Q', title=''),
            y=alt.Y('Stat:N', title='')
        ).properties(
            width=700,
            height=380
        )

        # Create a Streamlit column to organize elements
        col1, col2 = st.columns([1, 2])  # Mengatur lebar kolom

        # Add the label "Hp" to the left of the progress bar
        with col1:
            # Perkecil gambar dengan CSS
            st.image(filtered_data['Link'].values[0], use_column_width=True, output_format='PNG', width=100)

        # Display a completion message
        with col2:
            st.altair_chart(chart, use_container_width=True)

    else:
        st.warning("No data found for the selected hero.")

def competition():
    # Membaca data dari file CSV
    df = pd.read_csv('combined_file.csv')

    # Opsi filter untuk mengurutkan hero
    sort_option = st.selectbox("Urutkan berdasarkan:", ["Nama", "Winrate", "Ban"])

    # Mengurutkan DataFrame berdasarkan pilihan pengguna
    if sort_option == "Nama":
        sorted_df = df.sort_values(by='Name')
    elif sort_option == "Winrate":
        sorted_df = df.sort_values(by='Bs_winrate', ascending=False)
    elif sort_option == "Ban":
        sorted_df = df.sort_values(by='Ban_percentage', ascending=False)

    # Menampilkan data dengan gambar yang lebih kecil, nama, dan keterangan di sebelah gambar
    for index, row in sorted_df.iterrows():
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f'<img src="{row["Link"]}" style="max-width: 90%;" />'
                f'<hr/>'
                ,
                unsafe_allow_html=True
            )

        with col2:
            st.title(row['Name'])
            st.write("Winrate:", row['Bs_winrate'])
            st.write("Ban:", row['Ban_percentage'])
            st.write("Pick & Ban:", row['Pick&Ban percentage'])

def manga():
    # Load data from the CSV file
    data = pd.read_csv("manga.csv")

    # Set the number of manga items to display in one column
    items_per_column = 5

    # Split the data into multiple columns
    num_manga = len(data)
    num_columns = (num_manga + items_per_column - 1) // items_per_column

    st.write("List of Manga")

    # Create columns for manga display
    for column_idx in range(num_columns):
        manga_column = st.columns(items_per_column)

        start_idx = column_idx * items_per_column
        end_idx = min((column_idx + 1) * items_per_column, num_manga)

        for manga_idx in range(start_idx, end_idx):
            manga = data.iloc[manga_idx]
            with manga_column[manga_idx % items_per_column]:
                # Display the image from the link
                st.image(manga["Link"], use_column_width=True)

                # Custom CSS untuk mengatur posisi tombol ke tengah
                custom_css = f"""
                <style>
            .stButton > button {{
                border: none;
                background-color: transparent;
                display: block;
                margin: auto;
                margin-top: -35px;
            }}
            
            .stButton:hover > button,
            .stButton:active > button {{
                border: none;
                background-color: transparent;
            }}
        </style>
                """
                st.markdown(custom_css, unsafe_allow_html=True)
                st.button(label=manga["Manga series"])

def manga_detal():
    # Baca data dari manga.csv
    data = pd.read_csv("manga.csv")

    # Tampilkan judul
    st.title("Detail Manga")

    # Buat kolom untuk mengambil judul manga yang akan ditampilkan
    selected_manga = st.selectbox("Pilih Manga", data["Manga series"])

    # Cari baris yang sesuai dengan manga yang dipilih
    manga_row = data[data["Manga series"] == selected_manga]

    # Menggunakan layout kolom untuk mengatur tampilan
    col1, col2 = st.columns(2)

    # Tampilkan gambar di kolom pertama
    with col1:
        img_url = manga_row["Link"].values[0]
        image = Image.open(img_url)
        image = image.resize((300, 400))  # Ubah ukuran gambar sesuai yang Anda inginkan
        st.image(image, caption=selected_manga)

    # Tampilkan detail manga di kolom kedua
    with col2:
        st.subheader(f"Detail Manga {selected_manga}")
        st.write(f"**Judul:** {selected_manga}")
        st.write(f"**Author:** {manga_row['Author'].values[0]}")
        st.write(f"**Publisher:** {manga_row['Publisher'].values[0]}")
        st.write(f"**Demographic:** {manga_row['Demographic'].values[0]}")
        st.write(f"**Jumlah Volume:** {manga_row['No. of collected volumes'].values[0]}")
        st.write(f"**Tanggal Serialisasi:** {manga_row['Serialized'].values[0]}")
        st.write(f"**Penjualan :** {manga_row['Approximate sales in million'].values[0]} Juta")
        st.write(
            f"**Rata-rata Penjualan per Volume:** {manga_row['Average sales per volume in million'].values[0]} Juta")


