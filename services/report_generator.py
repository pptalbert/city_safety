"""Rule-based localized safety report generation."""

from config import METRICS
from models import AnalysisResult
from utils.i18n import location_name, metric_label


SUMMARIES = {
    "zh": ("整体安全风险突出", "整体存在较高安全风险", "整体安全状况一般", "整体安全状况较好", "整体安全状况非常好"),
    "en": ("has significant overall safety risks", "has elevated overall safety risks", "has a moderate overall safety profile", "has a good overall safety profile", "has an excellent overall safety profile"),
    "ja": ("は全体的な安全リスクが顕著です", "は全体的な安全リスクが高めです", "の全体的な安全状況は標準的です", "の全体的な安全状況は良好です", "の全体的な安全状況は非常に良好です"),
    "fr": ("présente des risques de sécurité globaux importants", "présente des risques de sécurité globaux élevés", "présente un niveau de sécurité global moyen", "présente un bon niveau de sécurité global", "présente un excellent niveau de sécurité global"),
    "es": ("presenta riesgos generales de seguridad importantes", "presenta riesgos generales de seguridad elevados", "presenta un nivel general de seguridad moderado", "presenta un buen nivel general de seguridad", "presenta un nivel general de seguridad excelente"),
    "de": ("weist erhebliche allgemeine Sicherheitsrisiken auf", "weist erhöhte allgemeine Sicherheitsrisiken auf", "weist ein mittleres allgemeines Sicherheitsniveau auf", "weist ein gutes allgemeines Sicherheitsniveau auf", "weist ein ausgezeichnetes allgemeines Sicherheitsniveau auf"),
}

