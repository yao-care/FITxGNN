---
layout: default
title: Avibactam Sodium
parent: Pelkkä mallin ennuste (L5)
nav_order: 54
evidence_level: L5
indication_count: 0
---

# Avibactam Sodium
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **0** kpl
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

# Avibactam-natrium: Uudelleenkäytön arviointi epäselvä — TxGNN-ennusteita ei ole saatavilla

## Yksisäikeinen yhteenveto

Avibactam-natrium on ei-β-laktaami β-laktamaasi-inhibiittori, jota käytetään yhdessä keftatsidiimin kanssa vakavien gram-negatiivisten bakteeritartuntojen hoitoon. TxGNN-malli ei tuottanut mitään uudelleenkäytön ennusteita tälle yhdisteelle nykyisessä todistepaketissa, eikä Suomen viranomaishyväksynnät ole rekisteröity. Muodollista uudelleenkäytön arviointia ei voida suorittaa tässä vaiheessa.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen lääkeindikaatio | Gram-negatiiviset bakteeritartunnat (keftatsidiimin yhdistelmäkumppani; todisteet ulkoisista lähteistä — ei ole olemassa todistepaketissa) |
| Ennustettu uusi lääkeindikaatio | Ennustetta ei ole saatavilla |
| TxGNN-ennustepistemäärä | N/A |
| Todisteen taso | L5 — ennusteita ei luotu |
| Suomen markkinoiden asema | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odota |

---

## Miksi ennustetta ei ole saatavilla

Avibactam-natrium on β-laktamaasi-inhibiittori, jolla ei ole luontaista antibakteeriaktiviteettia. Sen ainoa toimintamekanismi on peruuttamaton, kovalenttinen sitoutuminen seriini-β-laktamaaseihin (luokat A, C ja jotkut luokan D entsyymit), jolloin sen yhdistelmäkumppani (keftatsidiimi) suojataan entsymaattiselta inaktivoinnilta. Tämä erittäin spesifinen, aputoiminen mekanistinen rooli — pikemminkin kuin suora reseptorilla välitetty tai polkujen tasolla vaikuttava vaikutus — saattaa rajoittaa TxGNN:n kykyä tunnistaa sairauden-graafin liittymiä yhdisteelle erillisenä solmuna.

Lisäksi todistepaketti vahvistaa, että mitään DrugBank-tunnusta ei ratkaistu (`drugbank_id: null`) ja mitään alkuperäisiä indikaatioita ei täytetty. Kartoitetun tietokaavion solmun puuttuminen on todennäköisin tekninen syy sille, miksi ennusteita ei palautettu.

---

## Turvallisuushuomiot

Lisätietoja turvallisuudesta löytyy pakkausselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Todistepaketti ei sisällä mitään TxGNN-uudelleenkäytön ennusteita, mitään Suomen viranomaishyväksyntöjä ja mitään turvallisuustietoja. Uudelleenkäytön arviointiin jatkamiselle ei ole todistuspohjaa.

**Jatkamista varten tarvitaan seuraava:**

- **Ratkaise DrugBank-tunnus**: Varmista, onko Avibactam-natriumilla DrugBank-merkintä (se voidaan listata yhdistelmätuotteen Keftatsidiimi-Avibactam alla, DB09050) ja kartoita tietokaavion solmu uudelleen.
- **Selventää arviointilaajuutta**: Määritä, onko arviointikohteena Avibactam-natrium itsenäisenä yhdisteenä vai Keftatsidiimi-Avibactam-yhdistelmänä — TxGNN-ennusteet eroavat merkittävästi näiden kahden välillä.
- **Suorita TxGNN-putkilinja uudelleen**: Kun solmu on oikein kartoitettu, suorita ennuste uudelleen saadaksesi pisteytetyt indikaatioiden ehdokkaat.
- **Hae pakkausseloste**: Hanki varoitukset, vasta-aiheet ja MOA virallisesta Suomen/EMA-hyväksytystä SmPC:stä (Zavicefta).
- **Täytä alkuperäiset indikaatiot**: Rekisteröi hyväksytyt indikaatiot (monimutkainen UTI, monimutkainen IAI, sairaalassa hankittu/ventilaattoriin liittyvä keuhkokalvontulehdus) todistepaketissa ennen uudelleen arviointia.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

