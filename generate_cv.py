import os
import asyncio
from jinja2 import Template

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @page { size: A4; margin: 15mm 15mm 15mm 15mm; }
  body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #111; line-height: 1.4; font-size: 10pt; margin: 0; }
  h1 { font-size: 18pt; margin: 0 0 2px 0; text-transform: uppercase; color: #0f172a; letter-spacing: 0.5px; }
  .subtitle { font-size: 10.5pt; font-weight: 600; color: #0284c7; margin-bottom: 6px; }
  .contact { font-size: 8.5pt; color: #475569; margin-bottom: 12px; border-bottom: 1.5px solid #0f172a; padding-bottom: 6px; }
  .contact a { color: #0284c7; text-decoration: none; }
  h2 { font-size: 11pt; text-transform: uppercase; border-bottom: 1px solid #cbd5e1; color: #0f172a; margin: 12px 0 6px 0; padding-bottom: 2px; letter-spacing: 0.5px; }
  .item { margin-bottom: 8px; }
  .item-header { display: flex; justify-content: space-between; font-weight: bold; font-size: 9.5pt; }
  .item-sub { display: flex; justify-content: space-between; font-style: italic; font-size: 8.5pt; color: #334155; margin-bottom: 3px; }
  ul { margin: 2px 0 4px 16px; padding: 0; }
  li { margin-bottom: 2px; font-size: 9pt; color: #1e293b; }
  .skills-grid { font-size: 8.5pt; }
  .skills-row { margin-bottom: 3px; }
  .skills-label { font-weight: bold; color: #0f172a; }
</style>
</head>
<body>
  <h1>Maximiliano Rodriguez</h1>
  <div class="subtitle">Principal Software Architect & Data Engineer</div>
  <div class="contact">
    Misiones, Argentina (Open to Remote / Relocation) • 
    <a href="mailto:maxrodri0311@gmail.com">maxrodri0311@gmail.com</a> • 
    +54 3743 59-5673 • 
    <a href="https://linkedin.com/in/maximiliano-rodriguez-982674375/">linkedin.com/in/maximiliano-rodriguez</a> • 
    <a href="https://github.com/Maxrodri0311">github.com/Maxrodri0311</a>
  </div>

  <h2>Executive Summary</h2>
  <p style="font-size: 9pt; color: #1e293b; margin: 4px 0 8px 0;">
    System Architect and Software Engineer with specialized focus in Zero-Trust cloud infrastructure (OCI), distributed event-driven pipelines, and high-performance AI inference engines. Pursuing a Bachelor of Science in Cyberdefense (UNDEF). Proven track record of architecting decoupled microservices in Spring Boot and FastAPI, reducing memory consumption by 82% via INT8 quantization and designing tamper-proof cryptographic audit ledgers.
  </p>

  <h2>Production Engineering Projects</h2>
  <div class="item">
    <div class="item-header"><span>TECHMIND — Enterprise AI Microservices Platform</span><span>Remote</span></div>
    <div class="item-sub"><span>Principal Software Architect & Lead Engineer</span><span>Java 17, Spring Boot 3, FastAPI, ONNX, MySQL, OCI</span></div>
    <ul>
      <li>Optimized AI inference RAM from 2.5 GB to 110 MB (-82%) and latency from 1500ms to &lt;18ms using INT8 quantization with ONNX Runtime and NumPy vectorization.</li>
      <li>Enforced 100% data deduplication and referential integrity across MySQL tables via content-based SHA-256 cryptographic hashing pipelines.</li>
      <li>Secured microservices with zero public IP exposure by architecting an isolated OCI Virtual Cloud Network (VCN) with NAT Gateway routing.</li>
    </ul>
  </div>

  <div class="item">
    <div class="item-header"><span>DATA SENTINEL — Zero-Trust Financial Compliance Ledger</span><span>Remote</span></div>
    <div class="item-sub"><span>Principal Software Architect</span><span>Python, FastAPI, PostgreSQL, AES-256-GCM, Scikit-Learn, SHAP</span></div>
    <ul>
      <li>Maintained sub-3ms API latency during CPU-bound ML inference by offloading Isolation Forest and SHAP models to an asynchronous ProcessPoolExecutor.</li>
      <li>Engineered an append-only cryptographic ledger with PL/pgSQL triggers, achieving 100% rejection of unauthorized UPDATE/DELETE attempts.</li>
      <li>Protected sensitive financial PII using AES-256-GCM authenticated encryption with key-rotation architecture.</li>
    </ul>
  </div>

  <div class="item">
    <div class="item-header"><span>AEGIS STREAM — Real-Time SIEM Telemetry Pipeline</span><span>Remote</span></div>
    <div class="item-sub"><span>System Architect & Data Engineer</span><span>ClickHouse, Redpanda, aiokafka, Docker, AsyncIO</span></div>
    <ul>
      <li>Handled peak telemetry ingestion of 50,000 events/second without event loop starvation via asynchronous backpressure controls.</li>
      <li>Eliminated duplicate event records during compaction phases using ClickHouse ReplacingMergeTree engine and Materialized Views.</li>
    </ul>
  </div>

  <h2>Technical Skills</h2>
  <div class="skills-grid">
    <div class="skills-row"><span class="skills-label">Cloud & Infrastructure:</span> Oracle Cloud Infrastructure (OCI), Docker, Linux (Bash), NGINX, GitHub Actions, GitOps, CI/CD.</div>
    <div class="skills-row"><span class="skills-label">Languages & Runtimes:</span> Python 3.12+, Java 17+, SQL / PL-SQL, JavaScript/TypeScript, HTML5/CSS3.</div>
    <div class="skills-row"><span class="skills-label">Frameworks & Tools:</span> FastAPI, Spring Boot 3, ONNX Runtime, Pydantic V2, Pandas, NumPy, Scikit-Learn.</div>
    <div class="skills-row"><span class="skills-label">Databases & Streaming:</span> PostgreSQL, ClickHouse, Redpanda (Kafka), MySQL 8.0, Redis, Oracle Autonomous Database.</div>
    <div class="skills-row"><span class="skills-label">Security & Standards:</span> Zero-Trust Architecture, AES-256-GCM, Threat Intelligence, GRC Compliance, Cryptographic Ledgers.</div>
  </div>

  <h2>Education & Verified Credentials</h2>
  <div class="item">
    <div class="item-header"><span>Licenciatura en Ciberdefensa (Bachelor in Cyberdefense)</span><span>In Progress</span></div>
    <div class="item-sub"><span>Universidad de la Defensa Nacional (UNDEF)</span><span>Buenos Aires, Argentina</span></div>
  </div>
  <div class="item">
    <div class="item-header"><span>Oracle Cloud Infrastructure Certified Foundations Associate</span><span>Oracle</span></div>
    <div class="item-sub"><span>Verification ID: 103477615OCI26FNDCFA</span><span>Cloud Architecture & Security</span></div>
  </div>
  <div class="item">
    <div class="item-header"><span>Certificación Profesional en Ciberseguridad</span><span>IBM SkillsBuild</span></div>
    <div class="item-sub"><span>Network Security, Threat Intelligence & Active Defense</span><span>Credential ID Verified</span></div>
  </div>
</body>
</html>"""

async def generate_pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(HTML_TEMPLATE)
        pdf_path = "Resume_Maximiliano_Rodriguez.pdf"
        await page.pdf(path=pdf_path, format="A4", print_background=True)
        await browser.close()
        print(f"[+] PDF generado exitosamente en: {pdf_path}")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
