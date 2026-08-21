"""Translations and locale-aware labels for the application."""

from config import METRICS

LANGUAGES = {
    "zh": "中文",
    "en": "English",
    "ja": "日本語",
    "fr": "Français",
    "es": "Español",
    "de": "Deutsch",
}

UI = {
    "language": {"zh": "语言", "en": "Language", "ja": "言語", "fr": "Langue", "es": "Idioma", "de": "Sprache"},
    "caption": {
        "zh": "基于多维指标的城市安全评估 · 优先使用已注明来源的真实数据，缺失项明确回退为 Mock",
        "en": "Multi-factor city safety assessment · Uses cited real data where available, with explicit mock fallback",
        "ja": "多要因の都市安全評価 · 出典付き実データを優先し、欠損項目はモックと明示",
        "fr": "Évaluation urbaine multifactorielle · Données réelles citées si disponibles, sinon données fictives signalées",
        "es": "Evaluación urbana multifactorial · Datos reales citados cuando existen y simulados claramente indicados",
        "de": "Mehrfaktorielle Stadtsicherheitsbewertung · Belegte Echtdaten, wo verfügbar; Mock-Rückfall klar markiert",
    },
    "country": {"zh": "国家", "en": "Country", "ja": "国", "fr": "Pays", "es": "País", "de": "Land"},
    "city": {"zh": "城市（可输入搜索）", "en": "City (searchable)", "ja": "都市（検索可能）", "fr": "Ville (recherche possible)", "es": "Ciudad (con búsqueda)", "de": "Stadt (durchsuchbar)"},
    "factors": {"zh": "选择影响因素并设置权重", "en": "Choose factors and set weights", "ja": "要因を選択し重みを設定", "fr": "Choisissez les facteurs et leurs poids", "es": "Elija factores y asigne pesos", "de": "Faktoren auswählen und gewichten"},
    "weight": {"zh": "{name}权重", "en": "{name} weight", "ja": "{name}の重み", "fr": "Poids : {name}", "es": "Peso: {name}", "de": "Gewichtung: {name}"},
    "weight_help": {
        "zh": "权重表示该因素对最终指数的影响程度：0 表示不计入，100 表示影响最大。权重不改变原始数据。",
        "en": "Weight controls this factor's influence on the final index: 0 excludes it and 100 gives maximum influence. It does not change the raw value.",
        "ja": "重みは最終指数への影響度です。0 は除外、100 は最大の影響を示し、元データ自体は変えません。",
        "fr": "Le poids règle l’influence sur l’indice final : 0 exclut le facteur et 100 lui donne l’influence maximale. Il ne modifie pas la valeur brute.",
        "es": "El peso controla la influencia en el índice final: 0 excluye el factor y 100 le da la máxima influencia. No cambia el valor original.",
        "de": "Die Gewichtung steuert den Einfluss auf den Gesamtindex: 0 schließt den Faktor aus, 100 gibt maximalen Einfluss. Der Rohwert bleibt unverändert.",
    },
    "environment_weight_help": {
        "zh": "权重仅控制该因素对独立环境评分的影响，不会改变总体安全指数。",
        "en": "Weight controls this factor's influence on the separate environmental score only; it cannot change the overall safety index.",
        "ja": "重みは独立した環境スコアだけに影響し、総合安全指数は変更しません。",
        "fr": "Le poids agit uniquement sur le score environnemental distinct, jamais sur l’indice global de sécurité.",
        "es": "El peso solo afecta la puntuación ambiental separada, nunca el índice general de seguridad.",
        "de": "Die Gewichtung beeinflusst nur den separaten Umweltwert, niemals den Gesamtsicherheitsindex.",
    },
    "environmental_factor_role": {
        "zh": "独立环境因素：权重不影响总体安全指数。",
        "en": "Separate environmental factor: its weight does not affect the overall safety index.",
        "ja": "独立した環境要因：総合安全指数には影響しません。",
        "fr": "Facteur environnemental distinct : sans effet sur l’indice global de sécurité.",
        "es": "Factor ambiental separado: no afecta el índice general de seguridad.",
        "de": "Separater Umweltfaktor: ohne Einfluss auf den Gesamtsicherheitsindex.",
    },
    "analyze": {"zh": "开始分析", "en": "Start analysis", "ja": "分析開始", "fr": "Lancer l’analyse", "es": "Iniciar análisis", "de": "Analyse starten"},
    "select_error": {"zh": "请至少选择一个影响因素。", "en": "Select at least one factor.", "ja": "要因を1つ以上選択してください。", "fr": "Sélectionnez au moins un facteur.", "es": "Seleccione al menos un factor.", "de": "Wählen Sie mindestens einen Faktor aus."},
    "weight_error": {"zh": "所选因素的总权重必须大于 0。", "en": "The total weight must be greater than 0.", "ja": "選択した要因の合計重みは0より大きくしてください。", "fr": "Le poids total doit être supérieur à 0.", "es": "El peso total debe ser mayor que 0.", "de": "Die Gesamtgewichtung muss größer als 0 sein."},
    "loading": {"zh": "正在获取数据并计算安全指数……", "en": "Fetching data and calculating the safety index…", "ja": "データを取得し安全指数を計算しています…", "fr": "Récupération des données et calcul de l’indice…", "es": "Obteniendo datos y calculando el índice…", "de": "Daten werden abgerufen und der Sicherheitsindex berechnet…"},
    "prompt": {"zh": "完成选择后点击“开始分析”查看结果。", "en": "Complete your selections and click “Start analysis” to view results.", "ja": "選択後、「分析開始」をクリックして結果を表示します。", "fr": "Terminez vos choix puis cliquez sur « Lancer l’analyse ».", "es": "Complete las selecciones y pulse «Iniciar análisis».", "de": "Treffen Sie Ihre Auswahl und klicken Sie auf „Analyse starten“."},
    "results": {"zh": "{place} 分析结果", "en": "Analysis results: {place}", "ja": "{place}の分析結果", "fr": "Résultats de l’analyse : {place}", "es": "Resultados del análisis: {place}", "de": "Analyseergebnisse: {place}"},
    "radar_hint": {"zh": "选择至少 3 个核心指标后可显示雷达图。", "en": "Select at least 3 core factors to display the radar chart.", "ja": "レーダーチャートには主要指標を3つ以上選択してください。", "fr": "Sélectionnez au moins 3 facteurs principaux pour afficher le radar.", "es": "Seleccione al menos 3 factores principales para mostrar el radar.", "de": "Wählen Sie mindestens 3 Kernfaktoren für das Radardiagramm."},
    "metrics": {"zh": "各项指标", "en": "Factor details", "ja": "指標の詳細", "fr": "Détail des facteurs", "es": "Detalle de factores", "de": "Faktordetails"},
    "score_raw": {"zh": "安全得分：{score}/100　原始值：{raw} {unit}", "en": "Safety score: {score}/100 · Raw value: {raw} {unit}", "ja": "安全スコア：{score}/100　元の値：{raw} {unit}", "fr": "Score de sécurité : {score}/100 · Valeur brute : {raw} {unit}", "es": "Puntuación de seguridad: {score}/100 · Valor original: {raw} {unit}", "de": "Sicherheitswert: {score}/100 · Rohwert: {raw} {unit}"},
    "environment_score_raw": {"zh": "环境得分：{score}/100　原始值：{raw} {unit}", "en": "Environmental score: {score}/100 · Raw value: {raw} {unit}", "ja": "環境スコア：{score}/100　元の値：{raw} {unit}", "fr": "Score environnemental : {score}/100 · Valeur brute : {raw} {unit}", "es": "Puntuación ambiental: {score}/100 · Valor original: {raw} {unit}", "de": "Umweltwert: {score}/100 · Rohwert: {raw} {unit}"},
    "environment_score": {"zh": "独立环境评分", "en": "Separate environmental score", "ja": "独立環境スコア", "fr": "Score environnemental distinct", "es": "Puntuación ambiental separada", "de": "Separater Umweltwert"},
    "environment_score_help": {"zh": "所选环境因素的加权平均；不计入总体安全指数。", "en": "Weighted average of selected environmental factors; excluded from the overall safety index.", "ja": "選択した環境要因の加重平均で、総合安全指数には含まれません。", "fr": "Moyenne pondérée des facteurs environnementaux sélectionnés, hors indice global.", "es": "Promedio ponderado de los factores ambientales seleccionados, fuera del índice general.", "de": "Gewichteter Mittelwert der gewählten Umweltfaktoren; nicht im Gesamtindex enthalten."},
    "report": {"zh": "自动分析报告", "en": "Automated analysis report", "ja": "自動分析レポート", "fr": "Rapport d’analyse automatique", "es": "Informe de análisis automático", "de": "Automatischer Analysebericht"},
    "calculation": {"zh": "查看计算说明", "en": "How the calculation works", "ja": "計算方法", "fr": "Méthode de calcul", "es": "Cómo se calcula", "de": "Berechnungsmethode"},
    "normalization": {"zh": "各原始指标先按配置区间标准化为 0–100 分，并统一为“越高越安全”的方向。", "en": "Raw factors are normalized to 0–100 and oriented so a higher score always means safer.", "ja": "各指標は0～100に正規化され、スコアが高いほど安全になるよう方向を統一します。", "fr": "Les valeurs sont normalisées de 0 à 100, un score élevé indiquant toujours plus de sécurité.", "es": "Los valores se normalizan de 0 a 100; una puntuación mayor siempre significa más seguridad.", "de": "Rohwerte werden auf 0–100 normiert; ein höherer Wert bedeutet stets mehr Sicherheit."},
    "formula": {"zh": "总体指数 = Σ（计分指标安全得分 × 用户权重）÷ Σ 用户权重。购买力平价直接替代名义人均收入；环境状况和其他犯罪率仅作背景，不计入总分。", "en": "Overall index = Σ(scored factor × weight) ÷ Σ(weights). PPP directly replaces nominal income; environmental state and other crime are context only and excluded.", "ja": "総合指数 = Σ（採点指標 × 重み）÷ Σ（重み）。購買力平価が名目所得を置き換え、環境状態とその他の犯罪は背景情報として除外します。", "fr": "Indice global = Σ(facteur noté × poids) ÷ Σ(poids). La PPA remplace le revenu nominal ; l’environnement et les autres infractions restent hors score.", "es": "Índice global = Σ(factor puntuado × peso) ÷ Σ(pesos). La PPA sustituye al ingreso nominal; ambiente y otros delitos quedan fuera del índice.", "de": "Gesamtindex = Σ(gewerteter Faktor × Gewichtung) ÷ Σ(Gewichtungen). KKP ersetzt Nominaleinkommen; Umwelt und sonstige Kriminalität bleiben Kontext."},
    "gauge": {"zh": "总体安全指数", "en": "Overall Safety Index", "ja": "総合安全指数", "fr": "Indice global de sécurité", "es": "Índice general de seguridad", "de": "Gesamtsicherheitsindex"},
    "official_source": {"zh": "真实数据 · {year} · 地理口径：{geography}", "en": "Real data · {year} · Geography: {geography}", "ja": "実データ · {year} · 地理範囲：{geography}", "fr": "Donnée réelle · {year} · Géographie : {geography}", "es": "Dato real · {year} · Geografía: {geography}", "de": "Echtdaten · {year} · Geografie: {geography}"},
    "mock_source": {"zh": "Mock 回退数据 · 尚未接入可靠公开来源", "en": "Mock fallback · no reliable public source connected yet", "ja": "モック代替データ · 信頼できる公開情報源は未接続", "fr": "Donnée fictive de repli · aucune source publique fiable encore connectée", "es": "Dato simulado de respaldo · aún sin fuente pública fiable conectada", "de": "Mock-Rückfall · noch keine verlässliche öffentliche Quelle angebunden"},
    "environmental_state_role": {"zh": "单独列为环境关注项，不改变总体治安指数。", "en": "Reported separately as an environmental concern; it does not change the overall safety index.", "ja": "環境上の懸念として別途報告され、総合安全指数には影響しません。", "fr": "Signalé séparément comme enjeu environnemental ; il ne modifie pas l’indice global.", "es": "Se informa aparte como preocupación ambiental; no cambia el índice general.", "de": "Wird separat als Umweltbelastung ausgewiesen und verändert den Gesamtindex nicht."},
    "other_crime_rate_role": {"zh": "作为城市背景信息展示；不直接影响游客人身与财产安全总分。", "en": "Shown as city context; it does not directly affect the visitor personal/property safety score.", "ja": "都市の背景情報として表示し、旅行者の人身・財産安全スコアには直接影響しません。", "fr": "Présenté comme contexte urbain ; il n’affecte pas directement la sécurité personnelle et matérielle des visiteurs.", "es": "Se muestra como contexto urbano; no afecta directamente la seguridad personal y patrimonial del visitante.", "de": "Wird als Stadtkontext gezeigt und beeinflusst die Personen-/Sachgütersicherheit von Besuchern nicht direkt."},
    "value_of_money_role": {"zh": "不单独计分；用于调整人均收入的实际安全贡献。", "en": "Not scored independently; it adjusts the real safety contribution of income per capita.", "ja": "単独では採点せず、一人当たり所得の実質的な安全寄与を調整します。", "fr": "Non noté séparément ; il ajuste la contribution réelle du revenu par habitant.", "es": "No se puntúa por separado; ajusta la contribución real del ingreso per cápita.", "de": "Keine separate Wertung; passt den realen Beitrag des Pro-Kopf-Einkommens an."},
}

