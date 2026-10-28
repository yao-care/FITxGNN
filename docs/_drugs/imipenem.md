---
layout: default
title: Imipenem
parent: Pelkkä mallin ennuste (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "Imipenem"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "staphylococcus aureus infection", "eosinophilia-myalgia syndrome"]
description: "Imipenem: ennustettu uusi käyttöaihe Diffuse scleroderma (näytön taso L5). Alkuperäinen käyttöaihe: Gram-Negative Bacterial Infections"
---

# Imipenem
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

## Imipenem: Diffuse scleroderma
{: .text-alpha }

## Yhden lauseen tiivistelmä

Imipeneemi on karbapeneemiantibiootti, jota on alun perin käytetty Gram-negatiivisten bakteeri-infektioiden hoitoon.
TxGNN-malli ennustaa sen voivan olla tehokas mm. **Staphylococcus aureus -infektioon** (tarkasteltu, koska siitä löytyy eniten kliinistä näyttöä), mutta mallin korkeimmin pisteyttämä ennuste on **diffuusi skleroderma**.
Tämän kohteen tueksi on **2 kliinistä tutkimusta** ja **18 julkaisua**; useimpien muiden ennusteiden tuki on vain epäsuoraa herkkyys- ja resistenssitutkimuksiin perustuvaa tietoa.

> Huomio: ennusteen sijalla 1 on diffuusi skleroderma (TxGNN-pistemäärä 0,9999), mutta sille ei löytynyt yhtään tutkimusta eikä mekanistista perustetta. Tässä raportissa pääpainona on siksi ennuste, jolla on vahvin näyttö (sija 9, Staphylococcus aureus -infektio). Muut ennusteet käsitellään yhteenvetona.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Gram-Negative Bacterial Infections |
| Ennustettu uusi käyttöaihe (korkein pistemäärä) | Diffuse scleroderma |
| Ennustettu uusi käyttöaihe (vahvin näyttö) | Diffuse scleroderma |
| TxGNN-ennustepistemäärä | 0.9999 |
| Näytön taso | L5 (skleroderma); L3 (S. aureus -infektio) |
| Suomen markkinatilanne | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota); S. aureus -infektio: tutkimuskysymys jatkoselvitykseen |

---

## Miksi ennuste on perusteltu?

Tarkempia tietoja imipeneemin vaikutusmekanismista ei ole tämän raportin aineistossa saatavilla. Tunnetun tiedon perusteella imipeneemi on karbapeneemi, joka estää bakteerin soluseinän synteesiä sitoutumalla penisilliiniä sitoviin proteiineihin (PBP). Sen teho Gram-negatiivisissa infektioissa on osoitettu, ja mekanistisesti se voi soveltua myös muihin bakteeriperäisiin infektioihin.

**Diffuusi skleroderma (sija 1):** Antibakteerisella karbapeneemilla ei ole uskottavaa mekanistista yhteyttä systeemisen skleroosin autoimmuuni- ja fibroottiseen patologiaan. Korkea pistemäärä vaikuttaa graafipohjaiselta ennustevirheeltä, eikä tutkimuksia tai kirjallisuutta löytynyt.

**Staphylococcus aureus -infektio (sija 9):** Imipeneemi tehoaa metisilliiniherkkiin S. aureus -kantoihin, mutta metisilliinille resistentti S. aureus (MRSA) on luontaisesti resistentti PBP2a-proteiinin vuoksi. Kiinnostus kohdistuu yhdistelmähoitoihin, erityisesti imipeneemin ja fosfomysiinin yhdistelmään, joka osoitti synergiaa hoitoresistentissä MRSA-infektiossa, sekä karbapeneemin ja linetsolidin yhdistelmiin. Kyse on lähinnä olemassa olevan antibakteerisen käyttöaiheen laajennuksesta, ei aidosta uudelleenkäytöstä.

**Muut ennusteet:** Lavantauti, pitkäaikaiskuume (paratyfoidi) ja salmonelloosi ovat antibakteerisen käyttöaiheen luonnollisia laajennuksia, joissa näyttö koostuu in vitro -herkkyys- ja resistenssiseurantatutkimuksista. Poskiontelotulehduksessa, kroonisessa nuhakuumeessa ja etmoidaalisessa sinuiitissa suoraa imipeneemin tehoa kuvaavaa näyttöä ei ole, eikä systeeminen karbapeneemi ole tarkoituksenmukainen hoito. Poskionteloiden kasvain ja eosinofilia-myalgiasyndrooma ovat ilmeisiä ennusteartefakteja.

---

## Kliiniset tutkimukset (S. aureus -infektio)

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Vaihe 4 | Päättynyt | 50 | Fosfomysiinin ja imipeneemin teho ja turvallisuus MRSA-endokardiitin hoidossa verrattuna vankomysiiniin. Suorin imipeneemin yhdistelmäkäyttöä testaava tutkimus, mutta pieni otoskoko rajoittaa johtopäätöksiä. |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Vaihe 4 | Tuntematon | 60 | Linetsolidi yksin tai yhdessä karbapeneemin kanssa MRSA:ta vastaan hengityslaiteperäisessä keuhkokuumeessa. Karbapeneemi ei ole selvästi imipeneemi, joten sen osuus on epävarma. |

