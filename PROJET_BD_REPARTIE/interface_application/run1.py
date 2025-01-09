import cx_Oracle
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Configuration de la connexion à Oracle
# dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')
# conn = cx_Oracle.connect(user='system', password='sys', dsn=dsn_tns)
# cursor = conn.cursor()
cursor = "conn.cursor()"

# Vues de vos différentes requêtes SQL
@app.route('/')
def index():
    return redirect(url_for('login'))

# Vue pour la liste des étudiants ayant une inscription pour la filière MIC de l'ENO de Saint-Louis pour l'année académique 2019/2020
@app.route('/test')
def test():
    # Votre requête SQL ici
    query = "SELECT * FROM ENO"
    cursor.execute(query)
    donneoracle = cursor.fetchall()
    return render_template('test.html', data=donneoracle)
    #return data

@app.route('/req1')
def req1():
    # Votre requête SQL ici
    query = "SELECT ETUDIANT.NOM_ETUDIANT,ETUDIANT.PRENOM_ETUDIANT,FILIERE.NOM_FILIERE,ENO.NOM_ENO,INSCRIPTION.DATE_INSCRIPTION,INSCRIPTION.STATUT,ZONE.NOMZONE FROM ETUDIANT JOIN FILIERE ON FILIERE.ID_FILIERE = ETUDIANT.ID_ETUDIANT JOIN ENO ON ENO.IDENO = ETUDIANT.ID_ETUDIANT JOIN ZONE ON ZONE.IDZONE = ENO.IDENO JOIN INSCRIPTION ON INSCRIPTION.IDINS = ETUDIANT.ID_ETUDIANT AND EXTRACT(YEAR FROM DATE_INSCRIPTION)=2019"
    cursor.execute(query)
    donneoracle = cursor.fetchall()
    return render_template('req1.html', data=donneoracle)
    #return donneoracle
# ... Définissez des vues similaires pour les autres requêtes ...



@app.route('/req2')
def req2():
    # Votre requête SQL ici
    query = "SELECT NOM_FILIERE, COUNT(PREINSCRIPTION.IDPRES) AS NOMBRE_PREINSCRIPTION FROM FILIERE JOIN PREINSCRIPTION ON FILIERE.ID_FILIERE=PREINSCRIPTION.IDPRES WHERE EXTRACT(YEAR FROM PREINSCRIPTION.DATE_PRESINCRIPTION)=2019 GROUP BY FILIERE.NOM_FILIERE HAVING COUNT (PREINSCRIPTION.IDPRES)>1"
    cursor.execute(query)
    donneoracle = cursor.fetchall()
    return render_template('req2.html', data=donneoracle)
    #return donneoracle
# ... Définissez des vues similaires pour les autres requêtes ...
@app.route('/req3')
def req3():
    # Votre requête SQL ici
    query = "SELECT * FROM ETUDIANT INNER JOIN INSCRIPTION ON ETUDIANT.ID_ETUDIANT = INSCRIPTION.IDINS WHERE EXTRACT(YEAR FROM INSCRIPTION.DATE_INSCRIPTION)=2021"
    cursor.execute(query)
    donneoracle = cursor.fetchall()
    return render_template('req3.html', data=donneoracle)
    #return (donneoracle)
# ... Définissez des vues similaires pour les autres requêtes ...

@app.route('/req4')
def req4():
    # Votre requête SQL ici
    query = "SELECT * FROM ETUDIANT JOIN ZONE ON ZONE.IDZONE = ETUDIANT.ID_ETUDIANT JOIN PREINSCRIPTION ON PREINSCRIPTION.IDPRES = ETUDIANT.ID_ETUDIANT JOIN INSCRIPTION ON INSCRIPTION.IDINS = ETUDIANT.ID_ETUDIANT WHERE  EXTRACT(YEAR FROM INSCRIPTION.DATE_INSCRIPTION)=2021"
    cursor.execute(query)
    donneoracle = cursor.fetchall()
    return render_template('req4.html', data=donneoracle)
    #return donneoracle
# ... Définissez des vues similaires pour les autres requêtes ...

@app.route('/req5')
def req5():
    # Votre requête SQL ici
    query = "SELECT * FROM ENO"
    cursor.execute(query)
    donneoracle = cursor.fetchall()
    return render_template('req5.html', data=donneoracle)
    #return data
# ... Définissez des vues similaires pour les autres requêtes ...

@app.route('/req6')
def req6():
    # Votre requête SQL ici
    query = "SELECT * FROM ENO"
    cursor.execute(query)
    donneoracle = cursor.fetchall()
    return render_template('req6.html', data=donneoracle)
    #return data
# ... Définissez des vues similaires pour les autres requêtes ...

@app.route('/req7')
def req7():
    # Votre requête SQL ici
    query = "SELECT * FROM ENO"
    cursor.execute(query)
    donneoracle = cursor.fetchall()
    return render_template('req7.html', data=donneoracle)
    #return data
# ... Définissez des vues similaires pour les autres requêtes ...


#=====================================Ce que j'ai ajouté==============================================================================================
@app.route('/addEtudiant', methods=['GET'])
def formulaire_nouvel_etudiant():
    # Récupérer les données pour les clés étrangères depuis la base de données Oracle
    cursor.execute("SELECT id, nom FROM table_preinscription")
    preinscriptions = cursor.fetchall()

    # Vous pouvez ajouter d'autres requêtes pour les autres clés étrangères

    return render_template('nouvel_etudiant.html', preinscriptions=preinscriptions)

# Page de connexion
from flask import jsonify

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Ici, vous devez vérifier les identifiants dans la base de données Oracle
        if check_credentials(username, password):
            # Si les identifiants sont corrects, redirigez vers la page d'accueil
            return jsonify(success=True, redirect_url=url_for('index'))
        else:
            # Sinon, retournez un message d'erreur sous forme de réponse JSON
            return jsonify(success=False, error='Identifiants incorrects. Veuillez réessayer.'), 401

    return render_template('login.html', error=error)


def check_credentials(username, password):
    try:
        # Établir une connexion à Oracle avec les identifiants fournis
        conn = cx_Oracle.connect(user=username, password=password, dsn='localhost:1521/xe')
        cursor = conn.cursor()
        print("ok2")

        # Exécuter une requête pour vérifier la connexion
        cursor.execute("SELECT 1 FROM DUAL")
        result = cursor.fetchone()

        # Fermer la connexion et retourner True si la connexion est établie avec succès
        cursor.close()
        conn.close()
        return True
    except cx_Oracle.Error:
        # En cas d'erreur de connexion, retourner False
        return False


if __name__ == '__main__':
    app.run(debug=True)
