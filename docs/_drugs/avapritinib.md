---
layout: default
title: Avapritinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: Evidence Pack -tietojen puutteellisuus — alustava puuteanalyysin raportti

## Yhteenveto

Avapritinib (DB15233) on kiinaasi-inhibiittoriluokan lääkeaine, jota ei ole tällä hetkellä markkinoilla Taiwanissa.
Tämä Evidence Pack **ei sisällä mitään TxGNN-ennustettuja indikaatioita**, ja vaikutusmekanismin (MOA) sekä turvallisuustiedot sisältävät kriittisiä puutteita.
**Täydellisen vanhanlääkkeen uudelleenkäytön arviointia ei voida suorittaa**, ja suosituksena on merkitä se **Hold**-tilaan tietojen täydentämisen jälkeistä uudelleenarvointia varten.

---

## Nopea katsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäiset indikaatiot | Ei annettu Evidence Packissa |
| Ennustetut uudet indikaatiot | Tämä pakkaus ei sisällä TxGNN-ennusteita |
| TxGNN-ennustepistemäärä | Ei |
| Todisteen taso | L5 (malliennusteen taso, mutta pakkaus ei vielä sisällä ennusteita) |
| Taiwanin markkinatila | ✗ Not marketed |
| Lupapäätösten lukumäärä | 0 |
| Ehdotettu päätös | **Hold** |

---

## Miksi mekanismin yhdistämisen analyysia ei voida suorittaa

Tämä Evidence Pack puuttuu seuraavista kahdesta ydintiedoista, mikä tekee mekanismi-indikaation päättelyä mahdottomaksi:

Avapritinibin yksityiskohtainen vaikutusmekanismin tieto puuttuu tästä Packista (DG002, High severity). Alkuperäisen indikaation kenttä on myös tyhjä, eikä "alkuperäinen sairaus → vaikutusmekanismi → ennustettu sairaus" -päättelyketjua voida muodostaa.

Lisäksi TxGNN-malli **ei ole tuottanut tälle lääkeaineelle mitään ennustettuja indikaatioita** (`predicted_indications: []`), mikä osoittaa, että tässä arviointikierroksessa puuttuu vanhan lääkkeen uudelleenkäytön ehdokkaat, ja raportin ydinanalyysikappaleet eivät voi siten avautua.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä arvioitavia ennustettuja indikaatioita ei ole saatavilla, joten vastaavia kliinisen tutkimuksen tietoja ei ole.

---

## Kirjallisuustutkimuksen näyttö

Tällä hetkellä arvioitavia ennustettuja indikaatioita ei ole saatavilla, joten vastaavia kirjallisuustutkimuksen tietoja ei ole.

---

## Taiwanin markkinatiedot

Avapritinib **ei ole tällä hetkellä saavuttanut lääkkeen markkinointiluvan Taiwanissa**. TFDA-haku (hakupäivä: 2026-03-29) antoi 0 tuloksia, `taiwan_regulatory.licenses` on tyhjä.

---

## Turvallisuusnäkökohdat

Katso lääkkeen pakkausselosteesta varoitukset ja vasta-aiheet.

> Tämän Evidence Packin turvallisuusvaroitukset, vasta-aiheet ja lääkevuorovaikutus-kyselyt eivät palauttaneet käyttökelpoisia tietoja (DDI-kyselyjen tila: not_found). Fimea-pakkausselosteen varoitukset/vasta-aiheet (DG001, **Blocking**-tasoinen puute) odottavat täydentämistä, ja tämä puute estää S1-turvallisuusarvioinnin aloittamisen.

---

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Hold**

**Perustelu:**
Tämä Evidence Pack sisältää Blocking-tasoisen tietopuutteen (DG001: TFDA-pakkausseloste) sekä High-tasoisen puutteen (DG002: MOA), eikä TxGNN ole tuottanut mitään ennustettuja indikaatioita. Tällä hetkellä ei ole perusedellytyksiä vanhan lääkkeen uudelleenkäytön arviointiin.

**Seuraavaan vaiheeseen siirtymiseksi vaadittavat täydennykset:**

1. **（Blocking）** Täydennä TFDA-pakkausseloste PDF:nä ja analysoi varoitukset ja vasta-aiheet (DG001)
2. **（High）** Hae vaikutusmekanismin (MOA) tiedot DrugBank API:n kautta (DG002)
3. **（Vaatii）** Varmista, onko TxGNN jo suorittanut ennustuksen DB15233:lle. Jos ei, käynnistä ennustusprosessi
4. **（Suositus）** Varmista alkuperäiset hyväksytyt indikaatiot (GIST / systeeminen mastosolun proliferaatio jne.) ja täytä `original_indications`
5. **（Suositus）** Täydennä lääkevuorovaikutusten (DDI) tiedot

---

> ⚠️ **Tietojen täydellisyyden varoitus**
> Tämä raportti on tietojen puutepuolesta tehty analyysi, ei muodollinen vanhan lääkkeen uudelleenkäytön arviointiraportti. Kun edellä mainitut tiedot on täydennetty ja TxGNN on tuottanut ennustetut indikaatiot, on suoritettava täydellisen raportin prosessi uudelleen (ehdokas-ID: TW-DB15233-multi, versio v4, tietojen katkaisu: 2026-04-20).

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

