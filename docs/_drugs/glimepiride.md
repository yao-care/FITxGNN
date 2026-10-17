---
layout: default
title: Glimepiride
parent: Pelkkä mallin ennuste (L5)
nav_order: 205
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Glimepiride: ennustettu uusi käyttöaihe Fokaalinen jäykän raajan oireyhtymä (näytön taso L5). Alkuperäinen käyttöaihe: Tyypin 2 diabetes"
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **9** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

# Glimepiridi: Tyypin 2 diabeteksesta fokaaliseen jäykän raajan oireyhtymään

## Yhteenveto

Glimepiridi on sulfonyyliurearyhmän lääke, jota käytetään tyypin 2 diabeteksen hoitoon. TxGNN-malli ennustaa sen voivan tehota **fokaaliseen jäykän raajan oireyhtymään** (focal stiff limb syndrome). Ennusteen tueksi ei kuitenkaan ole **yhtään kliinistä tutkimusta eikä julkaisua**, joten kyseessä on pelkkä mallipohjainen ennuste.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Tyypin 2 diabetes |
| Ennustettu uusi käyttöaihe | Fokaalinen jäykän raajan oireyhtymä |
| TxGNN-ennustepistemäärä | 99,75 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi vaikuttaa uskottavalta?

Glimepiridin vaikutusmekanismitietoja ei ole tässä raportissa käytettävissä. Tunnetusti glimepiridi on sulfonyyliurea, joka sulkee haiman beetasolujen KATP-kanavia ja lisää insuliinin eritystä. Teho tyypin 2 diabeteksessa on osoitettu.

Ennuste perustuu todennäköisesti tiedon verkostoon (graafiin) liittyvään yhteyteen: jäykän raajan oireyhtymät ovat usein autoimmuunitaustaisia (anti-GAD65) ja esiintyvät yhdessä diabeteksen kanssa. Diabetekseen liittyvät solmut voivat siten paisuttaa pistemäärää.

Mekanistista perustetta ei kuitenkaan ole. Glimepiridillä ei ole tunnettua vaikutusta GABAergiseen toimintaan tai selkäytimen välineuronien yliärtyvyyteen. Ennuste on siis spekulatiivinen eikä sitä tue kliininen tieto.

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000680 | Tandemact | – | Tyypin 2 diabetes (peruutettu) |

## Turvallisuushuomiot

- **Muut mahdolliset sairausyhteydet (tietämysgraafista, ei valmisteyhteenvedosta):** Tietämysgraafin lääke–tauti-vasta-aihe-yhteyksiin kuuluvat mm. munuaissairaus, maksasairaus, sappirakon sairaus, kongestiivinen sydämen vajaatoiminta, aivolisäkkeen vajaatoiminta (hypopituitarismi), kasvuhormonin puutos, Kallmannin oireyhtymä, Sheehanin oireyhtymä, kateenkorvan sairaus, osteoporoosi ja infektiosairaudet. Nämä ovat mallin tuottamia yhteyksiä, eivät valmisteyhteenvedon tekstiä.
- **Yhteisvaikutukset:** Yhteisvaikutushaussa löytyi 100 yhteisvaikutusta. Esimerkkejä keskivaikeista (Moderate) yhteisvaikutuksista: fenyylefriini, asebutololi, asetatsoliamidi, famotidiini, ranitidiini, asitretiini, formoteroli, pseudoefedriini, ketorolaakki, adrenaliini, ibuprofeeni, etinyyliestradioli, hydrokortisoni, albiglutidi, salbutamoli, etanoli, nitatsoksanidi ja hydroklooritiatsidi. Lieviä (Minor) yhteisvaikutuksia ovat mm. paikallisesti käytettävä hydrokortisoni ja alklometasoni.

Valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat, joten ne on tarkistettava valmisteyhteenvedosta.

## Muut ennustetut käyttöaiheet (lyhyesti)

Muut ennusteet ovat myös tasolla L5 ja suositus on Hold:

- Klassinen jäykän ihmisen oireyhtymä (99,75 %): mekanistinen yhteys epätodennäköinen, vakiohoidot ovat bentsodiatsepiinit, baklofeeni ja IVIG.
- Opsismodysplasia (99,74 %): teoreettinen yhteys insuliinisignalointiin, ei kliinistä näyttöä.
- Tiamiinille vasteinen oireyhtymä (99,73 %): mahdollinen hyöty koskisi vain diabeteskomponenttia.
- Lääkeaineen aiheuttama paikallinen lipodystrofia sekä sentrifugaalinen, paineen aiheuttama ja idiopaattinen paikallinen lipodystrofia (99,56–99,62 %): ei uskottavaa farmakologista perustetta.
- Haiman agenesia (99,55 %): sulfonyyliurea vaatii toimivia beetasoluja, joten teho on mekanistisesti epätodennäköinen. Ainoa löytynyt julkaisu (PMID 12720536) koskee insulinoomien endosonografiakuvantamista eikä tue glimepiridin käyttöä.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu vain graafipohjaiseen malliin ilman kliinistä tai kirjallista näyttöä, eikä uskottavaa vaikutusmekanismia ole. Lisäksi Suomessa on vain peruutettu myyntilupa.

**Etenemiseksi tarvitaan:**
- Valmisteyhteenvedon turvallisuustiedot Fimean sivustolta (estävä tietoaukko)
- Vaikutusmekanismin tiedot (esim. DrugBankista)
- Prekliininen tai kliininen näyttö glimepiridin vaikutuksesta jäykän raajan oireyhtymään
- Selvitys valmisteen saatavuudesta Suomessa, koska voimassa olevaa myyntilupaa ei ole
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

