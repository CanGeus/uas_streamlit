import streamlit as st
import pages
from streamlit_option_menu import option_menu

with st.sidebar:
    menu = option_menu(
        menu_title= None,
        options=['Home', 'Heroes', 'Store'],
        icons=['house-door-fill', 'people-fill', "shop"],
        menu_icon="cast", default_index=0
    )


# Pilih menu
if menu == 'Home':
    st.title('Selamat datang di Mobile Legends')
    st.write('Ini adalah tampilan beranda (home) yang berisi informasi tentang Mobile Legends.')

    st.write('Mobile Legends adalah sebuah permainan video berjenis Multiplayer Online Battle Arena (MOBA) yang dikembangkan oleh Moonton. Game ini dirancang untuk dimainkan pada perangkat seluler, seperti smartphone dan tablet. Dalam Mobile Legends, pemain bergabung dalam tim 5 vs 5 dan berusaha untuk mengalahkan tim lawan dengan tujuan akhir merusak basis lawan.')
    st.write('Setiap pemain memilih seorang hero dengan kemampuan unik yang dapat ditingkatkan selama pertandingan. Tujuan utama permainan ini adalah untuk menghancurkan "Nexus" atau "Turret" lawan dan menjaga Nexus tim sendiri agar tidak hancur. Selama pertandingan, pemain harus bekerja sama dalam tim, berkoordinasi, mengambil keputusan taktis, dan memanfaatkan kekuatan hero mereka untuk mencapai kemenangan.')
    st.write('Mobile Legends telah menjadi salah satu game mobile paling populer di berbagai negara, dan turnamen eSports sering diadakan untuk kompetisi profesional. Game ini memiliki komunitas yang besar dan aktif, serta berbagai mode permainan dan hero yang terus diperbarui untuk menjaga keseruannya.')

elif menu == 'Heroes':
    nav = option_menu(None, ['Heroes', 'Position', 'Statistik','Competition'],
                      icons=['people-fill', 'box-arrow-in-up-right', 'pie-chart-fill', 'award-fill'],
                      menu_icon="cast", default_index=0, orientation="horizontal")

    if nav == 'Heroes':
        st.title('Daftar Pahlawan (Heroes)')
        st.write('Di sini Anda dapat melihat daftar pahlawan dalam Mobile Legends.')

        # Tampilkan daftar pahlawan dari file CSV atau database
        pages.list_hero()

    elif nav == 'Position':
        st.title('Daftar Position Heroes(lane)')
        st.write('Di sini Anda dapat melihat daftar posisi hero dalam Mobile Legends.')

        # Tampilkan daftar item dari file CSV atau database
        pages.hero_lane()

    elif nav == 'Statistik':
        st.title('Statistik Heroes')
        st.write('Lihat Statistik Heroes Mobile Legends di sini.')

        # Tampilkan papan peringkat dari data yang sesuai
        pages.hero_stat()

    elif nav == 'Competition':
        pages.competition()


elif menu == 'Store':
    nav = option_menu(None, ['Home', 'Detail'],
                      icons=['house-door-fill', 'book-fill'],
                      menu_icon="cast", default_index=0, orientation="horizontal")

    if nav == 'Home':
        st.title('Store')
        pages.manga()

    elif nav == 'Detail':
        # Tampilkan daftar item dari file CSV atau database
        pages.manga_detal()