METRIC_TEXT = {
    "safety_crime_rate": ("人身与财产安全犯罪率", "Personal/property crime rate", "人身・財産犯罪率", "Criminalité contre les personnes/biens", "Delitos contra personas/bienes", "Personen-/Eigentumsdelikte", "每千人案件", "cases/1,000 people"),
    "other_crime_rate": ("其他犯罪率", "Other crime rate", "その他の犯罪率", "Autres infractions", "Otros delitos", "Sonstige Kriminalität", "每千人案件", "cases/1,000 people"),
    "purchasing_power_parity": ("购买力平价", "Purchasing power parity", "購買力平価", "Parité de pouvoir d’achat", "Paridad de poder adquisitivo", "Kaufkraftparität", "本地购买力指数", "local purchasing-power index"),
    "crime_rate": ("犯罪率", "Crime rate", "犯罪率", "Taux de criminalité", "Tasa de delincuencia", "Kriminalitätsrate", "每千人案件", "cases/1,000 people"),
    "unemployment_rate": ("失业率", "Unemployment rate", "失業率", "Taux de chômage", "Tasa de desempleo", "Arbeitslosenquote", "%", "%"),
    "income_per_capita": ("人均收入", "Income per capita", "一人当たり所得", "Revenu par habitant", "Ingreso per cápita", "Pro-Kopf-Einkommen", "CAD等值/年", "CAD-equivalent/year"),
    "population_density": ("人口密度", "Population density", "人口密度", "Densité de population", "Densidad de población", "Bevölkerungsdichte", "人/km²", "people/km²"),
    "night_lighting": ("夜间照明", "Night lighting", "夜間照明", "Éclairage nocturne", "Iluminación nocturna", "Nachtbeleuchtung", "覆盖指数", "coverage index"),
    "police_count": ("警察数量", "Police presence", "警察官数", "Présence policière", "Presencia policial", "Polizeipräsenz", "每万人", "per 10,000 people"),
    "education_level": ("教育水平", "Education level", "教育水準", "Niveau d’éducation", "Nivel educativo", "Bildungsniveau", "综合指数", "composite index"),
    "housing_price": ("房价", "Housing price", "住宅価格", "Prix du logement", "Precio de vivienda", "Wohnungspreis", "USD/m²", "USD/m²"),
    "tourist_count": ("游客数量", "Visitor volume", "観光客数", "Fréquentation touristique", "Volumen turístico", "Touristenaufkommen", "万人/年", "10,000/year"),
    "public_transport": ("公共交通便利程度", "Public transport access", "公共交通の利便性", "Accessibilité des transports", "Acceso al transporte público", "ÖPNV-Erreichbarkeit", "综合指数", "composite index"),
    "environmental_state": ("环境状况", "Environmental state", "環境状態", "État environnemental", "Estado ambiental", "Umweltzustand", "环境质量指数", "environmental quality index"),
    "air_quality": ("空气质量", "Air quality", "大気質", "Qualité de l’air", "Calidad del aire", "Luftqualität", "空气质量指数", "air-quality index"),
    "water_quality": ("水质", "Water quality", "水質", "Qualité de l’eau", "Calidad del agua", "Wasserqualität", "水质指数", "water-quality index"),
    "green_space": ("绿色空间", "Green space", "緑地", "Espaces verts", "Espacios verdes", "Grünflächen", "覆盖与可达性指数", "coverage/access index"),
    "noise_environment": ("声环境", "Noise environment", "音環境", "Environnement sonore", "Entorno acústico", "Lärmumgebung", "安静程度指数", "quietness index"),
    "climate_resilience": ("气候韧性", "Climate resilience", "気候レジリエンス", "Résilience climatique", "Resiliencia climática", "Klimaresilienz", "韧性指数", "resilience index"),
    "value_of_money": ("货币购买力", "Value of money", "貨幣価値", "Pouvoir d’achat", "Valor del dinero", "Kaufkraft", "购买力指数", "purchasing-power index"),
    "social_media_reputation": ("社交媒体口碑", "Social media reputation", "ソーシャルメディア評判", "Réputation sur les réseaux sociaux", "Reputación en redes sociales", "Social-Media-Reputation", "安全口碑指数", "safety sentiment index"),
}

