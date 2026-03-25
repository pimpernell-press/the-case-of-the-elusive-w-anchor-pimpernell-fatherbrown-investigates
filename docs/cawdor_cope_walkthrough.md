---
title: "Cawdor Gardens COPE Walkthrough"
subtitle: "The Operational Engine Applied to the First Live Deployment"
site: Cawdor Gardens, Ross-on-Wye, Herefordshire
units: 25 homes (Phase II), 4 Almshouse affordable
GDV: £13.8m
date: 2026-03-25
---

# Cawdor Gardens COPE Walkthrough

The analytical cathedral has 187 nodes. The operational shed has 7.
This document builds the shed — walking the Collaborative Origination
and Procurement Engine through its first live deployment.

---

## 1. ORIGINATION

### 1.1 Plot Identification

The site is a brownfield parcel in Ross-on-Wye, Herefordshire, adjacent
to a Victorian railway arch. A previous consent for 32 units had lapsed.
The previous developer's scheme proposed demolishing the arch to maximise
unit count. Home@ix identified the site as a candidate precisely because
the lapsed consent established **residential principle** — the local
authority had already accepted this as a housing site — while the
lapsed approach (demolish, maximise) left room for a higher-value,
lower-unit scheme (retain, customise).

**Brain node:** `c8643971` (Savills Brief History of UK Housing) — provides
the market context for site identification.
**NEW NODE NEEDED:** `cawdor-plot-identification` — the specific site
assessment, lapsed consent analysis, and residential principle argument.

### 1.2 Design Brief

Home@ix's design brief for Cawdor inverts the volume-builder model:
- 25 homes (down from lapsed 32) — maximise value per unit, not units per hectare
- Retain the Victorian railway arch as a placemaking asset
- Custom/self-build Plot Passport model — premium pricing, higher design quality
- 4 Almshouse affordable homes — delivered via conditional sale agreement,
  not reluctant planning obligation

**Brain node:** `1045054d` (Habitat Design) — relevant principle but contains
no Cawdor-specific content.
**NEW NODE NEEDED:** `cawdor-design-brief` — the architectural vision, unit
mix, arch retention strategy, and Plot Passport specifications.

### 1.3 Planning

The planning case is built on three foundations:
1. **Established residential principle** — the lapsed consent means the
   Council has already accepted the site for housing
2. **Self-Build Act tailwind** — custom and self-build is explicitly
   supported in Ross-on-Wye's Neighbourhood Development Plan
3. **Malmesbury precedent** — appeal decision establishing that a
   custom-build scheme can succeed where a standard scheme might not.
   Cawdor application explicitly aligned with this case law.

The data room contains: full planning history of lapsed consent, flood
risk assessment (SuDS mitigation), transport statement (shuttle traffic
management through the arch), heritage statement (English Heritage
consulted), biodiversity reports (reptile translocation — routine for
brownfield), and the Plot Passport precedent from Greylands Oakwrights.

**Brain node:** No existing node.
**NEW NODE NEEDED:** `cawdor-planning-strategy` — the planning case,
precedent alignment, and data room contents.

### 1.4 Architect and Catalogue

[NEEDS HUMAN INPUT: Which architect is specified for Cawdor Phase II?
Is this a Potton catalogue design adapted to site, a bespoke design by
an external architect, or a Home@ix in-house specification? What house
types are proposed — detached, semi, terrace? What size range?]

**NEW NODE NEEDED:** `cawdor-house-types` — the design specification
linking Potton catalogue to site-specific adaptation.

---

## 2. PROCUREMENT

### 2.1 Supplier System

The Potton timber-frame system is the primary structural procurement
route. Potton (est. 1964, acquired from Kingspan 12 November 2025)
provides:
- 60 years of planning authority relationships
- 50 years of mortgage lender recognition (critical for self-build mortgages)
- 2022 Build It Awards shortlist (Tadpole Garden Village, 14 custom plots)
- ~560 homes delivered across portfolio

**Brain node:** `9cc43c5f` (moduloft-the-affordable-housing-manufacturers)
— Moduloft is the Home@ix origin story. Potton is the successor brand.
**NEW NODE NEEDED:** `cawdor-potton-procurement` — the Potton specification
for Cawdor, frame type, delivery schedule, and relationship to Kingspan exit.

