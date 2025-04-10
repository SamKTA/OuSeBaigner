import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import io
import random

# Configuration de la page
st.set_page_config(
    page_title="Où se baigner ? - Qualité des eaux en Nouvelle-Aquitaine",
    page_icon="💦",
    layout="wide"
)

# Titre et introduction
st.title("🏊 Où se baigner ? - Qualité des eaux en Nouvelle-Aquitaine")
st.markdown("""
Cette application vous permet de trouver des points de baignade en Nouvelle-Aquitaine 
et de consulter la qualité de l'eau. Recherchez par ville ou filtrez selon vos critères !
""")

# Création du dataframe à partir des données extraites
def create_data():
    # Définition des codes de qualité et leur signification
    quality_codes = {
        "E": "Excellente qualité",
        "B": "Bonne qualité",
        "S": "Qualité suffisante",
        "I": "Qualité insuffisante",
        "P": "Insuffisamment de prélèvements",
        "N": "Site non classé"
    }
    
    # Données extraites des PDFs
    data = []
    
    # 87 - HAUTE-VIENNE
    locations_87 = [
        ["AMBAZAC", "JONAS", "douce", "5N"],
        ["BEAUMONT-DU-LAC", "NERGOUT", "douce", "5E"],
        ["BEAUMONT-DU-LAC", "PIERREFITTE", "douce", "5E"],
        ["BESSINES-SUR-GARTEMPE", "SAGNAT", "douce", "5E"],
        ["BUJALEUF", "SAINTE-HELENE", "douce", "5E"],
        ["BUSSIERE-GALANT", "PLAN D'EAU DE BUSSIERE-GALANT", "douce", "5E"],
        ["CHATEAU-CHERVIX", "ETANG DU PUY-CHAUMARTIN", "douce", "5E"],
        ["CHATEAUNEUF-LA-FORET", "PLAN D'EAU DE CHATEAUNEUF-LA-FORET", "douce", "5P"],
        ["CHEISSOUX", "CAMPING LOUS SUAIS", "douce", "5E"],
        ["COGNAC-LA-FORET", "PLAN D'EAU DE COGNAC-LA-FORET", "douce", "5E"],
        ["COMPREIGNAC", "LES CHABANNES", "douce", "5E"],
        ["FLAVIGNAC", "SAINT FORTUNAT", "douce", "5E"],
        ["MEUZAC", "LA ROCHE", "douce", "5E"],
        ["PEYRAT-LE-CHATEAU", "AUPHELLE", "douce", "5E"],
        ["PEYRAT-LE-CHATEAU", "ETANG DU BOURG DE PEYRAT-LE-CHATEAU", "douce", "5E"],
        ["RAZES", "SANTROP", "douce", "5E"],
        ["SAINT-GERMAIN-LES-BELLES", "MONTREAL", "douce", "5E"],
        ["SAINT-HILAIRE-LES-PLACES", "PLAISANCE", "douce", "6E"],
        ["SAINT-JULIEN-LE-PETIT", "LA MAULDE", "douce", "5E"],
        ["SAINT-MARTIN-TERRESSUS", "PLAN D'EAU DU SOLEIL LEVANT", "douce", "5E"],
        ["SAINT-MATHIEU", "LE LAC", "douce", "5E"],
        ["SAINT-PARDOUX-LE-LAC", "FREAUDOUR", "douce", "5E"],
        ["SAINT-YRIEIX-LA-PERCHE", "ARFEUILLE", "douce", "5S"],
        ["SUSSAC", "LES SAULES", "douce", "5E"],
        ["SUSSAC", "PLAN D'EAU DE SUSSAC", "douce", "5E"],
        ["VIDEIX", "LA CHASSAGNE", "douce", "5E"]
    ]
    
    for item in locations_87:
        data.append({
            "departement": "87",
            "departement_nom": "HAUTE-VIENNE",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine"
        })
    
    # 86 - VIENNE
    locations_86 = [
        ["BEAUMONT SAINT-CYR", "ST CYR - PARC DE LOISIRS (ETANG)", "douce", "6E"],
        ["BONNEUIL-MATOURS", "BONNEUIL MATOURS - PARC DE CREMAULT (LA VIENNE)", "douce", "5B"],
        ["BUSSIERE (LA)", "LA BUSSIERE - LA BERTHOLIERE (LA GARTEMPE)", "douce", "5I"],
        ["CHATELLERAULT", "CHATELLERAULT - LAC DE LA FORET", "douce", "5E"],
        ["LATHUS-SAINT-REMY", "LATHUS ST REMY - LA VOULZIE", "douce", "5I"],
        ["LUSIGNAN", "LUSIGNAN - CAMPING (LA VONNE)", "douce", "5E"],
        ["MONCONTOUR", "MONCONTOUR - PLAN D'EAU DU GRAND MAGNE (LA DIVE)", "douce", "5E"],
        ["POITIERS", "POITIERS - TISON", "douce", "6N"],
        ["PUYE (LA)", "LA PUYE - PLAN D'EAU COMMUNAL", "douce", "5P"],
        ["QUEAUX", "QUEAUX - CAMPING (LA VIENNE)", "douce", "5I"],
        ["ROCHE-POSAY (LA)", "LA ROCHE-POSAY (BAIGNADE SUR LA CREUSE)", "douce", "5B"],
        ["SAINT-MACOUX", "ST MACOUX - PLAN D'EAU COMMUNAL DU MARAIS", "douce", "5E"],
        ["SAINT-MARTIN-L'ARS", "ST MARTIN L'ARS - PLAN D'EAU COMMUNAL (LE CLAIN)", "douce", "0P"]
    ]
    
    for item in locations_86:
        data.append({
            "departement": "86",
            "departement_nom": "VIENNE",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine"
        })
    
    # 79 - DEUX-SEVRES
    locations_79 = [
        ["CHERVEUX", "PLAN D'EAU DE CHERVEUX", "douce", "6E"],
        ["VERRUYES", "PLAN D'EAU DE VERRUYES", "douce", "6E"]
    ]
    
    for item in locations_79:
        data.append({
            "departement": "79",
            "departement_nom": "DEUX-SEVRES",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine"
        })
    
    # 64 - PYRENEES-ATLANTIQUES (échantillon)
    locations_64 = [
        ["ANGLET", "LA BARRE", "mer", "18E"],
        ["BIARRITZ", "COTE DES BASQUES", "mer", "19E"],
        ["BIARRITZ", "GRANDE PLAGE NORD (PALAIS)", "mer", "16E"],
        ["HENDAYE", "CASINO", "mer", "18E"]
    ]
    
    for item in locations_64:
        data.append({
            "departement": "64",
            "departement_nom": "PYRENEES-ATLANTIQUES",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine"
        })
    
    # 33 - GIRONDE (échantillon)
    locations_33 = [
        ["ANDERNOS-LES-BAINS", "LE BETEY", "mer", "11E"],
        ["ARCACHON", "JETEE THIERS", "mer", "13E"],
        ["LACANAU", "CENTRE", "mer", "14E"],
        ["BORDEAUX", "LAC DE BORDEAUX", "douce", "15E"]
    ]
    
    for item in locations_33:
        data.append({
            "departement": "33",
            "departement_nom": "GIRONDE",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine"
        })
    
    # Conversion en DataFrame
    df = pd.DataFrame(data)
    
    # Ajout de la colonne qualité (libellé)
    df["qualite"] = df["qualite_code"].map(quality_codes)
    
    # Ajout de coordonnées simulées pour la démonstration
    # Dans une application réelle, il faudrait utiliser une API de géocodage
    # ou avoir les coordonnées précises dans les données sources
    coordinates = {
        # Coordonnées approximatives pour quelques villes
        "ANGLET": (43.4831, -1.5142),
        "BIARRITZ": (43.4832, -1.5586),
        "HENDAYE": (43.3784, -1.7735),
        "BORDEAUX": (44.8378, -0.5792),
        "LACANAU": (45.0014, -1.1958),
        "ARCACHON": (44.6523, -1.1677),
        "ANDERNOS-LES-BAINS": (44.7431, -1.0989),
        "POITIERS": (46.5802, 0.3404),
        "SAINT-YRIEIX-LA-PERCHE": (45.5147, 1.2055),
        "BEAUMONT-DU-LAC": (45.7876, 1.8724)
    }
    
    # Pour les villes sans coordonnées, générons des positions aléatoires dans la région Nouvelle-Aquitaine
    def generate_random_coordinates():
        # Limites approximatives pour la Nouvelle-Aquitaine
        min_lat, max_lat = 43.0, 47.0
        min_lon, max_lon = -1.8, 2.5
        return (min_lat + random.random() * (max_lat - min_lat),
                min_lon + random.random() * (max_lon - min_lon))
    
    # Ajout des coordonnées au DataFrame
    latitudes = []
    longitudes = []
    
    for commune in df["commune"]:
        if commune in coordinates:
            lat, lon = coordinates[commune]
        else:
            # Coordonnées aléatoires pour les communes non répertoriées
            lat, lon = generate_random_coordinates()
            # Sauvegarde pour la cohérence (même commune = mêmes coordonnées)
            coordinates[commune] = (lat, lon)
        
        latitudes.append(lat)
        longitudes.append(lon)
    
    df["latitude"] = latitudes
    df["longitude"] = longitudes
    
    return df

