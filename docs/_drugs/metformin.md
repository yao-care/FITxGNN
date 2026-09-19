---
layout: default
title: Metformin
parent: Pelkkä mallin ennuste (L5)
nav_order: 245
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **5** kpl
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

# Metformiini: Tyypin 2 diabeteksesta fokaaliseen jäykkään raajasyndromaan

## Yhden lauseen yhteenveto

Metformiini on biguaniidipohjainen antidiabeettinen lääke, joka on hyvin vakiintunut tyypin 2 diabeteksen hoitoon (tätä erityistä seikkaa ei ole tallennettu näyttöpakettiin, joka ei luettele alkuperäisiä indikaatioita).
TxGNN-malli ennustaa, että se saattaa olla tehokas **fokaalisessa jäykässä raajasyndromassa**, mutta tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua** tukee tätä suuntaa — ennustus perustuu kokonaan graafin upotusten samankaltaisuuteen.

## Pika-yleiskatsaus

| Kohta | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Ei tallennettu näyttöpakettiin (Metformiini tunnetaan yleisesti tyypin 2 diabeteksen hoidosta) |
| Ennustettu uusi indikaatio | Fokaali jäykkä raajasyndrooma |
| TxGNN-ennuste-pistemäärä | 99.45% |
| Näyttötaso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoitu |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennustus on järkevä?

Tällä hetkellä metformiinin yksityiskohtainen toimintamekanismi ei ole saatavilla tässä näyttöpakettissa ([Data Gap]). Yleisen farmakologisen tiedon perusteella metformiinin tunnettu mekanismi sisältää AMPK:n aktivoinnin ja mitokondrion kompleksin I:n estämisen — mekanismit, jotka ovat keskeisiä sen glukoosia alentavaan vaikutukseen.

Fokaali jäykkä raajasyndrooma ja klassinen jäykkä henkilö -syndrooma sijaitsevat sairauskirjossa, jota ohjaavat ensisijaisesti GABAergisen neurotransmission puutteet ja anti-GAD65-autoimmuunipathologia. AMPK:n ja mitokondrion reittien sekä tämän neuro-autoimmuuniprosessin välillä ei ole vakiintunutta mekanistista yhteyttä. TxGNN:n paljastama yhteys näyttää olevan pelkkä graafin upotukseen perustuva yhteys pikemminkin kuin biologisesti perustettu hypoteesi, ja sitä tulisi käsitellä vain tutkimuksellisena.

Huomionarvoista on, että neljä muuta TxGNN:n rankaamaa metformiinin kandidaattia (klassinen jäykkä henkilö -syndrooma, opsismodysplasia, tiamiinille herkkä häiriöoireyhtymä ja lääkkeen aiheuttama paikallinen lipodystrofia) osoittavat vastaavasti heikkoa tai jopa ristiriitaista mekanistista perustelua — erityisesti tiamiinille herkkä kandidaatti on ristiriidassa metformiinin tunnetun tiamiinin/B12-imeytymisen häiriön kanssa, ja sitä tulisi merkitä mahdolliseksi mekanistiseksi kontraindikaatioksi eikä hoitomahdollisuudeksi.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta

## Turvallisuusnäkökohdat

Turvallisuustietoja varten katso pakkausseloste.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Ennustusta tukee vain TxGNN-upotusten pistemäärä (L5, S0) nolla kliinisen tutkimuksen ja nolla kirjallisuuden kanssa kaikkien viiden ennustetun indikaation osalta, ja TFDA:n pakkausselosteen varoituksista ja kontraindikaatioista puuttuva tieto estää tällä hetkellä jopa alkuvaiheen (S1) turvallisuustarkastelun.

**Jatkamiseksi tarvitaan seuraavaa:**
- TFDA:n pakkausselosteen tieto (varoitukset, kontraindikaatiot) — tällä hetkellä esto
- Metformiinin alkuperäisen toimintamekanismin (MOA) vahvistaminen
- Prekliininen tai mekanistinen kirjallisuus, joka spesifisesti yhdistää AMPK/mitokondrion reittejä GABAergisiin/anti-GAD65-patologioihin
- Suomen/Taiwanin markkinoiden ja lisensointitilanteen uudelleenarviointi (tällä hetkellä tallennettu tilanne: ei markkinoitu, 0 hyväksyntää)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

