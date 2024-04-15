# Ohjelmistotekniikka harjoitustyö

## Ajanvaraus sovellus

Sovelluksen avulla käyttäjät voivat varata tunnin mittaisia vuoroja (esim. urheilukenttävuoroja) käyttöönsä. Sovelluksessa käyttäjä näkee vuorolistan, josta tulee ilmi mitkä vuorot ovat muiden käyttäjien varaamia ja mitkä vapaita.

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.10`. Jos Python-versiosi on vanhempi, saattaa ilmentyä ongelmia.


### Dokumentaatio

* [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
* [Changelog](./dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat tietokannan alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelma suoritetaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu linkkiin, joka tulee komennon suoritettua näkyviin.
