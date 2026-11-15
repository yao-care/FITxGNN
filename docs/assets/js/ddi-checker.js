/**
 * FITxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking with 15 built-in curated rules (DDInter consulted as a reference; not a full database lookup).
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author FITxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    // This site does not publish /data/ddi-index.json; only the curated rules
    // below are used. Set a URL here once such a file exists.
    ddiDataUrl: null,
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'Vakava' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'Kohtalainen' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'Lievä' }
  };

  // 15 built-in high-priority DDI rules (hand-curated, DDInter consulted as a reference)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'Varfariini + Ibuprofeeni: lisääntynyt verenvuotoriski',
      detail: 'Tulehduskipulääkkeet estävät verihiutaleiden toimintaa ja voivat voimistaa varfariinin antikoagulanttivaikutusta, mikä lisää merkittävästi ruoansulatuskanavan verenvuodon riskiä.',
      recommendation: 'Käytä sen sijaan parasetamolia tai lisää mahansuojaksi protonipumpun estäjä.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'Varfariini + Asetyylisalisyylihappo: lisääntynyt verenvuotoriski',
      detail: 'Molemmat vaikuttavat hemostaasiin; yhteiskäyttö lisää verenvuotoriskiä huomattavasti.',
      recommendation: 'Jos yhdistelmä on välttämätön, käytä pieniannoksista asetyylisalisyylihappoa ja seuraa INR-arvoa tiiviisti.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'Varfariini + Naprokseeni: lisääntynyt verenvuotoriski',
      detail: 'Naprokseenin ja varfariinin yhdistäminen lisää ruoansulatuskanavan ja muiden verenvuotojen riskiä.',
      recommendation: 'Käytä kivunlievitykseen sen sijaan parasetamolia.'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'Metformiini + jodivarjoaineet: maitohappoasidoosin riski',
      detail: 'Varjoaineet voivat aiheuttaa äkillisen munuaisvaurion, jolloin metformiinia kertyy elimistöön ja voi syntyä maitohappoasidoosi.',
      recommendation: 'Lopeta metformiini 48 tuntia ennen toimenpidettä ja aloita uudelleen vasta, kun munuaisten toiminta on todettu normaaliksi.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'Kolkisiini + Klaritromysiini: toksisuuden riski',
      detail: 'Klaritromysiini on voimakas CYP3A4:n estäjä ja suurentaa kolkisiinin pitoisuuksia veressä huomattavasti.',
      recommendation: 'Vältä yhdistelmää tai pienennä kolkisiiniannosta huomattavasti.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'Kolkisiini + HIV-proteaasin estäjät: vakavan toksisuuden riski',
      detail: 'HIV-proteaasin estäjät suurentavat kolkisiinipitoisuuksia merkittävästi ja voivat aiheuttaa kuolemaan johtavan myrkytyksen.',
      recommendation: 'Vasta-aiheinen potilaille, joilla on munuaisten tai maksan vajaatoiminta.'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Simvastatiini + Amiodaroni: myopatian riski',
      detail: 'Amiodaroni suurentaa simvastatiinin pitoisuuksia, mikä lisää rabdomyolyysin riskiä.',
      recommendation: 'Älä ylitä simvastatiiniannosta 20 mg/vrk tai vaihda toiseen statiiniin.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'SSRI + Tramadoli: serotoniinioireyhtymän riski',
      detail: 'Molemmat lisäävät serotonergistä aktiivisuutta; yhteiskäyttö voi aiheuttaa hengenvaarallisen serotoniinioireyhtymän.',
      recommendation: 'Seuraa tiiviisti oireita (hypertermia, myoklonia, muuttunut tajunnantila) ja harkitse muuta kipulääkettä.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'SSRI + Linetsolidi: serotoniinioireyhtymän riski',
      detail: 'Linetsolidi on MAO:n estäjä; sen yhdistäminen SSRI-lääkkeeseen on erittäin vaarallista.',
      recommendation: 'Vältä yhdistelmää. Jos linetsolidi on välttämätön, lopeta SSRI-lääke ja pidä riittävä lääketauko.'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'Amiodaroni + Moksifloksasiini: QT-ajan pidentymisen riski',
      detail: 'Molemmat voivat pidentää QT-aikaa; yhteiskäyttö lisää kääntyvien kärkien takykardian riskiä.',
      recommendation: 'Vältä yhdistelmää tai seuraa EKG:tä tiiviisti.'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Digoksiini + Amiodaroni: digoksiinimyrkytyksen riski',
      detail: 'Amiodaroni suurentaa digoksiinin pitoisuuksia veressä noin 70%.',
      recommendation: 'Kun amiodaroni aloitetaan, puolita digoksiiniannos ja seuraa pitoisuuksia.'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'Klopidogreeli + PPI: heikentynyt verihiutaleiden estovaikutus',
      detail: 'Omepratsoli estää CYP2C19:ää ja vähentää klopidogreelin muuttumista aktiiviseksi metaboliitiksi.',
      recommendation: 'Harkitse sen sijaan pantopratsolia tai H2-salpaajaa.'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'Litium + tulehduskipulääkkeet: litiummyrkytyksen riski',
      detail: 'Tulehduskipulääkkeet vähentävät litiumin erittymistä munuaisten kautta, jolloin sen pitoisuus veressä suurenee.',
      recommendation: 'Vältä yhdistelmää tai seuraa litiumpitoisuuksia tiiviisti.'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'Kaliumvalmisteet + kaliumia säästävät diureetit: hyperkalemian riski',
      detail: 'Molemmat suurentavat seerumin kaliumpitoisuutta; yhteiskäyttö voi aiheuttaa hengenvaarallisen hyperkalemian.',
      recommendation: 'Seuraa seerumin kaliumpitoisuutta säännöllisesti ja vältä samanaikaisia kaliumvalmisteita.'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'Metotreksaatti + Trimetopriimi-sulfametoksatsoli: luuydinlaman riski',
      detail: 'Molemmat estävät folaattiaineenvaihduntaa; yhteiskäyttö lisää luuydinlaman ja limakalvotulehduksen riskiä.',
      recommendation: 'Vältä yhdistelmää tai huolehdi riittävästä foolihappolisästä ja seuraa verenkuvaa tiiviisti.'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;
    if (!CONFIG.ddiDataUrl) {
      isLoaded = true;
      return;
    }

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'FITxGNN-sivuston sisäiset yhteisvaikutussäännöt (15 valittua sääntöä; ei kattava DDInter-haku)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">Yhteisvaikutusvaroituksia ei löytynyt</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>Suositus:</strong> ${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">Lähde: ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nSuositus: ${alert.recommendation}`,
      source: {
        label: 'FITxGNN DDI Checker',
        url: 'https://fitxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.TwTxGNN = global.TwTxGNN || {};
  global.TwTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
