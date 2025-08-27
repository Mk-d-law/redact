# Project Guardian 2.0 – Proposal

This project can be built with **DataFog (PII detection)**, an open-source tool that provides efficient PII detection using a **pattern-first approach**. It processes text significantly faster than traditional NLP methods while maintaining high accuracy.

## Performance Comparison

| Engine          | 10KB Text Processing | Relative Speed | Accuracy       |
|-----------------|-----------------------|----------------|----------------|
| DataFog (Regex) | ~2.4ms               | 190x faster    | High (structured) |
| DataFog (GLiNER)| ~15ms                | 32x faster     | Very High      |
| DataFog (Smart) | ~3–15ms              | 60x faster     | Highest        |

✅ **Best suited for low latency and environments with limited computational power.**

---

## Enhancements

For the given constraints, **conditional rules** are added on top of DataFog’s detection engine.

---

## Novelty and Creativity

We propose deployment as an **API Gateway Plugin** at the **data egress layer** for all outbound APIs and external integrations.

The solution operates as a **dual-layer system**, serving both as a compliance enforcer and a fraud-prevention filter:

### 1. Internal Storage of Raw PII
- Used for fraud prevention, ML models, and compliance-justified purposes.  
- Secured with **encryption** and **access controls**.  

### 2. Automatic Redaction/Tokenization of Outbound Data
- Applied to APIs, logs, and external integrations.  
- Ensures compliance with data protection regulations.  
- Prevents **PII leaks** before data leaves the system.  
