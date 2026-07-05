import streamlit as st
import joblib

# Charger le modèle
model = joblib.load("../model.pkl")

# Titre de l'application
st.title("Détection de Tweets Suspects")

st.write("Saisissez un tweet pour savoir s'il est considéré comme suspect par le modèle.")

# Saisie du tweet
tweet = st.text_area("Entrez un tweet")

# Correspondance des labels
label_map = {
    0: "Non suspect",
    1: "Suspect"
}

if st.button("Prédire"):

    if not tweet.strip():
        st.warning("Veuillez entrer un tweet.")
    else:

        # Prédiction
        prediction = model.predict([tweet])[0]
        probabilites = model.predict_proba([tweet])[0]

        # Résultat
        st.subheader("Résultat")

        if prediction == 1:
            st.error(f"**{label_map[prediction]}**")
        else:
            st.success(f"**{label_map[prediction]}**")

        # Affichage de la classe numérique
        st.write(f"Classe prédite : **{prediction}**")

        # Probabilités
        st.subheader("Probabilités")

        st.write(f"Non suspect : **{probabilites[0]*100:.2f}%**")
        st.progress(float(probabilites[0]))

        st.write(f"Suspect : **{probabilites[1]*100:.2f}%**")
        st.progress(float(probabilites[1]))

        # Confiance
        confiance = max(probabilites)
        st.info(f"Confiance du modèle : **{confiance*100:.2f}%**")