# DHARMA TO DECISIONS
### *An Interactive Decision-Learning Simulation Inspired by the Mahābhārata*

> **"Ancient dilemmas. Modern decisions."**  
> *Step into the dilemma. Make the decision. Learn from the consequences.*

---

## 1. Product Overview & Core Innovation

**Dharma to Decisions** is not a static Mahābhārata storytelling website, nor is it a trivia quiz or a gamified combat arena. It is a **cognitive decision-learning laboratory** that converts foundational ethical and strategic crises from the Mahābhārata into structured modern decision cases.

### The Cognitive Learning Loop:
```
Mahābhārata Episode 
  → Ethical & Strategic Dilemma 
  → Multi-Stakeholder Impact Analysis
  → Competing Values Prioritization
  → Decision Commitment & Reasoning Tags
  → Multi-Tier Consequence Engine
  → Mahābhārata Principle Deep Dive (IKS)
  → Modern Scenario Transfer Bridge
  → Transfer Decision & Reflection Synthesis
  → Cognitive Reasoning Radar Profile & Badges
```

The system does not preach dogmatic moralisms or declare simplistic "correct vs. wrong" answers. In classical Indian epistemology, **Dharma** is contextual, role-bound (*Svadharma*), and replete with competing obligations (*Dharma-sankata*). The application teaches structured reasoning under uncertainty, consequence foresight, and multi-stakeholder stewardship.

---

## 2. Research Problem & Innovation Statement

### The Educational Problem
Students, young professionals, and emerging leaders frequently confront high-stakes decisions involving competing loyalties, asymmetric risks, whistleblowing, and resource allocation. However, traditional education relies on passive lectures, retrospective Harvard-style cases where the outcome is already known, or simplistic multiple-choice quizzes that provide no opportunity to practice decision-making under uncertainty.

### The Research Gap
While modern scholarship frequently examines Mahābhārata and *Bhagavad Gītā* principles in relation to leadership and ethics, digital implementations historically collapse into two unhelpful poles:
1. Passive religious storytelling or apologetics.
2. Violent video games focused on combat mechanics and weapons, omitting the ethical deliberations entirely.

### The Innovation
**Dharma to Decisions** operationalises ancient epic dilemmas into an active simulator. Users are placed directly into the decision-maker's shoes, navigate incomplete information, weigh contradictory values, face realistic multi-order consequences, and immediately test transfer learning through parallel modern professional cases.

---

## 3. The 6 Curated Mahābhārata Cases

All six cases are grounded in the **Bhandarkar Oriental Research Institute (BORI) Critical Edition** and authoritative academic translations:

| # | Case Title | Parva | Protagonists | Core Dilemma | Modern Transfer Scenario |
|---|---|---|---|---|---|
| **1** | **Arjuna's Dilemma on the Threshold of War** | *Bhīṣmaparvan* (VI.23–VI.40) | Arjuna, Krishna, Bhishma, Drona | Duty (*Svadharma*) vs. Attachment (*Rāga*) and Familial Grief | Student lead confronting closest friend who plagiarized code for team capstone |
| **2** | **Krishna's Peace Mission to Hastinapura** | *Udyogaparvan* (V.82–V.137) | Krishna, Duryodhana, Dhritarashtra, Vidura | Exhaustion of Peaceful Means (*Sāma/Dāna*) vs. Preemptive Strike | Boardroom ombudsperson mediating predatory investor buyout vs. whistleblowing |
| **3** | **Yudhishthira and the Yaksha at the Pool** | *Vanaparvan* (III.295–III.299) | Yudhishthira, Yaksha (Dharma), Nakula | Restraint, Wisdom, and Compassionate Equity (*Ānṛśaṁsya*) | Disaster triage director choosing between sibling clinic vs. vulnerable community clinic |
| **4** | **Vidura's Midnight Counsel to the Sleepless King** | *Udyogaparvan* (V.33–V.40) | Vidura, King Dhritarashtra | Speaking Unvarnished Truth to Power (*Satya*) vs. Flattery | Chief Risk Officer deciding whether to halt a defective autonomous vehicle launch before $10B IPO |
| **5** | **Karna's Choice: Patron Loyalty vs. Cosmic Justice** | *Udyogaparvan* (V.140–V.146) | Karna, Krishna, Duryodhana, Kunti | Personal Gratitude (*Mitra-Dharma*) vs. Universal Order (*Sāmānya-Dharma*) | Founding engineer discovering their benevolent CEO is embezzling from municipal pension funds |
| **6** | **Abhimanyu and the Chakravyuha** | *Droṇaparvan* (VII.34–VII.49) | Abhimanyu, Yudhishthira, Drona, Jayadratha | Asymmetric Risk, Incomplete Egress Knowledge, and Overextension | Junior engineer pressured to execute an irreversible banking data migration without tested rollback |

