---
layout: default
title: Palivizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
---

# Palivizumab
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

# Palivizumab: RSV-profylaksiasta kielen hyvänlaatuiseen kasvaimeen

## Yhden lauseen yhteenveto

Palivizumab on humanisoidusta monoklonaalista vasta-aineesta valmistettu lääke, jota käytetään hengitysteiden synkytiaaliviruksen (RSV) infektioiden ehkäisyyn korkean riskin keskoilla. TxGNN-malli ennustaa, että se saattaa olla tehokas **kielen hyvänlaatuiselle kasvaimelle**, mutta tätä ennustetta tuetaan tällä hetkellä **0 kliinisella tutkimuksella** ja **0 julkaisulla**.

## Pika-yleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikatio | RSV-infektioiden profylaksia (perustuu tunnettuun lääkkeen luokitteluun; ei markkinoitu Suomessa, joten strukturoitua hyväksymistekstiä ei ole saatavana) |
| Ennustettu uusi indikatio | Kielen hyvänlaatuinen kasvain |
| TxGNN-ennustepisteet | 99.94% |
| Näyttötaso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoitu |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odottaa |

## Miksi tämä ennuste on järkevä?

Palivizumab on humanisoidusta monoklonaalista vasta-aineesta valmistettu lääke, joka kohdistuu RSV:n fuusioproteiiniin (F). Se toimii neutraloimalla virusta ja estämällä solusta soluun siirtymisen, joten se on hengitysteiden antiviraalinen profylaktiikka-aine eikä onkologinen lääke.

RSV-pinnan glykoproteiinin neutraloinnin ja hyvänlaatuisen suun/kielen kasvainbiologian välillä ei tunneta mekanistista yhteyttä. Mitään yhteistä reittiä, reseptoria tai solubiologista prosessia ei yhdistä näitä kahta.

Merkittävää on, että kaikki kymmenen parasta TxGNN-ennustetta tälle lääkkeelle (kielen kasvain, kurkunkannen kasvain, kaulan neuroblastoma, nielusuun kasvain, suun pohjan kasvain, testiksen kasvain, kystinen kasvain, kaula-aukon schwannoma, mesenkymaoma, kilpirauhasen kielen kanavan kystä) ryhmittyvät kapealle pistealueelle (99.93–99.94%) ja kattavat toisiinsa liittymättömiä pään/kaulan ja sukupuolielinten patologioita. Tämä kuvio on yhteensopivampi tietokaavion upotuksen artefaktin kanssa — esimerkiksi solun läheisyys pediatrisen/harvinaisen taudin ontologiaklusterissa — kuin todellisen syy-suhteen kanssa. Mitkään näistä kymmenestä ennusteesta eivät ole tällä hetkellä tuettuina kliinisellä tai kirjallisuusnäytöllä.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole rekisteröityjä liittyvää kliinisiä tutkimuksia

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla liittyvää kirjallisuutta

## Turvallisuusnäkökohdat

Turvallisuustiedot löytyvät pakkausselosteesta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odottaa**

**Perustelut:**
Ennusteella on korkea TxGNN-pistemäärä, mutta nolla tukevia kliinisiä tutkimuksia tai kirjallisuutta, ja lääkkeen tunnetulla mekanismilla (RSV:n F-proteiinin neutralointi) ei ole uskottavaa biologista yhteyttä kielen kasvaimiin. Kymmenen epäliittyvän kasvainennusteen klusteroituminen lähes identtisiin pisteisiin viittaa edelleen enemmän tietokaavion upotuksen artefaktiin kuin todelliseen signaaliin (Näyttötaso L5, Päätösvaihe S0).

**Jatkon edellytykset:**
- TFDA/sääntelyviranomaisen pakkausselostedata (tällä hetkellä estävä datakohde, DG001)
- Vahvistettu vaikutusmekanismi DrugBankista tai alkuperäisestä kirjallisuudesta (korkean prioriteetin datakohde, DG002)
- Riippumaton prekliininen tai biologisen uskottavuuden arviointi, ennen kuin lisätodisteiden etsiminen on perusteltavaa
- TxGNN-tulosten uudelleen arviointi ontologiaklusterharhojen varalta koko pään/kaulan kasvainennustejoukossa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

