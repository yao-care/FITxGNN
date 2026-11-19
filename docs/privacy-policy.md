---
layout: default
title: Tietosuojaseloste
nav_order: 95
permalink: /privacy-policy/
description: "FITxGNN:n tietosuojaseloste: staattinen sivusto ilman käyttäjätilejä ja lomakkeita; se käyttää Google Analytics 4:n analytiikkaevästeitä käyttötilastoihin."
---

# Tietosuojaseloste

<div class="key-takeaway">
Tämä on staattinen sivusto — ei rekisteröitymistä eikä lomakkeita. Sivusto käyttää Google Analytics 4:n analytiikkaevästeitä käyttötilastojen laatimiseen.
</div>

---

## Mitä keräämme

<p class="key-answer" data-question="Kerääkö FITxGNN henkilötietoja?">
<strong>Vain käyttötilastoja Google Analytics 4:n avulla.</strong> Tätä sivustoa ylläpidetään GitHub Pagesissa puhtaasti
staattisena sivustona. Sivustolla ei ole tilijärjestelmää eikä lomakkeita, emmekä kerää nimiä, sähköpostiosoitteita
tai potilastietoja. Sivusto käyttää Google Analytics 4:n analytiikkaevästeitä käyttötilastojen laatimiseen (katsotut
sivut, viittaava sivusto, vierityssyvyys ja sivulla vietetty aika). Evästeet asetetaan, kun sivu latautuu;
hakusanoja, lomakkeiden sisältöä tai URL-osoitteen kyselyparametreja ei lähetetä.
</p>

---

## Kolmansien osapuolten palvelut

Sivusto käyttää seuraavia kolmansien osapuolten resursseja, jotka voivat kirjata käyttöä omien
käytäntöjensä mukaisesti:

| Palvelu | Käyttötarkoitus | Tietosuojaseloste |
|---------|---------|----------------|
| GitHub Pages | Sivuston ylläpito | [GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Käyntitilastot (katsotut sivut, viittaava sivu); käyttää analytiikkaevästeitä. Hakusanoja, lomakkeiden sisältöä tai URL-parametreja ei lähetetä. | [Googlen tietosuojakäytäntö](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Skriptikirjastot: d3-kaaviot kaikilla sivuilla; Fuse.js nimien vertailuun ja SMART on FHIR -asiakaskirjasto SMART-sivuilla | [jsDelivrin tietosuojakäytäntö](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Kliinisten tutkimusten haku SMART-sivuilla: vain kun pyydät sitä, lääkkeen ja käyttöaiheen nimet lähetetään ClinicalTrials.gov-rajapintaan | [NLM:n verkkokäytännöt](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | SMART-sovellus: sähköisestä potilastietojärjestelmästä luettujen lääkkeiden RxNorm-koodit lähetetään NLM:n RxNav-rajapintaan vaikuttavan aineen nimen hakemiseksi (ei potilaan tunnistetietoja) | [NLM:n verkkokäytännöt](https://www.nlm.nih.gov/web_policies.html) |

Kun käynnistät SMART on FHIR -sovelluksen itse, se pyytää lääkitystietoja
potilastietojärjestelmästäsi. Potilaan henkilöllisyyttä ja potilastietojärjestelmän tietoja <strong>ei lähetetä tämän
sivuston palvelimille</strong> (sivusto on staattinen eikä sillä ole taustapalvelinta), eikä sivusto tallenna niitä.
Lääkenimien täsmäyttämiseksi sovellus lähettää lääkkeiden RxNorm-koodit Yhdysvaltain kansallisen lääketieteellisen
kirjaston (NLM) RxNav-palveluun; koodit eivät sisällä potilaan tunnistetietoja. Kun pyydät kliinisiä tutkimuksia,
lääkkeen nimi ja käyttöaihe lähetetään ClinicalTrials.gov-palveluun.

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Sovellettava laki

Suomessa sovelletaan [EU:n yleistä tietosuoja-asetusta](https://eur-lex.europa.eu/eli/reg/2016/679/oj) ja sitä täydentävää [tietosuojalakia (1050/2018)](https://finlex.fi/fi/lainsaadanto/2018/1050); evästeisiin sovelletaan lisäksi sähköisen viestinnän palveluista annettua lakia. Valvova viranomainen on [tietosuojavaltuutetun toimisto](https://tietosuoja.fi/). Ylläpitäjä toimii Taiwanissa eikä sillä ole toimipaikkaa EU:ssa; käsittely koskee Google Analytics 4:n evästeillä keräämiä käyttötietoja.

## Oikeutesi ja niiden käyttäminen

- Oikeus saada pääsy tietoihin (15 artikla) ja oikaista ne (16 artikla).
- Oikeus tietojen poistamiseen (17 artikla) ja käsittelyn rajoittamiseen (18 artikla).
- Vastustamisoikeus (21 artikla), myös analytiikan osalta.
- Oikeus tehdä valitus tietosuojavaltuutetulle (77 artikla).

Pyynnöt ja kysymykset: service@yao.care. Koska sivustolla ei ole tilejä, voimme käsitellä Google Analyticsin tietoja vain, jos annat riittävät tiedot (esim. käynnin päivän ja sivut); voit myös estää tai poistaa analytiikkaevästeet selaimessasi.

## Tekijänoikeus ja tietolähteet

Sivuston tekstit on suojattu [tekijänoikeuslailla (404/1961)](https://finlex.fi/fi/lainsaadanto/1961/404). Sivuston koodi on julkaistu MIT-lisenssillä [GitHub-repositoriossa](https://github.com/yao-care/FITxGNN); raporttien tekstit © 藥提醒科技有限公司 (yao.care).

Sivuston tietolähteet ja niiden ehdot:

- **TxGNN**-ennustedata (Harvard Dataverse): CC0 1.0 (luovutettu vapaaseen käyttöön); viittaa julkaisuun Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov** ja **PubMed**: Yhdysvaltain National Library of Medicine; katso [ClinicalTrials.gov:n ehdot](https://clinicaltrials.gov/about-site/terms-conditions) ja [NCBI:n käytännöt](https://www.ncbi.nlm.nih.gov/home/about/policies/) (osa PubMedin tiivistelmistä on kustantajan tekijänoikeuden alaisia).
- **DrugBank**-tunnisteet ja -tiedot: [DrugBankin](https://go.drugbank.com/) lisenssiehtojen mukaan (ei-kaupallinen käyttö).
- **Paikallinen aineisto**: [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx), julkaisija Euroopan lääkevirasto (EMA); uudelleenkäyttöön sovelletaan julkaisijan ehtoja, eikä tämä sivusto myönnä lisäoikeuksia.

<!-- privacy-law:end -->

---

## Muutokset tähän selosteeseen

Kaikki muutokset julkaistaan suoraan tällä sivulla.

---

## Kehittäjästä

Tämän alustan on kehittänyt ja sitä ylläpitää **藥提醒科技有限公司** (yao.care). Yhtiön tiedot, TxGNN-mallin
tausta ja tuotelinjan kaikki sivustot löytyvät <a href="{{ '/about/' | relative_url }}">Tietoa</a>-sivulta.

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
