---
layout: default
title: Asfotase Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase alfa: Arviointi odottaa – riittämätön näyttöpaketti

## Yhden lauseen yhteenveto

Asfotase alfa on rekombinantti kudosspesifioitumaton alkalinen fosfataasi (TNSALP) -entsyymin korvaushoito, joka on hyväksytty kansainvälisesti hypofosfolatasiaan (HPP) — harvinaiseen, potentiaalisesti henkeä uhkaavaan perittyyn aineenvaihdunnan ja luuston häiriöön.
Nykyinen näyttöpaketti sisältää **ei TxGNN:n ennustamia uudelleenhyödyntöindikaatioita**, ja kaksi kriittistä tietoaukoa (vaikutusmekanismi ja turvallisuusvaroitukset) jäävät ratkaisematta.
Täydellinen uudelleenhyödyntöarviointi **ei voi edetä**, kunnes nämä aukot on korjattu.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Hypofosfolataasia (HPP) — perinataalinen/lapsuusikäinen/nuoruusikäinen alkaminen (kansainvälinen hyväksyntä; puuttuu Taiwanin sääntelyrekistereistä) |
| Ennustettu uusi indikaatio | Ei saatavilla |
| TxGNN-ennustepisteet | Ei saatavilla |
| Näytön taso | N/A — ei TxGNN-ennusteita olemassa |
| Taiwanin markkinatilanne | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Pidä varalla** |

---

## Miksi ennusteita ei ole saatavilla?

Asfotase alfa on suurimolekyylinen rekombinantti entsyymin korvaushoito — lääkeryhmä, joka eroaa merkittävästi pienimolekyylisistä lääkkeistä, joiden perusteella TxGNN:n tietokaavioupotuksia pääasiassa opetetaan.

Kolme tekijää selittävät todennäköisesti ennusteiden puuttumisen:

1. **Biologi / ERT-luokka**: Entsyymin korvaushoitot toimivat täyttämällä puuttuvan endogeenisen entsyymin (TNSALP). Niiden mekanismi on substraattikohtainen, mikä jättää rajoitetun toiminta-alan eri indikaatioiden välisille uudelleenhyödyntöille verrattuna reseptorikohteisiin suuntautuneisiin pienimolekyylisiin lääkkeisiin. TxGNN-mallissa ei välttämättä ole riittävästi kaaviokytkentöjä tälle yhdisteelle uudelleenhyödyntöhypoteesien muodostamiseksi.

2. **Ultra-harvinaisen sairauden signaali**: HPP:n arvioidaan esiintyvän noin 1 henellä 300 000:sta. Tämän lääkkeen tietokaavion koulutustiedot ovat harvat, mikä vähentää mallin kykyä päätellä uusia indikaatiokytkentöjä sairauksien välisten tai geeni-sairaus-rinnakkaisesiintymisen reittien kautta.

3. **MOA:n tietoaukko**: Näyttöpaketti ei sisällä vaikutusmekanismin merkintää lääkkeelle DB09105 (merkitty DG002, vakavuus: High). Ilman MOA-solmua tietokaavioissa, mekanistista samankaltaisuusanalyysiä ei voida suorittaa, ja uudelleenhyödyntömoottorilla ei ole ankkurikohtaa, josta ehdokasindikaa ionit voitaisiin projisioida.

Kunnes TxGNN palauttaa ennusteehdokkaat tälle yhdisteelle, uudelleenhyödyntösuositusta ei voida tehdä.

---

## Taiwanin markkinatiedot

Asfotase alfa **ei ole tällä hetkellä hyväksytty eikä markkinoilla Taiwanissa**.

| Hyväksynnän numero | Tuotteen nimi | Antomuoto | Hyväksytty indikaatio |
|---------------------|--------------|-------------|---------------------|
| — | — | — | Ei hyväksynnöistä rekistereissä |

---

## Turvallisuusnäkökohdat

Katso turvallisuustiedoista pakkausselosteesta.

Kaikki turvallisuuskentät nykyisessä näyttöpaketissa ovat ratkaisemattomia tietoaukkoja: kriittiset varoitukset (DG001, vakavuus: Blocking), vasta-aiheet (DG001, vakavuus: Blocking) ja lääkkeiden vuorovaikutustiedot eivät ole saatavilla. Turvallisuusarviointia ei voida suorittaa tässä vaiheessa.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä varalla**

**Perustelut:**
Asfotase alfan näyttöpaketti on kriittisesti epätäydellinen — ei TxGNN-ennusteita, ei Taiwanin sääntelyrekistereita ja ei hyödynnettävää turvallisuustietoa. Yhdistettä ei voida arvioida uudelleenhyödyntöpotentiaalin osalta ennen kuin estävät tietoaukot on ratkaistu.

**Jatkamiseksi tarvitaan seuraavaa:**

- **Vahvista TxGNN-putkilinjan kattavuus**: Tarkista, sisältyikö DB09105 ennusteiden suoritukseen. Biologit ja entsyymin korvaushoitot saattavat vaatia omistettua kaaviosidonnaislisäysvaihetta tai poissulkemislipun dokumentointia.
- **Nouda MOA DrugBankista** (DG002): Kysy DrugBank API:ta vaikutusmekanismimerkinnälle DB09105:lle. Tämä vaaditaan kaikille myöhemmille mekanistisille analyyseille.
- **Jäsennä Taiwanin pakkausseloste TFDA:sta** (DG001, Blocking): Lataa ja poimi 仿單 PDF saadaksesi viralliset varoitukset, vasta-aiheet ja varotoimet ennen kliinistä turvallisuusarviointia.
- **Vahvista kansainvälinen hyväksyntätilanne**: Asfotase alfalla on FDA:n ja EMA:n hyväksynnät HPP:lle. Vahvista, onko Suomen Fimea myöntänyt vastaavan hyväksynnän, sillä se vahvistaisi perustavanlaatuisen sääntelyllisen ennakkotapauksen kaikelle uuden indikaation hakemukselle.
- **Arvioi harvinaisen sairauden kehikon soveltuvuutta**: HPP:llä on harvinaisen lääkkeen nimitys useissa lainkäyttöalueissa. Kaikki uudelleenhyödyntöehdokkaat tulisi arvioida harvinaisen sairauden sääntelypolussa, mikä voi vaikuttaa näytön kynnysarvoihin ja hyväksyntäaikatauluihin.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

