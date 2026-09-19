---
layout: default
title: Inclisiran
parent: Pelkkä mallin ennuste (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: määrittelemättömästä alkuperäisestä indikaatiosta kaliumin puutostautiin

## Yhden lauseen tiivistelmä

Inclisiran alkuperäinen hyväksytty indikaatio ja virallinen vaikutusmekanismi eivät ole dokumentoituja tässä evidenssipakkauksessa (merkitty estäväksi/korkean vakavuuden tietokuiluksi). TxGNN-mallin paras ennuste on **Kaliumin puutostautti**, mutta tämä on puhdas mallin artefakti — **0 klinistä tutkimusta** ja **0 julkaisua** tukevat sitä, eikä malli itse tunnista tunnettu mekanistista yhteyttä lääkkeen signalointireitin ja kaliumin homeostaasin välillä.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Ei saatavilla — `original_indications` on tyhjä tässä evidenssipakkauksessa |
| Ennustettu uusi indikaatio | Kaliumin puutostautti |
| TxGNN-ennusteen pistemäärä | 99.93% |
| Evidenssitaso | L5 (vain mallin ennuste, ei tukevia tutkimuksia tai kirjallisuutta) |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidä |

---

## Miksi tämä ennuste on järkevä?

Muodollinen vaikutusmekanismi-data lääkeprofiilin tasolla on merkitty tietokuiluksi (DG002, korkea vakavuus). Kuitenkin evidenssipaketin oma indikaatiokohtainen perusteluteksti (liitettynä rank-8-merkintään "aortan epämuodostuma") kuvaa inclisirania pieneksi interferenssi-RNA:ksi (siRNA), joka kohdentuu maksassa olevaan PCSK9-mRNA:han, estää PCSK9-synteesiä ja lisää hepatisten LDL-reseptorien kierrätystä LDL-kolesterolin alentamiseksi — eli lipidiaineenvaihdunnan väylän lääkkeeksi, mikä on yhteensopivaa kyseisessä merkinnässä löydettyjen kahden todellisen tutkimuksen kanssa (NCT06597006, NCT06597019), jotka todellisuudessa tutkivat lapsuusiän familaarista hyperkolesterolemiaa eikä merkittyä sairautta.

Parhaiten sijoittuvassa ennusteessa, Kaliumin puutostaudissa, evidenssipakkaus nimenomaisesti toteaa, ettei PCSK9/LDL-väylän ja kaliumin homeostaasin välillä ole tunnettu mekanistista yhteyttä. Pistemäärä 99.93% on graafimallin korkean varmuuden tuloste, mutta sitä ei tue mikään tutkimus, tapausraportti tai mekanistinen kirjallisuus — malli, joka on yhteensopiva pisteytysartefaktin kanssa pikemminkin kuin biologisesti perustetun hypoteesin kanssa.

Tämä malli toistuu kaikissa kymmenen paremmuusjärjestyksessä sijoittuvassa ennusteessa: millään ei ole kirjallisuutta tai tutkimuksia, jotka suoraan ja pätevällä tavalla yhdistäisivät inclisirania ennustettuun tautiin. Rank 8 ("aortan epämuodostuma") palautti kaksi tutkimushittiä, mutta evidenssipaketin oma vahvistus löysi nämä ontologia-kartoitusvirheiksi (tutkimukset tutkivat HoFH/HeFH:tä, eivät aortan epämuodostumaa). Rank 7 ("migreeni ilman aurataa tai ilman, herkkyyteen") palautti 20 PubMed-osumaa, mutta kaikki koskevat epilepsia/migreeni-yhteisen genetiikan (esim. SCN1A, MTHFR) eikä mainita inclisirania, PCSK9:ää tai lipidireittejä.

---

## Klinisten tutkimusten evidenssi

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä klinisiä tutkimuksia.

---

## Kirjallisuuden evidenssi

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta.

---

## Turvallisuushuomiot

Viitatkaa pakkausselosteeseen turvallisuustiedoista.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelut:**
Kaikki kymmenen paremmuusjärjestyksessä sijoittuvaa ennustetta sijaitsevat evidenssitasolla L5 (vain mallin pistemäärä). Parhaiten sijoittuvalla ennusteella on nimenomaisesti tunnustettu mekanistisen uskottavuuden puute, ja ainoa paikka, jossa todellisia tutkimusaineistoja esiintyi muualla luettelossa (rank 8), osoittautui sairauden-merkinnän kartoitusvirheeksi, joka ei liity ennustettuun tilaan. Ei ole perusteita edistää mitään ehdokasta S0:n yli.

**Jatkamista varten tarvitaan seuraavaa:**
- TFDA/Fimea-pakkausseloste (DG001, estävä) — vaaditaan ennen S1-turvallisuusseulontaa
- Vahvistettu alkuperäinen indikaatio ja vaikutusmekanismi DrugBankista (DG002)
- Tautikohtainen tutkimus- tai kirjallisuustodiste mille tahansa paremmuusjärjestyksen ennusteelle, saatu oikaistun taudin ontologia-kartoituksen kautta (aorta-epämuodostuma-ristiriita viittaa siihen, että myös muut tämän erän merkinnät voivat olla väärin kartalla)
- TxGNN-evidenssien hakemisen uusinta kerran ontologia-kartoitus on vahvistettu, ennen kuin arvioidaan uudelleen mitään ehdokasta tässä joukossa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

