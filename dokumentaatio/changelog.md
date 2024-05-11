# Changelog

## Viikko 3

- Käyttäjä näkee kirjautumisruudun
- Lisätty SQLite-tietokanta
- Lisätty UserRepository-luokka, joka vastaa käyttäjien tallentamisesta tietokantaan
- Lisätty User-luokka, joka vastaa yksittäisestä käyttäjästä
- Testattu, että UserRepository luo käyttäjän tietokantaan

## Viikko 4

- Kirjautumisruudulta pääsee rekisteröintiruutuun
- Käyttäjä voi luoda käyttäjän
- Lisätty virheilmoituksia rekisteröintiin
- Lisätty Service-luokka, joka vastaa sovelluslogiikasta
- Testattu Service ja UserRepository -luokkia monipuolisesti

## Viikko 5

- Käyttäjä voi kirjautua sisään ja ulos
- Lisätty virheilmoitukset sisäänkirjautumiseen
- Lisätty ajanvarauskalenteri näkyväksi kirjautuneelle käyttäjälle
- Testattu Service-luokka käyttäjän sisään- ja uloskirjautumisen sekä virheilmoitusten osalta

## Viikko 6

- Vaihdettu Service-luokan nimeksi UserService, vastaamaan käyttäjän sovelluslogiikasta
- Lisätty ReservationService-luokka, joka vastaa ajanvarausten sovelluslogiikasta
- Lisätty ReservationRepository-luokka, joka vastaa ajanvarausten tallentamisesta tietokantaan
- Lisätty Reservation-luokka, joka vastaa yksittäisestä ajanvarauksesta
- Käyttäjä voi tehdä ajanvarauksen
- Testattu ReservationService ja ReservationRepository -luokkia monipuolisesti

## Viikko 7

- Käyttäjä voi olla ylläpitäjä
- Lisätty User-luokkaan admin-rooli käyttäjälle
- Viimeistelty toiminnallisuudet
- Viimeistelty testit kaikille luokille
- Viimeistelty dokumentaatio
- Ohjelma saatu valmiiksi