ADVICE = {
    "safety_crime_rate": ("避开人身与财产案件高发区域，并关注当地治安通报", "avoid areas with high rates of violence or property crime and monitor local safety notices", "人身・財産犯罪の多発地域を避け、現地の安全情報を確認してください", "évitez les zones à forte criminalité contre les personnes ou les biens et consultez les alertes locales", "evite zonas con muchos delitos contra personas o bienes y consulte los avisos locales", "meiden Sie Gebiete mit vielen Personen- oder Eigentumsdelikten und beachten Sie lokale Hinweise"),
    "purchasing_power_parity": ("结合当地物价评估预算，避免因实际购买力不足进入高风险居住或出行环境", "assess the budget against local prices to avoid higher-risk accommodation or travel choices caused by weak real purchasing power", "現地物価に照らして予算を確認し、実質購買力不足による高リスクな滞在・移動を避けてください", "évaluez le budget selon les prix locaux afin d’éviter des choix d’hébergement ou de déplacement plus risqués", "evalúe el presupuesto frente a los precios locales para evitar opciones de alojamiento o transporte de mayor riesgo", "bewerten Sie das Budget anhand lokaler Preise, um riskantere Unterkunfts- oder Reiseentscheidungen zu vermeiden"),
    "social_media_reputation": ("交叉核验近期游客评论与官方通报，不要仅依赖网络口碑", "cross-check recent visitor reviews with official notices rather than relying on online sentiment alone", "最近の旅行者レビューと公式情報を照合し、オンライン評判だけに頼らないでください", "recoupez les avis récents avec les alertes officielles au lieu de vous fier uniquement au sentiment en ligne", "contraste reseñas recientes con avisos oficiales y no dependa solo de la percepción en línea", "gleichen Sie aktuelle Besucherbewertungen mit offiziellen Hinweisen ab, statt nur der Online-Stimmung zu vertrauen"),
    "crime_rate": ("避开案件高发区域，并关注当地治安通报", "avoid high-crime areas and monitor local safety notices", "犯罪多発地域を避け、現地の安全情報を確認してください", "évitez les zones à forte criminalité et consultez les alertes locales", "evite las zonas con alta delincuencia y consulte los avisos locales", "meiden Sie Gebiete mit hoher Kriminalität und beachten Sie lokale Sicherheitshinweise"),
    "unemployment_rate": ("关注经济压力可能带来的社区风险", "consider community risks associated with economic pressure", "経済的圧力に伴う地域リスクに注意してください", "tenez compte des risques communautaires liés aux pressions économiques", "tenga en cuenta los riesgos comunitarios asociados a la presión económica", "berücksichtigen Sie Gemeinschaftsrisiken durch wirtschaftlichen Druck"),
    "income_per_capita": ("优先选择公共服务更完善的区域", "favor areas with stronger public services", "公共サービスが充実した地域を優先してください", "privilégiez les secteurs dotés de meilleurs services publics", "priorice zonas con mejores servicios públicos", "bevorzugen Sie Gebiete mit besseren öffentlichen Dienstleistungen"),
    "population_density": ("在人群拥挤的场所注意个人财物", "protect personal belongings in crowded places", "混雑した場所では所持品に注意してください", "surveillez vos effets personnels dans les lieux très fréquentés", "vigile sus pertenencias en lugares concurridos", "achten Sie an belebten Orten auf persönliche Gegenstände"),
    "night_lighting": ("夜间结伴出行并选择照明良好的道路", "travel with others at night and choose well-lit routes", "夜間は複数人で、明るい道を選んでください", "déplacez-vous accompagné la nuit et choisissez des itinéraires éclairés", "viaje acompañado de noche y elija rutas bien iluminadas", "gehen Sie nachts in Begleitung und nutzen Sie gut beleuchtete Wege"),
    "police_count": ("提前了解附近警务站和紧急联系方式", "identify nearby police stations and emergency contacts", "近くの警察署と緊急連絡先を確認してください", "repérez les postes de police proches et les contacts d’urgence", "localice comisarías cercanas y contactos de emergencia", "informieren Sie sich über Polizeistationen und Notfallkontakte"),
    "education_level": ("关注不同社区间的公共资源差异", "consider differences in public resources between neighborhoods", "地域ごとの公共資源の差に注意してください", "tenez compte des écarts de ressources publiques entre quartiers", "considere las diferencias de recursos públicos entre barrios", "beachten Sie Unterschiede bei öffentlichen Ressourcen zwischen Vierteln"),
    "housing_price": ("结合居住成本评估社区配套与安全性", "assess neighborhood services and safety alongside housing costs", "住居費と地域サービス、安全性を併せて評価してください", "évaluez les services et la sécurité du quartier avec le coût du logement", "evalúe los servicios y la seguridad del barrio junto al coste de vivienda", "bewerten Sie Angebote und Sicherheit zusammen mit den Wohnkosten"),
    "tourist_count": ("在人流密集景点防范盗窃和诈骗", "watch for theft and scams in crowded attractions", "混雑した観光地では盗難や詐欺に注意してください", "restez vigilant face aux vols et arnaques dans les sites fréquentés", "tenga cuidado con robos y estafas en atracciones concurridas", "achten Sie an belebten Sehenswürdigkeiten auf Diebstahl und Betrug"),
    "public_transport": ("提前规划夜间返程和备用交通方式", "plan nighttime return trips and backup transport in advance", "夜間の帰路と代替交通手段を事前に計画してください", "planifiez à l’avance le retour nocturne et un transport de secours", "planifique con antelación el regreso nocturno y transporte alternativo", "planen Sie nächtliche Rückwege und Alternativen im Voraus"),
}

LANGUAGE_ORDER = {"zh": 0, "en": 1, "ja": 2, "fr": 3, "es": 4, "de": 5}


