# Python Automation Tool - Setup & Run Guide

## 📋 Prerequisites

Before starting, make sure you have:
- **Python 3.9+** installed on your machine
- **VS Code** installed
- **Git** (optional, for cloning the repository)
- **Node.js 16+** (for the web dashboard)

## 🚀 Quick Start Setup

### Step 1: Clone/Download the Project

\`\`\`bash
# If using Git
git clone <your-repo-url>
cd python-automation-tool

# OR manually download and extract the project folder
\`\`\`

### Step 2: Install Python Dependencies

Open VS Code and navigate to the project folder:

\`\`\`bash
# Windows Users
python -m venv venv
venv\Scripts\activate

# Mac/Linux Users
python3 -m venv venv
source venv/bin/activate
\`\`\`

Once the virtual environment is activated, install the required packages:

\`\`\`bash
pip install -r scripts/requirements.txt
\`\`\`

### Step 3: Install Node.js Dependencies (For Dashboard)

\`\`\`bash
# In the root directory
npm install
# or
yarn install
\`\`\`

### Step 4: Start the Web Dashboard

\`\`\`bash
# Development mode
npm run dev

# The dashboard will be available at: http://localhost:3000
\`\`\`

### Step 5: Run Python Scripts

In a **new terminal** (keep the dashboard running), run the automation scripts:

\`\`\`bash
# Make sure your virtual environment is still activated

# Run System Monitor
python scripts/system_monitor.py

# Run Data Processor
python scripts/data_processor.py

# Run File Manager
python scripts/file_manager.py
\`\`\`

## 📁 Project Structure

\`\`\`
python-automation-tool/
├── app/                          # Next.js application
│   ├── page.tsx                 # Main page
│   ├── layout.tsx               # Layout wrapper
│   └── globals.css              # Global styles
├── components/
│   ├── sidebar.tsx              # Sidebar navigation
│   ├── header.tsx               # Header component
│   ├── dashboard.tsx            # Main dashboard
│   ├── tabs/
│   │   ├── overview.tsx         # Overview charts
│   │   ├── tasks.tsx            # Tasks management
│   │   ├── analytics.tsx        # Analytics page
│   │   └── settings.tsx         # Settings page
│   └── ui/
│       └── card.tsx             # Card component
├── scripts/                      # Python automation scripts
│   ├── data_processor.py        # Data processing automation
│   ├── system_monitor.py        # System monitoring
│   ├── file_manager.py          # File management
│   └── requirements.txt         # Python dependencies
└── SETUP_INSTRUCTIONS.md        # This file
\`\`\`

## 🔧 Running Individual Python Scripts

### Data Processor
\`\`\`bash
cd scripts
python data_processor.py
\`\`\`
**What it does:**
- Loads and cleans data from CSV/JSON files
- Removes duplicates and handles missing values
- Generates statistical analysis
- Saves processed data

### System Monitor
\`\`\`bash
python system_monitor.py
\`\`\`
**What it does:**
- Monitors CPU, Memory, Disk usage
- Checks network statistics
- Tracks top processes
- Generates health reports
- Can run continuous monitoring

### File Manager
\`\`\`bash
python file_manager.py
\`\`\`
**What it does:**
- Lists files in directories
- Cleans up old files
- Organizes files by extension
- Calculates directory sizes
- Creates backups

## 💻 VS Code Setup

### Recommended Extensions
1. **Python** - Microsoft Official
2. **Pylance** - Microsoft (Python language server)
3. **ES7+ React/Redux/React-Native snippets** - dsznajder.es7-react-js-snippets
4. **Thunder Client** or **REST Client** - For API testing

### VS Code Debug Configuration

Create `.vscode/launch.json`:

\`\`\`json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: Monitor Script",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/scripts/system_monitor.py",
      "console": "integratedTerminal"
    }
  ]
}
\`\`\`

### Running with Debugger in VS Code
1. Open a Python script in VS Code
2. Press `F5` or click "Run and Debug"
3. Select the configuration you want to run

## 🎯 Common Tasks

### Check if Virtual Environment is Activated
Look for `(venv)` at the start of your terminal prompt. If not present, activate it:

**Windows:**
\`\`\`bash
venv\Scripts\activate
\`\`\`

**Mac/Linux:**
\`\`\`bash
source venv/bin/activate
\`\`\`

### Install New Python Package
\`\`\`bash
pip install package-name
\`\`\`

### Update Python Dependencies
\`\`\`bash
pip install -r scripts/requirements.txt --upgrade
\`\`\`

### Deactivate Virtual Environment
\`\`\`bash
deactivate
\`\`\`

## 🚨 Troubleshooting

### Issue: "Python command not found"
**Solution:** 
- Windows: Use `python` or `py`
- Mac/Linux: Use `python3`
- Make sure Python is added to PATH

### Issue: ModuleNotFoundError
**Solution:**
\`\`\`bash
# Ensure virtual environment is activated
# Then reinstall requirements
pip install -r scripts/requirements.txt
\`\`\`

### Issue: Port 3000 already in use
**Solution:**
\`\`\`bash
# Mac/Linux: Find and kill the process
lsof -i :3000
kill -9 <PID>

# Windows: Use a different port
npm run dev -- -p 3001
\`\`\`

### Issue: Permission Denied (Linux/Mac)
**Solution:**
\`\`\`bash
chmod +x scripts/*.py
python scripts/system_monitor.py
\`\`\`

## 📊 Dashboard Features

- **Overview Tab**: Real-time system metrics and charts
- **Automation Tasks Tab**: Manage and monitor automation scripts
- **Analytics Tab**: Historical performance data and trends
- **Settings Tab**: Configure integrations and preferences

## 🎨 Customization

### Change API URL
Edit in `components/tabs/settings.tsx`:
\`\`\`tsx
const [settings, setSettings] = useState({
  apiUrl: 'http://localhost:8000', // Change this
  // ...
});
\`\`\`

### Modify Python Scripts
All Python scripts are in the `scripts/` folder and are fully customizable.

## 📈 Next Steps for Portfolio

1. **Deploy the Dashboard**: Deploy to Vercel (supports Next.js natively)
   \`\`\`bash
   npm run build
   vercel deploy
   \`\`\`

2. **Create API Backend**: Build a Flask/FastAPI backend to connect Python scripts
   
3. **Add Database**: Integrate MongoDB/PostgreSQL for data persistence
   
4. **CI/CD Pipeline**: Set up GitHub Actions for automated testing

## 📝 Notes

- Keep the virtual environment activated while developing
- The web dashboard and Python scripts run independently
- For production, consider containerizing with Docker
- All logs are printed to console; capture them for monitoring

## ✅ Success Checklist

- [ ] Virtual environment created and activated
- [ ] Python dependencies installed (`pip list` shows required packages)
- [ ] Node.js dependencies installed (`npm list` runs without errors)
- [ ] Dashboard running on http://localhost:3000
- [ ] Python scripts execute without errors
- [ ] All tabs and features visible in dashboard

## 🎓 Learning Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [Python psutil Documentation](https://psutil.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [React/Recharts Documentation](https://recharts.org/)

---

**Happy Automating! 🚀**
