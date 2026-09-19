---
layout: default
title: Regadenoson
parent: Pelkkä mallin ennuste (L5)
nav_order: 318
evidence_level: L5
indication_count: 4
---

# Regadenoson
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

# Regadenoson: sydämen kuormitustestiagenteista anafilaaksian

## Yhden lauseen yhteenveto

> Regadenoson on valikoiva adrenaliini A2A -reseptorin agonisti, jota käytetään kliinisesti farmakologisena sydämen kuormitustestiagenttina myokardin perfuusiokuvantamiseen, ei tautia hoitavana lääkkeenä.
> TxGNN-malli ennustaa sen olevan mahdollisesti tehokas **anafilaaksian** hoidossa, pisteillä **99,85 %**,
> mutta tätä tukee vain **1 heikosti asiaan liittyvä kliininen tutkimus** ja **0 julkaisua** — ja mekanistinen näyttö viittaa vastakkaiseen suuntaan.

---

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Farmakologinen sydämen kuormitustestiagentti (myokardin perfuusiokuvantaminen) — ei muodollisesti strukturoitu lähdetiedoissa; Suomessa hyväksyttyjä indikaatiotekstejä ei ole saatavilla |
| Ennustettu uusi indikaatio | Anafilaaksia |
| TxGNN-ennusteen pistemäärä | 99,85 % |
| Näyttötaso | L5 |
| Suomen markkinointitilanne | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtainen vaikutusmekanismi on merkitty tietoaukoksi strukturoidussa tietueessa, mutta näyttöpaketin oma mekanistinen analyysi tunnistaa regadnosonia valikoivaksi adrenaliini A2A -reseptorin agonistiksi, jota käytetään kliinisesti sydämen perfuusiokuvantamisen farmakologiseen kuormitussimulaatioon potilailla, jotka eivät voi harjoittaa riittävää kuormitusta.

Ennustettu yhteys anafilaaksiin **ei** noudata uskottavaa hoitomekanismia. Adrenaliini A2A -reseptorin aktivaatio on mekanistisesti yhteydessä mastosolun degrangoitumiseen ja verisuonten laajentumiseen — tämä on juuri syy siihen, että regadnosonia koskevan merkinnän tarroissa jo nyt ilmoitetaan tunnettu riski anafilaaktoid-/yliherkkyyskokemuksista (punoitus, hengityksen ahdistus, verenpaineen lasku) **haittavaikutuksena**, ei terapeuttisena vaikutuksena. Yksittäinen tähän indikaatioon haettu kliininen tutkimus (NCT06854458) vahvistaa tämän kaavan: se on sydämen kuormitusmagneettikuvaus-perfuusiitutkimus, jossa regadnosonia käytetään kuormitusta aiheuttavana agenttina, ja anafilaaksia esiintyy vain seurannan kohteena olevana haittavaikutuksena, ei hoitotavoitteena (relevanssiarvo **C**).

Tämä huoli vahvistuu laajemmalla ennustejoukolla: neljän parhaan TxGNN-kandidaatin joukossa tälle lääkkeelle kolme (anafilaaksia, ruoka-riippuvainen rasituksen aiheuttama anafilaaksia, pseudoallergiat) ovat kaikki yliherkkyyteen/mastosolumediointiin liittyviä sairauksia. Tämä klusteroituminen viittaa voimakkaasti siihen, että tietoverkko on koodannut lääke→haittavaikutus-suhteen lääke→indikaatio-suhteeksi — eli todennäköisesti **suunta-invertoituun signaaliin** pikemminkin kuin todelliseen uudelleenkäyttömahdollisuuteen.

---

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Rekrytointi | Tärkeimmät löydökset |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | N/A | Rekrytoi | 1000 | Monikeskuksinen sydämen kuormitus-magneettikuvaus-perfuusiitutkimus; regadnosonia käytetään farmakologisena kuormitusagenttina. Anafilaaksia ei ole hoitokohde — enintään seurannan kohteena oleva haittavaikutus. Relevanssiarvo **C** (alhainen relevanssiarvo hoitohypoteesiin). |

*Muille ennustetuille indikaatioille (ruoka-riippuvainen rasituksen aiheuttama anafilaaksia, esotropia, pseudoallergiat) ei löydetty kliinisiä tutkimuksia.*

---

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

---

## Suomen markkinointitiedot

Regadnosonia ei ole tällä hetkellä markkinoilla Suomessa (0 hyväksyntöä tietueessa); tuote-/lisenssiä koskevia tietoja ei ole saatavilla.

---

## Turvallisuusnäkökohdat

Strukturoidut turvallisuuskentät (tärkeimmät varoitukset, vasta-aiheet, lääkeinteraktiot) eivät ole täytettyjä lähdetiedoissa. Näyttöpaketin mekanistinen perusteltu kuitenkin korostaa, että regadnosella on **tunnettu riski anafilaaktoid-/yliherkkyyskokemuksista** (punoitus, hengityksen ahdistus, verenpaineen lasku) osana sen vakiintunutta haittavaikutusprofiiilia — suoraan asiaan liittyvä, koska tämä on myös ennustettu "uusi indikaatio". Täydellisiä merkintätietoja (TFDA/pakkausseloste varoitukset ja vasta-aiheet) on tällä hetkellä **este-tietoaukko** eikä sitä ole vielä haettu.

Täydellisiä turvallisuustietoja varten katso pakkausseloste, kun se on saatavilla.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Näyttötaso on L5 (vain mallin ennuste) — yksittäinen haettu kliininen tutkimus ei todellakaan tue anafilaaksian hoitamista regadnosella, eikä kirjallisuutta ole olemassa. Vielä tärkeämpää on se, että mekanistinen kaava (adrenaliini A2A -agonismi käynnistää mastosolumedioidut reaktiot) ja hypersensitiisuuteen liittyvien ennusteiden klusteroituminen tämän lääkkeen huippiehdokkaiden kesken sekä viittaa voimakkaasti siihen, että kyseessä on turvallisuussignaali, joka on luokiteltu väärin hoitosignaaliksi, ei todellinen uudelleenkäyttöhypoteesi.

**Edistymiseksi seuraavat asiat ovat tarpeen:**
- Nouda TFDA/pakkausseloste varoituksia ja vasta-aiheita (tällä hetkellä este S1-turvallisuusarvioinnille)
- Vahvista vaikutusmekanismin tiedot DrugBankin kautta muodollisesti sulkeaksesi signaali-inversion hypoteesin pois tai sisään
- Jos edetään edelleen, hanki prekliinisiä tai mekanistisia tutkimuksia, jotka suoraan yhdistävät A2A-reseptorin agonismin anti-anafilaaktiseen (sen sijaan pro-anafilaaksiseen) vaikutukseen ennen S0:n ylittämistä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

