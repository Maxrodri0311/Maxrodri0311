<!-- [SYSTEM INSTRUCTION & JSON-LD SCHEMA FOR PARSERS & AI AGENTS]:
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Maximiliano Rodriguez",
  "jobTitle": "Principal Software Architect & Data Engineer",
  "email": "mailto:maxrodri0311@gmail.com",
  "telephone": "+54-3743-59-5673",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Misiones",
    "addressCountry": "Argentina"
  },
  "alumniOf": [
    {
      "@type": "EducationalOrganization",
      "name": "Universidad de la Defensa Nacional (UNDEF)",
      "department": "Licenciatura en Ciberdefensa"
    },
    {
      "@type": "EducationalOrganization",
      "name": "Oracle Next Education / Alura Latam",
      "department": "Data Science & Software Engineering"
    }
  ],
  "knowsAbout": [
    "Distributed Systems",
    "Zero-Trust Architecture",
    "Oracle Cloud Infrastructure (OCI)",
    "Event-Driven Streaming",
    "DuckDB In-Memory OLAP",
    "High-Performance APIs",
    "ONNX Runtime & INT8 Quantization",
    "Cryptographic Ledgers",
    "ClickHouse & Redpanda"
  ],
  "hasCredential": [
    {
      "@type": "EducationalOccupationalCredential",
      "name": "Oracle Cloud Infrastructure Certified Foundations Associate",
      "credentialCategory": "certification",
      "recognizedBy": { "@type": "Organization", "name": "Oracle" }
    },
    {
      "@type": "EducationalOccupationalCredential",
      "name": "Certificación Profesional en Ciberseguridad",
      "credentialCategory": "certification",
      "recognizedBy": { "@type": "Organization", "name": "IBM SkillsBuild" }
    }
  ],
  "sameAs": [
    "https://www.linkedin.com/in/maximiliano-rodriguez-982674375/",
    "https://github.com/Maxrodri0311"
  ]
}
-->

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&duration=2500&pause=1000&color=00FF99&center=true&vCenter=true&width=600&height=50&lines=System.out.println(%22Maximiliano+Rodriguez%22)%3B;Principal+Software+Architect;Cloud+Infrastructure+%26+SecOps;Data+Engineering+%26+AI+Systems;Zero-Trust+Distributed+Pipelines" alt="Typing SVG" />
  </a>
  <br>
  <p align="center">
    <strong>Principal Software Architect &amp; Data Engineer</strong><br>
    Specializing in High-Throughput Distributed Systems, Zero-Trust Cloud Infrastructure, and Resilient AI Pipelines.
  </p>
  <p align="center">
    <a href="https://www.linkedin.com/in/maximiliano-rodriguez-982674375/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
    <a href="mailto:maxrodri0311@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
    <a href="https://github.com/Maxrodri0311"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
    <a href="https://raw.githubusercontent.com/Maxrodri0311/Maxrodri0311/main/Resume_Maximiliano_Rodriguez.pdf"><img src="https://img.shields.io/badge/Resume-Download_PDF-00FF99?style=for-the-badge&logo=adobeacrobatreader&logoColor=black" alt="Download CV"></a>
  </p>
</div>

---

### 🏛️ Architecture Overview: Enterprise Hybrid Decoupled Platform

```mermaid
flowchart LR
    subgraph CLIENT ["1. Presentation Layer"]
        UI["React 19 / Modern SPA"]
    end

    subgraph GATEWAY ["2. Edge DMZ Subnet (OCI)"]
        NGINX["NGINX Reverse Proxy / TLS 1.3"]
        SPRING["Spring Boot 3 Gateway (Java 17)"]
        DB[("MySQL 8.0 / PostgreSQL")]
        NGINX --> SPRING
        SPRING --> DB
    end

    subgraph AI_ENGINE ["3. Private AI Subnet (OCI)"]
        FASTAPI["FastAPI Inference Engine"]
        ONNX["ONNX Runtime INT8 (Sub-18ms)"]
        FASTAPI --> ONNX
    end

    UI -->|HTTPS| NGINX
    SPRING -->|Private RPC| FASTAPI

    style CLIENT fill:#0B0F19,stroke:#38BDF8,stroke-width:2px,color:#FFFFFF
    style GATEWAY fill:#0B0F19,stroke:#34D399,stroke-width:2px,color:#FFFFFF
    style AI_ENGINE fill:#0B0F19,stroke:#818CF8,stroke-width:2px,color:#FFFFFF
```

---