HELP = {
    "safety_crime_rate": {"en": "Violence, robbery, assault, theft, burglary, and similar cases per 1,000 residents (2–100). Higher values directly lower visitor safety.", "zh": "暴力、抢劫、袭击、盗窃、入室盗窃等人身与财产案件数（每千人 2–100）。数值越高，游客安全得分越低。"},
    "other_crime_rate": {"en": "Regulatory, administrative, and other crimes not normally directed at visitors (1–80 per 1,000). Shown as context and excluded from the visitor safety index.", "zh": "通常不直接针对游客的监管、行政及其他类别犯罪（每千人 1–80）。仅作背景展示，不计入游客安全指数。"},
    "purchasing_power_parity": {"en": "PPP-based local purchasing-power index (0–100), comparing what income can actually buy after local prices. Higher values reduce modeled economic pressure and raise safety.", "zh": "基于购买力平价的本地实际购买力指数（0–100），反映收入在当地物价下真正可以买到多少。越高表示经济压力越低，安全得分越高。"},
    "crime_rate": {"en": "Recorded cases per 1,000 residents (range 5–120). Higher values increase danger and lower the safety score.", "zh": "每千名居民的记录案件数（范围 5–120）。数值越高，危险程度越高，安全得分越低。"},
    "unemployment_rate": {"en": "Unemployed share of the workforce (2–20%). Higher values are treated as greater socioeconomic risk.", "zh": "劳动力中的失业比例（2–20%）。数值越高，社会经济风险越高。"},
    "income_per_capita": {"en": "Average annual income per resident (CAD-equivalent 5,000–100,000). Higher nominal income raises the base score; value of money can then raise or lower its real contribution.", "zh": "居民平均年收入（5,000–100,000 加元等值）。名义收入越高，基础得分越高；货币购买力随后可上调或下调其实际贡献。"},
    "population_density": {"en": "Residents per km² (100–20,000). In this model, higher density increases crowding-related risk.", "zh": "每平方公里居民数（100–20,000）。本模型中，密度越高，拥挤相关风险越高。"},
    "night_lighting": {"en": "Street-light coverage and quality index (0–100). Higher values reduce modeled nighttime risk.", "zh": "街道照明覆盖与质量指数（0–100）。数值越高，模型中的夜间风险越低。"},
    "police_count": {"en": "Police officers per 10,000 residents (5–60). Higher presence raises the modeled safety score.", "zh": "每万名居民的警察数量（5–60）。警力越充足，模型中的安全得分越高。"},
    "education_level": {"en": "Composite education attainment index (0–100). Higher values raise the modeled safety score.", "zh": "教育程度综合指数（0–100）。数值越高，模型中的安全得分越高。"},
    "housing_price": {"en": "Typical price per m² (USD 500–20,000), used here as a proxy for neighborhood investment. Higher values raise the score but do not prove safety.", "zh": "典型每平方米房价（500–20,000 美元），作为社区投入的替代指标。较高值会提高得分，但不能单独证明安全。"},
    "tourist_count": {"en": "Annual visitors in units of 10,000 (1–3,000), used as a proxy for public activity and services. Higher values raise the score but may also bring crowded-area risks.", "zh": "年游客量，以万人计（1–3,000），作为公共活力和服务的替代指标。较高值会提高得分，但人流密集区仍有风险。"},
    "public_transport": {"en": "Transit availability and convenience index (0–100). Higher values improve mobility and raise the modeled safety score.", "zh": "公共交通覆盖和便利性指数（0–100）。数值越高，出行条件越好，模型中的安全得分越高。"},
    "environmental_state": {"en": "Air, water, contamination, and industrial-impact quality index (0–100). Lower values indicate a separate health/environment concern but do not change the crime-safety index.", "zh": "空气、水质、污染及工业影响综合指数（0–100）。较低值表示独立的健康与环境隐患，但不改变治安指数。"},
    "air_quality": {"en": "Air cleanliness and pollution exposure index (0–100). Higher is better; used only in the separate environmental score.", "zh": "空气清洁度与污染暴露指数（0–100）。越高越好，仅计入独立环境评分。"},
    "water_quality": {"en": "Drinking and surface-water quality index (0–100). Higher is better; used only in the separate environmental score.", "zh": "饮用水与地表水质量指数（0–100）。越高越好，仅计入独立环境评分。"},
    "green_space": {"en": "Green-space coverage and accessibility index (0–100). Higher is better; used only in the separate environmental score.", "zh": "绿色空间覆盖率与可达性指数（0–100）。越高越好，仅计入独立环境评分。"},
    "noise_environment": {"en": "Quietness and protection from harmful noise index (0–100). Higher is better; used only in the separate environmental score.", "zh": "安静程度与噪声防护指数（0–100）。越高越好，仅计入独立环境评分。"},
    "climate_resilience": {"en": "Preparedness for heat, flooding, storms, and other climate hazards (0–100). Higher is better; used only in the separate environmental score.", "zh": "应对高温、洪水、风暴等气候风险的韧性指数（0–100）。越高越好，仅计入独立环境评分。"},
    "value_of_money": {"en": "Local purchasing power of a fixed income benchmark (0–100). Higher values mean income covers more necessities; this scales the income-per-capita safety score and is not counted twice.", "zh": "固定收入基准在当地的购买力指数（0–100）。越高表示收入可覆盖更多生活必需品；它用于调整人均收入安全得分，不重复计分。"},
    "social_media_reputation": {"en": "Public safety sentiment from social posts and reviews (0–100). Higher values mean safer perceived experience; this is perception data, not verified crime statistics.", "zh": "根据公开社交帖子和评论汇总的安全口碑指数（0–100）。越高表示公众感知越安全；它是主观口碑，不是经核实的犯罪统计。"},
}

