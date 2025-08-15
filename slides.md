---
marp: true
title: Product Documentation Presentation
description: Interactive product docs with Marp
author: Technical Writer
theme: custom
paginate: true
_paginate: true
---

<!--
theme: custom
class: lead
style: |
  section {
    font-family: 'Segoe UI', sans-serif;
    font-size: 1.1em;
  }
  h1, h2 {
    color: #004080;
  }
  footer {
    color: #888;
    font-size: 0.8em;
  }
-->
<!-- _footer: "© 2025 Software Company | Contact: 22f3002631@ds.study.iitm.ac.in" -->

# Product Documentation  
## Modern, Maintainable & Portable

**Author:** Technical Writer  
**Contact:** 22f3002631@ds.study.iitm.ac.in

---

## Why Marp?

- **Markdown-based** – easy to maintain in version control
- **Multiple export formats** – PDF, HTML, PPTX
- **Custom styling** – match company branding
- **Developer-friendly** – integrates with CI/CD

---

<!-- _backgroundImage: url('https://images.unsplash.com/photo-1518770660439-4636190af475?fit=crop&w=1600&q=80') -->
<!-- _backgroundColor: rgba(0,0,0,0.5) -->
<!-- _color: white -->
# Product Architecture Overview

1. **Frontend** – React + Tailwind  
2. **Backend** – Node.js + Express  
3. **Database** – PostgreSQL  
4. **Cloud** – AWS

---

## Mathematical Model

Algorithmic complexity for our data processing pipeline:

$$
T(n) = O(n \log n) + O(k \cdot n)
$$

Where:  
- \(n\) = number of records  
- \(k\) = number of processing stages

---

## Example Code

```javascript
// API call to fetch product data
async function getProduct(id) {
  const res = await fetch(`/api/products/${id}`);
  return res.json();
}
