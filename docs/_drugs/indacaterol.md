---
layout: default
title: Indacaterol
parent: Pelkkä mallin ennuste (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indakaterooli: Hengitysteiden bronkodilataatiosta nefrogeniseen sopimattoman antidiureesin oireyhtymään

## Yhden lauseen yhteenveto

Indakaterooli on pitkävaikutteinen β2-adrenergisen reseptorin agonisti (LABA), jota käytetään hengitysteiden sairauksiin (COPD/astma) liittyvän lääkityksen osana, yleisimmin yhdistettynä glykopirroniinin ja/tai mometasoniinin kiinteisiin kombinaatioihin. TxGNN-mallin korkeimmin sijoittuva ennuste tälle ehdokaspaketille on **nefrogeninen sopimattoman antidiureesin oireyhtymä (NSIAD)**, mutta tämä sijoittuu pakkauksen kymmenen ennusteen joukkoon, joilla on **nolla kliinistä tutkimusta ja nolla julkaisua**, jotka tukisivat sitä, ja mukana oleva mekanistinen katsaus ei löydä mitään uskottavaa biologista yhteyttä.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei muodollisesti dokumentoituna (ks. huomautus alla); näyttöpaketti vahvistaa, että indakaterooli vaikuttaa LABA-bronkodilataattorina hengitysteiden sairauksiin |
| Ennustettu uusi indikaatio | Nefrogeninen sopimattoman antidiureesin oireyhtymä |
| TxGNN-ennusteen pistemäärä | 99.54% |
| Näyttötaso | L5 |
| Suomen markkinatilanne | Ei markkinoilla |
| Lupien määrä | 0 |
| Suositeltu päätös | Pidätä |

*Huomautus: `taiwan_regulatory.licenses` on tyhjä (lääkettä ei ole markkinoilla Suomessa), joten virallista hyväksytyn indikaation tekstiä ei ole saatavilla kyseisestä lähteestä.*

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla (tietojen puutosvaatimus DG002). Tämän näyttöpaketin sisällä olevan tiedon perusteella indakaterooli on pitkävaikutteinen β2-adrenergisen reseptorin agonisti, joka aktivoi β2-reseptoreita keuhkoputkien sileiden lihasten pinnalla, nostaen solunsisäisen cAMP:n tasoa ja tuottaen bronkodilataatiota — vakiintunut mekanismi, joka on sen pääasiallisen hengitysteiden käytön taustalla (ks. alla oleva "keuhkoputkiston sairaus" -ehdokas, jolla on vahva näyttötuki mutta joka edustaa jo tunnettua käyttöä, ei uuden uudelleenkäytön mahdollisuutta).

Korkeimmin sijoittuneelle ehdokkaalle — nefrogeniselle sopimattoman antidiureesin oireyhtymälle — näyttöpaketin oma mekanistinen katsaus ei löydä **mitään uskottavaa yhteyttä**: NSIAD johtuu munuaisen V2-vasopressiini-reseptorin aktivoivista mutaatioista, ja sen standardi hallinta (nesteen rajoittaminen tai vaptaanit/V2-reseptoriantagoniistit) toimii polulla, jolla ei ole tunnettua vuorovaikutusta β2-adrenergisen signaloinnin kanssa. Korkea TxGNN-pistemäärä näyttää siis heijastavan graafi-upotusten samankaltaisuutta biologisesti perustellun hypoteesin sijaan, eikä kliinisiä tutkimuksia, ICTRP-tietueita tai PubMed-kirjallisuutta ole olemassa sen perustelemiseksi (kyselylokin merkinnät #5–#7, kaikki nolla tuloksia).

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole olemassa asiaan liittyviä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

## Suomen markkinatiedot

Indakateroolia ei ole tällä hetkellä markkinoilla Suomessa — 0 valtuutusta on rekisterissä (`taiwan_regulatory.market_status`: Ei markkinoilla / Not Marketed).

## Turvallisuutta koskevat näkökohdat

Katso turvallisuustiedot pakkausselosteesta. (TFDA-pakkausselosteen varoitukset ja kontraindikaatiot on merkitty **estäväksi** aineistopuutokseksi — DG001 — odottamassa hakemista ja jäsentämistä, ennen kuin S1-turvallisuuskatsaus voidaan aloittaa.)

## Muut ennustetut indikaatiot tässä näyttöpaketissa

Tämä ehdokaspaketti (`TW-DB05039-multi`) sisältää 10 TxGNN-ennustetta indakateroolille. Kontekstiksi ne on esitetty alla; vain sijoituksella 7 on tällä hetkellä merkitsevää tukea, ja se heijastaa jo vakiintunutta käyttöä (hengitysteiden bronkodilataatio) eikä uuden uudelleenkäytön mahdollisuutta.

| Sijoitus | Ennustettu indikaatio | TxGNN-pistemäärä | Näyttötaso | Suositus |
|----------|----------------------|-----------------|----------|----------|
| 1 | Nefrogeninen sopimattoman antidiureesin oireyhtymä | 99.54% | L5 | Pidätä |
| 2 | Päänsärkyoireyhtymä | 99.53% | L5 | Pidätä |
| 3 | Kolmoissilmähermon autonominen kefalalgia | 99.33% | L5 | Pidätä |
| 4 | Paratenonitis | 99.26% | L5 | Pidätä |
| 5 | Kalsifioituva jänteiden tulehdus | 99.25% | L5 | Pidätä |
| 6 | Hypertrikoosi (sairaus) | 99.23% | L5 | Pidätä |
| 7 | Keuhkoputkiston sairaus | 99.18% | L1 | Jatka varauksin (tunnettu indikaatio, ei uutta) |
| 8 | Myosiitti | 99.12% | L5 | Pidätä |
| 9 | Anafilaksia | 99.07% | L4 | Pidätä |
| 10 | Ambras-tyypin yleinen synnynnäinen hypertrikoosi | 99.06% | L5 | Pidätä |

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Vaikka NSIAD:n TxGNN-pistemäärä on korkea (99.54%), sitä ei tue mikään kliininen tutkimus tai kirjallisuuden näyttö, ja tämän näyttöpaketin sisällä oleva mekanistinen katsaus ei eksplisiittisesti löydä mitään biologista perustelua, joka yhdistäisi β2-adrenergisen bronkodilataation V2-reseptorivälitteiseen vesitasapainohäiriöön. Tämä on L5-ehdokas (vain mallin ennuste), jolle pisteytysvaihe suosittaa jo pidättämistä.

**Jatkaakseen seuraavaa tarvitaan:**
- TFDA/Suomen pakkausselosteen varoitukset ja kontraindikaatiot (Estävä aukko DG001) ennen kuin turvallisuusarviointi on mahdollinen
- Vahvistetut vaikutusmekanismin tiedot (Korkea-prioriteettinen aukko DG002)
- Prekliinisiä tai mekanistisia tutkimuksia, jotka testaavat β2-agonismin vaikutusta NSIAD:iin tai siihen liittyviin vesitasapainohäiriöihin, koska sellaisia ei tällä hetkellä ole olemassa
- Jos uudelleenkäytettävää ehdokasta haetaan tästä paketista, kannattaa harkita paremmin perusteltuja signaaleita (esim. sijoitus 9, anafilaksia, L4) nykyisen korkeimmin sijoittuneen, mutta mekanistisesti perustelemattoman ennusteen sijaan

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

