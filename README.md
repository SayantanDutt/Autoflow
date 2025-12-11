🚀 Python Automation Tool — Full Project Documentation

A modern, modular automation dashboard built using Next.js, TypeScript, and Python automation scripts.
This tool streamlines data processing, system monitoring, and workflow automation with a clean UI and robust backend logic.

📌 Features
Frontend (Next.js)

⚡ Built using Next.js 14 (App Router)

🎨 Fully modular UI with components in /components

⚙ Configurable automation workflows

📁 API layer using /app/api

🌗 Responsive and theme-ready UI

Backend (Python Automation Scripts)

🔄 Automated data processing

📊 System monitoring workflows

🧮 Pandas, NumPy, Matplotlib support

🏗 Extensible script structure

🔌 Exposed via API endpoints


python-automation-tool/
│
├── app/                    # Next.js app router pages & routes
├── components/             # UI components
├── hooks/                  # Reusable React hooks
├── lib/                    # Utility functions
├── public/                 # Static assets
├── styles/                 # Global CSS & styling config
│
├── api/                    # Backend automation logic (Python)
│   ├── scripts/            # Individual automation scripts
│   └── utils/              # Helpers for automation tasks
│
├── scripts/                # Node/Python helper scripts
├── package.json            # Node dependencies
├── pnpm-lock.yaml          # pnpm lock file
├── next.config.mjs         # Next.js configuration
├── tsconfig.json           # TypeScript configuration
├── SETUP_INSTRUCTIONS.md   # Internal developer setup files
└── README.md               # (This file)


🛠 Tech Stack
Frontend

Next.js 14

React

TypeScript

TailwindCSS

ShadCN components (if included)

Backend Automation

Python 3.10+

Pandas

NumPy

Matplotlib

Custom algorithmic workflows

# 🛠 Tech Stack

### **Frontend**
- Next.js 14  
- React  
- TypeScript  
- TailwindCSS  
- ShadCN/UI Components (if included)

### **Backend Automation**
- Python 3.10+
- Pandas
- NumPy
- Matplotlib
- Custom workflow automation scripts

---

# ⚙️ Installation & Setup

## **1. Install Node.js**
Download from: https://nodejs.org  
Recommended version: **18 LTS or 20 LTS**

Check version:
```sh
node -v


Install pnpm (required)
npm install -g pnpm


Verify:

pnpm -v

3. Install Python Dependencies

Inside /api or wherever your scripts live:

pip install -r requirements.txt

4. Install Project Dependencies (Frontend)

Inside project root:

pnpm install

5. Run the Development Server
pnpm dev


Visit:

http://localhost:3000

🧪 Production Build
Create production build:
pnpm build

Start server:
pnpm start

📡 API Endpoints (Next.js App Router)

Your API routes live inside:

/app/api/...


Example routes:

/app/api/run-automation/route.ts
/app/api/get-status/route.ts


Each endpoint may:

Trigger Python scripts

Return JSON data

Handle automation logic

🔌 Running Python Automation Scripts

Example (inside /api/scripts):

python api/scripts/data_processor.py


Run all workflows:

python api/run_all.py

🧩 Adding New Automation Scripts

Create script in:

/api/scripts/<script_name>.py


Write automation logic (Pandas, NumPy, Monitoring, etc.)

Add a corresponding API endpoint:

/app/api/<endpoint>/route.ts


In the API route, call your Python file:

import { exec } from "child_process";
