---
layout: default
title: Pegvaliase
parent: Pelkkä mallin ennuste (L5)
nav_order: 290
evidence_level: L5
indication_count: 3
---

# Pegvaliase
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

# Pegvaliase: Fenylketonuriasta (PKU) diabeettiseen retinopatiahin (ennuste)

## Yksirivinen yhteenveto

Pegvaliase (DrugBank DB12839) on PEGyloidun fenyylialaniini-ammoniakkilyaasi (PAL) -entsyymiterapia, jota käytetään veren fenyylialaniinipitoisuuden alentamiseen PKU-potilailla — tämä tausta on johdettu mallin omasta perustelutekstistä, sillä muodollisia alkuperäisen käyttöaiheen tai sääntelytietoja ei ole saatavilla. TxGNN-malli ennustaa mahdollista tehokkuutta **Diabeettiseen retinopatiahin**, ennustetulla pistemäärällä **99,17 %**, mutta tällä hetkellä **nolla kliinisiä tutkimuksia ja nolla julkaisuja** tukea tätä suuntaa. Tämä on pelkkä malliennuste (L5), jolla ei ole vahvistettua biologista perustelua, ja suositeltu päätös on **Odota**.

---

## Pikayleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen käyttöaihe | Ei sisältynyt sääntelytietoihin (lääketta ei markkinoida Suomessa); taustafarmakologia viittaa käyttöön PKU-liittyvän hyperfenyylialaninemian hoidossa |
| Ennustettu uusi käyttöaihe | Diabeettinen retinopatia |
| TxGNN-ennusteen pistemäärä | 99,17 % (sijoitus 8141 mallin tuloksissa) |
| Näytön taso | L5 (pelkkä malliennuste — ei kliinisiä tutkimuksia, ei kirjallisuutta) |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Odota |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtainen, jäsennelty vaikutusmekanismin tieto on merkitty tietoaukoksi tässä näyttöpaketissa (DG002, korkea vakavuus). Kuitenkin mallin omassa uudelleenkäytön perustelutekstissä kuvataan Pegvaliasin tunnettu farmakologia: se hajottaa kiertävää fenyylialaniinia PAL-entsyymiaktiivisuuden kautta, ja sitä käytetään hyperfenyylialaninemian hallintaan PKU-potilailla.

Diabeettinen retinopatia on pohjimmiltaan eri patofysiologia — krooninen hyperglykemia johtaa verkkokalvon pienten verisuonten peruskalvon paksuuntumiseen, perityytin menetykseen, VEGF-ohjattuun uusien verisuonten muodostumiseen ja verisuonten vuotoon. Fenyylialaniinin aineenvaihdunnan/PAL-entsyymitoiminnan ja tämän VEGF/mikrovaskulaarisen sairauden välillä ei ole tunnettua biokemiallista tai farmakologista yhteyttä.

Näyttöpaketin omaan arviointiin perustuen korkea TxGNN-pistemäärä on todennäköisesti **väärä positiivinen tulos**, joka johtuu epäsuorasta tietoverkkojen topologiasta — esimerkiksi jaetuista solmuista, kuten "aineenvaihduntasairaus" tai PKU-liittyvät silmä-/neurologiset komplikaatiot, jotka yhdistyvät diabetes-liittyvän silmäsairauden klustereihin, eikä todellisesta jaetusta mekanismista. Kaksi muuta liittyvää ennustetta (vaikea ei-proliferatiivinen diabeettinen retinopatia ja diabeettinen katarakta) ovat saman diabeettisen silmäsairauden alaryhmiä tai variantteja ja jakavat saman riippumattoman mekanistisen tuen puutteen — ne näyttävät olevan saman taustalla olevan kuvaajan artefaktin tuloksia eikä kolme riippumatonta signaalia.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä liittyviä kliinisiä tutkimuksia.

*(Vahvistettu suorilla ClinicalTrials.gov- ja ICTRP-kyselyillä Pegvaliasista diabeettiseen retinopatiahin, vakavaan ei-proliferatiiviseen diabeettiseen retinopatiahin ja diabeettiseen kataraktaan — kaikki palautuivat nollatulokseen.)*

---

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla liittyvää kirjallisuutta.

*(Vahvistettu suorilla PubMed-kyselyillä Pegvaliasista diabeettiseen retinopatiahin, vakavaan ei-proliferatiiviseen diabeettiseen retinopatiahin ja diabeettiseen kataraktaan — kaikki palautuivat nollatulokseen.)*

---

## Suomen markkinatiedot

Pegvaliasilla ei ole tällä hetkellä myyntilupaa Suomessa — markkinatilanne on **Ei markkinoilla**, sillä saatavilla on 0 lupaa. Tuotetietoja, antomuotoja tai hyväksyttyjä käyttöaiheita koskevia tietoja ei ole saatavilla.

---

## Turvallisuusnäkökohdat

Turvallisuustietoja koskevia lisätietoja saat pakkausselosteesta.

*(Pegvaliasin tärkeät varoitukset, vasta-aiheet tai lääkkeiden yhteisvaikutustiedot eivät ole tällä hetkellä saatavilla tässä näyttöpaketissa; TFDA:n pakkausseloste-tietojen keräys (DG001, estävä vakavuus) on vielä odottamassa.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Tämä ennuste on tuettu ainoastaan TxGNN-mallin pistemäärällä (L5), eikä sen tueksi ole kliinisiä tutkimuksia, kirjallisuutta tai vahvistettua biologista mekanismia, joka yhdistäisi PAL-entsyymitoiminnan diabeettisen retinopatian patofysiologiaan. Näyttöpaketti itsessään arvioi tämän todennäköisesti tietoverkko-väärä positiiviseksi. Tämä ei täytä kynnystä edetä turvallisuuden esiseulontaan (S1).

**Edistymiseksi tarvitaan seuraavaa:**
- TFDA/EMA pakkausseloste-tieto (varoitukset, vasta-aiheet) sulkiakseen estävä tietoaukko DG001
- Tarkistettu, jäsennelty vaikutusmekanismin tieto sulkiakseen korkean vakavuuden tietoaukko DG002
- Riippumaton biologisen perustelun tarkastelu (esimerkiksi mikä tahansa näyttö fenyylialaniinin/PAL-polun osallistumisesta verkkokalvon pienten verisuonten sairauksiin)
- Jatkuva määräaikainen seuranta ClinicalTrials.gov-, ICTRP- ja PubMed-tietokannoista uusien näyttöjen varalta, koska mitään ei ole tällä hetkellä saatavilla yhdellekään kolmesta liittyvästä ennustetusta käyttöaiheesta

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

