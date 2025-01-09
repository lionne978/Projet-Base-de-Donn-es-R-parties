select*from ETUDIANT where PRENOM='Soukeye' AND NOM='Sembene';
CREATE DATABASE LINK systemsud CONNECT TO zonesud IDENTIFIED BY  sud USING 'localhost:1521/XE';
CREATE DATABASE LINK systemnord CONNECT TO zonenord IDENTIFIED BY  nord USING 'localhost:1521/XE';
CREATE DATABASE LINK systemcentre CONNECT TO zonecentre IDENTIFIED BY  centre USING 'localhost:1521/XE';
CREATE DATABASE LINK systemcapvert CONNECT TO zonecapvert IDENTIFIED BY  capvert USING 'localhost:1521/XE';




select* from ETUDIANT where NOM ='Barry' AND PRENOM='Sophia';



