Muille ennustetuille käyttöaiheille ei ole rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö (S. aureus -infektio)

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [3901207](https://pubmed.ncbi.nlm.nih.gov/3901207/) | 1985 | RCT | Reviews of Infectious Diseases | Imipeneemi/silastatiini vs. kefotaksiimi 31 potilaalla keuhko-, pehmytkudos- ja munuaisinfektioissa. |
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Kliininen tutkimus | Antimicrob Agents Chemother | Imipeneemi-silastatiini 23 potilaalla, joilla MSSA- tai MRSA-infektio. |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | Prekliininen (eläinmalli) | J Antimicrob Chemother | Imipeneemi oli in vitro erittäin tehokas S. aureus -endokardiittikantoihin; verrattu nafsilliiniin kaniinimallissa. |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Tapausselostus/kommentaari | Antimicrob Agents Chemother | Imipeneemi/silastatiini ja fosfomysiini hoitoresistentissä MRSA-infektiossa: uudenlainen yhdistelmähoito. |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In vitro / eläinmalli | J Antimicrob Chemother | Vankomysiinin ja imipeneemin synergia 34 MRSA-isolaatilla 36:sta sekä neutropeenisessa hiirimallissa. |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Katsaus | Int J Antimicrob Agents | MRSA:n patogeneesi, hoito ja resistenssi. |
| [18649613](https://pubmed.ncbi.nlm.nih.gov/18649613/) | 2008 | Katsaus | Am Fam Physician | Diabeettisen jalan infektio. |
| [23545527](https://pubmed.ncbi.nlm.nih.gov/23545527/) | 2013 | In vitro | Antimicrob Agents Chemother | Telavansiinin yhdistelmät nafsilliinin, imipeneemin ja gentamisiinin kanssa S. aureus -kannoilla. |

Muista ennusteista huomionarvoista: lavantaudin osalta [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) (Cureus, 2025) tarkastelee karbapeneemeja viimeisenä hoitovaihtoehtona MDR/XDR-lavantaudissa, mutta kyse ei ole kontrolloidusta tutkimuksesta.

---

## Suomen markkinatiedot

| Lupanumero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004808 | Recarbrio | – | Gram-negatiiviset bakteeri-infektiot (myyntilupa peruutettu) |

---

## Turvallisuushuomioita

**Tietograafin mukaiset vasta-aiheet** (tietograafin lääke–tauti-yhteydet, ei valmisteyhteenvedon teksti): epilepsia, munuaissairaus, virtsanjohtimen märkäpesäke, Clostridium difficile -paksusuolitulehdus ja vastasyntyneen nekrotisoiva enterokoliitti.

**Lääkkeiden yhteisvaikutukset:** Yhteensä 15 yhteisvaikutusta.
- **Merkittävät (Major):** bupropioni, ioheksoli, iopamidoli.
- **Kohtalaiset (Moderate):** varfariini, dikumaroli, teofylliini ja muut ksantiinit (aminofylliini, dyfylliini, oksitrifylliini), siklosporiini, etinyyliestradioli, mykofenolihappo, pemetreksedi, lindaani, polyetyleeniglykoli (elektrolyyttien kanssa).

Muuta turvallisuustietoa ei ole saatavilla; lisätiedot on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**; S. aureus -infektion osalta tutkimuskysymys jatkoselvitykseen.

**Perustelut:**
- Korkeimmin pisteytetyille ennusteille (diffuusi skleroderma, poskionteloiden kasvain, eosinofilia-myalgiasyndrooma) ei ole tutkimus- tai mekanistista näyttöä, ja ne vaikuttavat mallin artefakteilta. Lavantauti-, salmonelloosi- ja sinuiittiennusteet perustuvat epäsuoraan herkkyysnäyttöön ja ovat antibakteerisen käyttöaiheen laajennuksia. S. aureus -infektiolla on ainoana kohtalaista (L3) näyttöä: kaksi pientä vaiheen 4 tutkimusta ja yhdistelmähoitoja koskevaa tutkimusta, mutta MRSA:n luontainen resistenssi ja karbapeneemien käytön rajoittamistarve heikentävät asetelmaa.

**Jatkotoimiin tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (kriittinen puute, estää turvallisuusseulonnan jatkamisen)
- Yksityiskohtaiset vaikutusmekanismitiedot (MOA)
- Suuremmat kontrolloidut tutkimukset imipeneemi–fosfomysiini-yhdistelmästä MRSA-infektioissa, huomioiden karbapeneemien käytön hallinta
- Suomen myyntiluvan tilanteen selvittäminen, sillä ainoa lupa on peruutettu
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

