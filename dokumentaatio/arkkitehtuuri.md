# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraavan UML-kaavion mukainen:

![](./kuvat/pakkausrakenne.png)

Pakkaus **ui** sisältää käyttöliittymästä, **services** sovelluslogiikasta ja **repositories** tietojen pysyväistallennuksesta vastaavan koodin. Pakkauksen **entities** sisällä on luokkia, jotka edustavat sovelluksen käsittelemiä tietokohteita.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat [User](https://github.com/levomaaa/ot-harjoitustyo/blob/main/src/entities/user.py) ja [Calender] (tulossa), jotka kuvaavat käyttäjiä ja ajanvarauskalenteria:

```mermaid
 classDiagram
      User "*" --> "1" Calender
      class User{
          username
          password
      }
      class Calender{
          id
          name
          day
          time
      }
```

Sovelluslogiikka saattaa hiukan muuttua kurssin edetessä, mutta runko tulee olemaan samanlainen.

Toiminnallisista kokonaisuuksista vastaa luokan [Service](https://github.com/levomaaa/ot-harjoitustyo/blob/main/src/services/service.py) ainoa Service-olio. Jokaiselle käyttöliittymän toiminnolle on määritelty omat metodinsa Service-luokassa.