HELP_LOCALIZED = {
    "ja": {
        "safety_crime_rate": "暴力、強盗、暴行、窃盗など人身・財産に関する事件数（住民1,000人当たり2～100）。値が高いほど旅行者の安全スコアが下がります。",
        "other_crime_rate": "通常旅行者を直接対象としない行政・規制上などの犯罪（1,000人当たり1～80）。背景情報のみで安全指数には含めません。",
        "purchasing_power_parity": "現地価格を考慮した購買力平価指数（0～100）。高いほど実質的な経済圧力が低く、安全スコアが上がります。",
        "social_media_reputation": "公開投稿やレビューによる安全評判指数（0～100）。高いほど安全と感じられていますが、検証済み犯罪統計ではありません。",
        "crime_rate": "住民1,000人当たりの記録犯罪件数（5～120）。値が高いほど危険度が上がり、安全スコアが下がります。",
        "unemployment_rate": "労働人口の失業割合（2～20%）。値が高いほど社会経済的リスクが高いと評価します。",
        "income_per_capita": "住民1人当たりの平均年収（5,000～100,000カナダドル相当）。名目所得の基礎スコアを購買力が上下に調整します。",
        "population_density": "1 km²当たりの住民数（100～20,000）。このモデルでは高密度ほど混雑関連リスクが上がります。",
        "night_lighting": "街灯の範囲と品質の指数（0～100）。値が高いほど夜間リスクが下がります。",
        "police_count": "住民1万人当たりの警察官数（5～60）。値が高いほど安全スコアが上がります。",
        "education_level": "教育達成度の総合指数（0～100）。値が高いほど安全スコアが上がります。",
        "housing_price": "1 m²当たりの代表的住宅価格（500～20,000米ドル）。地域投資の代替指標で、高いほど得点は上がりますが安全を保証しません。",
        "tourist_count": "年間観光客数（1万単位、1～3,000）。公共活動とサービスの代替指標ですが、混雑によるリスクもあります。",
        "public_transport": "公共交通の利用可能性と利便性指数（0～100）。値が高いほど移動性と安全スコアが上がります。",
        "environmental_state": "大気、水質、汚染、産業影響の環境指数（0～100）。低い値は健康・環境上の懸念として別途表示され、治安指数は変えません。",
        "value_of_money": "固定収入の現地購買力指数（0～100）。高いほど必需品を多く賄え、一人当たり所得スコアを調整します。二重計上はしません。",
    },
    "fr": {
        "safety_crime_rate": "Violences, vols, agressions et atteintes aux biens pour 1 000 habitants (2–100). Une valeur élevée réduit directement la sécurité des visiteurs.",
        "other_crime_rate": "Infractions administratives, réglementaires et autres rarement dirigées contre les visiteurs (1–80 pour 1 000). Contexte uniquement, hors indice.",
        "purchasing_power_parity": "Indice local fondé sur la parité de pouvoir d’achat (0–100). Une valeur élevée signifie moins de pression économique réelle et augmente le score.",
        "social_media_reputation": "Sentiment de sécurité issu de publications et avis publics (0–100). Une valeur élevée indique une perception plus sûre, pas des statistiques vérifiées.",
        "crime_rate": "Infractions enregistrées pour 1 000 habitants (5–120). Une valeur élevée augmente le danger et réduit le score de sécurité.",
        "unemployment_rate": "Part de la population active au chômage (2–20 %). Une valeur élevée représente un risque socio-économique accru.",
        "income_per_capita": "Revenu annuel moyen par habitant (équivalent 5 000–100 000 CAD). Le pouvoir d’achat ajuste ensuite la contribution du revenu nominal.",
        "population_density": "Habitants par km² (100–20 000). Dans ce modèle, une forte densité accroît les risques liés à la foule.",
        "night_lighting": "Indice de couverture et de qualité de l’éclairage (0–100). Une valeur élevée réduit le risque nocturne.",
        "police_count": "Policiers pour 10 000 habitants (5–60). Une présence élevée augmente le score de sécurité.",
        "education_level": "Indice composite du niveau d’études (0–100). Une valeur élevée augmente le score de sécurité.",
        "housing_price": "Prix type au m² (500–20 000 USD), indicateur indirect de l’investissement local. Un prix élevé augmente le score sans garantir la sécurité.",
        "tourist_count": "Visiteurs annuels par unités de 10 000 (1–3 000), indicateur de l’activité et des services. La foule peut aussi créer des risques.",
        "public_transport": "Indice de disponibilité et de commodité des transports (0–100). Une valeur élevée améliore la mobilité et le score.",
        "environmental_state": "Indice de qualité de l’air, de l’eau, de la pollution et de l’impact industriel (0–100). Une valeur faible signale un enjeu distinct sans modifier l’indice de sûreté.",
        "value_of_money": "Pouvoir d’achat local d’un revenu fixe (0–100). Une valeur élevée signifie que le revenu couvre davantage de besoins et ajuste le score du revenu sans double comptage.",
    },
    "es": {
        "safety_crime_rate": "Violencia, robos, agresiones y delitos patrimoniales por cada 1.000 habitantes (2–100). Un valor mayor reduce directamente la seguridad del visitante.",
        "other_crime_rate": "Delitos administrativos, regulatorios y otros que normalmente no se dirigen al visitante (1–80 por 1.000). Solo contexto, fuera del índice.",
        "purchasing_power_parity": "Índice local basado en la paridad de poder adquisitivo (0–100). Un valor mayor implica menor presión económica real y aumenta la puntuación.",
        "social_media_reputation": "Percepción de seguridad en publicaciones y reseñas públicas (0–100). Un valor mayor indica mejor percepción, no estadísticas verificadas.",
        "crime_rate": "Delitos registrados por cada 1.000 habitantes (5–120). Un valor mayor aumenta el peligro y reduce la puntuación de seguridad.",
        "unemployment_rate": "Porcentaje de la población activa desempleada (2–20 %). Un valor mayor representa más riesgo socioeconómico.",
        "income_per_capita": "Ingreso anual medio por habitante (equivalente a 5.000–100.000 CAD). El poder adquisitivo ajusta después la contribución del ingreso nominal.",
        "population_density": "Habitantes por km² (100–20.000). En este modelo, una densidad mayor aumenta los riesgos por aglomeración.",
        "night_lighting": "Índice de cobertura y calidad del alumbrado (0–100). Un valor mayor reduce el riesgo nocturno.",
        "police_count": "Agentes por cada 10.000 habitantes (5–60). Una presencia mayor aumenta la puntuación de seguridad.",
        "education_level": "Índice compuesto de nivel educativo (0–100). Un valor mayor aumenta la puntuación de seguridad.",
        "housing_price": "Precio típico por m² (500–20.000 USD), indicador indirecto de inversión vecinal. Un precio mayor sube la puntuación, pero no garantiza seguridad.",
        "tourist_count": "Visitantes anuales en unidades de 10.000 (1–3.000), indicador de actividad y servicios. Las multitudes también pueden crear riesgos.",
        "public_transport": "Índice de disponibilidad y comodidad del transporte (0–100). Un valor mayor mejora la movilidad y la puntuación.",
        "environmental_state": "Índice de aire, agua, contaminación e impacto industrial (0–100). Un valor bajo señala una preocupación aparte sin cambiar el índice de seguridad ciudadana.",
        "value_of_money": "Poder adquisitivo local de un ingreso fijo (0–100). Un valor mayor cubre más necesidades y ajusta la puntuación de ingreso sin contarse dos veces.",
    },
    "de": {
        "safety_crime_rate": "Gewalt, Raub, Übergriffe, Diebstahl und Eigentumsdelikte je 1.000 Einwohner (2–100). Höhere Werte senken direkt die Besuchersicherheit.",
        "other_crime_rate": "Verwaltungs-, Regulierungs- und andere Delikte ohne üblichen Besucherbezug (1–80 je 1.000). Nur Kontext, nicht im Index.",
        "purchasing_power_parity": "Lokaler Kaufkraftparitätsindex unter Berücksichtigung der Preise (0–100). Höhere Werte bedeuten weniger realen wirtschaftlichen Druck.",
        "social_media_reputation": "Sicherheitsempfinden aus öffentlichen Posts und Bewertungen (0–100). Höhere Werte bedeuten bessere Wahrnehmung, nicht geprüfte Kriminalstatistik.",
        "crime_rate": "Erfasste Straftaten je 1.000 Einwohner (5–120). Höhere Werte erhöhen die Gefahr und senken den Sicherheitswert.",
        "unemployment_rate": "Anteil der Erwerbsbevölkerung ohne Arbeit (2–20 %). Höhere Werte gelten als größeres sozioökonomisches Risiko.",
        "income_per_capita": "Durchschnittliches Jahreseinkommen je Einwohner (5.000–100.000 CAD-Äquivalent). Die Kaufkraft passt danach den Beitrag des Nominaleinkommens an.",
        "population_density": "Einwohner je km² (100–20.000). In diesem Modell erhöht eine höhere Dichte Risiken durch Gedränge.",
        "night_lighting": "Index für Abdeckung und Qualität der Straßenbeleuchtung (0–100). Höhere Werte senken das nächtliche Risiko.",
        "police_count": "Polizeikräfte je 10.000 Einwohner (5–60). Eine höhere Präsenz erhöht den Sicherheitswert.",
        "education_level": "Zusammengesetzter Bildungsindex (0–100). Höhere Werte erhöhen den Sicherheitswert.",
        "housing_price": "Typischer Preis je m² (500–20.000 USD) als indirekter Indikator für Investitionen. Höhere Werte erhöhen den Wert, garantieren aber keine Sicherheit.",
        "tourist_count": "Jährliche Besucher in Einheiten von 10.000 (1–3.000) als Indikator für Aktivität und Dienste. Menschenmengen können auch Risiken schaffen.",
        "public_transport": "Index für Verfügbarkeit und Komfort des Nahverkehrs (0–100). Höhere Werte verbessern Mobilität und Sicherheitswert.",
        "environmental_state": "Index für Luft, Wasser, Verschmutzung und Industrieauswirkungen (0–100). Niedrige Werte zeigen ein separates Umweltproblem, ändern aber nicht den Sicherheitsindex.",
        "value_of_money": "Lokale Kaufkraft eines festen Einkommens (0–100). Höhere Werte decken mehr Grundbedarf und passen den Einkommenswert ohne Doppelzählung an.",
    },
}

