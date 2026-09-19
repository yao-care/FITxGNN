---
layout: default
title: Pegaspargase
parent: Vahva näyttö (L1-L2)
nav_order: 287
evidence_level: L2
indication_count: 10
---

# Pegaspargase
{: .fs-9 }

Näytön taso: **L2** | Ennustetut käyttöaiheet: **10** kpl
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

# Pegaspargase: Akuutista lymfoblastisesta leukemiasta Hodgkinin lymfoomaan (Ekstranodaalinen NK/T-solu lymfooma)

## Yhden lauseen yhteenveto

> Pegaspargase (PEGylöity L-asparaginaasi) on vakiintunut kemoterapiakomponentti akuutissa lymfoblastisessa leukemiassa (ALL)/lymfoblastisessa lymfoomassa, jossa se kuluttaa serumin asparaginiinitasoa valinnollisesti tappakseen asparaginaasisyntaasi-puutteellisia pahanlaatuisia lymfoblasteja.
> Tämä todistepaketti sisältää **10 TxGNN-luokiteltua kandidaattisairastumusosoitusta**; kahdesta viiden parhaan joukossa (prekursorin lymfoblastinen lymfooma/leukemia ja "akuutti lymfoblastinen leukemia") ovat yksinkertaisesti lääkkeen **olemassa olevat, jo hyväksytyt käyttöindikaatiot** kuin uus hypoteesi.
> Uskottavin todella **uuden käytön** signaali tässä paketissa on sijoitukseltaan #8 ja merkitty **"Hodgkinin lymfoomaksi,"** mutta lähes kaikki sen tukevat tutkimukset ja kirjallisuus tutkivat itse asiassa **Ekstranodaalista NK/T-solu lymfoomaa (ENKTL)** — erillinen, aggressiivinen non-Hodgkin alaryhmä, jossa asparaginaasipohjaisia skeemoja (SMILE, P-GEMOX, GELOX, DDGP) käytetään jo käytännön toteutuksessa, tukena **18 kliinisen tutkimuksen** ja **20 julkaisun**.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Akuutti lymfoblastinen leukemia (ALL) / Lymfoblastinen lymfooma *(päätellään kliinisen tutkimuksen kontekstista ja uudelleenkäytön perustelusta — `original_indications` kenttä oli tyhjä todistepakettissa)* |
| Ennustettu uusi indikaatio | Hodgkinin lymfooma (merkintä) — tukevia todisteita vastaa pääasiassa **Ekstranodaalinen NK/T-solu lymfooma (ENKTL)** |
| TxGNN ennustamispistemäärä | 99.71% (sijoitus 3726 mallin tuloksesta) |
| Todistustaso | L2 |
| Suomen markkinatila | Ei markkinoitu |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Tutkimuskysymys |

**Huomio tästä todistupaketista:** Tämä on monisairastumuskohtainen kandidaattipaketti (`candidate_id: TW-DB00059-multi`), joka sisältää 10 luokiteltua TxGNN ennustetta. Alla oleva taulukko tiivistää ne kaikki, jotta lukija ymmärtää koko salkun ennen syvää analyysiä pääkandidaatista.

### Kaikkien TxGNN-Ennustettujen Sairastumusten Salkku Tässä Paketissa

