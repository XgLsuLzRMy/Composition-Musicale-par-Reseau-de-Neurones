from keras.models import load_model

# instanciation du modèle, compilation et entrainement
# ...

# Enregistrement du moèdle dans un fichier
model.save('fichier_du_modele.h5')

# Chargement du modèle stocké dans le fichier
model = load_model('fichier_du_modele.h5')