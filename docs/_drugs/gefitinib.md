---
layout: default
title: Gefitinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinibi: keuhkoputken ei-pienisoluisesta syövästä gingivaalisen fibromatoosiin (ennustettu)

## Yhden lauseen yhteenveto

Gefitinibi (Iressa) on maailmanlaajuisesti tunnettu ensimmäisen sukupolven EGFR-tyrosiinikinaasin estäjä, jota käytetään keuhkoputken ei-pienisoluisen syövän (NSCLC) hoitoon, mutta tämä näyttöpaketti ei itsessään dokumentoi tuota alkuperäistä indikaatiota – sisäisesti merkitty tietovajeeksi, joka on epäjohdonmukainen tosimaailman hyväksynnän kanssa. TxGNN-mallin parhaiten sijoittunut ennuste on **Gingivaalinen fibromatoosi**, mutta tätä ehdokasta tukee **0 kliinistä tutkimusta** ja **0 julkaisua**, ja paketin oman mekanistisen arvioinnin mukaan EGFR-signaloinnin ja gingivaalisen fibromatoosin patogeneesiyksen välillä ei ole uskottavaa biologista yhteyttä.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei dokumentoitu tässä näyttöpaketissa (tosimaailma: NSCLC – merkitty sisäisesti tietovajeksi, katso DG002) |
| Ennustettu uusi indikaatio | Gingivaalinen fibromatoosi |
| TxGNN-ennustepisteet | 99.89% |
| Näytön taso | L5 |
| Suomen markkinoiden asema | ✗ Ei markkinoilla (Ei markkinoilla) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidä varauksessa |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtainen gefitinibin vaikutusmekanismin tieto ei ole saatavilla tässä näyttöpaketissa (tietovahe DG002). Yleisen farmakologisen tiedon perusteella – ja tämän paketin muualla haetulla kirjallisuudella vahvistettu (esim. PMID 24794908, PMID 12841190) – gefitinibi on palautuva pienimolekyylinen epidermaalisen kasvutekijän reseptorin (EGFR) tyrosiinikinaasin estäjä, joka on maailmanlaajuisesti vakiintunut EGFR-mutaatiota kantavien keuhkoputken ei-pienisoluisen syövän potilaitten hoitovalmiste. Tämä alkuperäinen indikaatio ei kuitenkaan ole kirjattu tämän paketin strukturoituun `original_indications`-kenttään, eroa, jota paketin omassa rank-5-perustelussa nimenomaisesti merkitään manuaalisen vahvistamisen tarpeeksi.

Korkeimman sijoituksen ennustettu indikaatio, gingivaalinen fibromatoosi, on hyvänlaatuinen gingivaalinen ylikasvain, joka on useimmiten yhdistetty SOS1/REST-geenimuutoksiin tai lääkkeiden – kuten siklosporiinin, fenytoiinin tai kalsiumkanavaestäjien – aiheuttamaan. Näyttöpaketin omassa mekanistisessa arvioinnissa todetaan, ettei EGFR-signaloinnin ja gingivaalisen fibromatoosin patogeneesiyksen välillä ole tunnettua yhteyttä, eikä mitään kliinisen tutkimuksen tai kirjallisuuden näyttöä (0/0) ole saatu linkin tueksi – tämä ennuste näyttää olevan mallin pisteytysartefakti eikä perusteltu hypoteesi.

Kymmenen tarkistamansa ennusteen joukossa rank #5 (keuhkon juuren syöpä) ja rank #9 (keuhkon sulkus-neoplasma) – molemmat NSCLC:n anatomisia alamuotoja – kantavat selvästi vahvemman mekanistisen perustan, koska gefitinibin EGFR-TKI-aktiivisuus on suoraan merkityksellinen NSCLC-biologialle. Näitä tulisi käsitellä uskottavimmiksi tutkimuskysymyksiksi, jotka nousevat tästä näyttöpaketista, eikä korkeimman sijoituksen mutta mekanistisesti perusteetonta gingivaalisen fibromatoosin ennusteesta.

---

## Kliinisen tutkimuksen näyttö

Parhaillaan ei ole olemassa asiaan liittyviä rekisteröityjä kliinisiä tutkimuksia

---

## Kirjallisuuden näyttö

Parhaillaan ei ole asiaan liittyviä kirjallisuuslähteitä saatavilla

---

## Suomen markkinoiden tieto