| Sijoitus | Sairauden merkintä | Pistemäärä | Todistustaso | Suositus | Huomio |
|------|---------------|-------|-----------------|-----------------|------|
| 1 | Prekursorin lymfoblastinen lymfooma/leukemia | 99.96% | L1 | Jatka varauksilla | **Ei uusi indikaatio** — tämä on lääkkeen ydinperustakausi |
| 2 | Pregerminalisen keskuksen CLL/SLL | 99.95% | L5 | Pidä odottamassa | Ei tutkimuksia/kirjallisuutta; mekanistisesti heikko (kypsät, hitaasti leviävät B-solut) |
| 3 | CLL/SLL (IGHV-mutattu alaryhmä) | 99.95% | L5 | Pidä odottamassa | Sama kuin edellä |
| 4 | Folliculaarinen lymfooma | 99.90% | L5 | Pidä odottamassa | Ei todisteita; indolenttigerminaalikeskus-lymfooma, heikko perusteltu |
| 5 | Akuutti lymfoblastinen leukemia | 99.89% | L1 | Jatka varauksilla | **Ei uusi indikaatio** — sijoituksen 1 kaksikappale |
| 6 | Metyylkobalamiiini puute (cblE) | 99.74% | L5 | Pidä odottamassa | Biologisesti epätodennäköinen (B12/MTRR metabolinen vika) — todennäköisesti graafisen melun kohinaa; suosita poissulkemista |
| 7 | Lymfoidinen neoplasma | 99.71% | L2 | Tutkimuskysymys | Liian laaja merkintä; todisteet päällekkäin merkittävästi olemassa olevien ALL-tutkimusten kanssa |
| **8** | **Hodgkinin lymfooma** | **99.71%** | **L2** | **Tutkimuskysymys** | **Analysoidaan pääkandidaattina alla — todistusperusta on pääosin ENKTL, ei klassinen Hodgkinin lymfooma** |
| 9 | CLL/SLL | 99.68% | L5 | Pidä odottamassa | Ei todisteita |
| 10 | Räjähdysvaiheen CML, BCR-ABL1+ | 99.61% | L3 | Tutkimuskysymys | Uskottava vain jos lymfoidinen räjähdyskriisi; heikko todistus (2 tutkimusta, 1 tapausselostus) |

---

## Miksi tämä ennuste on järkevä?

Pegaspargase on PEGylöity *E. coli* -peräisen L-asparaginaasi muoto. Pahanlaatuiset lymfoblastit ALL:ssa/lymfoblastisessa lymfoomassa usein puuttuvat asparaginaasisyntaasista (ASNS) ja riippuvat ulkoisesta serumin asparaginasta proteiinisynteesin ylläpitämiseen. Pegaspargase kuluttaa plasma-asparaginiiä, selvästi nälkiintyttäen nämä pahanlaatuiset solut samalla kun säästävät useimmat normaali kudokset — mekanismi, joka on eksplisiittisesti vahvistettu todistepaketin omassa perustelutekstissä, vaikka lääke-tason `original_moa` kenttä itsessään on merkitty tiedon puutteeksi (DG002).

Sijoitukset 1 ja 5 tässä paketissa ("prekursorin lymfoblastinen lymfooma/leukemia" ja "akuutti lymfoblastinen leukemia") ovat **eivät uusia hypoteeseja** — ne ovat yksinkertaisesti lääkkeen jo vakiintunutta indikaatiota, jota mallin tulee re-pinnaalla hyvin suurella luottamuksella. Tämä on hyödyllinen mallikalibration signaali (se vahvistaa, että TxGNN oikein tunnistaa pegaspargasen todellisen farmakologian) mutta sillä ei ole uudelleenkäytön arvoa.

Eniten toimintakuntoinen **todella uusi** signaali on sijoitus 8. TxGNN:n sairauden ontologia merkitsee sen "Hodgkinin lymfoomaksi," mutta oleellisesti kaikki liittyvät tutkimukset ja artikkelit (SMILE, P-GEMOX, GELOX, DDGP skeemoja) kuvaavat **Ekstranodaalista NK/T-solu lymfoomaa (ENKTL)** — kypsän NK/T-solun neoplasma, joka, kuten ALL, usein osoittaa matalia ASNS ilmentymisen ja on asparaginiiiriippuvainen, antaen biologisesti johdonmukaisen perustelun asparaginaasipohjaisen hoidon kannalta. ENKTL on biologisesti ja kliinisesti erillään klassisesta Hodgkinin lymfoomasta, joten tämä on hyvin todennäköisesti **ontologia/merkintä kartoituksen ongelma** kuin todellinen Hodgkinin lymfooma signaali. Koska asparaginaasipohjaisia skeemoja ENKTL:lle käytetään jo laajalti Aasian ja Tyynenmeren alueella kliinisessä käytännössä (pääosin länsimaisten merkintöjen ulkopuolella), tämä edustaa uskottavaa "vanhaa lääkettä, jo käyttöön otettua uutta käyttöä" tarinaansa, joka ansaitsee muodollisen merkinnän/merkintä selvennyksen ennen lisätoimia.

---

## Kliiniset tutkimustodisteet

