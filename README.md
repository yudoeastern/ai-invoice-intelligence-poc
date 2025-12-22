# AI Invoice Intelligence – OCR POC

Proof of Concept for OCR-based invoice processing using
Computer Vision + LLM (Qwen) + FastAPI.

## Architecture Overview

![OCR Architecture](docs/images/architecture.png)

## OCR Flow

1. Upload invoice (PDF / Image)
2. OCR + Layout Analysis
3. Field Extraction using LLM
4. Validation & Confidence Scoring
5. Output JSON → SAP Integration

![OCR Flow](docs/images/ocr-flow.png)

## Sample Invoice

![Sample Invoice](docs/images/sample-invoice.png)
