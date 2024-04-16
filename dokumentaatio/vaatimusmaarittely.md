# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on, että käyttäjät voivat varata tunnin mittaisia ajanjaksoja itselleen, esimerkiksi urheilukenttävuoron. Sovelluksen käyttäjät näkevät varaamattomat vapaat vuorot, sekä muiden käyttäjien varaamat varatut vuorot.

## Käyttäjät

Sovelluksessa on kaksi käyttäjäroolia eli _normaali käyttäjä (user)_ sekä _ylläpitäjä (admin)_. User voi varata itselleen vuoroja sekä peruuttaa varaamiaan vuoroja. Admin voi varata vuoroja, sekä peruuttaa kenen tahansa vuoron. Tämän lisäksi admin voi luoda kalenteriin uusia varauskohteita ja tehdä normaalista käyttäjästä ylläpitäjän.

## Käyttöliittymäluonnos

Sovellus koostuu seitsemästä eri näkymästä, joista kahteen on oikeudet vain ylläpitäjällä

![](./kuvat/kayttoliittyma-hahmotelma.png)

Sovellus aukeaa kirjautumisnäkymään, josta on mahdollista siirtyä uuden käyttäjän luomiseen tai kirjautumisen onnistuessa siirtyä kirjautuneena kalenterisivulle.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen "tehty"
  - Käyttäjätunnuksen täytyy olla uniikki ja vähintään 3 merkkiä pitkä ja ei saa sisältää välilyöntejä "tehty"
  - Salasana syötetään rekisteröityessä kahdesti ja sen täytyy olla molemmilla kerroilla sama "tehty"
    - Salasana ei saa sisältää välilyöntejä ja täytyy olla vähintään 3 merkkiä pitkä "tehty"
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu kirjoittaessa jo olemassaolevat käyttäjätunnus ja salasana kirjautumislomakkeelle
  - Jos käyttäjää ei ole olemassa tai salasana ei täsmää, antaa järjestelmä virheilmoituksen

### Kirjautumisen jälkeen

- Käyttäjä näkee varauskalenterin
  - Käyttäjä voi vaihtaa varauskohdetta ylhäältä klikkaamalla ja valitsemalla haluamansa
- Käyttäjä voi varata vapaana olevan ajan, mutta vain tunniksi per päivä per varauskohde
- Käyttäjä voi peruuttaa tekemänsä varauksen
- Käyttäjä voi kirjautua ulos järjestelmästä

- Käyttäjän ollessa lisäksi ylläpitäjä:
  - Ylläpitäjä voi peruuttaa kenen tahansa varauksen
  - Ylläpitäjä voi luoda ylhäältä klikkaamalla uuden varauskohteen
  - Ylläpitäjä voi tehdä käyttäjästä ylläpitäjän klikkaamalla ylhäältä

## Jatkokehitysideoita

Perusversion jälkeen voidaan järjestelmää täydentää ajan salliessa esimerkiksi alla mainituilla ominaisuuksilla:

- Varausta klikattaessa näkyy lisätietoja koskien varausta
- Käyttäjät näkevät listan kaikista omista varauksistaan
- Käyttäjien poistaminen