*(Alla esitetyt tutkimukset ovat todisteita, jotka tukevat sijoituksen 8 kandidaattia; lähes kaikki tutkivat ENKTL:ää eikä klassista Hodgkinin lymfoomaa — katso varoitus edellä.)*

| Tutkimuksen numero | Vaihe | Tila | Osallistujamäärä | Keskeisiä tuloksia |
|---------|------|------|------|---------|
| [NCT02085655](https://clinicaltrials.gov/study/NCT02085655) | Vaihe 3 | Tuntematon | 264 | Satunnaistettu PA-Gemox:in ja thalidomiidin sekä AspaMetDex-skeeman vertailu NKTCL:ssa |
| [NCT02631239](https://clinicaltrials.gov/study/NCT02631239) | Vaihe 3 | Tuntematon | 256 | Etopositiidi/deksametasoni/pegaspargase ± metotreksaatti sandwitched säteilyhoidolla vaiheen I–II ENKTL:ssa, nenätyyppi |
| [NCT02359162](https://clinicaltrials.gov/study/NCT02359162) | Vaihe 3 | Lopetettu | 50 | Satunnaistettu P-Gemox vs. EPOCH ensimmäisen linjan kemoterapiana NK/T-solulymfoomassa |
| [NCT02918747](https://clinicaltrials.gov/study/NCT02918747) | Vaihe 2 | Tuntematon | 100 | Satunnaistettu P-Gemoxd + säteily vs. P-CHOP + säteily varhaisvaiheen ENKTL:ssa |
| [NCT02533323](https://clinicaltrials.gov/study/NCT02533323) | Vaihe 2 | Lopetettu | 50 | Pegaspargase-Gemox (P-Gemox) ensimmäisen linjan hoitona uudisksi diagnosoidussa nenätyyppi ENKTL:ssa |
| [NCT06583083](https://clinicaltrials.gov/study/NCT06583083) | Vaihe 2 | Rekrytoi | 84 | Sintilimab (PD-1 vasta-aine) + P-GEMOX vs. P-GEMOX yksin edistynyt-vaiheen ENKTL:ssa |
| [NCT02080234](https://clinicaltrials.gov/study/NCT02080234) | Vaihe 2 | Tuntematon | 40 | GELOX (gemcitabiini/oksaliplatini/asparaginaasi) samanaikaisella säteilyhoidolla vaiheen IE/IIE ENKTL:ssa |
| [NCT02705508](https://clinicaltrials.gov/study/NCT02705508) | Vaihe 2 | Tuntematon | 35 | PEG-ASP + etopositiidi + gemcitabiini (PEG skeema) ensimmäisen linjan hoitona NK/T-solulymfoomalle |
| [NCT07457177](https://clinicaltrials.gov/study/NCT07457177) | Vaihe 2 | Ei vielä rekrytoimassa | 40 | Golidocitinibi + pegaspargase + anti-PD-1 vasta-aine ensimmäisen linjan hoitona edistynyt ENKTL:ssa |
| [NCT06953739](https://clinicaltrials.gov/study/NCT06953739) | Vaihe 3 | Ei vielä rekrytoimassa | 60 | Pegaspargase + P-GEMD vs. P-Gemox kohdeltamattomassa varhaisvaiheen (ei ylempi-ilmaekeiskunetään) tai edistynyt ENKTL:ssa |

---

## Kirjallisuustodisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeisiä tuloksia |
|------|-----|------|------|---------|
| [27723108](https://pubmed.ncbi.nlm.nih.gov/27723108/) | 2017 | RCT | Hematological Oncology | Vaihe 2 monikeeskisen MESA:n (metotreksaatti/etopositiidi/deksametasoni/pegaspargase) tutkimus uudisksy diagnosoidussa, uusiutuneessa tai vastustuksessa olevassa nenätyyppi ENKTL:ssa; CR 43.5%, ORR 87% |
| [34449095](https://pubmed.ncbi.nlm.nih.gov/34449095/) | 2021 | Kohortti | American Journal of Hematology | Monikeeskinen peräkkäisen P-GEMOX + säteilyn tutkimus varhaisvaiheen ENKTL:ssa |
| [29194798](https://pubmed.ncbi.nlm.nih.gov/29194798/) | 2018 | Kohortti | European Journal of Haematology | Monikeeskinen retrospektiivinen GELOXD/P-GEMOXD tehokkuuden ja siedettävyyden tutkimus uudisksy diagnosoidussa nenätyyppi ENKTL:ssa |
| [2345067](https://pubmed.ncbi.nlm.nih.gov/2345067/) | 1990 | Katsaus/Vaihe 2 | Investigational New Drugs | Vaihe 2 PEG-L-asparaginaasi tutkimus vastustuksessa olevassa non-Hodgkin lymfoomassa (21 potilasta) |
| [30241515](https://pubmed.ncbi.nlm.nih.gov/30241515/) | 2018 | Kohortti | BMC Cancer | PEG-L-CHOP skeema osoitettiin turvalliseksi ja tehokkaaksi aikuisen ENKTL:ssa alhaisen yliherkkyyden kanssa |
| [24299319](https://pubmed.ncbi.nlm.nih.gov/24299319/) | 2014 | Tapaussarja | Neoplasma | DDGP skeema (pegaspargase/deksametasoni/sisplaatini/gemcitabiini) uudisksy diagnosoidussa ENKTL:ssa |
| [37486391](https://pubmed.ncbi.nlm.nih.gov/37486391/) | 2023 | Kohortti | Annals of Hematology | "Sandwich" modifioitu SMILE skeema (sisältäen pegaspargasen) pediatrisessa uudisksy diagnosoidussa ENKTL:ssa |
| [29764116](https://pubmed.ncbi.nlm.nih.gov/29764116/) | 2019 | Kohortti | Cancer Research and Treatment | Matala kiertävä CD4+ T-solun lukumäärä ennustaa huonoa ennustetta ENKTL:ssä, jota käsitellään pegaspargase-pohjaisella kemoterapialla |
| [19786301](https://pubmed.ncbi.nlm.nih.gov/19786301/) | 2010 | Tapausselostus | Leukemia Research | Kaksi CHOP-vastustuksessa olevaa ENKTL potilasta vastasivat yksittäiseen pegaspargaasiin |
| [8481665](https://pubmed.ncbi.nlm.nih.gov/8481665/) | 1993 | Katsaus | Leukemia & Lymphoma | Historiallinen L-asparaginaasi/PEG-asparaginaasi kehityksen ja lymfoidisen-malignanssin sovellusten katsaus |

---

## Suomen markkinatiedot

Pegaspargase:lla ei ole tällä hetkellä **myyntilupaa Suomessa** (`market_status: Not Marketed`, `total_licenses: 0`). Mitään tuotetietoja, annosmuotoja tai hyväksyttyjä merkintötekstejä ei ollut saatavilla tässä todistepakettissa Suomen markkinoille.

---

## Sytotoksisuus

Pegaspargase on antineoplastinen lääke, jota käytetään yksinomaan monilääkkeisen kemoterapian yhteydessä hemaattisissa malignansseissa, joten tämä osio koskee.

| Kohta | Sisältö |
|------|------|
| Sytotoksisuuden luokitus | Perinteinen sytotoksinen — entsyymin pohjainen, asparaginiiniekuluttava aine (ei DNA-vaurioittava sytotoksinen; mekanismi on metabolinen/proteiinisynteesin estäminen) |
| Luuytimen tukahduttamisen riski | Alhainen - kohtalainen yksinään käytettäessä — asparaginaasi itsessään ei ole vahvasti luuytimen tukahduttava, mutta se yhdistetään väistämättä luuytimen tukahduttaviin aineisiin (vinkristiini, antrasykliinit, sytarbiini, jne.) ALL/ENKTL skeemoissa, ja yhdistelmäskeeman luuytimen tukahduttaminen on hyvin dokumentoitu yllä olevassa kirjallisuustodisteissa |
| Pahoinvoinnin aiheuttamiskyky | Matala (asparaginaasi-luokan lääkkeet on yleensä luokiteltu matalaksi pahoinvoinnin aiheuttamisrisikiksi) |
| Monitoroinnin kohteita | Maksan toiminnon testit (maksatoksisuus), rasva-arvojen mittaus/triglyseeridit (hypertriglyseridemia), hyytymisparametrit — fibrinogeeni, antitrombiini (tromboosin/verenvuodon riski), amylaasi/lipaasin (pankreatiitti), verensokeri (hyperglykemia) ja yliherkkyys seuranta; verensolujen laskenta (CBC) erotusvärityksellä tavallisen yhdistelmäskeeman käytännön mukaan |
| Käsittelysuojaus | Kyllä — täytyy käsitellä vakio-sytotoksisen/vaarallisen lääkkeen käsittelystandardien mukaisesti (suljettu järjestelmän siirto, henkilösuojaimet) |

*(Yllä olevat myrkyllisyyden kohdat ovat johdettu tämän paketin kirjallisuustodisteista — esim. pankreatiitti, hypertriglyseridemia ja pegaspargasen hepatotoksisuus tapaussarjat/kohorteista — koska DrugBank-tason toksisuus/varoitustiedot eivät olleet suoraan saatavilla tässä todistepakettissa.)*

---

## Turvallisuushuomiot

Viitatkaa pakkausselosteeseen turvallisuustiedoista.

*(Sekä `key_warnings` että `contraindications` merkittiin tiedon puutteeksi, ja lääkkeiden väliset vuorovaikutuskyselyt eivät tuottaneet tuloksia tässä todistepakettissa. Huomaa erikseen: Tiedon puute DG001 ilmoittaa, että TFDA/Fimea pakkausselosteen varoitukset ja vasta-aiheet ovat **Estävän**-vakavuusaste puute — tämä täytyy ratkaista ennen kuin mitään S1 turvallisuuden esitutkimusta voidaan jatkaa, riippumatta yllä käsitellystä tehokkuuden todistustasosta.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Tutkimuskysymys**

**Perustelut:**
- Kaksi tämän paketin huipuista ennustetta (sijoitukset 1 ja 5) toistavat yksinkertaisesti pegaspargasen olemassa olevaa hyväksyttyä käyttöä ja ne eivät ole uudelleenkäytön arvoa; useat muut (sijoitukset 2, 3, 4, 6, 9) eivät ole tutkimus- tai kirjallisuustodisteita ja ovat todennäköisesti mallin kohinaa, mukaan lukien yksi (cblE, sijoitus 6), joka on biologisesti epätodennäköinen.
- Ainoa uskottava uuden käytön signaali (sijoitus 8) on sekoitettu sairauden merkinnän ristiriidasta — todellisen maailman todisteet tukevat **Ekstranodaalista NK/T-solu lymfoomaa**, ei klassista Hodgkinin lymfoomaa — ja vaikka ENKTL todistusperusta on todella merkittävä (L2, 18 tutkimusta, 20 julkaisua, mukaan lukien Vaihe 3 RCT:t), sitä ei voida arvioida tai toimia oikein, kunnes sairauden merkinnän kartoitus on varmennettu.
- Erikseen, tämä kandidaatti on tällä hetkellä estetty **Estävän**-vakavuusaste tiedon puutteella (DG001: puuttuva TFDA/Fimea pakkausseloste varoitukset/vasta-aiheet), mikä estää minkä tahansa turvallisuus esitutkimusta riippumatta tehokkuuden todistusten laadusta.

**Jatkamiseksi tarvitaan seuraavaa:**
- Varmentaa ja korjata sijoituksen 8 ennusteen sairauden ontologian kartoitus (vahvistaa ENKTL vs. klassinen Hodgkinin lymfooma ennen mitään lisäarvioita)
- Hankkia TFDA/Fimea pakkausseloste (varoitukset, vasta-aiheet) tiedon puutteen (DG001) ratkaisemiseksi
- Hankkia muodollinen DrugBank/MOA dokumentaatio tiedon puutteen (DG002) ratkaisemiseksi
- Jos ENKTL vahvistetaan aiotuksi kohde-indikaatioksi, pyydä päivitettyä todisteiden hakua käyttäen "ekstranodaalinen NK/T-solulymfooma" sairauden kyselytermina "Hodgkinin lymfooma" sijasta
- Koska markkinointi on nolla Suomessa tällä hetkellä, arvioi toteutettavuus/sääntelyn polku ennen uudelleenkäyttöohjelman aloittamista

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

