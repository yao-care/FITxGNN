"""疾病映射模組 - 葡萄牙語適應症/治療類別映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 葡萄牙語-英語疾病/症狀對照表
DISEASE_DICT = {
    # === Sydän ja verisuonet (Cardiovascular) ===
    "verenpainetauti": "hypertension",
    "korkea verenpaine": "hypertension",
    "matala verenpaine": "hypotension",
    "sydäninfarkti": "myocardial infarction",
    "angina pectoris": "angina",
    "rytmihäiriö": "arrhythmia",
    "eteisvärinä": "atrial fibrillation",
    "sydämen vajaatoiminta": "heart failure",
    "sepelvaltimotauti": "coronary artery disease",
    "syvä laskimotukos": "deep vein thrombosis",
    "keuhkoembolia": "pulmonary embolism",
    "hyperkolesterolemia": "hypercholesterolemia",
    "dyslipidemia": "dyslipidemia",
    "ateroskleroosi": "atherosclerosis",
    "endokardiitti": "endocarditis",
    "myokardiitti": "myocarditis",
    "perikardiitti": "pericarditis",
    # === Hengityselimistö (Respiratory) ===
    "keuhkoahtaumatauti": "chronic obstructive pulmonary disease",
    "astma": "asthma",
    "keuhkokuume": "pneumonia",
    "keuhkoputkentulehdus": "bronchitis",
    "influenssa": "influenza",
    "tuberkuloosi": "tuberculosis",
    "kystinen fibroosi": "cystic fibrosis",
    "uniapnea": "obstructive sleep apnea",
    "hengenahdistus": "dyspnea",
    "keuhkolaajentuma": "emphysema",
    "sivuontelotulehdus": "sinusitis",
    "allerginen nuha": "allergic rhinitis",
    # === Ruoansulatuselimistö (Gastrointestinal) ===
    "refluksitauti": "gastroesophageal reflux disease",
    "närästys": "gastroesophageal reflux disease",
    "mahahaava": "gastric ulcer",
    "pohjukaissuolihaava": "duodenal ulcer",
    "gastriitti": "gastritis",
    "ärtyvän suolen oireyhtymä": "irritable bowel syndrome",
    "tulehduksellinen suolistosairaus": "inflammatory bowel disease",
    "crohnin tauti": "crohn disease",
    "haavainen paksusuolentulehdus": "ulcerative colitis",
    "ummetus": "constipation",
    "ripuli": "diarrhea",
    "pahoinvointi": "nausea",
    "oksentelu": "vomiting",
    "rasvamaksa": "hepatic steatosis",
    "maksakirroosi": "liver cirrhosis",
    "hepatiitti": "hepatitis",
    "hepatiitti b": "hepatitis b",
    "hepatiitti c": "hepatitis c",
    "haimatulehdus": "pancreatitis",
    "sappikivet": "cholelithiasis",
    # === Hermosto (Neurological) ===
    "alzheimerin tauti": "alzheimer disease",
    "parkinsonin tauti": "parkinson disease",
    "epilepsia": "epilepsy",
    "ms-tauti": "multiple sclerosis",
    "migreeni": "migraine",
    "päänsärky": "headache",
    "aivohalvaus": "stroke",
    "neuropatia": "neuropathy",
    "perifeerinen neuropatia": "peripheral neuropathy",
    "aivokalvontulehdus": "meningitis",
    "aivotulehdus": "encephalitis",
    # === Mielenterveys (Psychiatric) ===
    "masennus": "depression",
    "vakava masennus": "major depressive disorder",
    "ahdistuneisuushäiriö": "anxiety disorder",
    "yleistynyt ahdistuneisuushäiriö": "generalized anxiety disorder",
    "kaksisuuntainen mielialahäiriö": "bipolar disorder",
    "skitsofrenia": "schizophrenia",
    "pakko-oireinen häiriö": "obsessive-compulsive disorder",
    "traumaperäinen stressihäiriö": "post-traumatic stress disorder",
    "unettomuus": "insomnia",
    "tarkkaavuushäiriö": "attention deficit hyperactivity disorder",
    "adhd": "attention deficit hyperactivity disorder",
    # === Umpieritys (Endocrine) ===
    "diabetes": "diabetes mellitus",
    "sokeritauti": "diabetes mellitus",
    "tyypin 1 diabetes": "type 1 diabetes mellitus",
    "tyypin 2 diabetes": "type 2 diabetes mellitus",
    "kilpirauhasen vajaatoiminta": "hypothyroidism",
    "kilpirauhasen liikatoiminta": "hyperthyroidism",
    "struuma": "goiter",
    "cushingin oireyhtymä": "cushing syndrome",
    "addisonin tauti": "addison disease",
    "lihavuus": "obesity",
    "metabolinen oireyhtymä": "metabolic syndrome",
    "kihti": "gout",
    "hyperurikemia": "hyperuricemia",
    # === Tuki- ja liikuntaelimistö (Musculoskeletal) ===
    "niveltulehdus": "arthritis",
    "nivelreuma": "rheumatoid arthritis",
    "nivelrikko": "osteoarthritis",
    "osteoporoosi": "osteoporosis",
    "systeeminen lupus": "systemic lupus erythematosus",
    "fibromyalgia": "fibromyalgia",
    "selkärankareuma": "ankylosing spondylitis",
    "jännetulehdus": "tendinitis",
    "alaselkäkipu": "low back pain",
    # === Ihotaudit (Dermatological) ===
    "psoriasis": "psoriasis",
    "ihottuma": "eczema",
    "atooppinen ihottuma": "atopic dermatitis",
    "nokkosihottuma": "urticaria",
    "akne": "acne",
    "ruusufinni": "rosacea",
    "vitiligo": "vitiligo",
    "hiustenlähtö": "alopecia",
    "vyöruusu": "herpes zoster",
    "huuliherpes": "herpes simplex",
    "sieni-infektio": "fungal infection",
    # === Virtsaelimistö (Urological) ===
    "virtsatieinfektio": "urinary tract infection",
    "rakkotulehdus": "cystitis",
    "munuaistulehdus": "nephritis",
    "munuaisten vajaatoiminta": "renal failure",
    "krooninen munuaissairaus": "chronic kidney disease",
    "munuaiskivet": "nephrolithiasis",
    "eturauhasen liikakasvu": "benign prostatic hyperplasia",
    "virtsankarkailu": "urinary incontinence",
    # === Silmätaudit (Ophthalmological) ===
    "glaukooma": "glaucoma",
    "kaihi": "cataract",
    "silmänpohjan rappeuma": "macular degeneration",
    "sidekalvontulehdus": "conjunctivitis",
    "diabeettinen retinopatia": "diabetic retinopathy",
    "kuivasilmäisyys": "dry eye syndrome",
    # === Korva-, nenä- ja kurkkutaudit (ENT) ===
    "välikorvatulehdus": "otitis media",
    "nielutulehdus": "pharyngitis",
    "nielurisatulehdus": "tonsillitis",
    "kurkunpääntulehdus": "laryngitis",
    "huimaus": "vertigo",
    # === Infektiotaudit (Infectious) ===
    "hiv-infektio": "hiv infection",
    "aids": "acquired immunodeficiency syndrome",
    "malaria": "malaria",
    "covid-19": "covid-19",
    "koronavirus": "covid-19",
    "sepsis": "sepsis",
    "verenmyrkytys": "sepsis",
    "kandidoosi": "candidiasis",
    "toksoplasmoos": "toxoplasmosis",
    # === Allergiat (Allergic) ===
    "allergia": "allergy",
    "anafylaksia": "anaphylaxis",
    "allerginen astma": "allergic asthma",
    "heinänuha": "allergic rhinitis",
    "kosketusihottuma": "contact dermatitis",
    "ruoka-allergia": "food allergy",
    # === Naistentaudit (Gynecological) ===
    "endometrioosi": "endometriosis",
    "munasarjojen monirakkulaoireyhtymä": "polycystic ovary syndrome",
    "vaihdevuodet": "menopause",
    "kuukautiskivut": "dysmenorrhea",
    "emättimen tulehdus": "vaginitis",
    "kohtumyooma": "uterine fibroid",
    "pre-eklampsia": "preeclampsia",
    # === Syöpä (Oncological) ===
    "syöpä": "cancer",
    "rintasyöpä": "breast cancer",
    "keuhkosyöpä": "lung cancer",
    "suolistosyöpä": "colorectal cancer",
    "eturauhassyöpä": "prostate cancer",
    "maksasyöpä": "liver cancer",
    "mahasyöpä": "stomach cancer",
    "haimasyöpä": "pancreatic cancer",
    "leukemia": "leukemia",
    "lymfooma": "lymphoma",
    "melanooma": "melanoma",
    "munuaissyöpä": "kidney cancer",
    "virtsarakkosyöpä": "bladder cancer",
    "kilpirauhassyöpä": "thyroid cancer",
    # === Yleisoireet (General) ===
    "kuume": "fever",
    "kipu": "pain",
    "krooninen kipu": "chronic pain",
    "tulehdus": "inflammation",
    "turvotus": "edema",
    "väsymys": "fatigue",
    "anemia": "anemia",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症/治療類別文字提取個別適應症

    使用葡萄牙語常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip().lower()

    # 使用分隔符分割
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        # 再用逗號細分
        sub_parts = re.split(r"[,/]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見前綴
            sub = re.sub(r"^(para |tratamento de |indicado para |usado para )", "", sub)
            # 移除常見後綴
            sub = re.sub(r"( e outros| etc\.?)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將葡萄牙語適應症翻譯為英文關鍵詞"""
    keywords = []
    indication_lower = indication.lower()

    for pt, en in DISEASE_DICT.items():
        if pt in indication_lower:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "CLASSE_TERAPEUTICA",
) -> pd.DataFrame:
    """將巴西 ANVISA 藥品治療類別映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        # ANVISA 使用 CLASSE_TERAPEUTICA 而非適應症
        indication_str = row.get(indication_field, "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                        "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                        "CLASSE_TERAPEUTICA": indication_str[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                    "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                    "CLASSE_TERAPEUTICA": indication_str[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
