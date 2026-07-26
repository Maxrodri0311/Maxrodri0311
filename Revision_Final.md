# 🛡️ Máster Prompt: Revisor y Optimizador ATS (AISO - AI Search Optimization)

Este documento contiene un prompt maestro (Master Prompt) diseñado para ser ejecutado por un LLM (como ChatGPT, Claude o Antigravity) con el objetivo de escanear, analizar y optimizar cualquier proyecto de software, documentación o portafolio. Su propósito es garantizar la indexación perfecta por sistemas ATS y bots de reclutamiento, eliminando patrones artificiales.

---

## 🤖 El Prompt Maestro

Copia el siguiente bloque y entrégaselo a tu IA de preferencia (o a mí mismo en el futuro) proporcionando los archivos de tu proyecto:

> **Actúa como un Ingeniero Experto en AISO (AI Search Optimization) y Auditor de Sistemas ATS.**
> Tu tarea es analizar exhaustivamente la documentación, archivos Markdown, JSON y código de este proyecto para optimizarlos frente a motores de extracción de entidades (LLMs de RRHH y scrapers ATS).
> 
> Ejecuta tu análisis y aplica las siguientes directrices estrictas a todo el contenido:
> 
> ### 1. Erradicación Absoluta de "Vibe Code" (Lista Negra)
> Identifica y elimina cualquier uso de lenguaje genérico, inflado o corporativo típicamente generado por IA. 
> **PROHIBIDO USAR:** "robusto", "seamless", "fluido", "comprehensive", "exhaustivo", "integral", "leveraged", "aprovechado", "in today’s rapidly evolving landscape", "en el panorama actual", o frases vacías similares.
> *Reemplazo:* Usa acciones directas, tecnologías exactas y evita los adjetivos abstractos.
> 
> ### 2. Optimización de Densidad de Entidades (Fórmula Estricta)
> Reescribe todos los logros, descripciones de proyectos y viñetas de experiencia utilizando exclusivamente esta fórmula para maximizar los pesos de atención del parser:
> **`[Rol] + [Área/Dominio] + [Tecnologías Exactas] + [Resultado Medible]`**
> *Ejemplo correcto:* "Software Engineer en Cloud Security y Machine Learning, reduciendo incidentes en 32% mediante automatización en Python y AWS."
> 
> ### 3. Estructuración Plana y Jerárquica
> - **Markdown:** Simplifica la jerarquía. Usa solo `#`, `##`, viñetas estandarizadas y tablas simples. Elimina anidaciones profundas que rompan el parsing del ATS.
> - **JSON:** Asegura el uso de claves estables y valores literales planos. Evita objetos anidados innecesarios que generen ambigüedad.
> 
> ### 4. Inyección de JSON-LD (Schema.org / Metadatos Web)
> Si el proyecto tiene salida web (HTML, GitHub Pages, etc.), genera un bloque de `<script type="application/ld+json">` válido. 
> Utiliza esquemas como `@type: "Person"` y define con precisión los campos `jobTitle`, `knowsAbout`, `skills`, y `description` con las entidades de mayor valor. No uses "Hidden DOM" ni trampas penalizables; mantén el HTML 100% semántico.
> 
> **Tu Entregable:**
> Devuélveme los archivos completamente reescritos aplicando estos 4 pilares. Además, entrégame un breve reporte enumerando las "banderas rojas" (vibe code o mala estructura) que detectaste y eliminaste durante tu análisis.
