---
layout: default
title: Ponatinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 303
evidence_level: L5
indication_count: 2
---

# Ponatinib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# Ponatinibi: kroonisesta myeloisesta leukemiasta gingivaalisen fibromatoosin hoitoon

## Yksisäikeinen yhteenveto

Ponatinibi on moniaineinen tyrosiinkinaasin estäjä, joka tunnetaan parhaiten kroonisen myeloisen leukemian (CML) ja Philadelphia-kromosomin positiivisen akuutin lymfoblastisen leukemian (Ph+ ALL) hoidosta. TxGNN-malli ennustaa, että se saattaa olla tehokas **gingivaalisen fibromatoosin** hoidossa, mutta tätä ennustusta tukee tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua** — se perustuu pelkästään mallin pistemäärään.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Krooninen myeloinen leukemia (CML) / Ph+ akuutti lymfoblastinen leukemia (yleinen lääketieto; ei vahvistettu paikallisen hyväksynnän perusteella) |
| Ennustettu uusi indikaatio | Gingivaalinen fibromatoosi |
| TxGNN-ennustepistemäärä | 99.04% |
| Näyttötaso | L5 |
| Markkinoinnin tila | Ei saatavilla markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia toimintamekanismia koskevia tietoja ei ole saatavilla (merkitty aineistovajiksi tässä näyttöpaketissa). Tunnettujen tietojen perusteella ponatinibi on kolmannen sukupolven moniaineinen tyrosiinkinaasin estäjä (BCR-ABL, mukaan lukien T315I-resistentti mutantti, sekä VEGFR, FGFR, PDGFR ja SRC-perheen kinaasit), ja sen tehokkuus CML/Ph+ ALL:n hoidossa on todistettu; mekanismiltaan jotkut näistä samoista kinaaseista (erityisesti PDGFR ja niihin liittyvät fibroblaastien proliferaatiota edistävät signalointireitit) osallistuvat ienien fibroblaastisen liikakasvamisen syntyyn, mikä on todennäköisesti se teoreettinen perusta, johon TxGNN:n tietoverkko perustui.

Krooninen myeloinen leukemia ja gingivaalinen fibromatoosi ovat biologisesti toisiaan liittymättömiä sairauksia — toinen on verisolujen malignanssi, jonka ajaa BCR-ABL-fuusiokinaasi, toinen on hyvänlaatuinen, usein perinnöllinen ientulehdusta aiheuttava fibroblaastien proliferatiosairaus. Mekanistinen yhteys on siis epäsuora: se riippuu ponatinibin vaiotarkoitteisesta PDGFR/kinaasireiteille kohdituvasta estämisestä, jotka edistävät sekä fibroblaastien proliferaatiota että solunulkoisen matriisin kertymistä, pikemminkin kuin siitä, että CML ja gingivaalinen fibromatoosi jakaisisivat yhteisen tautibiologian. Koska tällä ennustuksella ei ole mitään kliinisen tutkimuksen tai kirjallisuuden tukea, sitä tulisi käsitellä hypoteesina, joka on muodostunut puhtaasti mallin opittujen assosiaatioiden perusteella, eikä näyttöpohjaisen signaalin perusteella.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole kirjattuja asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuustutkimuksen näyttö

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

---

## Markkinatiedot

Ponatinibilla ei tällä hetkellä ole myyntilupaa tässä kotimaassa (tila: **Ei saatavilla markkinoilla**, 0 lupaa rekisterissä), joten hyväksyttyä indikaatiotekstiä ei ole saatavilla vertailua varten.

---

## Sytotoksiksuus

| Kohta | Sisältö |
|------|--------|
| Sytotoksiksuusluokitus | Kohdennettu lääkitys (moniaineinen tyrosiinkinaasin estäjä: BCR-ABL, VEGFR, FGFR, PDGFR, SRC-perhe) |
| Luuydinsortumusriski | Viitattava pakkauselosteeseen |
| Pahoinvointipotentiaalin luokitus | Viitattava pakkauselosteeseen |
| Seurattavat asiat | Viitattava pakkauselosteeseen |
| Käsittelyturvallisuus | Viitattava pakkauselosteeseen |

---

## Turvallisuusnäkökohdat

Katso pakkausseloste turvallisuustietojen osalta.

---

## Lisähuomautus: 2. Sijan ennustettu indikaatio

Toinen ennustettu indikaatio, **liposarkooma**, sai lähes yhtä korkean pistemäärän (99.00%, TxGNN-ranking 9484) ja toisin kuin gingivaalinen fibromatoosi, sillä on yksi tukeva prekliininen julkaisu: [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) (2017, *Journal of Hematology & Oncology*), kinaasien profilointi-/RNAi-lääkkeiden seulontatutkimus, joka tunnisti lääkkeettäviä kinaasikohteita liposarkoomassa. Tämä on prekliininen, ei kliininen, näyttö, mutta se antaa liposarkooman osalta vahvemman (vaikka silti varhaisen) näyttöperustan kuin etusijalla oleva indikaatio ja voi vaatia erillistä tutkimista.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Korkeimman sijoituksen saaneen indikaation (gingivaalinen fibromatoosi) tukeina ei ole mitään kliinisiä tutkimuksia tai kirjallisuusviitteitä — vain mallin pistemäärä, mikä asettaa sen näyttötasolle L5. Kriittisen aineistovajeen (pakkausseloste/turvallisuustiedot, DG001) ja lääkkeen markkinointiluvattoman aseman vuoksi ei ole riittävää perustetta edetä alkuseulonnasta eteenpäin.

**Jotta voidaan edetä, tarvitaan seuraavaa:**
- TFDA/Fimea-pakkauselosteen tiedot (varoitukset, vasta-aiheet, lääkkeiden yhteisvaikutukset) — tällä hetkellä kriittinen aineistovaje
- Vahvistettu toimintamekanismi DrugBankista — tällä hetkellä korkean vakavuuden aineistovaje
- Kohdennettu kirjallisuus-/prekliininen haku, joka on spesifinen gingivaalisen fibromatoosin osalta, mekanistisen hypoteesin testaamiseksi
- Harkitse rinnakkaista liposarkooma-signaalin (ranking 2) arviointia, jolla on vähintään yksi tukeva prekliininen julkaisu

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

