---
layout: default
title: Aztreonam
parent: Pelkkä mallin ennuste (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Aztreonam: ennustettu uusi käyttöaihe Hyperamylasemia (sijalla 1 (näytön taso L5). Alkuperäinen käyttöaihe: Gramnegatiiviset bakteeri-infektiot, virtsatieinfektiot…"
monitor_inn: "AZTREONAM"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
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

# Atstreonaami: Bakteeri-infektioista gonokokkiuretriittiin

## Yhden virkkeen yhteenveto

Atstreonaami on monobaktaamiantibiootti, jota käytetään alun perin gramnegatiivisten bakteeri-infektioiden, virtsatieinfektioiden, sairaalaperäisen keuhkokuumeen ja pehmytkudosinfektioiden hoitoon.
TxGNN-malli ennustaa sen voivan tehota ensisijaisesti kohteeseen **hyperamylasemia**, mutta tämä ennuste ei perustu mihinkään tutkimusnäyttöön. Kliinisesti uskottavin ennustettu käyttöaihe on **gonokokkiuretriitti**, jota tukee **6 julkaisua** mutta **ei yhtään rekisteröityä kliinistä tutkimusta**.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Gramnegatiiviset bakteeri-infektiot, virtsatieinfektiot, sairaalaperäinen keuhkokuume, pehmytkudosinfektiot |
| Ennustettu uusi käyttöaihe | Hyperamylasemia (sijalla 1; näyttöön perustuen kiinnostavin on gonokokkiuretriitti, sijalla 4) |
| TxGNN-ennustepistemäärä | 99,73 % (hyperamylasemia); 99,59 % (gonokokkiuretriitti) |
| Näytön taso | L5 (hyperamylasemia); L3 (gonokokkiuretriitti) |
| Markkinatilanne Suomessa | Vain peruutettu myyntilupa |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) – gonokokkiuretriitti: jatkotutkimuskysymys |

---

## Miksi ennuste on perusteltu (tai ei)?

Atstreonaamin vaikutusmekanismitietoja ei ole tällä hetkellä saatavilla kootussa aineistossa. Tunnetun farmakologian mukaan atstreonaami on monobaktaamiantibiootti, joka sitoutuu gramnegatiivisten bakteerien penisilliiniä sitovaan proteiiniin 3 (PBP3) ja estää soluseinän synteesiä.

**Ykkösennuste (hyperamylasemia):** Mekanistista yhteyttä amylaasiaineenvaihduntaan ei ole. Korkea pistemäärä on pelkkä mallin ennuste ilman tukevia tutkimuksia tai kirjallisuutta. Samoin ennusteet polyklonaalinen hyperviskositeettioireyhtymä, synnynnäinen analbuminemia ja esiasteinen hematologinen sairaus eivät ole mekanistisesti perusteltuja; ne ovat todennäköisesti tietämysgraafin artefakteja.

**Gonokokkiuretriitti:** Tämä on biologisesti uskottava, koska atstreonaami sitoutuu *Neisseria gonorrhoeae* -bakteerin PBP3:een ja on tehonnut penisilliiniresistentteihin gonokokkeihin. 1980-luvun kerta-annostutkimukset ja vuoden 2020 yhden haaran avoin tutkimus (2 g) tukevat kliinistä tehoa. Kyse on kuitenkin suorasta antibakteerisesta käytöstä, joka on lähellä alkuperäisiä käyttöaiheita, ei varsinaista uudelleenkäyttöä. Lisäksi vuoden 2001 raportti kuvaa kefeemi- ja atstreonaamiresistenttien kantojen ilmaantumista. Nykysuositukset nojaavat muihin lääkkeisiin, joten atstreonaami olisi korkeintaan marginaalinen vaihtoehto resistentissä infektiossa tai beetalaktaami-allergiassa.

**Ureaplasma-uretriitti:** Mekanistisesti epäedullinen, koska *Ureaplasmalta* puuttuu soluseinä, eikä soluseinän synteesiä estävä beetalaktaami todennäköisesti tehoa.

---

## Kliininen tutkimusnäyttö

Kliinisiä tutkimuksia ei ole tällä hetkellä rekisteröity yhdellekään ennustetulle käyttöaiheelle.

---

## Kirjallisuusnäyttö

Gonokokkiuretriitti (sija 4):

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Yhden haaran avoin kliininen tutkimus | Antimicrob Agents Chemother | Kerta-annos 2 g lihakseen *N. gonorrhoeae* -infektion hoidossa miehillä |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Kliininen tutkimus | Genitourin Med | 1 g lihakseen paransi komplisoitumattoman gonorrean lähes kaikilla 61 miehellä ja 26 naisella; toimi myös penisilliiniresistentteihin kantoihin |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Kliininen tutkimus | Antimicrob Agents Chemother | 1 g lihakseen vs. spektinomysiini 2 g: ei hoidon epäonnistumisia kummallakaan |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiologinen ja hoitotutkimus | Hinyokika Kiyo | Kerta-annoshoito atstreonaamilla gonorreainfektioissa |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Kliininen/in vitro -tutkimus | J Infect Dis | Teho penisilliiniresistentteihin gonokokkeihin |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Mikrobiologinen/resistenssitutkimus | J Infect Chemother | Kefeemi- ja atstreonaamiresistenttien, beetalaktamaasia tuottamattomien gonokokkien ilmaantuminen |

Muut ennusteet (epäsuora tai epärelevantti näyttö):

| PMID | Vuosi | Tyyppi | Lehti | Käyttöaihe | Keskeiset havainnot |
|------|-----|------|------|------|---------|
| [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/) | 1986 | Lasten tapaussarja | Am J Dis Child | Epiglottiitti | 59 lasta, vakavat gramnegatiiviset infektiot; epäsuora tuki |
| [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/) | 1985 | Kliininen tutkimus | Jpn J Antibiot | Monoklonaalinen gammopatia | Hematologisten sairauksien vakavat infektiot; hoitovaste 51,1 %; tuki infektion hoidolle, ei gammopatian hoidolle |
| [34956120](https://pubmed.ncbi.nlm.nih.gov/34956120/) | 2021 | Mikrobiologinen/genominen | Front Microbiol | Veriryhmäyhteensopimattomuus | blaNDM-1 ja mcr-9 -geenien yhteisesiintyminen; ei liity käyttöaiheeseen (todennäköinen hakusanavirhe) |

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/006113 (peruutettu) | Emblaveo | – | Gramnegatiiviset bakteeri-infektiot, virtsatieinfektiot, sairaalaperäinen keuhkokuume, pehmytkudosinfektiot |

---

## Turvallisuushuomiot

Valmisteyhteenvedon varoitus- ja vasta-aihetietoja ei ole saatavilla tässä aineistossa. Tietämysgraafin (PrimeKG) lääke–tauti-vasta-aihe-yhteyksien perusteella (ei valmisteyhteenvetoteksti) mahdollisia huomioitavia tiloja ovat: munuaissairaus, virtsanjohtimen märkäpesäke (pyoureter), maksasairaus, sappirakkosairaus, *Clostridium difficile* -paksusuolitulehdus, vastasyntyneen nekrotisoiva enterokoliitti ja keuhkoputkisairaus.

**Yhteisvaikutukset:** Yhteensä 27 yhteisvaikutusta löytyi. Merkittävimmät (kohtalainen taso):
- Pikosulfaatti
- Dikumarolli
- Varfariini

Muilla listatuilla lääkkeillä (mm. vankomysiini, amikasiini, metronidatsoli, omepratsoli, pantopratsoli, hepariini, takrolimuusi, amfoterisiini B) vaikutuksen vakavuutta ei ole luokiteltu.

Muilta osin turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Korkeimmin pisteytetyille ennusteille (hyperamylasemia, hyperviskositeettioireyhtymä, analbuminemia) ei ole mekanistista perustetta eikä tutkimusnäyttöä. Gonokokkiuretriitti on uskottavin (L3), mutta se on suora antibakteerinen käyttö ilman satunnaistettuja tutkimuksia, resistenssiä on raportoitu ja Suomen myyntilupa on peruutettu.

**Jatkoon tarvitaan:**
- Valmisteyhteenvedon varoitus- ja vasta-aihetiedot (Fimea) – estävä tietoaukko
- Vaikutusmekanismitiedot (DrugBank)
- Gonokokkiuretriitille satunnaistettu tutkimusnäyttö ja ajantasainen resistenssitieto sekä vertailu nykyisiin suosituksiin
- Arvio myyntiluvan tilanteesta ja saatavuudesta Suomessa (Emblaveo peruutettu)
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