class ReportGenerator:
    """Generate a concise, explainable report from metric scores."""

    @staticmethod
    def generate(result: AnalysisResult, language: str = "zh") -> str:
        """Describe strengths, weaknesses, and a practical recommendation."""

        scoring_metrics = [
            item for item in result.metrics if METRICS[item.key].contributes_to_overall
        ]
        ordered = sorted(scoring_metrics, key=lambda item: item.score)
        weakest = ordered[0]
        strongest = ordered[-1]
        band = 4 if result.overall_score >= 90 else 3 if result.overall_score >= 70 else 2 if result.overall_score >= 50 else 1 if result.overall_score >= 30 else 0
        index = LANGUAGE_ORDER.get(language, 1)
        place = (
            location_name(result.city.code, language)
            if location_name(result.city.code, language) != result.city.code
            else f"{result.city.country} · {result.city.name}"
        )
        summary = SUMMARIES.get(language, SUMMARIES["en"])[band]
        strong = metric_label(strongest.key, language)
        weak = metric_label(weakest.key, language)
        advice = ADVICE[weakest.key][index]
        templates = {
            "zh": f"{place}{summary}。{strong}表现相对突出，但{weak}是当前短板；建议{advice}。",
            "en": f"{place} {summary}. {strong} is a relative strength, while {weak} is the main weakness; we recommend that you {advice}.",
            "ja": f"{place}{summary}。{strong}は比較的良好ですが、{weak}が主な弱点です。{advice}。",
            "fr": f"{place} {summary}. {strong} constitue un point fort, tandis que {weak} est la principale faiblesse ; nous vous conseillons de {advice}.",
            "es": f"{place} {summary}. {strong} es un punto fuerte, mientras que {weak} es la principal debilidad; recomendamos que {advice}.",
            "de": f"{place} {summary}. {strong} ist eine relative Stärke, während {weak} die größte Schwäche darstellt; wir empfehlen: {advice}.",
        }
        report = templates.get(language, templates["en"])
        indexed = {item.key: item for item in result.metrics}

        environmental_metrics = [
            item for item in result.metrics
            if METRICS[item.key].contributes_to_environment and item.weight > 0
        ]
        if environmental_metrics and result.environmental_score is not None:
            severity = "concern" if result.environmental_score < 50 else "positive"
            weakest_environment = min(environmental_metrics, key=lambda item: item.score)
            environment_name = metric_label(weakest_environment.key, language)
            environmental_notes = {
                "zh": {
                    "concern": "独立环境评分为 {score}/100，其中{factor}最值得关注；环境权重仅影响该评分，未计入总体治安指数。",
                    "positive": "独立环境评分为 {score}/100，整体表现较好；{factor}相对较弱。环境权重未影响总体治安指数。",
                },
                "en": {
                    "concern": "The separate environmental score is {score}/100, with {factor} needing the most attention. Environmental weights affect only this score, not the overall safety index.",
                    "positive": "The separate environmental score is {score}/100 and is generally positive; {factor} is the relative weakness. Environmental weights did not affect the overall safety index.",
                },
                "ja": {
                    "concern": "別の懸念点：汚染または重工業の影響に注意が必要です。この項目は総合治安指数には含まれません。",
                    "positive": "環境状態に重大な追加懸念はありません。この項目は別途報告され、総合治安指数には含まれません。",
                },
                "fr": {
                    "concern": "Enjeu distinct : l’état environnemental indique une pollution ou un impact industriel à surveiller ; il n’a pas modifié l’indice global de sûreté.",
                    "positive": "L’état environnemental ne révèle pas d’enjeu supplémentaire majeur ; il est présenté séparément et n’a pas modifié l’indice global.",
                },
                "es": {
                    "concern": "Preocupación aparte: el estado ambiental indica contaminación o impacto industrial que merece atención; no modificó el índice general de seguridad.",
                    "positive": "El estado ambiental no muestra una preocupación adicional importante; se informa aparte y no modificó el índice general.",
                },
                "de": {
                    "concern": "Separater Hinweis: Der Umweltzustand deutet auf beachtenswerte Verschmutzung oder Industrieauswirkungen hin; der Gesamtsicherheitsindex blieb unverändert.",
                    "positive": "Der Umweltzustand zeigt keine größeren zusätzlichen Bedenken; er wird separat ausgewiesen und änderte den Gesamtindex nicht.",
                },
            }
            note = environmental_notes.get(
                language, environmental_notes["en"]
            )[severity]
            report += " " + note.format(
                score=f"{result.environmental_score:.1f}", factor=environment_name
            )

        other_crime = indexed.get("other_crime_rate")
        if other_crime is not None:
            other_notes = {
                "zh": "其他犯罪率仅作为城市背景信息展示，未计入游客人身与财产安全总分。",
                "en": "The other-crime rate is shown only as city context and was excluded from the visitor personal/property safety score.",
                "ja": "その他の犯罪率は都市の背景情報のみで、旅行者の人身・財産安全スコアには含まれません。",
                "fr": "Le taux des autres infractions sert uniquement de contexte urbain et n’entre pas dans le score de sécurité personnelle et matérielle des visiteurs.",
                "es": "La tasa de otros delitos se muestra solo como contexto urbano y no entra en la puntuación de seguridad personal y patrimonial del visitante.",
                "de": "Die sonstige Kriminalitätsrate dient nur als Stadtkontext und fließt nicht in die Personen-/Eigentumssicherheit von Besuchern ein.",
            }
            report += " " + other_notes.get(language, other_notes["en"])
        return report