# Création du dataframe
df = create_data()

# Sidebar pour les filtres
st.sidebar.header("Filtres")

# Recherche par ville
villes = ["Toutes les villes"] + sorted(df["commune"].unique().tolist())
ville_selectionnee = st.sidebar.selectbox("Choisissez une ville", villes)

# Filtre par type d'eau
types_eau = ["Tous les types"] + sorted(df["type_eau"].unique().tolist())
type_eau_selectionne = st.sidebar.selectbox("Type d'eau", types_eau)

# Filtre par qualité
qualites = ["Toutes les qualités", "Excellente qualité", "Bonne qualité", 
           "Qualité suffisante", "Qualité insuffisante"]
qualite_selectionnee = st.sidebar.selectbox("Qualité de l'eau", qualites)

# Application des filtres
filtered_df = df.copy()

if ville_selectionnee != "Toutes les villes":
    filtered_df = filtered_df[filtered_df["commune"] == ville_selectionnee]

if type_eau_selectionne != "Tous les types":
    filtered_df = filtered_df[filtered_df["type_eau"] == type_eau_selectionne]

if qualite_selectionnee != "Toutes les qualités":
    filtered_df = filtered_df[filtered_df["qualite"] == qualite_selectionnee]

# Affichage du nombre de résultats
st.write(f"**{len(filtered_df)} points de baignade** correspondent à vos critères")

