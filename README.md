# Oblig3
Hva jeg har gjort:
Før jeg startet med å sette opp Github Actions, opprettet jeg et nytt repository og la inn filene fra Oblig 2. Deretter klikket jeg meg inn på fanen 'Actions', 
hvor jeg opprettet en workflow fil som skal kjøre testene fra Oblig 2. 

  Linje 3 i denne filen får testen til å kjøre automatisk hver gang det blir gitt et git push. 
  
  Linje 5 og nedover, "bygger" en test med navnet Run tests. Denne testen er konfigurert til å kjøre på den nyeste versjonen av ubuntu. 
  
  Det første steget til testen (linje 10 – 16) er å gå igjennom koden og sette opp Python versjon 3.11. 
  
  Det neste steget er å installere dependencies (linje 18 – 21). Først oppdateres pip til sin nyeste versjon. Deretter skjekkes repository-en for en fil med navnet 
  requirements.txt. Dersom den eksisterer, vil tekst-filen bli lest og innholdet installert. 
  
  Til slutt (linje 23 – 25) kjøres testene til Oblig 2 med pytest, og det gis beskjed om de feilet eller lyktes (linje 27 – 41). 

Etter at workflow filen blie pushet til repository-en, kunne jeg med en gang se at testen kjørte og var vellykket. 
