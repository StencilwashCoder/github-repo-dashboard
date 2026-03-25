# GitHub Repo Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/StencilwashCoder/github-repo-dashboard)](https://github.com/StencilwashCoder/github-repo-dashboard/stargazers)

A beautiful CLI dashboard for visualizing GitHub repository statistics. Perfect for developers who want quick insights into their projects.

## ✨ Features

- 📊 **Repository Overview** - Stars, forks, watchers, and open issues
- 📈 **Contribution Analytics** - Commit activity and contributor stats
- 🏷️ **Language Breakdown** - Visual representation of code composition
- 🚀 **Release Tracking** - Latest releases and version history
- ⚡ **Fast & Lightweight** - Minimal dependencies, maximum performance

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/StencilwashCoder/github-repo-dashboard.git
cd github-repo-dashboard

# Install dependencies
pip install -r requirements.txt

# Set your GitHub token (optional, for higher rate limits)
export GITHUB_TOKEN=your_token_here
```

## 📖 Usage

```bash
# View dashboard for any public repository
python dashboard.py owner/repo-name

# Examples
python dashboard.py StencilwashCoder/github-repo-dashboard
python dashboard.py microsoft/vscode
python dashboard.py torvalds/linux
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
├─────────────────────────────────────────────────────────────┤
│  🏷️ Languages                                                │
│  Python        ████████████████████░░░░░  78.5%             │
│  Shell         ██████░░░░░░░░░░░░░░░░░░░  15.2%             │
│  Markdown      ██░░░░░░░░░░░░░░░░░░░░░░░   6.3%             │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Configuration

Create a `.env` file for persistent configuration:

```env
GITHUB_TOKEN=your_github_token
DEFAULT_OWNER=your_username
```

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- Uses [GitHub REST API](https://docs.github.com/en/rest) for data

---

Made with ❤️ by [StencilwashCoder](https://github.com/StencilwashCoder)