# Création de deux colonnes pour l'affichage
col1, col2 = st.columns([2, 3])

# Colonne 1: Liste des points de baignade
with col1:
    st.subheader("Liste des points de baignade")
    
    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            with st.expander(f"{row['commune']} - {row['point_prelevement']}"):
                st.write(f"**Département:** {row['departement_nom']} ({row['departement']})")
                st.write(f"**Type d'eau:** {row['type_eau']}")
                
                # Couleur selon la qualité pour une meilleure visualisation
                quality_colors = {
                    "Excellente qualité": "green",
                    "Bonne qualité": "blue",
                    "Qualité suffisante": "orange",
                    "Qualité insuffisante": "red",
                    "Insuffisamment de prélèvements": "gray",
                    "Site non classé": "gray"
                }
                
                quality_color = quality_colors.get(row["qualite"], "black")
                st.markdown(f"**Qualité de l'eau:** <span style='color:{quality_color}'>{row['qualite']}</span>", unsafe_allow_html=True)
                st.write(f"**Nombre de prélèvements:** {row['nb_prelevements']}")
    else:
        st.info("Aucun point de baignade ne correspond à vos critères. Veuillez modifier les filtres.")

# Colonne 2: Carte
with col2:
    st.subheader("Carte des points de baignade")
    
    if not filtered_df.empty:
        # Centre de la carte (moyenne des latitudes et longitudes)
        center_lat = filtered_df["latitude"].mean()
        center_lon = filtered_df["longitude"].mean()
        
        # Création de la carte
        m = folium.Map(location=[center_lat, center_lon], zoom_start=8)
        
        # Définition des couleurs des marqueurs selon la qualité
        def get_marker_color(quality):
            colors = {
                "Excellente qualité": "green",
                "Bonne qualité": "blue",
                "Qualité suffisante": "orange",
                "Qualité insuffisante": "red",
                "Insuffisamment de prélèvements": "gray",
                "Site non classé": "gray"
            }
            return colors.get(quality, "black")
        
        # Ajout des marqueurs pour chaque point de baignade
        for _, row in filtered_df.iterrows():
            popup_html = f"""
            <strong>{row['commune']} - {row['point_prelevement']}</strong><br>
            Département: {row['departement_nom']}<br>
            Type d'eau: {row['type_eau']}<br>
            Qualité: {row['qualite']}<br>
            Prélèvements: {row['nb_prelevements']}
            """
            
            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=row["point_prelevement"],
                icon=folium.Icon(color=get_marker_color(row["qualite"]), icon="tint", prefix="fa")
            ).add_to(m)
        
        # Affichage de la carte
        folium_static(m, width=700)
    else:
        st.info("Aucun point de baignade sur la carte avec les filtres actuels.")

# Légende des couleurs
st.sidebar.markdown("---")
st.sidebar.subheader("Légende")
st.sidebar.markdown("🟢 **Excellente qualité**")
st.sidebar.markdown("🔵 **Bonne qualité**")
st.sidebar.markdown("🟠 **Qualité suffisante**")
st.sidebar.markdown("🔴 **Qualité insuffisante**")
st.sidebar.markdown("⚪ **Insuffisamment de prélèvements / Non classé**")

# Informations complémentaires
st.sidebar.markdown("---")
st.sidebar.info("""
**À propos des données:**  
Les données présentées proviennent du Ministère des Solidarités et de la Santé, 
basées sur les analyses effectuées en 2024 dans le cadre du contrôle sanitaire 
des eaux de baignade en Nouvelle-Aquitaine.
""")

# Téléchargement des données
st.sidebar.markdown("---")
st.sidebar.subheader("Télécharger les données")

csv = df.to_csv(index=False)
st.sidebar.download_button(
    label="Télécharger en CSV",
    data=csv,
    file_name="points_baignade_nouvelle_aquitaine.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.markdown("Projet réalisé dans le cadre du cours OPEN DATA - M2 Data 2024-2025")