### 2.2 Tier 1 Supplier Map

[NEEDS HUMAN INPUT: Beyond Potton for the frame, who are the Tier 1
suppliers? Specifically:
- Groundworks / foundations contractor?
- Roofing system (tiles, membrane)?
- Window and door supplier?
- Kitchen and bathroom packages?
- Mechanical and electrical (M&E) contractor?
- Insulation specification (PIR, mineral wool, other)?
- External cladding (render, brick slip, timber, composite)?]

**Brain node:** No existing node for Tier 1 map.
**NEW NODE NEEDED:** `cawdor-tier1-supply-chain` — the complete
supplier map with named contractors.

### 2.3 BIM Library

The Home@ix corpus index references a BIM Catalogue with "regional
design specifications" (homeix_corpus_index.html, line 722). The
Cawdor deployment should draw from this library.

[NEEDS HUMAN INPUT: Was a BIM model created for Cawdor Phase II? If so:
- What software (Revit, ArchiCAD, other)?
- What LOD (Level of Development)?
- Does the Digital Twin inherit from the BIM model?
- Is the BIM model in the Google Drive archive?]

**Brain node:** No existing node.
**NEW NODE NEEDED:** `cawdor-bim-model` — the digital design asset,
LOD, and software stack.

### 2.4 Material Standards

[NEEDS HUMAN INPUT: What specification standard governs the Cawdor build?
Specifically:
- Thermal performance target (Part L / Future Homes Standard / Passivhaus)?
- Air tightness target?
- SAP rating?
- Timber frame structural standard (BS EN 1995 / proprietary)?
- Foundation type (strip, raft, piled)?]

**Brain node:** `f95f517f` (Exceed Air Tightness Testing Requirements)
— exists in the COPE brain with 1 attachment.
**NEW NODE NEEDED:** `cawdor-material-spec` — the full specification
matrix for the build.

---

## 3. PROCESS

### 3.1 Build Programme

[NEEDS HUMAN INPUT: What is the construction sequence?
- Phase I: show home timeline?
- Phase II: outline planning target (late 2026 per investor materials)
- First Plot Passport issued: early 2027?
- Build duration per unit (weeks)?
- Overall programme duration?
- Critical path items?]

**Brain node:** No existing node.
**NEW NODE NEEDED:** `cawdor-build-programme` — the Gantt or
equivalent showing the sequence from planning to occupation.

### 3.2 Site Logistics

The Victorian railway arch creates a constrained access point. The
transport statement models signal-controlled shuttle traffic management
— the same principle used at thousands of UK single-lane access sites.

[NEEDS HUMAN INPUT:
- Crane access and lifting plan?
- Material storage compound location?
- Timber frame delivery sequence (how many loads per house)?
- Weather constraints on erection (wind speed limits for crane)?]

**Brain node:** `c3dd5da0` (Logistics Innovations) — generic.
**NEW NODE NEEDED:** `cawdor-site-logistics` — the specific access,
storage, and delivery plan.

### 3.3 QA / Inspection

[NEEDS HUMAN INPUT:
- Building control route (local authority or approved inspector)?
- NHBC or equivalent warranty provider?
- Stage inspection points (foundations, frame, first fix, completion)?
- Air tightness test at which stage?
- EPC (Energy Performance Certificate) target rating?]

**Brain node:** `40e7e814` (Quality Control) — generic, no attachments.
**NEW NODE NEEDED:** `cawdor-qa-protocol` — the inspection matrix
and warranty route.

### 3.4 Handover Protocol

[NEEDS HUMAN INPUT:
- What does the buyer receive at completion?
- Operating manuals for systems (MVHR, heating, etc.)?
- Defects liability period (typically 12 months)?
- Snagging process?
- Homeowner induction / training?]

**NEW NODE NEEDED:** `cawdor-handover-protocol` — the completion
package specification.

### 3.5 Digital Twin

The investor materials describe a "Digital Twin lifetime data asset"
as part of the Home@ix platform stack. At Cawdor:

