# Bijdragen

Ontbreekt er een host, of staat er juist iets ten onrechte op de lijst? Issues en
pull requests zijn welkom.

## Opbouw

`DNS/` en `IP/` bevatten de lijsten. Elk bestand is platte tekst, één vermelding
per regel, en wordt rechtstreeks door blockers ingelezen — er is geen buildstap.

## Voor je een PR opent

- Houd het formaat aan dat de rest van het bestand gebruikt.
- Controleer op dubbele vermeldingen voordat je toevoegt.
- Noem in de samenvatting waaróm iets op de lijst hoort, met een bron als die er
  is. Een host zonder onderbouwing is later niet te beoordelen.

## Commitberichten

Dit project gebruikt [Conventional Commits](https://www.conventionalcommits.org/).

**Vorm:**

```text
<type>: <korte omschrijving>
```

**Types:**

| Type | Wanneer |
| --- | --- |
| `feat` | Nieuwe pagina, sectie of functionaliteit |
| `fix` | Bugfix — kapotte layout, verkeerde configuratie, renderfout |
| `docs` | README, CONTRIBUTING of andere metabestanden |
| `chore` | Onderhoud — dependencies, CI/CD, configuratie |
| `style` | Opmaak, witruimte, typefouten |
| `refactor` | Herstructurering zonder gedragsverandering |
| `content` | Bestaande pagina-inhoud bijwerken of verbeteren |
| `revert` | Een eerdere commit terugdraaien |

**Regels:**

- Type en omschrijving in kleine letters
- Onderwerpregel onder de 72 tekens
- Geen punt aan het eind
- Gebiedende wijs ("add", "fix", "update" — niet "added", "fixed", "updated")

## Pull requests

- PR-titels volgen dezelfde conventie als hierboven. De controle
  "Conventional commit title" kijkt daarop en is verplicht.
- Eén logische wijziging per PR
- Richt de PR op `main`
- De PR-template vult zichzelf deels aan: het vinkje voor de titel en het
  opruimen van de niet-gekozen types gebeurt automatisch.