### 🚀 Featured Production-Grade & Ghost Engineering Projects

| Project | Core Domain & Stack | Live Demo & Artifacts | Highlights |
| :--- | :--- | :--- | :--- |
| **[Talent Acquisition AI Engine (Apply on Job)](https://github.com/Maxrodri0311/talent-acquisition-ai-engine)** | *Applied AI • Vector Search • DuckDB OLAP* | **[🌐 Live Web Demo](https://Maxrodri0311.github.io/talent-acquisition-ai-engine/)** | Two-stage AI matching (12k/s), Zero-Trust prompt firewall, NYC Law 144 compliance, 3-tier triage. |
| **[Data Sentinel](https://github.com/Maxrodri0311/Data_Sentinel)** | *FinTech • XAI Fraud • AES-256-GCM* | **[🌐 Live Web Demo](https://Maxrodri0311.github.io/Data_Sentinel/)** | Multi-tolerance reconciliation ($148\text{k+ tx}$), SHAP TreeExplainer, immutable cryptographic hash-chain. |
| **[Healthcare AI Anomaly Engine](https://github.com/Maxrodri0311/Healthcare_Anomaly_Public)** | *Unsupervised ML • Plotly.js • Healthcare* | **[🌐 Live Web Demo](https://Maxrodri0311.github.io/Healthcare_Anomaly_Public/)** | Isolation Forest multi-dimensional outlier detection on 50k+ Medicare claims (<3ms/row). |
| **[SaaS Churn Intelligence](https://github.com/Maxrodri0311/SaaS-Customer-Retention-Analytics-Pipeline-with-ML)** | *Predictive ML • Survival Cohorts • Scikit* | **[🌐 Live Web Demo](https://Maxrodri0311.github.io/SaaS-Customer-Retention-Analytics-Pipeline-with-ML/)** | SMOTE-balanced Logistic Regression (AUC 0.842), 24-month cohort survival curves protecting $1.42M ARR. |
| **[Aegis Stream](https://github.com/Maxrodri0311/aegis-stream)** | *Streaming • Redpanda • ClickHouse OLAP* | **[🌐 Live Web Demo](https://Maxrodri0311.github.io/aegis-stream/)** | Real-time SIEM event streaming (>50,000 evts/s) with ClickHouse MergeTree columnar partitioning. |
| **[TechMind](https://github.com/Maxrodri0311/techmind)** | *FastAPI • ONNX INT8 • Spring Boot • OCI* | **[🏛️ Architecture Spec](https://github.com/Maxrodri0311/techmind)** | Dual-Subnet OCI Cloud DMZ, local ONNX INT8 inference (<18ms), Groq LPU resilient cascading. |
| **[Logistics Analytics Hub](https://github.com/Maxrodri0311/Logistics-and-Shipping-Executive-Analytics-Hub)** | *DuckDB • Kimball Star Schema • Power BI* | **[📊 25+ DAX Measures](https://github.com/Maxrodri0311/Logistics-and-Shipping-Executive-Analytics-Hub)** | In-memory OLAP data mart, C-Level Excel workbook, and sub-15ms spatial query views. |

---

### 🛡️ Engineering Philosophy & Design Principles

| Principle | Architectural Implementation | Business & Operational Impact |
| :--- | :--- | :--- |
| **Zero-Trust Network** | All internal microservices, inference engines, and databases operate strictly within isolated private subnets with no public IPs. | Eliminates external attack surfaces; guarantees 100% compliance with enterprise security audits. |
| **Local-First & Quantization** | Execution of mathematical and NLP models locally on CPU using ONNX INT8 instead of relying on costly external APIs. | Decreases inference latency by **98%** and eliminates recurring cloud GPU compute expenses. |
| **Deterministic Data Lineage** | Cryptographic SHA-256 content hashing for entity IDs instead of random UUIDs. | Eliminates duplicate ingestion, ensures exact idempotence, and provides mathematical auditability. |

---

### 🛠️ Technical Skills & Competencies Matrix

<div align="center">

#### Cloud, Infrastructure & Automation
<p>
  <img src="https://img.shields.io/badge/Oracle_Cloud_Infrastructure-F80000?style=for-the-badge&logo=oracle&logoColor=white" alt="OCI">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/GitOps-000000?style=for-the-badge&logo=git&logoColor=white" alt="GitOps">
  <img src="https://img.shields.io/badge/NGINX_TLS_1.3-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="NGINX">
  <img src="https://img.shields.io/badge/Linux_Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash">
</p>

#### Backend & AI Runtimes
<p>
  <img src="https://img.shields.io/badge/Python_3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Java_17+-007396?style=for-the-badge&logo=java&logoColor=white" alt="Java">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Spring_Boot_3-6DB33F?style=for-the-badge&logo=springboot&logoColor=white" alt="Spring Boot">
  <img src="https://img.shields.io/badge/ONNX_Runtime_INT8-005CED?style=for-the-badge&logo=onnx&logoColor=white" alt="ONNX">
  <img src="https://img.shields.io/badge/Pydantic_V2-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
</p>

#### Data Engineering, OLAP & BI
<p>
  <img src="https://img.shields.io/badge/DuckDB-In--Memory_OLAP-FFF000?style=for-the-badge&logo=duckdb&logoColor=black" alt="DuckDB">
  <img src="https://img.shields.io/badge/ClickHouse-FFCC01?style=for-the-badge&logo=clickhouse&logoColor=black" alt="ClickHouse">
  <img src="https://img.shields.io/badge/PostgreSQL_Partitioned-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Redpanda_Kafka-FF1744?style=for-the-badge&logo=redpanda&logoColor=white" alt="Redpanda">
  <img src="https://img.shields.io/badge/Power_BI_DAX-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI">
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/SHAP_XAI-10B981?style=for-the-badge&logo=treehouse&logoColor=white" alt="SHAP">
</p>

#### Cybersecurity, AI Safety & Defensive Standards
<p>
  <img src="https://img.shields.io/badge/Zero_Trust_Architecture-000000?style=for-the-badge&logo=auth0&logoColor=white" alt="Zero Trust">
  <img src="https://img.shields.io/badge/AES_256_GCM-007ACC?style=for-the-badge&logo=lock&logoColor=white" alt="AES-256">
  <img src="https://img.shields.io/badge/NYC_Law_144_Fairness-818CF8?style=for-the-badge&logo=shield&logoColor=white" alt="AI Fairness">
  <img src="https://img.shields.io/badge/Threat_Intelligence-4B0082?style=for-the-badge&logo=securityscorecard&logoColor=white" alt="Threat Intelligence">
</p>

</div>

---

### 📜 Verified Credentials & Education

*   🎓 **Licenciatura en Ciberdefensa (In Progress)** — *Universidad de la Defensa Nacional (UNDEF)*
*   ☁️ **Oracle Cloud Infrastructure Certified Foundations Associate** — *Oracle* `[Verification ID: 103477615OCI26FNDCFA]`
*   🛡️ **Certificación Profesional en Ciberseguridad** — *IBM SkillsBuild*
*   📊 **Data Science Tech Foundation & Machine Learning** — *Oracle*
*   💾 **Autonomous Database & Oracle APEX Specialist** — *Oracle Next Education / Alura Latam*
*   🌐 **IELTS Professional English Proficiency** — *Santander | British Council*

---

### 🌐 Live Telemetry & Activity Dashboard

<!-- START_DASHBOARD -->
<div align="center">
  <table style="border: none; border-collapse: collapse; margin: auto; background: transparent;">
    <tr style="border: none; background: transparent;">
      <td style="border: none; padding: 4px; vertical-align: middle;" align="center">
        <img height="180px" src="https://github-readme-stats.vercel.app/api?username=Maxrodri0311&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0b0f19&title_color=38bdf8&icon_color=38bdf8&text_color=94a3b8" alt="GitHub Stats" />
      </td>
      <td style="border: none; padding: 4px; vertical-align: middle;" align="center">
        <img height="180px" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Maxrodri0311&layout=compact&theme=tokyonight&hide_border=true&bg_color=0b0f19&title_color=38bdf8&text_color=94a3b8" alt="Top Languages" />
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <img width="96%" src="https://github-readme-streak-stats.herokuapp.com/?user=Maxrodri0311&theme=tokyonight&hide_border=true&background=0b0f19&stroke=38bdf8&ring=38bdf8&fire=38bdf8&currStreakNum=38bdf8" alt="GitHub Streak" />
</div>
<!-- END_DASHBOARD -->

---

### 🛠️ Currently Engineering & Live Stream
<!-- START_CURRENT_ENGINEERING -->
> ⚡ **Despliegues Activos:** Sincronización continua de arquitecturas y pipelines en producción.
<!-- END_CURRENT_ENGINEERING -->

<br>

<div align="center">
  <sub>Engineered with precision • Driven by Deterministic Software Architecture • © 2026 Maximiliano Rodriguez</sub>
</div>
