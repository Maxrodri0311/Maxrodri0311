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
    <a href="https://github.com/Maxrodri0311/Maxrodri0311/actions/workflows/generate-cv.yml"><img src="https://img.shields.io/badge/Resume-Download_PDF-00FF99?style=for-the-badge&logo=adobeacrobatreader&logoColor=black" alt="Download CV"></a>
  </p>
</div>

---

### 🏛️ Architecture Overview: Enterprise Hybrid Decoupled Platform

```mermaid
flowchart LR
    subgraph CLIENT["Client Layer"]
        UI["React 19 / Modern SPA"]
    end

    subgraph OCI["Oracle Cloud Infrastructure (Zero-Trust VCN)"]
        direction TB
        subgraph GATEWAY["Edge Layer"]
            NGINX["NGINX Reverse Proxy / TLS"]
        end

        subgraph BACKEND["Core Business Logic"]
            SPRING["Spring Boot 3 (Java 17)<br/>JWT Auth • Rate Limiting"]
        end

        subgraph INFERENCE["AI Engine (Local-First)"]
            FASTAPI["FastAPI Inference Engine<br/>Async I/O • ProcessPool"]
            ONNX["ONNX Runtime INT8<br/>RAM: 110MB • Latency: <18ms"]
        end

        subgraph STORAGE["Isolated Data Layer"]
            DB[("MySQL 8.0 / PostgreSQL<br/>SHA-256 Content Hashing")]
        end
    end

    UI -->|HTTPS| NGINX
    NGINX -->|Reverse Proxy| SPRING
    SPRING -->|Async Internal RPC| FASTAPI
    FASTAPI --> ONNX
    SPRING -->|Deterministic Hashing| DB
```

---

### 🚀 Core Engineering Projects (Production-Grade)

#### 1. [Techmind — Enterprise AI Microservices Platform](https://github.com/Maxrodri0311/techmind)
*Decoupled microservices architecture combining Spring Boot 3 business logic with a Python FastAPI AI engine hosted on Oracle Cloud Infrastructure (OCI).*
* **Memory & Latency Optimization:** Reduced AI inference RAM from **2.5 GB to 110 MB (-82%)** and latency from **1500ms to <18ms** by implementing INT8 model quantization with ONNX Runtime and NumPy vectorized operations.
* **Deterministic Integrity:** Enforced 100% data deduplication and referential integrity across MySQL tables using content-based **SHA-256 cryptographic hashing**.
* **Zero-Trust Network:** Secured all database and AI inference services inside an isolated OCI Virtual Cloud Network (VCN) with **zero public IPs**, routing outbound traffic strictly through a secure NAT Gateway.

#### 2. [Data Sentinel — Zero-Trust Financial Compliance & Ledger](https://github.com/Maxrodri0311/data-sentinel)
*Financial audit and anomaly detection system built with Clean Architecture, Domain-Driven Design (DDD), and tamper-proof ledgering.*
* **Non-Blocking Inference:** Maintained sub-3ms API latency during CPU-intensive machine learning by offloading Isolation Forest and SHAP calculations to a `ProcessPoolExecutor`.
* **Tamper-Proof Auditability:** Engineered an append-only audit trail with PL/pgSQL triggers and cryptographic hash-chaining, achieving a **100% rejection rate** against unauthorized UPDATE and DELETE attempts.
* **Cryptographic PII Protection:** Shielded sensitive financial data with **AES-256-GCM** encryption and zero-downtime key rotation support.

#### 3. [Aegis Stream — Real-Time SIEM Telemetry Pipeline](https://github.com/Maxrodri0311/aegis-stream)
*Event-driven telemetry ingestion engine designed for massive log streams and real-time security analytics.*
* **Zero-Loss Throughput:** Handled peak ingestion rates of **50,000 events/second** without event loop starvation via asynchronous backpressure controls (`aiokafka` + `asyncio`).
* **Compaction Deduplication:** Eliminated duplicate telemetry records during merge compaction phases using ClickHouse’s native `ReplacingMergeTree` engine.
* **Zero-Copy Ingestion:** Streamlined streaming pipelines by utilizing ClickHouse native Kafka Engines connected directly to reactive Materialized Views.

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
  <img src="https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="NGINX">
  <img src="https://img.shields.io/badge/Linux_Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash">
</p>

#### Backend & Core Runtimes
<p>
  <img src="https://img.shields.io/badge/Python_3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Java_17+-007396?style=for-the-badge&logo=java&logoColor=white" alt="Java">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Spring_Boot_3-6DB33F?style=for-the-badge&logo=springboot&logoColor=white" alt="Spring Boot">
  <img src="https://img.shields.io/badge/ONNX_Runtime-005CED?style=for-the-badge&logo=onnx&logoColor=white" alt="ONNX">
  <img src="https://img.shields.io/badge/Pydantic_V2-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
</p>

#### Data Engineering, Streaming & Analytics
<p>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/ClickHouse-FFCC01?style=for-the-badge&logo=clickhouse&logoColor=black" alt="ClickHouse">
  <img src="https://img.shields.io/badge/Redpanda_Kafka-FF1744?style=for-the-badge&logo=redpanda&logoColor=white" alt="Redpanda">
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-Learn">
</p>

#### Cybersecurity & Defensive Standards
<p>
  <img src="https://img.shields.io/badge/Zero_Trust_Architecture-000000?style=for-the-badge&logo=auth0&logoColor=white" alt="Zero Trust">
  <img src="https://img.shields.io/badge/AES_256_GCM-007ACC?style=for-the-badge&logo=lock&logoColor=white" alt="AES-256">
  <img src="https://img.shields.io/badge/Threat_Intelligence-4B0082?style=for-the-badge&logo=securityscorecard&logoColor=white" alt="Threat Intelligence">
  <img src="https://img.shields.io/badge/GRC_Compliance-2E8B57?style=for-the-badge&logo=checkmarx&logoColor=white" alt="GRC">
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
*   ⚙️ **Electromechanical Technician** — *EPET N°7*

---

### 🌐 Live Telemetry & Activity Dashboard

<!-- START_DASHBOARD -->
<div align="center">
  <table style="border: none; border-collapse: collapse; margin: auto; background: transparent;">
    <tr style="border: none; background: transparent;">
      <td style="border: none; padding: 4px; vertical-align: middle;" align="center">
        <img height="195px" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Maxrodri0311&theme=tokyonight" alt="GitHub Profile Details" />
      </td>
      <td style="border: none; padding: 4px; vertical-align: middle;" align="center">
        <img height="195px" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Maxrodri0311&theme=tokyonight" alt="Top Languages by Commit" />
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <img width="96%" src="https://github-readme-activity-graph.vercel.app/graph?username=Maxrodri0311&theme=tokyo-night&hide_border=true&area=true" alt="Contribution Activity Graph" />
</div>
<!-- END_DASHBOARD -->

---

### 🛠️ Currently Engineering & Live Stream
<!-- START_CURRENT_ENGINEERING -->
> ⚡ **Despliegues Activos:** Mantenimiento de arquitecturas y pipelines en producción.
<!-- END_CURRENT_ENGINEERING -->

<br>

<div align="center">
  <sub>Engineered with precision • Driven by Deterministic Software Architecture • © 2026 Maximiliano Rodriguez</sub>
</div>