[NEEDS HUMAN INPUT:
- Is a Digital Twin being created for each home?
- What data does it contain (BIM geometry, material specs, M&E layout, warranty dates)?
- Is it handed to the homeowner at completion?
- What platform hosts it (Home@ix proprietary, third-party)?
- Does it integrate with the Plot Passport and Moneym@ix?]

**NEW NODE NEEDED:** `cawdor-digital-twin` — the lifetime data asset
for Cawdor units.

### 3.6 Post-Occupancy Evaluation

[NEEDS HUMAN INPUT:
- Is there a planned post-occupancy evaluation?
- Who conducts it (Home@ix, independent, BRE)?
- What metrics (actual energy use vs. design, occupant satisfaction,
  defect rates, thermal comfort)?
- At what intervals (3 months, 12 months, 3 years)?]

**NEW NODE NEEDED:** `cawdor-post-occupancy` — the feedback loop
that closes the COPE cycle.

---

## 4. COST / MARGIN

### 4.1 Going-Direct Saving

The Home@ix model eliminates the volume housebuilder margin. At Tadpole
Garden Village, Potton delivered 14 custom-build plots as a subcontractor;
Crest Nicholson captured the equity value. At Cawdor, Home@ix holds the
platform position:

| | Tadpole (old model) | Cawdor (COPE model) |
|--|---------------------|---------------------|
| Land holder | Crest Nicholson | Almshouse trustees → Home@ix (conditional sale) |
| Design | Potton (subcontractor) | Home@ix / Potton (platform owner) |
| Build | External contractor | Home@ix Tier 1 chain |
| Equity value | Crest Nicholson | Home@ix + investors |
| Buyer premium | Standard housebuilder | Plot Passport custom — premium pricing |

**Project economics (confirmed):**

| Metric | Value |
|--------|-------|
| GDV | £13.8m |
| Total costs | £10.3m |
| Gross profit | £3.5m |
| Margin on GDV | ~25% |
| Margin on cost | ~34% |
| Post-consent land value | ~£1.4m |

**Brain node:** Multiple cost_margin nodes (53 in total), but none are
Cawdor-specific.
**NEW NODE NEEDED:** `cawdor-project-economics` — the Cawdor-specific
financial model with the going-direct comparison.

### 4.2 FAIR-Index Context

[NEEDS HUMAN INPUT: What is the FAIR-Index reading for the Ross-on-Wye
/ Herefordshire market? Specifically:
- Local price-to-earnings ratio?
- Turnover rate (% of stock transacting annually)?
- Cash buyer share locally?
- How does the FAIR-Index scoring affect the Cawdor pricing strategy?]

### 4.3 Mortgage Pathway

Potton's 50-year mortgage lender recognition is a structural advantage
for self-build mortgages. The Moneym@ix pathway connects buyers with
appropriate finance products.

[NEEDS HUMAN INPUT:
- Which lenders are pre-approved for Potton self-build?
- Is there a specific Cawdor mortgage panel?
- Shared equity or community land trust options for the affordable units?
- Stage payment schedule for self-build drawdowns?]

**NEW NODE NEEDED:** `cawdor-mortgage-pathway` — the Moneym@ix
configuration for Cawdor buyers.

---

## 5. EVIDENCE CROSS-REFERENCE

### Brain Nodes (Existing)

| ID | Name | Category | Cawdor Relevance |
|----|------|----------|-----------------|
| `c8643971` | Savills Brief History UK Housing | origination | Market context |
| `9cc43c5f` | moduloft-the-affordable-housing-manufacturers | procurement | Origin story |
| `9e667f82` | Factory-Made-Housing-Research-NLA.pdf | procurement | MMC evidence |
| `c5cdab01` | Home@ix Affordable Homes Framework.pdf | procurement | Platform doc |
| `f95f517f` | Exceed Air Tightness Testing Requirements | process | Performance |
| `e9497386` | Real RLD and Home@ix Research (31 children) | integration | Parent hub |
| `342ff314` | Fixing Housing Shortage: Roger Lewis & Steve Baker | integration | Launch event |
| `dc47abc2` | Fixing Housing Shortage (variant) | integration | Launch event |
| `8130f470` | Home@ix Overview BTR Market | integration | BTR strategy |

### YouTube / Audio (Confirmed)

