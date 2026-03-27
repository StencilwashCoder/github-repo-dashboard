# 📊 GitHub Repo Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/StencilwashCoder/github-repo-dashboard?style=flat-square&color=yellow" alt="Stars">
  <img src="https://img.shields.io/github/forks/StencilwashCoder/github-repo-dashboard?style=flat-square" alt="Forks">
  <img src="https://github.com/StencilwashCoder/github-repo-dashboard/workflows/CI/badge.svg?style=flat-square" alt="CI">
</p>

<p align="center">
  <b>A beautiful CLI dashboard for visualizing GitHub repository statistics.</b><br>
  Perfect for developers who want quick insights into their projects.
</p>

---

## ✨ Features

- 📊 **Repository Overview** - Stars, forks, watchers, and open issues at a glance
- 📈 **Contribution Analytics** - Commit activity and contributor stats
- 🏷️ **Language Breakdown** - Visual representation of code composition
- 🚀 **Release Tracking** - Latest releases and version history
- 👥 **Contributor Insights** - Top contributors and their activity
- 📅 **Issue/PR Metrics** - Open/closed ratios and average resolution time
- ⚡ **Fast & Lightweight** - Minimal dependencies, maximum performance
- 🔒 **Secure** - No data collection, uses official GitHub API

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Install

```bash
# Clone the repository
git clone https://github.com/StencilwashCoder/github-repo-dashboard.git
cd github-repo-dashboard

# Install dependencies
pip install -r requirements.txt

# Optional: Set your GitHub token for higher rate limits
export GITHUB_TOKEN=your_token_here
```

### Create GitHub Token (Optional but Recommended)

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select `public_repo` scope for public repos, or `repo` for private
4. Copy and export as `GITHUB_TOKEN`

## 📖 Usage

```bash
# View dashboard for any public repository
python dashboard.py owner/repo-name

# Examples
python dashboard.py StencilwashCoder/github-repo-dashboard
python dashboard.py microsoft/vscode
python dashboard.py torvalds/linux
python dashboard.py facebook/react

# With custom GitHub token
GITHUB_TOKEN=your_token python dashboard.py owner/repo
```

## 🖥️ Example Output

```
┌─────────────────────────────────────────────────────────────┐
│  📊 GitHub Repo Dashboard: StencilwashCoder/github-repo-dashboard  │
├─────────────────────────────────────────────────────────────┤
│  ⭐ Stars: 42          🍴 Forks: 8           👁️ Watchers: 3   │
│  🐛 Open Issues: 5     🔀 Open PRs: 2                        │
├─────────────────────────────────────────────────────────────┤
│  📈 Activity (Last 30 Days)                                  │
│  ████████████████████░░░░░░░░░░  142 commits                │
│  ████████░░░░░░░░░░░░░░░░░░░░░░   58 pull requests          │
├─────────────────────────────────────────────────────────────┤
│  🏷️ Languages                                                │
│  Python        ████████████████████░░░░░  78.5%             │
│  Shell         ██████░░░░░░░░░░░░░░░░░░░  15.2%             │
│  Markdown      ██░░░░░░░░░░░░░░░░░░░░░░░   6.3%             │
├─────────────────────────────────────────────────────────────┤
│  👥 Top Contributors                                         │
│  1. @stencilwashcoder        45 commits                     │
│  2. @contributor2            12 commits                     │
├─────────────────────────────────────────────────────────────┤
│  🚀 Latest Release: v1.2.0 (2 days ago)                     │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Configuration

Create a `.env` file for persistent configuration:

```env
GITHUB_TOKEN=your_github_token
DEFAULT_OWNER=your_username
CACHE_TTL=3600
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GITHUB_TOKEN` | GitHub personal access token | None |
| `DEFAULT_OWNER` | Default repository owner | None |
| `CACHE_TTL` | Cache time-to-live in seconds | 300 |

## 🧪 Development

```bash
# Setup development environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=dashboard --cov-report=html

# Format code
black .
isort .

# Lint
flake8 .
```

## 🐳 Docker

```bash
# Build image
docker build -t github-repo-dashboard .

# Run
docker run -e GITHUB_TOKEN=your_token github-repo-dashboard owner/repo
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Run tests (`pytest`)
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Feature Ideas

- [ ] Export to JSON/CSV
- [ ] Compare multiple repos
- [ ] Historical trend graphs
- [ ] Team/organization dashboard
- [ ] Web interface

## 📋 Roadmap

- [x] Basic repository stats
- [x] Language breakdown
- [x] Contribution activity
- [ ] Interactive mode
- [ ] Export functionality
- [ ] Web dashboard

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- GitHub API for the data
- Built with ❤️ by [Stencilwashcoder](https://github.com/stencilwashcoder)

---

<p align="center">
  <sub>⭐ Star this repo if you find it useful! ⭐</sub>
</p>