Gefitinibi ei ole parhaillaan **markkinoilla Suomessa** (markkinoiden asema: Ei markkinoilla) ja sillä on **0 rekisteröityä markkinointilupia** tässä näyttöpaketissa. Mitään lupahakemusennätyksiä ei ole saatavilla esitettäväksi.

---

## Sytotoksisuus

Gefitinibi on antineoplastinen lääkeaine (tämän paketin kirjallisuus dokumentoi suoraan sen käyttöä "kemoresistentin keuhkoputken ei-pienisoluisen syövän potilaitten hoitoon," PMID 24794908), farmakologisesti luokiteltu kohdennetuksi pienimolekyyliseksi kinaasin estäjäksi eikä perinteiseksi sytotoksiseksi kemoterapiaksi.

| Kohta | Sisältö |
|------|---------|
| Sytotoksisuuden luokittelu | Kohdennettu hoito (EGFR-tyrosiinikinaasin estäjä) |
| Luuydinsupression riski | Matala – kohdennetun EGFR-TKI-valmisteen gefitinibina ei ole suoraa luuydinelle sytostaattista vaikutusta, toisin kuin perinteisillä kemoterapialääkkeillä |
| Pahoinvointiin johtamisen luokittelu | Matala |
| Seurantakohteet | Maksatoiminto (hepatotoksisuuden riski), keuhkojen tila (interstitiaalinen keuhkosairaus – PMID 20942679, 20949670), EKG/QTc (PMID 34474028, 37258113), ihoreaktiot (akneenomainen ihottuma – PMID 18931563), lähtötaso-verenkuva |
| Käsittely ja suojaus | Suun kautta otettavan vaarallisen lääkkeen käsittelyohjeet suositellaan (vältä tabletin murskaamista, käytä suojakäsineitä), vaikka IV:n avulla annettavien sytotoksisten lääkkeiden käsittelyprotokollat eivät sovellu; vahvista virallisen pakkausselosteen kanssa kun DG001 on ratkaistu |

Huomautus: tämä taulukko on peräisin muualla tässä paketissa haetusta kirjallisuudesta, ei strukturoidusta DrugBank-sytotoksisuuskentästä. Vahvista virallisen pakkausselosteen kanssa, kun DG001 on ratkaistu.

---

## Turvallisuusnäkökohtia

Turvallisuustiedot on esitetty pakkausselosteessa.

**⚠ Huomautus:** Keskeiset varoitukset, vasta-aiheet ja lääkkeiden välisen yhteisvaikutuksen tieto on kaiken kaikkiaan kirjattu tietovajeiksi tässä paketissa. Puuttuvan TFDA/Fimea-pakkausselosteen (DG001) vakavuus on merkitty **Estäväksi** – se estää minkä tahansa S1-turvallisuuden esiarvioin ja on ratkaistava ennen jatkovaiheita.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä varauksessa**

**Perustelut:**
Korkeimman sijoituksen ennusteen (gingivaalinen fibromatoosi) takana ei ole nolla kliinisen tutkimuksen tai kirjallisuuden näyttöä eikä uskottavaa mekanistista perustelua paketin omassa arvioinnissa (näytön taso L5). Yhdessä pakkausselosteen turvallisuustietojen estävän tietovajeen kanssa (DG001) ei ole perusteita edetä tätä ehdokasta malliennusteen vaiheen ulkopuolelle.

**Jatkaakseen seuraavaa tarvitaan:**
- Fimea/TFDA:n hyväksymä pakkausseloste (ratkaisee DG001 – parhaillaan Estävä)
- Gefitinibin vahvistettu alkuperäinen indikaatio ja vaikutusmekanismin tieto (ratkaisee DG002)
- TxGNN-tuotoksen uudelleenvalidointi gefitinibin tunnettujen NSCLC-indikaatiovaatimuksien suhteen, erottaakseen varsinaisen signaalin upotuskohinasta
- Mikäli jatketaan keuhkojen syöpään liittyvien ehdokkaiden tutkimista, kohdennetut kliinisen tutkimuksen/kirjallisuushaet EGFR-mutaatiotilasta keuhkon juuren syövässä (rank #5) ja keuhkon sulkus-neoplasissa (rank #9), joissa näkyy vahvempi mekanistinen uskottavuus kuin nykyisessä korkeimman sijoituksen ennusteessa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

