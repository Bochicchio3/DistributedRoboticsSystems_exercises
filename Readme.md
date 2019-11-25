# Robotics Distributed System Exercises


1. Utilizzando il nodo turtlesim, visualizzare la posa della tartaruga su rviz mentre viene controllata con la tastiera. 

2. Scrivere un nodo che simuli un controllore di alto livello che, presa in ingresso una richiesta di controllo di tipo custom (contenente velocità lineare longitudinale e velocità angolare sullo yaw), generi un controllo per la tartaruga di tipo opportuno che applichi una saturazione sulla richiesta di controllo. I valori della saturazione devono essere impostabili come parametro del nodo. Dimostrare l'effettivo funzionamento del nodo confrontando la richiesta di controllo e il controllo effettuato su rqt_plot.

3. Settando la posizione iniziale della tartuga al centro della mappa, controllare la tartaruga con un controllo random in velocità lineare e angolare (in un intervallo limitato sensato) che vincoli il movimento nella metà superiore della mappa. 

4. Generare quattro tartarughe sparse sulla mappa. Controllarle in modo che vadano (una per volta, quindi aspettando l'arrivo di quella precedente) al punto di arrivo, scelto come la posizione del baricentro delle quattro tartarughe.

5. Generare tre tartarughe. Controllare la prima dal punto iniziale ad un punto dato finale con un controllo a 50 hz evitando la collisione con le altre due (ferme). Testare l'algoritmo in varie configurazioni delle tarturghe "ostacolo".
