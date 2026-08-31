# Prompt OS · P00–P17

# P00 · TENGO UNA IDEA, ¿QUÉ HAGO?

```text
Quiero crear una pieza visual con esta idea:
[IDEA]
Formato: [carrusel / Story / post / anuncio / portada]
Marca: [NOMBRE]
Audiencia: [AUDIENCIA]
Objetivo: [OBJETIVO]
Plantilla visual: [T01–T09]

Usa DESIGN.md como fuente de verdad.
1. Mejora el ángulo.
2. Propón el hook.
3. Crea la estructura.
4. Dime qué referencias necesito.
5. Genera un prompt por pieza/slide.
No copies el ejemplo: usa su lógica y adapta todo al branding.
```

---

# P01 · BUSCAR REFERENCIAS

```text
Tengo que crear contenido visual sobre: [TEMA].
Propón 12 búsquedas concretas para Pinterest para encontrar referencias de tipografía, composición, color, fotografía, UI/elementos gráficos y portadas.
Evita búsquedas genéricas. Usa términos visuales específicos, preferiblemente en inglés, y explica qué debería observar en cada búsqueda.
```

---

# P02 · EXTRAER ADN VISUAL

```text
Analiza todas las imágenes adjuntas como director de arte.
No copies una pieza concreta. Identifica las decisiones visuales que se repiten.
Separa lo que observas directamente de lo que interpretas.
Extrae: personalidad visual, paleta, tipografía y jerarquía, grid/márgenes/densidad, tratamiento de imagen, elementos repetidos, reglas fijas, lo que sí puede cambiar y qué rompería el estilo.
Explícalo primero en lenguaje sencillo y después entrégalo como JSON estructurado.
```

---

# P03 · JSON → DESIGN.md

```text
Actúa como un DESIGN COMPILER. Convierte el archivo `visual-dna.json` adjunto en un `DESIGN.md` trazable y operativo.

REGLAS DURAS:
- No inventes decisiones no respaldadas por el JSON.
- Mantén un enlace explícito a `./visual-dna.json`.
- Separa observaciones de reglas operativas.
- Toda regla importante debe poder rastrearse a una clave del JSON o a una referencia fuente.

ENTREGA `DESIGN.md` con:
1. metadata: id, versión, source_visual_dna y referencias fuente;
2. Visual Thesis;
3. Personalidad;
4. Color;
5. Tipografía y jerarquía;
6. Composición y espacio;
7. Tratamiento de imagen;
8. Componentes repetibles;
9. Invariants — lo que nunca cambia;
10. Freedom — lo que sí puede variar;
11. Reject Rules;
12. Reglas por formato;
13. Evidence Mapping: regla → clave JSON → confidence;
14. Change Policy.

Si el JSON no soporta una regla, marca `UNRESOLVED` en vez de completarla por intuición.
```

---

# P04 · GENERAR PRIMERA PIEZA

```text
Crea una pieza visual siguiendo el DESIGN.md adjunto.
IDENTIDAD sirve únicamente para mantener al sujeto.
REF_LAYOUT sirve para composición.
REF_TYPE sirve para jerarquía/tipografía.
DESIGN.md contiene las reglas generales.
FORMATO: [4:5 / 9:16 / otro]
TEXTO EXACTO: [PEGAR COPY]
Prioriza texto, identidad, jerarquía y ADN visual. No añadas elementos no solicitados. Genera una primera versión limpia.
```

---

# P05 · CORREGIR SIN REINICIAR

```text
Edita la pieza anterior. Mantén intacto todo lo que no menciono.
CORREGIR ÚNICAMENTE:
[DESCRIBE UNA VARIABLE]
MANTENER:
- identidad;
- copy exacto;
- paleta;
- composición aprobada;
- elementos que ya funcionan.
Devuelve una nueva versión corrigiendo solo ese problema.
```

---

# P06 · TRANSFERIR A OTRO FORMATO

```text
Adapta la pieza aprobada a [NUEVO FORMATO].
Mantén personalidad, paleta, tipografía, tratamiento de imagen y componentes de marca.
Cambia únicamente ratio, distribución, cantidad de información y escala cuando el formato lo exija.
No hagas un simple recorte: recompón manteniendo el ADN visual.
```

---

# P07 · REVERSE ENGINEERING DE UNA REFERENCIA

```text
Analiza esta referencia sin copiar su apariencia literal.
Explícame:
1. orden de lectura;
2. jerarquía tipográfica;
3. composición y distribución del espacio;
4. tratamiento de imagen;
5. color y contraste;
6. elementos secundarios;
7. qué reglas son transferibles;
8. qué elementos son específicos de esta pieza y no deberían copiarse.
Termina con 5 reglas reutilizables.
```

---

# P08 · CREAR ÁNGULO + HOOK

```text
Tema: [TEMA]
Audiencia: [AUDIENCIA]
Objetivo: [OBJETIVO]

Genera:
- 5 insights;
- 5 tensiones;
- 5 ángulos;
- 10 hooks cortos.

Evita títulos genéricos y listas previsibles.
Elige después el ángulo con mayor curiosidad + claridad y explica por qué.
```