---

## 4. Architecture & Tech Stack

The platform is designed with a full-stack, decoupled architecture:

### Frontend
- **Framework:** React 18 / 19 with TypeScript
- **Tooling:** Vite, ESNext
- **Styling:** Tailwind CSS with a custom Indian manuscript palette (*Muted Gold `#C5A059`, Deep Indigo `#0B101E`, Parchment `#F7F4EB`, Subtle Saffron `#E06D28`, Dark Charcoal `#0B0D13`*)
- **Typography:** *Cinzel* (classical headings), *Inter* (crisp UI body)
- **Icons:** Lucide React
- **Data Visualizations:** Custom SVG 6-Axis Radar Chart for cognitive reasoning profiles

### Backend
- **Framework:** Python 3.9+ with FastAPI
- **Web Server:** Uvicorn ASGI
- **Data Layer:** SQLite (production-ready for PostgreSQL) with SQLAlchemy ORM
- **Validation:** Pydantic v2 schemas
- **Architecture:** Clean REST API with automatic database seeding, deterministic reasoning evaluation (no mandatory external AI API needed for full functionality)

---

## 5. Project Structure

```
ADM/
├── backend/
│   ├── app/
│   │   ├── database.py         # SQLAlchemy engine and session factory
│   │   ├── models.py           # Database models (Cases, Decisions, Reflections, Evaluation)
│   │   ├── schemas.py          # Pydantic request/response models
│   │   ├── seed_data.py        # Complete scholarly data for all 6 cases
│   │   └── main.py             # FastAPI endpoints, CORS, analytics, evaluation
│   ├── dharma_decisions.db     # SQLite persistence database
│   └── venv/                   # Python virtual environment
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.tsx      # Navigation, branding, and Quick Demo launcher
│   │   │   ├── Footer.tsx      # Scholarly attribution & methodology footer
│   │   │   └── RadarChart.tsx  # SVG 6-Axis cognitive profile visualizer
│   │   ├── pages/
│   │   │   ├── LandingPage.tsx    # Atmospheric Kurukshetra hero & interactive previews
│   │   │   ├── CaseLibrary.tsx    # Filterable catalog of the 6 Mahābhārata cases
│   │   │   ├── CaseDetail.tsx     # Folio context, stakeholders, known vs uncertain info
│   │   │   ├── SimulationLab.tsx  # 10-phase interactive decision simulation engine
│   │   │   ├── Dashboard.tsx      # Reasoning dimensions radar, subtle badges, history
│   │   │   ├── KnowledgeGraph.tsx # Interactive entity ontology explorer
│   │   │   ├── Sources.tsx        # BORI Critical Edition bibliography
│   │   │   ├── Evaluation.tsx     # Pre-test, Post-test, and SUS research module
│   │   │   └── About.tsx          # Pedagogical cycle, problem, and IKS foundation
│   │   ├── services/
│   │   │   └── api.ts          # Resilient frontend API client with session management
│   │   ├── types/
│   │   │   └── index.ts        # TypeScript data contracts
│   │   ├── App.tsx             # Root layout and hash-routing controller
│   │   └── main.tsx            # React application entrypoint
│   ├── tailwind.config.js      # Custom theme colors and shadows
│   └── vite.config.ts          # Dev server and reverse proxy config
├── .env.example                # Environment variable documentation
└── README.md                   # Complete architectural guide
```

---

## 6. Installation & Quickstart

### Prerequisites
- Python 3.9 or higher
- Node.js 18+ and npm

### 1. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi "uvicorn[standard]" sqlalchemy pydantic python-multipart httpx

# Start the FastAPI server (runs on port 8000)
uvicorn app.main:app --host 127.0.0.1 --port 8000
```
*Note: The database automatically creates tables and seeds all 6 Mahābhārata cases on initial startup.*

### 2. Frontend Setup
```bash
cd frontend
npm install

# Start the Vite development server (runs on port 5173)
npm run dev
```

### 3. Open in Browser
Open `http://127.0.0.1:5173` in any modern web browser.

