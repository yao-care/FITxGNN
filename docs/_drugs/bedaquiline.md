---
layout: default
title: Bedaquiline
parent: Pelkkä mallin ennuste (L5)
nav_order: 71
evidence_level: L5
indication_count: 4
monitor_inn: "Bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
last_modified_at: 2026-10-28
description: "Bedaquiline: ennustettu uusi käyttöaihe Vulvovaginaalinen kandidoosi (vulvovaginal candidiasis) (näytön taso L5). Alkuperäinen käyttöaihe: Tuberculosis, Multidrug-Resistant"
---

# Bedaquiline
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

## Bedakiliini: mykobakteerien ATP-syntaasin estäjä → vulvovaginaalinen kandidoosi (vulvovaginal candidiasis)
{: .text-alpha }

## Yhteenveto

Bedakiliini on tuberkuloosilääke, joka estää mykobakteerien ATP-syntaasia. TxGNN-malli ennustaa sen mahdollisesti hyödylliseksi **vulvovaginaalisessa kandidoosissa (vulvovaginal candidiasis)**. Ennusteen tueksi ei ole löytynyt yhtään kliinistä tutkimusta eikä julkaisua, joten ennuste perustuu pelkästään laskennalliseen malliin.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Tuberculosis, Multidrug-Resistant |
| Ennustettu uusi käyttöaihe | Vulvovaginaalinen kandidoosi (vulvovaginal candidiasis) |
| TxGNN-ennusteen pistemäärä | 0,9988 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohtien ”Mechanism of Action” ja ”Microbiology” mukaan valmisteesta Bedaquiline (epävirallinen käännös): ”Bedakiliini on diaryylikinoliiniryhmän antimykobakteerinen lääke. […] SIRTURO on diaryylikinoliiniryhmän antimykobakteerinen lääke, joka estää mykobakteerien ATP (adenosiini-5'-trifosfaatti) -syntaasia sitoutumalla entsyymin c-alayksikköön, joka on välttämätön energian tuottamiselle M. tuberculosis -bakteerissa.” Englanninkielinen alkuteksti: "Bedaquiline is a diarylquinoline antimycobacterial drug. […] SIRTURO is a diarylquinoline antimycobacterial drug that inhibits mycobacterial ATP (adenosine 5'- triphosphate) synthase, by binding to subunit c of the enzyme that is essential for the generation of energy in M. tuberculosis." ([DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e), versio 2025-10-17; haettu 2026-11-19). Bedakiliinin tiedetään kohdistuvan mykobakteerien ATP-syntaasiin, eikä sillä ole osoitettua sienilääkevaikutusta.

Ennusteelle ei löydy mekanistista tukea. Candida-hiivat ovat sieniä, joiden energia-aineenvaihdunta ja lääkekohteet poikkeavat mykobakteereista. Korkea pistemäärä heijastaa todennäköisesti mallin tuottamaa artefaktia, eikä ennustetta voida pitää uskottavana lääkkeen uudelleenkäyttöehdokkaana nykytiedon valossa.

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002614 | Sirturo | – | Monilääkeresistentti tuberkuloosi |

## Turvallisuushuomioita

Lääkkeiden yhteisvaikutuksia on tunnistettu yhteensä 100. Keskeisiä **merkittäviksi (Major)** luokiteltuja yhteisvaikutuksia ovat:

- deksametasoni
- klaritromysiini
- pikosulfaatti
- polyetyleeniglykoli (3350, elektrolyyttien kanssa)
- dolasetroni
- palonosetroni
- natriumsulfaatti

Lisäksi mm. seuraavat on luokiteltu **kohtalaisiksi (Moderate)**: akarboosi, famotidiini, doksisykliini, pioglitatsoni, loperamidi, bupropioni, bisakodyyli, kenodeoksikolihappo, minosykliini, oksandroloni, oksimetoloni, tetrasykliini ja naltrekseoni.

Muiden turvallisuustietojen osalta katso valmisteyhteenveto.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
Ennusteelle ei ole kliinistä eikä kirjallisuusnäyttöä, eikä bedakiliinilla ole tunnettua sienilääkevaikutusta. Ennuste on pelkkä laskennallinen tulos (näytön taso L5).

**Eteenpäin siirtyminen edellyttää:**
- In vitro -tutkimuksia bedakiliinin vaikutuksesta Candida-lajeihin
- Vaikutusmekanismia koskevien tietojen täydentämistä
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden kokoamista turvallisuusarviointia varten

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera); mallin ennusteita, näytön tasoja ja johtopäätöksiä ei kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

