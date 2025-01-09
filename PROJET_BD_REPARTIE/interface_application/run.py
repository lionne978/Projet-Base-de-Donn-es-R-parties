import cx_Oracle
from flask import Flask, render_template, request, url_for, redirect, session, jsonify

app = Flask(__name__)
app.secret_key="15176c4e4366a4b13fff15e90a7923200e2f5a4d9cdb1955b98893130af07428"

# Fonction pour établir une connexion à Oracle avec les informations d'identification de l'utilisateur connecté
def connect_to_oracle(username, password):
    try:
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')
        conn = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)
        return conn
    except cx_Oracle.Error as error:
        print("Erreur de connexion à Oracle:", error)
        return None
    
def get_oracle_connection():
    # Récupérer les informations de connexion à partir de la session
    username = session.get('username')
    password = session.get('password')

    # Retourner une connexion Oracle
    return connect_to_oracle(username, password)

# Page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Tentative de connexion à Oracle avec les identifiants fournis
        conn = connect_to_oracle(username, password)
        #Si ça passe::::
        if conn:
            session['logged_in'] = True
            session['username'] = username
            session['password'] = password
            # session['oracle_connection'] = conn  # Stockage de la connexion dans la session

            return jsonify(success=True, redirect_url=url_for('index')), 200
        
        #Dans le cas contraire
        else:
            error = 'Identifiants incorrects. Veuillez réessayer.'

    return render_template('login.html', error=error)

# Votre fonction pour effectuer les requêtes en utilisant la connexion Oracle
def execute_query(query):
    oracle_conn = get_oracle_connection()

    if oracle_conn is None:
        return redirect(url_for("login"))

    cursor = oracle_conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

# Vos différentes vues nécessitant une connexion à Oracle
@app.route('/')
def index():
    logged = session.get("logged_in")
    if logged:
        return redirect(url_for('req1'))
    
    return redirect(url_for('login'))

# @app.route('/test')
# def test():
#     query = "SELECT * FROM ENO"
#     donneoracle = execute_query(query)
#     return render_template('test.html', data=donneoracle)

# Ajoutez vos autres routes pour les requêtes (req1, req2, etc.)

@app.route("/req1")
def req1():
    logged = session.get("logged_in")
    if logged:
        query = "SELECT ETUDIANT.NOM,ETUDIANT.PRENOM,FILIERE.NOM_FILIERE,ENO.NOM_ENO,INSCRIPTION.DATE_INSCRIPTION,INSCRIPTION.STATUT,ZONE.NOMZONE FROM ETUDIANT JOIN FILIERE ON FILIERE.ID_FILIERE = ETUDIANT.ID_ETUDIANT JOIN ENO ON ENO.IDENO = ETUDIANT.ID_ETUDIANT JOIN ZONE ON ZONE.IDZONE = ENO.IDENO JOIN INSCRIPTION ON INSCRIPTION.IDINS = ETUDIANT.ID_ETUDIANT AND EXTRACT(YEAR FROM DATE_INSCRIPTION)=2019"
        donneoracle = execute_query(query)
        return render_template('req1.html', data=donneoracle)  
    return redirect(url_for("login"))

@app.route("/req2")
def req2():
    logged = session.get("logged_in")
    if logged:
        query = "SELECT NOM_FILIERE, COUNT(PREINSCRIPTION.IDPRES) AS NOMBRE_PREINSCRIPTION FROM FILIERE JOIN PREINSCRIPTION ON FILIERE.ID_FILIERE=PREINSCRIPTION.IDPRES WHERE EXTRACT(YEAR FROM PREINSCRIPTION.DATE_PRESINCRIPTION)=2019 GROUP BY FILIERE.NOM_FILIERE HAVING COUNT (PREINSCRIPTION.IDPRES)>1"
        donneoracle = execute_query(query)
        return render_template('req2.html', data=donneoracle)  
    
    return redirect(url_for("login"))

@app.route("/req3")
def req3():
    logged = session.get("logged_in")
    if logged:
        query = "SELECT * FROM ETUDIANT INNER JOIN INSCRIPTION ON ETUDIANT.ID_ETUDIANT = INSCRIPTION.IDINS WHERE EXTRACT(YEAR FROM INSCRIPTION.DATE_INSCRIPTION)=2021"
        donneoracle = execute_query(query)
        #return donneoracle
        return render_template('req3.html', data=donneoracle)  
    
    return redirect(url_for("login"))