| Asset | Type | Cawdor Relevance |
|-------|------|-----------------|
| Home@ix revolution.mp3 | Audio | Platform announcement |
| launch Home@ix 4 key workers.mp3 | Audio | Key worker housing launch |
| key worker launch home@ix.mp3 | Audio | Key worker launch variant |
| Steve Baker launch event (Brain node) | Video | Acquisition announcement |

### Google Drive Archive

The Homeatix Prospects & Development Archive (6-year corpus) on Google
Drive contains planning applications, site layouts, viability models,
and Y:Cube Mitcham planning docs. The Cawdor Phase II data room
(referenced in investor briefing) should be in this archive or a
parallel confidential folder.

---

## 6. THE 15 NEW NODES NEEDED

| # | Node Name | Category | Parent | Cawdor Evidence | Chapter |
|---|-----------|----------|--------|-----------------|---------|
| 1 | `cawdor-plot-identification` | Origination | e9497386 (Home@ix Research) | Lapsed consent, residential principle | Ch 11 |
| 2 | `cawdor-design-brief` | Origination | e9497386 | Arch retention, unit mix, Plot Passport | Ch 11 |
| 3 | `cawdor-planning-strategy` | Origination | e9497386 | Data room, Malmesbury precedent, SB Act | Ch 11 |
| 4 | `cawdor-house-types` | Origination | e9497386 | [NEEDS INPUT] Potton catalogue adaptation | Ch 11 |
| 5 | `cawdor-potton-procurement` | Procurement | e9497386 | Potton spec, Kingspan exit, frame type | Ch 11 |
| 6 | `cawdor-tier1-supply-chain` | Procurement | e9497386 | [NEEDS INPUT] Named contractors | Ch 11 |
| 7 | `cawdor-bim-model` | Procurement | e9497386 | [NEEDS INPUT] Software, LOD, Digital Twin | Ch 11 |
| 8 | `cawdor-material-spec` | Procurement | e9497386 | [NEEDS INPUT] Part L / Future Homes target | Ch 11 |
| 9 | `cawdor-build-programme` | Process | e9497386 | [NEEDS INPUT] Gantt, critical path | Ch 11 |
| 10 | `cawdor-site-logistics` | Process | e9497386 | Arch access, shuttle traffic, crane plan | Ch 11 |
| 11 | `cawdor-qa-protocol` | Process | e9497386 | [NEEDS INPUT] Inspection matrix, warranty | Ch 11 |
| 12 | `cawdor-handover-protocol` | Process | e9497386 | [NEEDS INPUT] Completion package | Ch 11 |
| 13 | `cawdor-digital-twin` | Integration | e9497386 | [NEEDS INPUT] Lifetime data asset | Ch 11 |
| 14 | `cawdor-post-occupancy` | Process | e9497386 | [NEEDS INPUT] POE metrics, intervals | Ch 11 |
| 15 | `cawdor-project-economics` | Cost/Margin | e9497386 | £13.8m GDV, £3.5m profit, going-direct delta | Ch 11 |

**Nodes with confirmed evidence:** 1, 2, 3, 5, 10, 15 (6 of 15)
**Nodes needing human input:** 4, 6, 7, 8, 9, 11, 12, 13, 14 (9 of 15)

---

## 7. WHAT ROGER / STEVE NEEDS TO PROVIDE

To complete the operational shed, the following specific inputs are needed:

### Priority 1 (required for Ch 11 draft)
1. **House types** — what is being built? Detached/semi/terrace? Sizes? Potton models?
2. **Tier 1 supplier names** — groundworks, roofing, windows, M&E, insulation
3. **Build programme** — even a rough sequence (foundations → frame → first fix → completion)
4. **Thermal target** — Part L minimum or Future Homes Standard or other?

### Priority 2 (required for investor evidence)
5. **BIM status** — has a BIM model been created? What software?
6. **Digital Twin** — is this live? What does it contain?
7. **Mortgage panel** — which lenders for self-build at Cawdor?
8. **FAIR-Index local reading** — Herefordshire-specific data

### Priority 3 (completes the COPE cycle)
9. **QA route** — LA or approved inspector? NHBC or other warranty?
10. **Handover spec** — what does the buyer receive?
11. **Post-occupancy plan** — is there one? Who conducts it?
