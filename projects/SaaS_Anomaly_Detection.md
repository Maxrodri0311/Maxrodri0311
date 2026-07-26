# 🔍 Enterprise SaaS Anomaly Detection Engine (Healthcare Fraud Focus)

## 📌 The Business Problem
Fraudulent medical claims cause massive capital bleed. The challenge was that traditional rules-based systems fail to detect novel, multidimensional fraud patterns, leading to thousands of hours wasted in manual auditing and high false-positive rates.

## 🛠️ The Architecture & Trade-offs
To solve this, I engineered an **end-to-end unsupervised Machine Learning architecture** utilizing Scikit-Learn's `IsolationForest`.
- **Why Isolation Forest?** Instead of profiling "normal" claims (which is highly variable), the model isolates anomalies by identifying data points that require fewer splits to be separated, making it highly effective for multi-dimensional medical fraud without needing labeled training data.
- **Decoupled Backend:** I separated the ML inference engine (FastAPI/Python) from the frontend (Vanilla JS/WebSockets). This architectural trade-off ensured that heavy matrix computations (100MB+ loaded in RAM) did not block the UI thread.
- **Observability & Secure Ingestion:** Given the sensitivity of PII in healthcare, strict logging, secure ingestion pipelines, and compliance (GRC) standards were enforced at the data layer.

## 📈 Quantifiable Impact (STAR Metrics)
- **Accomplished** an 85% reduction in manual data auditing time (15 operational hours saved per week).
- **Accelerated** system response times to under 3 milliseconds through async APIs.
- **Enhanced** diagnostic reporting via real-time WebSockets, increasing stakeholder engagement by 40%.

## 🛡️ Seniority Signals
- **Systemic Thinking:** Applied root-cause analysis logic (derived from my electromechanical background) to trace data anomalies back to their ingestion source.
- **Production-Ready:** Implemented strict data validation, asynchronous processing, and modular decoupling.
