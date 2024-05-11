# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on, että käyttäjät voivat varata tunnin mittaisia vuoroja itselleen, esimerkiksi urheilukenttävuoron. Sovelluksen käyttäjät näkevät varaamattomat vapaat vuorot, sekä muiden käyttäjien varaamat varatut vuorot. Oman varauksen voi myös peruuttaa, ja admin-roolin omaava käyttäjä voi peruuttaa kenen tahansa vuoron.

## Käyttäjät

Sovelluksessa on kaksi käyttäjäroolia eli _normaali käyttäjä (user)_ sekä _ylläpitäjä/admin_ eli käyttäjä, jolle on annettu _(admin)_-rooli. User voi varata itselleen vuoroja sekä peruuttaa varaamiaan vuoroja. Admin voi varata vuoroja, sekä peruuttaa kenen tahansa vuoron. Tämän lisäksi admin voi antaa normaalille käyttäjälle admin-roolin.

## Käyttöliittymäluonnos

Sovellus koostuu neljästä eri näkymästä, sekä neljästä pienestä info-näkymästä:

![](./kuvat/kayttoliittyma-hahmotelma.jpg)

Sovellus aukeaa kirjautumisnäkymään, josta on mahdollista siirtyä uuden käyttäjän luomiseen tai kirjautumisen onnistuessa siirtyä kirjautuneena kalenterisivulle.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- [x] Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - [x] Käyttäjätunnuksen täytyy olla uniikki ja vähintään 3 merkkiä pitkä ja ei saa sisältää välilyöntejä
  - [x] Salasana syötetään rekisteröityessä kahdesti ja sen täytyy olla molemmilla kerroilla sama
    - [x] Salasana ei saa sisältää välilyöntejä ja täytyy olla vähintään 3 merkkiä pitkä
- [x] Käyttäjä voi kirjautua järjestelmään 
  - [x] Kirjautuminen onnistuu kirjoittaessa jo olemassaolevat käyttäjätunnus ja salasana kirjautumislomakkeelle
  - [x] Jos käyttäjää ei ole olemassa tai salasana ei täsmää, antaa järjestelmä virheilmoituksen

### Kirjautumisen jälkeen

- [x] Käyttäjä näkee varauskalenterin
- [x] Käyttäjä voi varata vapaana olevan ajan 
  - [x] Mutta vain tunniksi per päivä per varauskohde
- [x] Käyttäjä voi peruuttaa tekemänsä varauksen
- [x] Käyttäjä voi kirjautua ulos järjestelmästä

- [x] Käyttäjä voi olla myös ylläpitäjä
  - [x] Ylläpitäjä voi peruuttaa kenen tahansa varauksen
  - [x] Ylläpitäjä voi tehdä käyttäjästä ylläpitäjän valitsemalla sen listasta ja klikkaamalla napista


## Jatkokehitysideoita

Perusversion jälkeen voidaan järjestelmää täydentää ajan salliessa esimerkiksi alla mainituilla ominaisuuksilla:

- Varauskohteita/varauskalentereja useampia, ja klikkaamalla voi vaihtaa varauskalenteria
- Varausta klikattaessa näkyy lisätietoja koskien varausta
- Käyttäjät näkevät listan kaikista omista varauksistaan
- Käyttäjien poistaminen


