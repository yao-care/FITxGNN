---
layout: default
title: Epinephrine
parent: Vahva näyttö (L1-L2)
nav_order: 149
evidence_level: L1
indication_count: 4
---

# Epinephrine
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **4** kpl
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

# Epinefriini: Anafilaksiasta obstruktiiviseen keuhkosairauteen

## Yhden lauseen yhteenveto

Epinefriini (adrenaliini) on klassinen hätähoitolääke anafilaksialle, sydänpysähdykselle ja akuutille bronkospasmi/astmalle. TxGNN-malli ennustaa, että se voisi olla tehokas myös **obstruktiiviselle keuhkosairaudelle**, mikä on tukena jo **50 kliinisen tutkimuksen** ja **20 julkaisun** avulla — joista useissa testataan suoraan inhaloitavaa tai sumutettavaa epinefriiniä astmassa ja bronkiolitissa. Kuitenkin epinefriinillä ei ole tällä hetkellä **myyntilupaa Suomessa**, ja TFDA/Fimean pakkausselosteista puuttuva kriittinen tieto (Blocking-severity-luokan tietovaje) tarkoittaa, että kandidaatti ei voi vielä siirtyä muodolliseen (S1) turvallisuusseulontaan.

---

## Pika-yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Ei tiedossa Suomen sääntelytiedoissa (0 myyntilupaa, ei markkinoilla); epinefriinin vakiintuneet käyttöaiheet ovat anafilaksia, sydänpysähdys ja akuutti bronkospasmi/astma |
| Ennustettu uusi käyttöaihe | Obstruktiivinen keuhkosairaus |
| TxGNN-ennusteen pistemäärä | 99,71% |
| Näyttöaste | L1 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Myyntilupien lukumäärä | 0 |
| Suositeltu päätös | Jatka varautumistein (edellyttäen turvallisuustietovajeen ratkaisemista) |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtaiset vaikutusmekanismin tiedot eivät ole tällä hetkellä saatavilla DrugBankista tämän kandidaatin osalta (merkitty tietovajeeksi **DG002**, High severity). Hyvin vakiintuneen farmakologian perusteella epinefriini on kuitenkin **epäselektiivinen α/β-adrenerginen reseptoriagonisti**. Sen β2-reseptorin aktiviteetin kautta keuhkojen sileät lihakset rentoutuvat (bronkodilataatio), kun taas α1-reseptorin aktiviteetti vähentää ilmateiden limakalvon suonten tulehdusoireyhtymää ja turvotusta — molemmat toiminnot vastustavat suoraan obstruktiivisen keuhkosairauden määrittelemää ilmavirtauksen rajoittumista.

Kriittisesti, tämä ei ole puhtaasti teoreettinen ekstrapolaatio: epinefriinillä on jo dokumentoitu historia käytöstä akuutissa bronkospasmi ja astmassa. Historiallinen ilman reseptiä saatava inhalaattori Primatene Mist, sen tutkimusvaiheen HFA-uudelleenmuotoilu (E004), ja sumutettava "raseeminen epinefriini"/adrenaliini ovat kaikki epinefriinipohjaisia tuotteita, joita on tutkittu suoraan astmassa ja vauvojen bronkiolitissa — molemmat obstruktiivisen keuhkosairauden tunnustetut alatyypit. Tämä näkyy alla olevassa näyttötodistuksessa, jossa useat tutkimukset testasivat epinefriinin muotoiluja rinnakkain albuterolille, hypertoniselle suolaliuokselle ja plaseebolle juuri tässä sairauden tilassa.

Koska farmakologinen mekanismi on hyvin karakterisoitu ja "uusi" käyttöaihe merkittävästi limittää epinefriinin olemassa olevan off-label/historian hengitystieindikaation kanssa, tämä kandidaatti saavuttaa suhteellisen kypsän päätösvaiheen (S3) L1-näyttöasteella huolimatta siitä, että lääkkeellä ei ole tällä hetkellä Suomen indikaatiotietuetta.

---

