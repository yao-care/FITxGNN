"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定「正文張數自動改寫」；做法移植 KrTxGNN／MyTxGNN／DETxGNN 同名檔，規則是本站芬蘭文句型）。

正文裡「N myyntilupaa on voimassa」「N voimassa olevaa myyntilupaa」「N myyntilupaa, joista V on voimassa」「V myyntilupaa N:sta on voimassa」
「Kaikki N myyntilupaa ovat voimassa」「voimassa on N myyntilupaa」「Myyntilupien määrä: N」「(N lupa)」這類 EMA 集中許可張數敘述，
由程式依許可證快照（snapshots/fi_licenses.json.gz 的 facts）改寫，每週資料更新後跟著改，不逐筆寫查核紀錄
（同 Kr／My／Tw：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥 EMA 集中許可張數」的地方，其餘一律不動：
  - 句子要有許可字樣（myyntilupa／lupa 的各格），且沒有試驗、文獻、病人、劑量、年份、預測（ennuste、ehdokas、sija）等字樣（NOT_LICENSE）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、引言框、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（skipped）：有保留（vähintään、ainakin、osittain…）、講證據包或查詢（Evidence Pack、haku、palautti…）、
    相對數（muuta、muut、lisäksi、toinen）、劑型或單方／複方子集（tabletti、yksiaineinen、yhdistelmä…）、獸用、其他國家或國家許可
    （FDA、Fimea、kansallinen…）、廠商；講表格顯示筆數（taulukko、luettelo、alla、näytetään…，reason＝display）；
    事實層 partial 或總數 0 的頁整頁不動。