LEVELS = {
    "very_safe": {"zh": "非常安全", "en": "Very safe", "ja": "非常に安全", "fr": "Très sûr", "es": "Muy seguro", "de": "Sehr sicher"},
    "safe": {"zh": "较安全", "en": "Safe", "ja": "安全", "fr": "Sûr", "es": "Seguro", "de": "Sicher"},
    "moderate": {"zh": "一般", "en": "Moderate", "ja": "普通", "fr": "Modéré", "es": "Moderado", "de": "Mäßig"},
    "high_risk": {"zh": "风险较高", "en": "Higher risk", "ja": "リスク高め", "fr": "Risque élevé", "es": "Riesgo elevado", "de": "Erhöhtes Risiko"},
    "dangerous": {"zh": "危险", "en": "Dangerous", "ja": "危険", "fr": "Dangereux", "es": "Peligroso", "de": "Gefährlich"},
}

LOCATION_NAMES = {
    "CN-BJ": ("中国 · 北京", "China · Beijing", "中国 · 北京", "Chine · Pékin", "China · Pekín", "China · Peking"),
    "CN-SH": ("中国 · 上海", "China · Shanghai", "中国 · 上海", "Chine · Shanghai", "China · Shanghái", "China · Shanghai"),
    "CN-GZ": ("中国 · 广州", "China · Guangzhou", "中国 · 広州", "Chine · Canton", "China · Cantón", "China · Guangzhou"),
    "CN-SZ": ("中国 · 深圳", "China · Shenzhen", "中国 · 深圳", "Chine · Shenzhen", "China · Shenzhen", "China · Shenzhen"),
    "CA-TOR": ("加拿大 · 多伦多", "Canada · Toronto", "カナダ · トロント", "Canada · Toronto", "Canadá · Toronto", "Kanada · Toronto"),
    "CA-VAN": ("加拿大 · 温哥华", "Canada · Vancouver", "カナダ · バンクーバー", "Canada · Vancouver", "Canadá · Vancouver", "Kanada · Vancouver"),
    "CA-MTL": ("加拿大 · 蒙特利尔", "Canada · Montreal", "カナダ · モントリオール", "Canada · Montréal", "Canadá · Montreal", "Kanada · Montreal"),
    "US-NYC": ("美国 · 纽约", "United States · New York", "米国 · ニューヨーク", "États-Unis · New York", "Estados Unidos · Nueva York", "USA · New York"),
    "US-SFO": ("美国 · 旧金山", "United States · San Francisco", "米国 · サンフランシスコ", "États-Unis · San Francisco", "Estados Unidos · San Francisco", "USA · San Francisco"),
    "US-CHI": ("美国 · 芝加哥", "United States · Chicago", "米国 · シカゴ", "États-Unis · Chicago", "Estados Unidos · Chicago", "USA · Chicago"),
    "GB-LON": ("英国 · 伦敦", "United Kingdom · London", "英国 · ロンドン", "Royaume-Uni · Londres", "Reino Unido · Londres", "Vereinigtes Königreich · London"),
    "FR-PAR": ("法国 · 巴黎", "France · Paris", "フランス · パリ", "France · Paris", "Francia · París", "Frankreich · Paris"),
    "JP-TYO": ("日本 · 东京", "Japan · Tokyo", "日本 · 東京", "Japon · Tokyo", "Japón · Tokio", "Japan · Tokio"),
    "SG-SIN": ("新加坡 · 新加坡", "Singapore · Singapore", "シンガポール", "Singapour", "Singapur", "Singapur"),
    "AU-SYD": ("澳大利亚 · 悉尼", "Australia · Sydney", "オーストラリア · シドニー", "Australie · Sydney", "Australia · Sídney", "Australien · Sydney"),
}

