# DESIGN.md

> Source of truth for operational visual decisions.

```yaml
design_system:
  id: your-brand-v1
  version: 1.0.0
  source_visual_dna: ./visual-dna.json
  generated_from:
    - REF01
    - REF02
```

## 0. Visual thesis
Describe the visual personality in 3–5 sentences.

## 1. Personality
- ...

## 2. Color
- Background: ...
- Accent: ...
- Support colors: ...

## 3. Typography & hierarchy
- Display: ...
- Body: ...
- Reading order: ...

## 4. Composition & spacing
- Grid: ...
- Margins: ...
- Density: ...

## 5. Image treatment
- ...

## 6. Repeatable components
- ...

## 7. Invariants — never change
- ...

## 8. Freedom — may change
- ...

## 9. Reject rules
Reject an output if:
- ...

## 10. Format rules
### Carousel
...
### Story
...
### Cover / Ad
...

## 11. Evidence mapping
| Operational rule | visual-dna.json source | Confidence |
|---|---|---|
| ... | observations... | high |

## 12. Change policy
Only update this file from approved outputs or new verified evidence.
