
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
    
    # 64 - PYRENEES-ATLANTIQUES (sélection depuis le PDF)
    locations_64 = [
        ["ANGLET", "LA BARRE", "mer", "18E"],
        ["ANGLET", "LA MADRAGUE (CHIBERTA)", "mer", "10E"],
        ["ANGLET", "LES CAVALIERS", "mer", "10E"],
        ["BIARRITZ", "COTE DES BASQUES", "mer", "19E"],
        ["BIARRITZ", "GRANDE PLAGE NORD (PALAIS)", "mer", "16E"],
        ["BIARRITZ", "MIRAMAR", "mer", "20E"],
        ["HENDAYE", "CASINO", "mer", "18E"],
        ["HENDAYE", "LES DEUX JUMEAUX", "mer", "20E"],
        ["SAINT-JEAN-DE-LUZ", "GRANDE PLAGE NORD-CALE AUX CHEVAUX", "mer", "20B"],
        ["SAINT-PEE-SUR-NIVELLE", "PLAGE LAC ST PEE SUR NIVELLE", "douce", "6E"]
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
    
    # 33 - GIRONDE (sélection depuis le PDF)
    locations_33 = [
        ["ANDERNOS-LES-BAINS", "LE BETEY", "mer", "11E"],
        ["ARCACHON", "JETEE THIERS", "mer", "13E"],
        ["ARCACHON", "LE MOULLEAU", "mer", "9E"],
        ["BORDEAUX", "LAC DE BORDEAUX", "douce", "15E"],
        ["CARCANS", "CARCANS OCEAN", "mer", "10E"],
        ["HOURTIN", "HOURTIN OCEAN", "mer", "10E"],
        ["LACANAU", "CENTRE", "mer", "14E"],
        ["LACANAU", "PLAGE SUD", "mer", "12E"]
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
    
    # 40 - LANDES (sélection depuis le PDF)
    locations_40 = [
        ["BISCARROSSE", "PLAGE CENTRE", "mer", "5E"],
        ["BISCARROSSE", "PLAGE NORD", "mer", "6E"],
        ["CAPBRETON", "PLAGE CENTRALE", "mer", "10E"],
        ["MIMIZAN", "LES AILES", "mer", "10E"],
        ["MOLIETS-ET-MAA", "PLAGE PRINCIPALE", "mer", "9E"],
        ["SEIGNOSSE", "PENON", "mer", "10E"]
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
            "region": "Nouvelle-Aquitaine"
        })
    
    # 47 - LOT-ET-GARONNE (sélection depuis le PDF)
    locations_47 = [
        ["AIGUILLON", "PLAGE AIGUILLON", "douce", "5E"],
        ["CASTELJALOUX", "LAC DE CLARENS", "douce", "6E"],
        ["DAMAZAN", "LAC DU MOULINEAU", "douce", "5E"],
        ["LOUGRATTE", "LAC DE LOUGRATTE", "douce", "7E"]
    ]
    
    for item in locations_47:
        data.append({
            "departement": "47",
            "departement_nom": "LOT-ET-GARONNE",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine"
        })
    
    # 24 - DORDOGNE (sélection depuis le PDF)
    locations_24 = [
        ["ANGOISSE", "PLAN D'EAU DE ROUFFIAC", "douce", "7E"],
        ["BERGERAC", "POMBONNE", "douce", "5E"],
        ["CARSAC-DE-GURSON", "GURSON", "douce", "6E"],
        ["SAINT-ESTEPHE", "GRAND ETANG DE ST ESTEPHE", "douce", "6E"]
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
            "region": "Nouvelle-Aquitaine"
        })
    
    # 19 - CORREZE (sélection depuis le PDF)
    locations_19 = [
        ["AMBRUGEAT", "LAC DE SECHEMAILLES", "douce", "5E"],
        ["AURIAC", "PLAN D'EAU COMMUNAL", "douce", "5E"],
        ["NEUVIC", "LA PLAGE", "douce", "5E"],
        ["TREIGNAC", "LES BARIOUSSES", "douce", "5E"]
    ]
    
    for item in locations_19:
        data.append({
            "departement": "19",
            "departement_nom": "CORREZE",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine"
        })
    
    # 23 - CREUSE (sélection depuis le PDF)
    locations_23 = [
        ["ANZEME", "PECHADOIRE", "douce", "5B"],
        ["CHAMPAGNAT", "LA NAUTE", "douce", "5E"],
        ["GUERET", "COURTILLE", "douce", "5B"],
        ["ROYERE-DE-VASSIVIERE", "BROUSSAS", "douce", "5E"]
    ]
    
    for item in locations_23:
        data.append({
            "departement": "23",
            "departement_nom": "CREUSE",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine"
        })
    
    # 16 - CHARENTE (sélection depuis le PDF)
    locations_16 = [
        ["AUBETERRE-SUR-DRONNE", "BAIGNADE MUNICIPALE", "douce", "5B"],
        ["ECURAS", "VILLAGE LE CHAT", "douce", "9E"],
        ["SAINT-YRIEIX-SUR-CHARENTE", "LA GRANDE PRAIRIE", "douce", "7E"],
        ["VINDELLE", "LES PETITS ESSARDS", "douce", "5E"]
    ]
    
    for item in locations_16:
        data.append({
            "departement": "16",
            "departement_nom": "CHARENTE",
            "commune": item[0],
            "point_prelevement": item[1],
            "type_eau": item[2],
            "qualite_code": item[3][1:],
            "nb_prelevements": item[3][0],
            "region": "Nouvelle-Aquitaine"
        })
    
    # 17 - CHARENTE-MARITIME (sélection depuis le PDF)
    locations_17 = [
        ["ANGOULINS", "PLAGE DE LA PLATERRE", "mer", "6E"],
        ["BOURCEFRANC-LE-CHAPUS", "LA PLAGE", "mer", "10E"],
        ["FOURAS", "PLAGE DE L'ESPERANCE", "mer", "12E"],
        ["ROYAN", "PLAGE DE LA GRANDE CONCHE", "mer", "10E"]
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
        # Coordonnées approximatives pour quelques villes de Nouvelle-Aquitaine
        "ANGLET": (43.4831, -1.5142),
        

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