_ORDER = {code: index for index, code in enumerate(LANGUAGES)}


def tr(key: str, language: str, **values: object) -> str:
    """Translate a UI key and interpolate named values."""

    return UI[key].get(language, UI[key]["en"]).format(**values)


def metric_label(key: str, language: str) -> str:
    """Return the localized metric label."""

    return METRIC_TEXT[key][_ORDER.get(language, 1)]


def metric_unit(key: str, language: str) -> str:
    """Return the localized unit, falling back to the English form."""

    return METRIC_TEXT[key][6 if language == "zh" else 7]


def metric_help(key: str, language: str) -> str:
    """Return a localized explanation of a factor's meaning and direction."""

    return HELP_LOCALIZED.get(language, {}).get(key, HELP[key].get(language, HELP[key]["en"]))


def level_label(level: str, language: str) -> str:
    """Return a localized safety level."""

    return LEVELS[level].get(language, LEVELS[level]["en"])


def location_name(code: str, language: str) -> str:
    """Return the localized country and city name for a city code."""

    names = LOCATION_NAMES.get(code)
    return names[_ORDER.get(language, 1)] if names else code


def location_part(code: str, language: str, part: int) -> str:
    """Return only the country (0) or city (1) part of a localized location."""

    pieces = [piece.strip() for piece in location_name(code, language).split("·")]
    return pieces[min(part, len(pieces) - 1)]