@app.route("/req4")
def req4():
    logged = session.get("logged_in")
    if logged:
        query = "SELECT * FROM ETUDIANT JOIN ZONE ON ZONE.IDZONE = ETUDIANT.ID_ETUDIANT JOIN PREINSCRIPTION ON PREINSCRIPTION.IDPRES = ETUDIANT.ID_ETUDIANT JOIN INSCRIPTION ON INSCRIPTION.IDINS = ETUDIANT.ID_ETUDIANT WHERE  EXTRACT(YEAR FROM INSCRIPTION.DATE_INSCRIPTION)=2021"
        donneoracle = execute_query(query)
        return render_template('req4.html', data=donneoracle)  
    
    return redirect(url_for("login"))


@app.route("/req5")
def req5():
    logged = session.get("logged_in")
    if logged:
        query = "SELECT * FROM ENO"
        donneoracle = execute_query(query)
        return render_template('req5.html', data=donneoracle)  
    
    return redirect(url_for("login"))

@app.route("/req6")
def req6():
    logged = session.get("logged_in")
    if logged:
        query = "SELECT * FROM ENO"
        donneoracle = execute_query(query)
        return render_template('req6.html', data=donneoracle)  
    
    return redirect(url_for("login"))

@app.route("/req7")
def req7():
    logged = session.get("logged_in")
    if logged:
        query = "SELECT * FROM ENO"
        donneoracle = execute_query(query)
        return render_template('req7.html', data=donneoracle)  
    
    return redirect(url_for("login"))



@app.route('/addEtudiant', methods=['GET'])
def formulaire_nouvel_etudiant():
    logged = session.get("logged_in")
    if logged:
    
        query = "SELECT * FROM PREINSCRIPTION"
        preinscriptions = execute_query(query)

        query = "SELECT * FROM niveau"
        niveaux = execute_query(query)

        query = "SELECT * FROM filiere"
        fillieres = execute_query(query)

        query = "SELECT * FROM eno"
        enos = execute_query(query)

        query = "SELECT * FROM inscription"
        inscriptions = execute_query(query)

        return render_template('addEtudiant.html',
                                preinscriptions=preinscriptions,
                                niveaux=niveaux,
                                fillieres=fillieres,
                                enos=enos,
                                inscriptions=inscriptions
                                )
    
    return redirect(url_for("login"))



@app.route('/ajouter_etudiant', methods=['POST'])
def ajouter_etudiant():
    # Récupérer les données du formulaire
    ID = request.form['ID']
    INE = request.form['INE']
    nom = request.form['nom']
    prenom = request.form['prenom']
    age = request.form['age']
    adresse = request.form['adresse']
    email = request.form['email']
    id_preinscription = request.form['id_preinscription']
    id_niveau = request.form['id_niveau']
    id_filliere = request.form['id_filliere']
    id_eno = request.form['id_eno']
    id_inscription = request.form['id_inscription']
    validation = request.form['validation']
    mention = request.form['mention']

    # Connexion à la base de données Oracle
    connection = get_oracle_connection()

    # Création d'un curseur
    cursor = connection.cursor()

    # Requête d'insertion
    sql_insert = "INSERT INTO ETUDIANT (ID_ETUDIANT, INE, nom, prenom, age, addresse, email, id_preinscription, " \
                 "id_niveau, filiere_etudiant, id_eno, id_inscription, validation, mention) VALUES " \
                 "(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)"

    # Exécution de la requête d'insertion avec les données du formulaire
    cursor.execute(sql_insert, (ID, INE, nom, prenom, age, adresse, email, id_preinscription, id_niveau, id_filliere,
                                id_eno, id_inscription, validation, mention))

    # Commit des modifications dans la base de données
    connection.commit()

    # Fermeture du curseur et de la connexion
    cursor.close()
    connection.close()

    return redirect(url_for("req1"))
@app.route('/requete_sql', methods=['GET', 'POST'])
def requete_sql():
    logged = session.get("logged_in")
    if logged:
        if request.method == 'POST':
            query = request.form['sql_query']
            results = execute_query(query)
            return render_template('resultat.html', query=query, data=results)
        return render_template('req_sql.html')
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)