---

## 7. REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | System health check and case count |
| `GET` | `/api/cases` | List all cases with optional filters (`category`, `parva`, `difficulty`) |
| `GET` | `/api/cases/{case_id}` | Retrieve complete details, stakeholders, values, and options for a case |
| `POST` | `/api/decisions` | Submit epic decision; computes 6-axis scores and multi-tier consequence tree |
| `POST` | `/api/decisions/modern` | Commit choice in the modern transfer scenario; evaluates cognitive bridge |
| `POST` | `/api/reflections` | Record reflective answers and personal commitments; generates summary report |
| `GET` | `/api/reflections/{decision_id}` | Retrieve saved reflection report |
| `GET` | `/api/analytics/dashboard` | Returns aggregate reasoning dimensions, earned badges, and activity history |
| `GET` | `/api/graph` | Returns nodes and edges for the Mahābhārata Knowledge Graph |
| `GET` | `/api/sources` | Returns scholarly citations and textual methodology |
| `POST` | `/api/evaluation/pre` | Record baseline pre-test reasoning score |
| `POST` | `/api/evaluation/post` | Record post-test score and compute empirical improvement percentage |
| `POST` | `/api/evaluation/sus` | Record 10-item System Usability Scale responses and compute SUS score |
| `GET` | `/api/evaluation/stats` | Retrieve transparent cohort research metrics |

---

## 8. Cognitive Reasoning Profile (0–100 Dimensions)

Rather than judging moral worth, the application measures six structured cognitive dimensions:

1. **Responsibility Orientation (*Kartavya-Nishtha*):** Commitment to institutional role and collective duty.
2. **Strategic Thinking (*Yukti*):** Foreseeing secondary reactions, unintended consequences, and long-term positioning.
3. **Stakeholder Awareness (*Sarva-Bhūta-Hita*):** Perspective-taking across allies, opponents, vulnerable dependents, and civil society.
4. **Long-Term Thinking (*Dīrgha-Darśana*):** Prioritising generational sustainability over impulsive short-term relief.
5. **Ethical Consistency (*Dharma-Sthiratā*):** Maintaining normative standards regardless of pressure or personal emotional bias.
6. **Risk Awareness (*Sankaṭa-Boddha*):** Discerning asymmetric hazards, incomplete information, and irreversible actions.

---

## 9. Academic Sources & Scholarly Standards

All cases cite authentic academic scholarship:
- **Bhandarkar Oriental Research Institute (BORI):** The Mahābhārata Critical Edition (1919–1966), Pune, India.
- **J.A.B. van Buitenen:** *The Mahābhārata*, Books 1–5, University of Chicago Press (1973–1978).
- **Kisari Mohan Ganguli:** *The Mahabharata of Krishna-Dwaipayana Vyasa Translated into English Prose* (1883–1896).
- **IIT Kanpur Gita Supersite:** Primary Sanskrit recensions with classical commentaries (*Shankara, Ramanuja, Madhva*).
- **Bibek Debroy:** *The Mahabharata*, 10 Volumes, Penguin Books India (2010–2014).

---

## 10. Demo Walkthrough (3-Minute Tour for Reviewers)

1. Open `http://127.0.0.1:5173`.
2. Click **"Try Demo"** in the top navigation.
3. You immediately enter **Arjuna's Dilemma on the Threshold of War**.
4. Review the core crisis and historical folio context.
5. Inspect the **Stakeholder Impact Architecture** (Arjuna, Bhishma & Drona, Pandava brothers, Civil Society).
6. Calibrate the **Competing Values Sliders** (*Duty vs Compassion, Systemic Order vs Kinship*).
7. Review the **4 Nuanced Options** (Renunciation, Conditional Defending, Nishkama Duty, Unarmed Summit).
8. Commit your decision with quick reasoning tags and written justification.
9. Watch the animated **Consequence Engine** reveal immediate effects, secondary ripples, and unintended risks.
10. Inspect your **Decision Reasoning Profile** on the 6-axis Radar Chart.
11. Read the **IKS Principle Deep Dive** (*Nishkama Karma* and *Svadharma*).
12. Step across the **Transfer Bridge** into the modern dilemma: *The Student Lead & the Compromised Capstone*.
13. Select a modern action, review the consequence, write a personal reflection, and view your **Learning Dashboard** with earned badges.

---

*Developed under Indian Knowledge Systems (IKS) research guidelines as an open educational simulator.*