角色：「N myyntilupaa on voimassa」「N voimassa olevaa myyntilupaa」「voimassa on N」「joista N on voimassa」→有效；
「N peruttua／peruutettua myyntilupaa」「N myyntilupaa on peruttu」「joista N on peruttu」→註銷；
「N:sta」「kolmesta」（出格）、「N/M」的 M、「Kaikki N myyntilupaa」「Myyntilupien määrä: N」「myyntilupia on N」「yhteensä N」→總數；
其他「N myyntilupaa」沒有狀態字→總數（沒有限定詞，讀法＝總數或有效數）。數字可寫成阿拉伯數字或 kaksi～kymmenen（主格）、
kahdesta～kymmenestä（出格）、molemmat；「yksi／yhdestä」只在緊接（形容詞＋）lupa 時算 1。改寫時保留原寫法
（主格字改成主格字、出格字改成出格字，超過 10 用阿拉伯數字；「N:sta」照芬蘭文數詞的母音和諧換成 :sta／:stä）。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
數字已等於該角色的任一合理讀法就不動；不等於時兩種讀法相同才改，不同列為 ambiguous。
不改、列出（要改請寫查核紀錄）：原數字 0（zero-premise）、新數字 0（zero-result）、1 跟非 1 之間的改動（芬蘭文 1 用主格單數、
2 以上用單數分格，名詞與動詞要跟著改，grammar）、molemmat／kumpikin 而總數不是 2（grammar）、句子說「kaikki／molemmat … voimassa」
或「ei … peruttu」而事實不符、或說「ainoa」（只有一張）而要跨過 1（premise）。
"""
from __future__ import annotations

import re

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÄÖÅ*\[(>-])")
NOM = {"kaksi": 2, "kolme": 3, "neljä": 4, "viisi": 5, "kuusi": 6, "seitsemän": 7, "kahdeksan": 8, "yhdeksän": 9, "kymmenen": 10}
ELA = {"yhdestä": 1, "kahdesta": 2, "kolmesta": 3, "neljästä": 4, "viidestä": 5, "kuudesta": 6, "seitsemästä": 7, "kahdeksasta": 8,
       "yhdeksästä": 9, "kymmenestä": 10}
BOTH = {"molemmat": 2, "kumpikin": 2}
WORDS = {**NOM, **ELA, **BOTH}
NOM_OUT = {v: k for k, v in NOM.items()}
ELA_OUT = {v: k for k, v in ELA.items()}
LICN = r"(?:(?:myynti|EU-myynti|EMA-myynti|EU-|EMA-)?lu(?:pa|vat|paa|pia|van|pien|vien|vasta|vista|vassa|villa|valla|paan|piin))\b"
ADJS = (r"(?:(?:voimassa\s+olev\w*|peru(?:u)?tet\w*|peru\w*|keskitet\w*|EU:n|kirjat\w*|rekisteröi\w*|myönnet\w*|"
        r"suomalai\w*|eurooppalai\w*|ainoa\w*)\s+)*")
ONE = r"(?:yksi|yhdestä)"
NUM = re.compile(r"(?<![\w.,-])(\d{1,4}(?::st[aä])?|" + "|".join(sorted(WORDS, key=len, reverse=True)) + r"|" + ONE +
                 r"(?=\s+" + ADJS + LICN + r"))(?![\w%-])", re.I)
LICENSE = re.compile(r"myyntilup|myyntiluv|\blu(?:pa|vat|paa|pia|van|pien|vien)\b", re.I)
NOT_LICENSE = re.compile(r"tutkimu|tutkitt|koehenkil|potila|PMID|NCT|julkais|artikkel|tapaus|\bmg\b|\bml\b|%|vuo(?:si|den|nna|tta|sina)\b|"
                         r"kuukau|viiko|annos|pistemäär|ennust|ehdok|\bsija|vaihe|käyttöaihei|\b(?:19|20)\d\d\b", re.I)
HEDGED = re.compile(r"vähintään|ainakin|osittai|epätäydelli|puutteelli|mahdollisesti|todennäköis|arviolta|noin\b|valikoi|"
                    r"Evidence Pack|todistepak|näyttöpak|\bhaku|\bhaettu|haun\b|kysely|tietue|palautti|aineistopak|"
                    r"\bmuu(?:ta|t|ja|n|ssa|lla)?\b|lisäksi|\btoinen\b|\btoista\b|jäljellä|\bloput\b|\bjoukossa\b|"
                    r"eläinlääk|eläimil|EMEA/V|yksiaine|yhden vaikuttavan|yksittäisvalm|yhdistelmä|yksikomponent|"
                    r"tabletti|kapseli|injektio|infuusio|liuos|jauhe|\bkynä|tipat|voide|inhal|laastari|implantti|ruiskeen|"
                    r"FDA|Yhdysval|Fimea|kansallis|valmistaja|haltija|Ruotsi|Norja|Saksa|Taiwan", re.I)
DISPLAY = re.compile(r"taulukk|taulukos|taulukon|luettel|lueteltu|listat|\balla\b|yllä|näytet|ensimmäi|esimerk|seuraava", re.I)
CANC = r"(?:perut\w*|peruut\w*|lakan\w*|lakkaut\w*|kumot\w*|vanhentun\w*|rauen\w*|mitätö\w*|vedetty pois)"
VALID = r"(?:voimassa\w*)"
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)


def _val(tok):
    t = tok.lower()
    m = re.fullmatch(r"(\d+)(?::st[aä])?", t)
    if m:
        return int(m.group(1))
    if t in WORDS:
        return WORDS[t]
    return 1  # yksi／yhdestä


def _ela_suffix(v):
    """「N:sta／N:stä」：照芬蘭文數詞出格最後一個字的母音和諧"""
    if v % 100 == 0 or 11 <= v % 100 <= 19:
        return "sta"
    if v % 10 == 0:
        return "stä"
    return {1: "stä", 2: "sta", 3: "sta", 4: "stä", 5: "stä", 6: "sta", 7: "stä", 8: "sta", 9: "stä"}[v % 10]


def _fmt(tok, v):
    """保留原寫法；做不到回 None"""
    t = tok.lower()
    cap = (lambda w: w.capitalize() if tok[:1].isupper() else w)
    if re.fullmatch(r"\d+", t):
        return str(v)
    if re.fullmatch(r"\d+:st[aä]", t):
        return f"{v}:{_ela_suffix(v)}"
    if t in ELA or t == "yhdestä":
        return cap(ELA_OUT[v]) if v in ELA_OUT else f"{v}:{_ela_suffix(v)}"
    if t in NOM:
        return cap(NOM_OUT[v]) if v in NOM_OUT else str(v)
    return None  # yksi、molemmat：要改名詞格，交給 grammar


def _role(s, a, b):
    tok = s[a:b].lower()
    left, right = s[max(0, a - 60):a], s[b:b + 90]
    if re.fullmatch(r"\d+:st[aä]", tok) or tok in ELA or tok == "yhdestä":
        return "total"  # 出格「N:sta／kolmesta」＝「…中的」總數
    if re.search(r"\d\s*/\s*$", left):
        return "total"  # 「N/M」的 M
    if tok in BOTH:
        return "both" if re.match(r"\s+" + ADJS + LICN, right, re.I) else None
    if re.match(r"\s*/\s*\d+", right):  # 「N/M」的 N：看後面的狀態字
        tail = re.split(r"[.;]", right)[0]
        if re.search(CANC, tail, re.I):
            return "cancelled"
        return "valid" if re.search(VALID, tail, re.I) else None
    if re.search(r"\bjoista\s+(?:(?:nyt|tällä hetkellä|edelleen|enää)\s+)*$", left, re.I):
        if re.match(r"\s+(?:\w+\s+){0,2}" + CANC, right, re.I) or re.match(r"\s+(?:on|ovat)\s+(?:\w+\s+){0,2}" + CANC, right, re.I):
            return "cancelled"
        if re.match(r"\s+(?:on|ovat)\s+(?:\w+\s+){0,2}" + VALID, right, re.I) or re.match(r"\s+" + VALID, right, re.I):
            return "valid"
        return None
    if re.search(r"\b(?:määrä|lukumäärä)\s*(?:on\s*)?:?\s*$", left, re.I) and re.search(r"myyntilup|myyntiluv|lupien", left, re.I):
        return "total"  # 「Myyntilupien määrä: N」
    if re.search(r"(?:\d+:st[aä]|" + "|".join(ELA) + r")\s+(?:" + ADJS + LICN + r"\s+)?$", left, re.I):
        # 「Seitsemästä myyntiluvasta kuusi on voimassa」「7:stä luvasta 6 on peruttu」的後一個數字：看後面的狀態字
        if re.match(r"\s+(?:" + LICN + r"\s+)?(?:on|ovat)\s+(?:\w+\s+){0,2}" + CANC, right, re.I):
            return "cancelled"
        if re.match(r"\s+(?:" + LICN + r"\s+)?(?:on|ovat)\s+(?:\w+\s+){0,2}" + VALID, right, re.I):
            return "valid"
        return None
    mo = re.search(r"\b(?:on|ovat)\s+(?:(?:tällä hetkellä|nyt|yhteensä|kaikkiaan|kirjattu)\s+)*$", left, re.I)
    if mo:
        pre = left[:mo.start()]
        if re.search(VALID + r"[^.;,]{0,25}$", pre, re.I):
            return "valid"   # 「voimassa on N myyntilupaa」「voimassa olevia myyntilupia on N」
        if re.search(CANC + r"[^.;,]{0,25}$", pre, re.I):
            return "cancelled"
        if re.search(r"\b(?:myynti)?lup(?:ia|aa)\s*$", pre, re.I):
            return "total"   # 「myyntilupia on N」
        if not re.match(r"\s+" + ADJS + LICN, right, re.I):
            return None
    m = re.match(r"\s+(" + ADJS + r")" + LICN + r"([^.;]{0,50})", right, re.I)
    if m:
        adj, tail = m.group(1), m.group(2)
        if re.search(VALID, adj, re.I):
            return "valid"
        if re.search(CANC, adj, re.I):
            return "cancelled"
        if re.search(r"\b(kaikki|kaikkiaan|yhteensä)\s+$", left, re.I):
            return "total_x"
        tail0 = re.split(r"[,(:]|\s(?:ja|sekä|mutta|eli)\s", tail)[0]  # 只看同一子句
        if re.search(r"\b(?:on|ovat)\s+(?:\w+\s+){0,2}" + CANC, tail0, re.I):
            return "cancelled"
        if re.search(r"\b(?:on|ovat)\s+(?:\w+\s+){0,2}" + VALID, tail0, re.I):
            return "valid"
        return "total"
    # 「…, ja 6 on voimassa」：數字後面直接接狀態（主詞是前文的許可）
    if re.match(r"\s+(?:on|ovat)\s+(?:\w+\s+){0,2}" + CANC, right, re.I):
        return "cancelled"
    if re.match(r"\s+(?:on|ovat)\s+(?:\w+\s+){0,2}" + VALID, right, re.I):
        return "valid"
    return None


def _readings(role, f, explicit):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if role in ("total_x", "both") or explicit:
        return {t}, t
    return {t, v}, (t if t == v else None)


def _premise_ok(sent, f):
    lo = sent.lower()
    if re.search(r"\b(kaikki|molemmat|kumpikin)\b[^.;]{0,70}" + VALID, lo) and (f.get("valid") != f.get("total")):
        return False
    if re.search(r"\b(ei|eikä)\b[^.;]{0,30}" + CANC, lo) and f.get("cancelled"):
        return False
    return True


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not LICENSE.search(sent) or not NUM.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(1), m.end(1))) for m in NUM.finditer(sent)]
    found = [(m, r) for m, r in found if r]
    if not found:
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    if DISPLAY.search(sent):  # 講表格顯示筆數：不改；數字跟事實對不上時列出（reason＝display）
        bad = any(_val(m.group(1)) not in _readings(r, f, explicit)[0] for m, r in found)
        return sent, ("display" if bad else "display-ok")
    subs = []
    for m, role in found:
        old = _val(m.group(1))
        ok, v = _readings(role, f, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if v == 0:
            return sent, "zero-result"
        if role == "both" or (old == 1) != (v == 1):
            return sent, "grammar"
        if _fmt(m.group(1), v) is None:
            return sent, "grammar"
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f):
        return sent, "premise"
    if re.search(r"\bainoa\w*\b", sent, re.I):
        return sent, "premise"  # 「ainoa myyntilupa」：說只有一張
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(_fmt(m.group(1), v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", "{:", ">")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or not facts.get("total"):
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines = [ln if "\x00" in ln else _line(ln, facts, protect, skipped) for ln in body.split("\n")]
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
