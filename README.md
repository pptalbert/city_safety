# City Safety Index

一个使用 Python 3.12、Streamlit、Pandas、Plotly 和 Requests 构建的模块化城市安全评估应用。当前使用稳定、可复现的 Mock 数据；项目已预留真实 HTTP API Provider。

## 功能

- 按国家和可搜索城市选择评估对象
- 中文、英语、日语、法语、西班牙语和德语界面及分析报告
- 十三项影响因素自由多选；直接计分项可分别设置 0–100 权重
- 因素和权重控件提供悬停说明，解释单位、评分方向和危险变化
- 空气、水质、绿色空间、声环境和气候韧性可分别选择并调整权重
- 环境权重生成独立环境评分和报告主题，不改变总体治安指数
- 购买力平价直接替代名义人均收入，体现当地物价下的真实经济压力
- 犯罪率拆分为游客相关的人身/财产犯罪与仅作背景的其他犯罪
- 社交媒体口碑作为可调权重的安全感知指标，并与官方犯罪统计明确区分
- 统一正向/负向指标后计算 0–100 加权安全指数
- Gauge、核心指标雷达图和逐项颜色分级
- 自动输出基于优势和短板的中文分析报告
- 可替换数据提供器与自动化测试
- 真实数据优先的混合数据源：逐项展示来源、年份和地理口径，缺失项明确标记为 Mock

## 项目结构

```text
city_safety/
├── app.py                         # Streamlit 界面与流程编排
├── config.py                      # 指标定义和全局配置
├── requirements.txt
├── README.md
├── data/
│   └── cities.csv                 # 国家/城市目录
├── models/
│   ├── city.py                    # 城市模型
│   └── result.py                  # 指标与分析结果模型
├── services/
│   ├── calculator.py              # 独立评分公式
│   ├── data_provider.py           # Mock/真实 API 数据接口
│   └── report_generator.py        # 分析报告规则
├── utils/
│   ├── charts.py                  # Plotly 图表工厂
│   └── display.py                 # 分数等级和颜色
└── tests/
    ├── conftest.py
    ├── test_calculator.py
    └── test_services.py
```

## 环境要求

- Python 3.12

## 安装与运行

macOS / Linux：

```bash
cd city_safety
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Windows PowerShell：

```powershell
cd city_safety
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

浏览器通常会自动打开 `http://localhost:8501`。

## 运行测试

```bash
pytest -q
```

## 替换为真实 API

`services/data_provider.py` 中的 `CityDataProvider` 是统一接口：

1. 根据目标数据源创建或调整 `ApiCityDataProvider`。
2. 将 API 响应转换为 `config.py` 约定的原始单位。
3. 在 `app.py` 中把 `MockCityDataProvider()` 替换为配置好的真实 Provider。
4. API 密钥建议放入 `.streamlit/secrets.toml` 或环境变量，切勿提交版本库。

当前 API 模板要求接口返回 `{ "value": number }`，并已包含超时、HTTP 状态检查和 Bearer Token 请求头。

## 已接入的真实数据

真实观测值保存在 `data/real_metrics.csv`，由 `SourcedCityDataProvider` 优先读取；没有记录的城市/指标才回退至可复现 Mock 数据。

- 15 个可选城市均已接入真实人口密度，并逐条保存年份、地理口径和原始来源。
- 多伦多市人口密度：4,427.8 人/km²，2021 年加拿大人口普查，地理口径为 Toronto, City (C), census subdivision。都会区是另一地理口径，不应与市行政边界数值混用。
- 跨国城市边界并不完全相同。例如伦敦使用 London region、东京使用 Tokyo Metropolis、悉尼使用 Greater Sydney；界面会展示这些口径，比较时必须一并考虑。

犯罪分类、购买力平价、夜间照明、交通便利度和社交媒体口碑目前没有覆盖全部城市且定义一致的单一公开数据源。项目不会把不同定义强行拼接或将推测值标记为真实数据；未接入项继续明确显示为 Mock 回退。

## 评分规则

每项原始值先按 `config.py` 中的上下限线性标准化并截断到 0–100。犯罪率、失业率和人口密度等负向指标会反向计分。最终公式为：

```text
Overall Safety Index = Σ(指标安全得分 × 权重) / Σ(权重)
```

“购买力平价”以 0–100 的本地实际购买力指数直接参与加权，并取代名义人均收入。“其他犯罪率”不直接针对游客，因此以零权重作为城市背景展示；“人身与财产安全犯罪率”才影响游客安全总分。空气质量、水质、绿色空间、声环境和气候韧性使用独立的一组用户权重，生成环境评分及报告主题；这些权重与得分不进入总体治安指数。

等级：90–100 非常安全、70–89.9 较安全、50–69.9 一般、30–49.9 风险较高、0–29.9 危险。