## Kliiniset tutkimustodisteet

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset löydökset |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Vaihe 3 | Valmis | 373 | 12 viikon pituinen epinefriinin HFA-inhalatsio-aerosolipumpun MDI:n teho/turvallisuus vs. plaseeboa-HFA ja markkinoilla olevaa Primatene® Mist (CFC-epinefriininhalaaja) nuorissa/aikuisissa astmaatikoissa. |
| [NCT01300325](https://clinicaltrials.gov/study/NCT01300325) | Vaihe 4 | Valmis | 136 | Sumutettava 3 % hypertonisuolaliuos vs. normaali suolaliuos, molemmat epinefriinin kanssa, RSV-positiivisissa sairaalahoitoon otettuissa vauvoissa bronkiolitissa. |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Vaihe 2/3 | Lopetettu | 195 | Sumutettavan adrenaliinin + suullisen betametasonin yhdistelmä testattiin vaihtoehtona sairaalahoitoon joutumisen vähenemiseksi akuutin bronkioliitin yhteydessä lasten päivystyksessä. |
| [NCT05363670](https://clinicaltrials.gov/study/NCT05363670) | Vaihe 2 | Valmis | 18 | Ristiinvaihto-turvallisuus/teho-tutkimus sisäänhengitettävästä epinefriinistä (ARS-1) vs. albuterol neulattomana reittinä vaikealaatuisen astman oireen hoitamiselle. |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Vaihe 4 | Valmis | 28 | Ristiinvaihto-PK-vertailu sisäänhengitettävästä Primatene Mist (epinefriini) vs. IM-epinefriini-injektio vs. sisäänhengitettävä ProAir (albuterol) terveissä aikuisissa. |
| [NCT03614273](https://clinicaltrials.gov/study/NCT03614273) | EI | Valmis | 60 | Satunnaistettu tutkimus, jossa verrataan sumutettavaa 3 % hypertonista suolaliuosta vs. sumutettavaa adrenaliinia bronkiolitissa, myös vastetta alkuperäisiin ei-vastaajaiin. |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Vaihe 2 | Valmis | 24 | Deuteriumilla merkityn epinefriinin HFA-MDI (E004)-inhalatsio-aerosoliin PK-tutkimus, joka erottelee eksogeenisen ja endogeenisen epinefriinin. |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | EI | Tuntematon | 600 | Satunnaistettu tutkimus, jossa verrataan epinefriiniä ja albuterolia, kahta yleisimmin käytettävää bronkodilataattoria bronkiolitissa. |
| [NCT01737892](https://clinicaltrials.gov/study/NCT01737892) | Vaihe 1/2 | Lopetettu | 21 | Epinefriinin HFA-MDI (E004) seurantatutkimus deuteriumilla merkityllä epinefriinillä terveissä vapaaehtoisissa. |
| [NCT01216553](https://clinicaltrials.gov/study/NCT01216553) | Vaihe 4 | Tuntematon | 135 | Kotioksigeeni-hoito vs. standardisumutushoito (0,1% epinefriini + bromheksiin tai hypertonisuolaliuos) poliklinikalla hoidetuissa vauvoissa bronkiolitissa. |

---

## Kirjallisuusviitteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane-katsaus | The Cochrane Database of Systematic Reviews | "Epinefriini bronkiolitissa" — systematiinen katsaus bronkodilataattoreiden käytöstä; tehokkuus epävarma huolimatta yleisestä käytöstä. |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane-katsaus | The Cochrane Database of Systematic Reviews | Aikaisempi Cochrane-katsauksen versio; bronkodilataattorit osoittavat vaatimattomia lyhyen aikavälin hyötyjä lievässä-keskivaikeassa bronkiolitissa. |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Katsaus | Expert Review of Respiratory Medicine | Tarkastelee raseemisen epinefriinin, kortikosteroidien, hypertonisen suolaliuoksen ja korkeavirtausoksiterapian roolia lasten bronkioliitin hoidossa. |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Kohortti | Scandinavian Journal of Clinical and Laboratory Investigation | Kohonnut plasman noradrenalin kroonisen obstruktiivisen keuhkosairauden potilaissa, korrelaation verinen hemodynamiikka ja verikaasupoimintahäiriöt. |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Katsaus | BMJ Clinical Evidence | Yleiskatsaus bronkioliitin epidemiologiaan ja hoitoon eniten leikkaavaksi vauvojen alemman hengitysteiden infektio. |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Katsaus | BMJ Clinical Evidence | Aiempi versio samasta bronkioliitin kliinisen näytön katsauksesta. |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Luokittelua odottaa | Clinical Pharmacology and Therapeutics | "Terbutaliiinin ja epinefriinin bronkodilataattori-vaikutukset obstruktiivisessa keuhkosairaudessa" — suora historiallinen vertailu epinefriinin bronkodilataattori-vaikutuksesta. |
| [4551435](https://pubmed.ncbi.nlm.nih.gov/4551435/) | 1972 | Luokittelua odottaa | Annals of Allergy | "Sumutettavat bronkodilataattorit obstruktiivisessa keuhkosairaudessa II" — varhainen arviointi sumutettavasta bronkodilataattori-terapeuttisesta sisällöstä myös epinefriini. |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Katsaus | Journal of Allergy and Clinical Immunology | Katsaus lapsuuden astman patofysiologiaan, joissa astma karakterisoidaan obstruktiiviseksi ilmateiden sairaudeksi. |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | Muu | The Medical Letter on Drugs and Therapeutics | Primatene Mist (epinefriinin halaaja) ilman reseptiä saatavaksi palautumisen kattavuus astman oireista helpotukseen. |

---

## Suomen markkinatiedot

Epinefriinillä ei ole tällä hetkellä myyntilupaa Suomessa (0 myyntilupaa; markkinatilanne: Ei markkinoilla / Not Marketed). Tuotteen nimeä, annosmuotoa tai hyväksyttyä käyttöaihetta ei ole saatavilla sääntelytiedoista tälle kandidaatille.

---

## Turvallisuusnäkökohdat

Strukturoitua turvallisuusdata (avainosaat, vasta-aiheet tai lääke-lääke-vuorovaikutukset) ei ole tällä hetkellä saatavilla tälle kandidaatille — DDI-kysely palautti `not_found` nolla vuorovaikutuksia tiedoissa. Katso pakkausselosteesta turvallisuustiedot.

**Huomautus turvallisuustiedon tilasta:** Tämä on merkitty näyttötodistuksessa **Blocking**-severity-luokan vajeeksi (DG001) — TFDA/Fimean pakkausselosteista puuttuva varoitus ja vasta-aiheet tarkoittavat, että tämä kandidaatti **ei voi vielä siirtyä S1 turvallisuuden alkuarvioinnin vaiheeseen**, riippumatta siitä kuinka vahva ennustetun käyttöaiheen teho/mekanistinen näyttö on. Korjaaminen edellyttää virallisen pakkausselosteen PDF-dokumentin lataamista ja jäsennystä asiaankuuluvasta sääntelylähteestä.

---

## Muut TxGNN-ennustetut käyttöaiheet (ei priorisoitu)

Näyttötodistus arvioi kolme lisäkandidaattikäyttöaihetta epinefriinille, joista mitään ei suositella edistettäväksi tällä hetkellä:

| Sijoitus | Käyttöaihe | Pistemäärä | Näyttöaste | Suositus | Huomautus |
|------|-----------|-------|----------------|-----------------|------|
| 2 | Ruoan aiheuttama rasituksesta johtuva anafilaksia (FDEIA) | 99,57% | L3 | Jatka varautumistein | Vahva mekanistinen perustelu (epinefriini on standardi anafilaksian pelastushoito), mutta ei kliinisiä tutkimuksia — 20 katsaus/tapaus-tason julkaisua vain; edustaa indikaatio-etiketin laajennusta pikemmin kuin uutta farmakologiaa. |
| 3 | Rienhoffin oireyhtymä | 99,57% | L5 | **Pidä taukoa** | Ei kliinisiä tutkimuksia, ei kirjallisuutta, ei mekanistista yhteyttä adrenergisen farmakologian kanssa (harvinainen LTBP3-liittyvä sidekudoksen häiriö). Todennäköisesti mallin kohina/väärä positiivinen harva sairauden koulutusdata — ei mielekkää signaalia. |
| 4 | Hengitysteiden väärämuodostuma | 99,56% | L4 | **Pidä taukoa** | Haetut todisteet ovat epäsuhteisia sairauden etiketin kanssa — tutkimukset ja kirjallisuus liittyvät toiminnallisiin hengitystiehätätilanteisiin (sydänpysähdyksen elvytys, kruupi/yläilmatie-obstruksio) pikemmin kuin rakenteelliseen ilmateiden väärämuodostumaan. Vaatii sairauden-etiketin selkeytystä ennen jatkokehitystä. |

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varautumistein (ehdollinen turvallisuustiedon perusteella)**

**Perustelut:**
Korkeimmalle sijoittunut ennuste — epinefriini obstruktiiviselle keuhkosairaudelle — on tuettu L1-näyttöasteella, joka sisältää valmistuneen vaihe 3:n satunnaistetun tutkimuksen (NCT01357642, N=373) ja merkittävän, epinefriini-spesifisen näyttörekisterin, joka kattaa sekä astman että bronkioliitin. Tämä on pikemmin tietojen perustuva vahvistus epinefriinin olemassa olevasta historian hengitystieindikaatiosta kuin uutuusennuste. Kuitenkin kandidaatti ei voi siirtyä alkuperäisen turvallisuusseulonnan jälkeen ennen kuin Blocking-severity-luokan pakkausselosteen tietovaje (DG001) ratkaistu, ja Suomen markkinatilanne (ei markkinoilla, 0 myyntilupaa) silti vaatii määriteltyä sääntelypolkua.

**Edetäkseen seuraavat ovat vaadittavat:**
- TFDA/Fimean pakkausseloste (varoitukset ja vasta-aiheet) — Blocking-vahe (DG001), vaaditaan ennen S1-turvallisuuden arviointia
- Vahvistettu DrugBank vaikutusmekanismi-tietue — Korkea-prioriteettinen vaje (DG002), tukeakseen mekanistisen linkin analyysia
- Määritelty Suomen sääntelyllinen/rekistöinti-polku, koska lääke on tällä hetkellä ei markkinoilla nolla myyntiluvalla
- Valmiiksi toteutettu lääke-lääke-vuorovaikutus (DDI) kysely, koska nykyinen kysely palautti nolla tuloksia
- Reitti-yhteensopivuuden vahvistus (saatavilla vs. vaadittu hallintoreitti), tällä hetkellä merkitty "odottaa" näyttötodistuksessa
- Sairauden-etiketin vahvistus "hengitysteiden väärämuodostumalle" (sijoitus 4), jossa haetut näyttötodisteet eivät vastaa ilmoitettua käyttöaihetta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