---

# P09 · STORYBOARD DEL CARRUSEL

```text
Construye un storyboard de [8-10] slides.
Cada slide debe tener:
- función narrativa;
- headline;
- apoyo mínimo;
- idea visual;
- continuidad con la siguiente.

Reglas:
- una idea dominante por slide;
- slide 1 interrumpe;
- slide 2 confirma la promesa;
- el cuerpo aumenta valor/tensión;
- la última cierra o activa CTA.
No diseñes todavía: define la secuencia.
```

---

# P10 · PROMPT POR SLIDE

```text
Usa el DESIGN.md y el storyboard adjuntos.
Para la slide [N], crea un prompt de generación que especifique:
- función de la slide;
- texto exacto;
- referencia de identidad si existe;
- referencia de composición;
- tratamiento visual;
- jerarquía;
- formato;
- safe area;
- elementos que NO deben aparecer.
No cambies el copy.
```

---

# P11 · QA VISUAL

```text
Evalúa esta pieza del 0 al 100.
Puntúa por separado:
- claridad en 3 segundos;
- jerarquía;
- identidad;
- tipografía;
- copy exacto;
- consistencia con DESIGN.md;
- composición;
- legibilidad móvil.

Lista únicamente:
1. lo que pasa;
2. lo que falla;
3. la única corrección de mayor impacto.
No propongas un rediseño completo si no es necesario.
```

---

# P12 · ACTUALIZAR DESIGN.md

```text
Compara DESIGN.md con la versión final aprobada.
Identifica qué aprendizaje nuevo merece convertirse en regla reusable.
Propón un cambio mínimo al DESIGN.md:
- regla nueva o modificada;
- por qué mejora el sistema;
- qué problema previene;
- si es regla fija, recomendación o excepción.
No reescribas todo el archivo.
```

---

# P13 · DESIGN.md → SKILL.md

```text
Convierte `DESIGN.md` + `visual-dna.json` en una `SKILL.md` reusable para ejecutar el sistema visual con agentes.

La skill debe incluir:
- purpose;
- activation conditions;
- required inputs;
- optional inputs;
- workflow paso a paso;
- output contract;
- reject rules;
- visual QA;
- failure states;
- learning policy;
- versioning.

El workflow mínimo debe cubrir: idea → template → hook → storyboard → prompts por slide → QA → corrección → aprendizaje.

No inventes reglas visuales. `DESIGN.md` manda. `visual-dna.json` conserva la evidencia.
```

---

# P14 · ADAPTAR AL RUNTIME

```text
Adapta esta `SKILL.md` al runtime: [CODEX / CLAUDE CODE / HIGGSFIELD SUPERCOMPUTER].

No cambies el comportamiento de la skill. Crea únicamente la capa de adaptación necesaria para que el runtime sepa:
1. qué archivos debe leer;
2. en qué orden;
3. qué inputs recibe del usuario;
4. qué output debe devolver;
5. qué no puede modificar sin aprobación.

Devuelve un adapter corto y ejecutable en lenguaje natural, portable y sin depender de memoria del chat.
```

---

# P15 · RUN BRAND SYSTEM

```text
Ejecuta el Brand System con estos inputs:
- IDEA: [IDEA]
- OBJETIVO: [OBJETIVO]
- AUDIENCIA: [AUDIENCIA]
- FORMATO: [FORMATO]

Lee primero `SKILL.md`, luego `DESIGN.md` y después `visual-dna.json`.

Entrega:
1. template recomendado + motivo;
2. hook;
3. storyboard;
4. prompt exacto por slide / asset;
5. inputs visuales necesarios por rol;
6. QA esperado;
7. siguiente acción.

No generes reglas nuevas y no copies literalmente referencias.
```

---

# P16 · LEARN FROM APPROVED

```text
Tenemos un output FINAL APROBADO. Compara:
- output final;
- DESIGN.md;
- SKILL.md;
- visual-dna.json.

Identifica únicamente aprendizajes realmente nuevos. Clasifica cada uno como:
A) nueva observación → patch a visual-dna.json;
B) nueva regla operativa → patch a DESIGN.md;
C) nuevo comportamiento automatizable → patch a SKILL.md.

Propón patches mínimos, con justificación y cambio de versión. No reescribas archivos completos.
```

---

# P17 · RELEASE AUDIT

```text
Haz una auditoría de release del Brand System.

Comprueba:
- visual-dna.json existe y es válido;
- DESIGN.md enlaza al JSON;
- SKILL.md enlaza a DESIGN.md + JSON;
- referencias están clasificadas por rol;
- hay ejemplos approved/rejected;
- reject rules son verificables;
- output contract es claro;
- no hay reglas inventadas;
- el sistema es portable fuera de esta conversación.

Devuelve PASS / FAIL por criterio, blockers P0/P1/P2 y el patch mínimo para sellar release.
```
