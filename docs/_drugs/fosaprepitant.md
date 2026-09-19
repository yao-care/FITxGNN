---
layout: default
title: Fosaprepitant
parent: Pelkkä mallin ennuste (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# Fosaprepitant: Kemoterapiaan liittyvän pahoinvoinnin ja oksentamisen hoidosta Neprogeneettiseen sopimattoman antidiureettisen hormonin oireyhtymään

## Yhden lauseen yhteenveto

Fosaprepitant on aprepitanin intravenöösä farmakko, NK1 (Substance P) -reseptoriantagonisti, joka on vakiintunut käytettäväksi kemoterapiaan liittyvän pahoinvoinnin ja oksentamisen (CINV) ehkäisyyn. TxGNN-malli ennustaa, että se voisi olla tehokas **Neprogeneettiseen sopimattoman antidiureettisen hormonin oireyhtymään (NSIAD)**, mutta tämä ennustus ei tällä hetkellä ole tuettu **millään kliinisillä tutkimuksilla eikä kirjallisuudella** — se on puhtaasti mallin pistemäärien ennustus, ja todistuspaketin oma mekanistinen arviointi merkitsee biologisen yhteyden olevan heikko.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Kemoterapiaan liittyvän pahoinvoinnin ja oksentamisen (CINV) ehkäisy (päätelty tukevasta tutkimus-/kirjallisuuskontekstista; ei ole strukturoidussa `original_indications`-kentässä) |
| Ennustettu uusi indikaatio | Neprogeneettisen sopimattoman antidiureettisen hormonin oireyhtymä (NSIAD) |
| TxGNN-ennusteen pistemäärä | 99.92% |
| Näyttötaso | L5 |
| Suomen markkinatilanne | Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidä varauksella |

## Miksi tämä ennustus on järkevä?

Yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla DrugBankissa tälle merkinnälle (merkitty korkeaksi tietojen puutokseksi). Todistuspaketin muualla olevien tietojen perusteella fosaprepitant on aprepitanin fosforyloitu farmakko, ja sen vakiintunut farmakologia on NK1-reseptoriantagonismi (Substance P), jota käytetään kliinisesti antiemeettinä yhdessä 5-HT3-antagonistien ja deksametasonin kanssa CINV-ehkäisyyn.

NSIAD on erillinen kliininen kokonaisuus, jonka aiheuttavat AVPR2-reseptorin (vasopressiini V2) toimintaa lisäävät mutaatiot, jotka tuottavat nestepidätys/hyponatremia-fenotyypin vasopressiinitasoista riippumatta. NK1/Substance P -signaloinnin ja NSIAD:ta ohjaavan AVPR2-polun välillä ei ole vakiintunutta farmakologista yhteyttä.

Näin ollen mallin oma lääkkeen uudelleenkäyttöä koskevassa perustelussa mekanistinen yhteys luonnehtitaan selvästi heikoksi ("與AVPR2功能增益型突變...無已知交互作用，機轉關聯薄弱"), ja siinä suositellaan tämän ehdokkaan sulkemista pois prioriteettitutkimusjonosta. 99.92 %:n TxGNN-pistemäärää olisi luettava vain graafisen embedding-samankaltaisuussignaalina, ei biologisena uskottavuutena — sitä ei tue mikään tutkimus tai julkaisu.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröity yhtään siihen liittyvää kliinistä tutkimusta.

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla yhtään siihen liittyvää kirjallisuutta.

## Suomen markkinatiedot

Fosaprepitant-lääkettä ei tällä hetkellä markkinoida Suomessa (markkinatilanne: Ei markkinoilla; rekisteröityjen lupien kokonaismäärä: 0). Tuotteiden tason lisensointi- ja lupadata ei ole saatavilla yhteenvetoon.

## Turvallisuusnäkökohdat

Katso turvallisuustietoja pakkausselosteesta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä varauksella**

**Perustelut:**
Parhaiten sijoitetulla ennustuksella (NSIAD) ei ole tukevia kliinisiä tutkimuksia tai kirjallisuutta, ja sen oma mekanistinen perustelunsa kuvaa biologisen yhteyden heikoksi, joten se ei täytä kynnystä edetä mallin seulonnan ohitse (S0). Tätä pahentaa kriittisen vakavuuden tietojen puutos (Fimea/TFDA-vastaava pakkausseloste ei ole vielä haettu), mikä estää jopa alustavaa turvallisuusarviointia.

**Edetäkseen, seuraavaa tarvitaan:**
- Virallisen pakkausselosteen hakeminen ja jäsentäminen (merkinnät, varoitukset, vasta-aiheet) — tällä hetkellä kriittinen puutos
- Strukturoidut vaikutusmekanismin tiedot DrugBankista oikean mekanistisen uskottavuuden arvioimiseksi
- Jos tutkitaan tämän lääkkeen uudelleenkäyttöä, harkitse sijoituksen 7 (retiniitti, L4 — tuettu prekliinisellä mekanistisella tutkimuksella, joka osoittaa fosaprepitantin estävän NK1/Substance P -vetoisesti silmän tulehusta) priorisointia nykyisen parhaiten sijoitetun NSIAD-ehdokkaan sijaan, jolla ei ole mitään tukevaa näyttöä
- Vahvista itsenäisesti uudelleen kolme "useita endokriinisiä neoplasioita" varten ilmennyttä kliinistä tutkimusta (sijoitus 5): kaikki kolme ovat CINV-antiemeettisen tuen tutkimuksia potilailla, joilla on sukusolu-/hematologisia pahanlaatuisuuksia, eivät MEN-hoidon tutkimuksia — tämä yhdistelmä näyttää olevan lääkkeen ja sairauden väärä täsmäys oikean näytön sijaan

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

