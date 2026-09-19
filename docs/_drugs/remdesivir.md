---
layout: default
title: Remdesivir
parent: Pelkkä mallin ennuste (L5)
nav_order: 320
evidence_level: L5
indication_count: 6
---

# Remdesivir
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **6** kpl
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

# Remdesivir: COVID-19:stä monisisäisen endokrinisen neoplasian hoitoon

## Yhden lauseen yhteenveto

> Remdesivir on nukleotidin esiainemuoto, joka on alun perin kehitetty COVID-19:n (SARS-CoV-2-infektio) hoitoon ja jolla on myös kliininen tutkimushistoria Ebola-virustaudissa.
> TxGNN-malli ennustaa sen olevan tehokas **monisisäiseen endokriseen neoplasiaan**, **99.50% ennustuspistemäärällä**,
> mutta tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua** eivät tue tätä suuntaa — itse todisteistopaketti merkitsee ennusteen todennäköiseksi tiedon graafin artefaktiksi.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | COVID-19 / Ebola-virustauti (päätelty tässä paketissa olevasta kliinisen tutkimuksen todisteesta; ei erikseen vahvistettu `drug.original_indications`-kentän kautta, joka on tyhjä) |
| Ennustettu uusi indikaatio | Monisisäinen endokrininen neoplasia |
| TxGNN-ennustuspistemäärä | 99.50% (sijoitus #5453) |
| Todisteiden taso | L5 (vain mallin ennuste, ei tukevia tutkimuksia) |
| Suomen markkinoiden asema | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidossa |

---

## Miksi tämä ennuste on kohtuullinen?

Tällä hetkellä remdesiviriä koskevia yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla strukturoidussa `original_moa`-kentässä (merkitty korkean vakavuusasteen tietovajeeksi DG002). Kuitenkin todisteistopaketin omat perustelukentät kuvaavat remdesiviriä adenosiinin nukleotidin esiainemuotona, joka kohdistuu viraalisen RNA-riippuvaisen RNA-polymeraasiin (RdRp) ja aiheuttaa viivästyneen ketjun päättynnyksen — tehokas RNA-viruksia, kuten Ebola-virusta ja SARS-CoV-2:ta, vastaan.

Monisisäinen endokrininen neoplasia (MEN) on perinnöllinen syöpäoireyhtymä, jota aiheuttavat sikiölinjan mutaatiot geeneissä, kuten *RET* ja *MEN1*, ja jonka patofysiologia keskittyy endokrinisten solujen proliferaatioon — mekanismiin, jolla ei ole tunnettua yhteyttä viraalisen RdRp-estoon. Todisteistopaketin oman perustelun mukaan tälle korkeimmalle sijoitetulle ennusteelle todetaan nimenomaisesti: *"無已知機轉關聯...高分應屬圖嵌入雜訊"* ("no known mechanistic link... the high score is likely graph-embedding noise").

Yhdenmukaista tämän kanssa, remdesiviri–MEN-parille ei haettu kliinisiä tutkimuksia, ICTRP-tietoja tai PubMed-kirjallisuutta (kyselyiden tunnukset 5–7 kyselyiden lokissa kaikki palauttivat nolla tulosta). Tämä ennuste tulee käsitellä varmentamattomana laskennallisena signaalina eikä mekaanisesti tai kliinisesti tuettuna hypoteesina. Kontekstiksi: paketin toiselle sijoitetulla ennusteella (HIV-infektio, pistemäärä 99.32%) on 23 tutkimusta ja 20 julkaisua, mutta näiden tietueiden tarkastelu osoittaa, että ne ovat pääosin COVID-19/Ebola-tutkimuksia, jotka on virheellisesti yhdistetty "HIV"-taudin nimikkeeseen, ja paketin oman mekaanisen arvioinnin mukaan ei myöskään löydy antiretroviirivaikutuksen perustaa — mikä vahvistaa, että mikään paketin korkeimmalle sijoitetuista TxGNN-ennusteista ei ole tällä hetkellä uskottavasti tuettu.

---

## Kliinisten tutkimusten todisteet

Tällä hetkellä ei ole liittyviä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuustodisteet

Tällä hetkellä ei ole saatavilla liittyvää kirjallisuutta.

---

## Suomen markkinatiedot

Remdesiviri ei ole tällä hetkellä markkinoilla Suomessa (0 markkinointihyväksyntöä tietueissa).

---

## Turvallisuusnäkökohdat

Viitatkaa tuotepakettiin turvallisuustietojen osalta.

*(Huomautus: TFDA-tuotepakettiohjeiden varoitukset/vasta-aiheet ovat estävän vakavuusasteen tietovajeita (DG001), jotka on ratkaistava, ennen kuin voidaan aloittaa mikä tahansa S1-turvallisuustarkastelu.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidossa**

**Perustelut:**
Korkeimmalle sijoitetulla ennusteella (monisisäinen endokrininen neoplasia) ei ole tukevia kliinisiä tutkimuksia tai kirjallisuutta, ja todisteistopaketin oman mekaanisen analyysin mukaan biologista uskottavuutta ei ole — ennuste on todennäköisesti tiedon graafin artefakti. Yhdistettynä Suomen markkinoiden puuttumiseen ja turvallisuus-/merkintätietojen estävän vakavuusasteen vajeeseen, tämä ehdokas ei täytä vaatimuksia S0-vaiheesta etenemiseksi.

**Jatkamiseksi seuraava on tarpeen:**
- TFDA/Fimea-vastaavat tuotepakettiohjeiden tiedot (varoitukset, vasta-aiheet) — tällä hetkellä estävä vajeeksi (DG001)
- Vahvistettu vaikutusmekanismi DrugBankista — tällä hetkellä korkean vakavuusasteen vajeeksi (DG002)
- Kaikki prekliiniset tai mekaaniset todisteet, jotka yhdistävät RdRp-kohdistuvat nukleotidin analogit MEN-liittyviin signalointireitteihin (*RET*, *MEN1*), ennen kuin tämä ehdokas voidaan ottaa uudelleen tarkasteluun
- Jos sen sijaan päätetään tutkia muita TxGNN-sijoitettuja ehdokkaita (esim. HIV-infektio), haettujen tutkimusten/kirjallisuuden uudelleentarkastelu on tarpeen, koska nykyiset tietueet näyttävät olevan COVID-19/Ebola-tutkimuksia, jotka on virheellisesti yhdistetty taudin nimikkeeseen pikemminkin kuin aito HIV-spesifinen todiste

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

