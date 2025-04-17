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
st.title("🏊 Où se baigner ? - Qualité des eaux autour de Bordeaux et Arcachon")


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
    
    # Données extraites des PDFs - Zone de Bordeaux et Arcachon (100km environ)
    data = []
    
    # 33 - GIRONDE (Bassin d'Arcachon et alentours) - Avec coordonnées précises
    locations_33 = [
        # Arcachon et Bassin
        ["ARCACHON", "JETEE THIERS", "mer", "13E", 44.6642, -1.1679],
        ["ARCACHON", "LE MOULLEAU", "mer", "9E", 44.6415, -1.2177],
        ["ARCACHON", "PEREIRE", "mer", "13E", 44.6527, -1.2002],
        ["LA TESTE-DE-BUCH", "PLAGE CAZAUX", "douce", "13E", 44.5430, -1.1468],
        ["LA TESTE-DE-BUCH", "LA SALIE NORD", "mer", "8E", 44.5489, -1.2546],
        ["LA TESTE-DE-BUCH", "PETIT NICE", "mer", "8B", 44.5678, -1.2499],
        ["LA TESTE-DE-BUCH", "LA LAGUNE", "mer", "7E", 44.5967, -1.2379],
        ["LEGE-CAP-FERRET", "CAP-FERRET PHARE", "mer", "11E", 44.6354, -1.2529],
        ["LEGE-CAP-FERRET", "GRAND CROHOT", "mer", "9E", 44.7786, -1.2614],
        ["LEGE-CAP-FERRET", "TRUC VERT", "mer", "9E", 44.7189, -1.2607],
        ["LEGE-CAP-FERRET", "L'HORIZON", "mer", "8E", 44.6689, -1.2584],
        ["LEGE-CAP-FERRET", "CLAOUEY", "mer", "11E", 44.7307, -1.1916],
        ["ANDERNOS-LES-BAINS", "LE BETEY", "mer", "11E", 44.7404, -1.1147],
        ["ANDERNOS-LES-BAINS", "PLAGE DU CENTRE", "mer", "10E", 44.7462, -1.1025],
        ["LANTON", "TAUSSAT", "mer", "12E", 44.7324, -1.1304],
        ["LANTON", "CASSY", "mer", "9E", 44.7264, -1.1470],
        ["GUJAN-MESTRAS", "LARROS", "mer", "9E", 44.6402, -1.0745],
        ["GUJAN-MESTRAS", "LA HUME", "mer", "8B", 44.6334, -1.0957],
        
        # Bordeaux et lac
        ["BORDEAUX", "LAC DE BORDEAUX", "douce", "15E", 44.8774, -0.5706],
        ["BRUGES", "PLAGE DU BOIS", "douce", "8E", 44.8863, -0.5963],
        
        # Médoc atlantique (< 100km)
        ["CARCANS", "CARCANS OCEAN", "mer", "10E", 45.0848, -1.1939],
        ["CARCANS", "MAUBUISSON", "douce", "12E", 45.0731, -1.1427],
        ["HOURTIN", "HOURTIN OCEAN", "mer", "10E", 45.2192, -1.1883],
        ["HOURTIN", "LAC D'HOURTIN", "douce", "10E", 45.1845, -1.0878],
        ["LACANAU", "CENTRE", "mer", "14E", 44.9983, -1.2012],
        ["LACANAU", "PLAGE SUD", "mer", "12E", 44.9913, -1.2029],
        ["LACANAU", "NORD", "mer", "10E", 45.0067, -1.1997],
        ["LACANAU", "LE MOUTCHIC", "douce", "12E", 44.9750, -1.1184],
        ["LACANAU", "GRANDE ESCOURE", "douce", "8E", 44.9344, -1.1015],
        
        # Libourne et environs
        ["LIBOURNE", "LES DAGUEYS", "douce", "10E", 44.9394, -0.2379]
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
            "region": "Nouvelle-Aquitaine",
            "latitude": item[4],
            "longitude": item[5]
        })
    
    # 40 - LANDES (proche Bassin d'Arcachon <100km)
    locations_40 = [
        ["BISCARROSSE", "PLAGE CENTRE", "mer", "5E", 44.4456, -1.2534],
        ["BISCARROSSE", "PLAGE NORD", "mer", "6E", 44.4558, -1.2525],
        ["BISCARROSSE", "PLAGE SUD", "mer", "10E", 44.4281, -1.2559],
        ["BISCARROSSE", "ISPE-NAVARROSSE", "douce", "9E", 44.3811, -1.1649],
        ["BISCARROSSE", "PLAGE MAGUIDE", "douce", "9E", 44.3980, -1.1695],
        ["SANGUINET", "CATON", "douce", "9E", 44.4977, -1.0823],
        ["PARENTIS-EN-BORN", "PLAGE MUNICIPALE", "douce", "9E", 44.3453, -1.0753]
    ]
    
    for item in locations_40:
        data.append({
            "departement": "40",
            "departement_nom": "LANDES",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine",
            "latitude": item[4],
            "longitude": item[5]
        })
        
    # 17 - CHARENTE-MARITIME (nord Gironde, <100km de Bordeaux)
    locations_17 = [
        ["ROYAN", "PLAGE DE LA GRANDE CONCHE", "mer", "10E", 45.6230, -1.0341],
        ["ROYAN", "PLAGE DE PONTAILLAC", "mer", "12B", 45.6326, -1.0485],
        ["ROYAN", "PLAGE DU CHAY", "mer", "6E", 45.6259, -1.0422],
        ["SAINT-PALAIS-SUR-MER", "PLAGE DE LA GRANDE COTE", "mer", "10E", 45.6567, -1.0878],
        ["SAINT-PALAIS-SUR-MER", "PLAGE DU BUREAU", "mer", "12B", 45.6425, -1.0686],
        ["SAINT-GEORGES-DE-DIDONNE", "PLAGE CENTRALE", "mer", "10E", 45.6082, -1.0187]
    ]
    
    for item in locations_17:
        data.append({
            "departement": "17",
            "departement_nom": "CHARENTE-MARITIME",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine",
            "latitude": item[4],
            "longitude": item[5]
        })
    
    # 24 - DORDOGNE (proche Bordeaux <100km)
    locations_24 = [
        ["BERGERAC", "POMBONNE", "douce", "5E", 44.8681, 0.4704],
        ["SAINT-ESTEPHE", "GRAND ETANG DE ST ESTEPHE", "douce", "6E", 45.5640, 0.6326],
        ["CARSAC-DE-GURSON", "GURSON", "douce", "6E", 44.9823, 0.2262]
    ]
    
    for item in locations_24:
        data.append({
            "departement": "24",
            "departement_nom": "DORDOGNE",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine",
            "latitude": item[4],
            "longitude": item[5]
        })
    
    # Conversion en DataFrame
    df = pd.DataFrame(data)
    
    # Ajout de la colonne qualité (libellé)
    df["qualite"] = df["qualite_code"].map(quality_codes)
    
    # Les coordonnées sont déjà intégrées dans les données
    # Nous n'avons pas besoin de générer des coordonnées aléatoires
    # puisque toutes les données ont maintenant des coordonnées précises
    
    # Note: dans une version future, nous pourrions utiliser une API de géocodage
    # pour automatiser ce processus avec d'autres points de baignade
    
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
