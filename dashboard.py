#!/usr/bin/env python3
"""
GitHub Repo Dashboard - A CLI tool for visualizing GitHub repository statistics.
"""

import os
import sys
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich import box

console = Console()

GITHUB_API_BASE = "https://api.github.com"

def get_github_token():
    """Get GitHub token from environment variable."""
    return os.environ.get('GITHUB_TOKEN')

def get_headers():
    """Get request headers with authentication if available."""
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'GitHub-Repo-Dashboard'
    }
    token = get_github_token()
    if token:
        headers['Authorization'] = f'token {token}'
    return headers

def fetch_repo_data(owner, repo):
    """Fetch repository data from GitHub API."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = requests.get(url, headers=get_headers())
    
    if response.status_code == 404:
        console.print(f"[red]❌ Repository '{owner}/{repo}' not found![/red]")
        sys.exit(1)
    elif response.status_code == 403:
        console.print("[yellow]⚠️ API rate limit exceeded. Set GITHUB_TOKEN for higher limits.[/yellow]")
        sys.exit(1)
    elif response.status_code != 200:
        console.print(f"[red]❌ Error: {response.status_code}[/red]")
        sys.exit(1)
    
    return response.json()

def fetch_languages(owner, repo):
    """Fetch language statistics for the repository."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/languages"
    response = requests.get(url, headers=get_headers())
    return response.json() if response.status_code == 200 else {}

def fetch_contributors(owner, repo):
    """Fetch top contributors for the repository."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contributors?per_page=5"
    response = requests.get(url, headers=get_headers())
    return response.json() if response.status_code == 200 else []

def format_number(num):
    """Format large numbers with K/M suffixes."""
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    return str(num)

def create_language_bar(languages, total_bytes, width=40):
    """Create a visual bar for language distribution."""
    if not languages or total_bytes == 0:
        return "No language data available"
    
    bars = []
    sorted_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]
    
    for lang, bytes_count in sorted_langs:
        percentage = (bytes_count / total_bytes) * 100
        bar_length = int((percentage / 100) * width)
        bars.append(f"[cyan]{lang:12}[/cyan] {'█' * bar_length}{'░' * (width - bar_length)} {percentage:.1f}%")
    
    return "\n".join(bars)

def display_dashboard(owner, repo):
    """Display the repository dashboard."""
    with console.status("[bold green]Fetching repository data..."):
        data = fetch_repo_data(owner, repo)
        languages = fetch_languages(owner, repo)
        contributors = fetch_contributors(owner, repo)
    
    # Calculate total bytes for languages
    total_bytes = sum(languages.values()) if languages else 0
    
    # Create main stats panel
    stats_table = Table(show_header=False, box=None)
    stats_table.add_column("Metric", style="cyan", width=15)
    stats_table.add_column("Value", style="white")
    
    stats_table.add_row("⭐ Stars", format_number(data.get('stargazers_count', 0)))
    stats_table.add_row("🍴 Forks", format_number(data.get('forks_count', 0)))
    stats_table.add_row("👁️ Watchers", format_number(data.get('watchers_count', 0)))
    stats_table.add_row("🐛 Open Issues", format_number(data.get('open_issues_count', 0)))
    stats_table.add_row("📦 Size", f"{data.get('size', 0)} KB")
    
    # Create info panel
    info_table = Table(show_header=False, box=None)
    info_table.add_column("Field", style="green", width=15)
    info_table.add_column("Value", style="white")
    
    info_table.add_row("📝 Description", data.get('description', 'N/A')[:50])
    info_table.add_row("🏠 Homepage", data.get('homepage', 'N/A') or 'N/A')
    info_table.add_row("📅 Created", data.get('created_at', 'N/A')[:10])
    info_table.add_row("🔄 Updated", data.get('updated_at', 'N/A')[:10])
    info_table.add_row("🔖 Default Branch", data.get('default_branch', 'N/A'))
    
    # Create language panel
    lang_panel = Panel(
        create_language_bar(languages, total_bytes),
        title="[bold yellow]🏷️ Languages[/bold yellow]",
        border_style="yellow"
    )
    
    # Create contributors panel
    contrib_table = Table(show_header=False, box=None)
    contrib_table.add_column("Contributor", style="magenta")
    contrib_table.add_column("Contributions", style="white", justify="right")
    
    for contributor in contributors[:5]:
        contrib_table.add_row(
            contributor.get('login', 'Unknown'),
            str(contributor.get('contributions', 0))
        )
    
    contrib_panel = Panel(
        contrib_table if contributors else "No contributor data available",
        title="[bold magenta]👥 Top Contributors[/bold magenta]",
        border_style="magenta"
    )
    
    # Main dashboard layout
    console.print()
    console.print(Panel.fit(
        f"[bold blue]📊 GitHub Repo Dashboard: {owner}/{repo}[/bold blue]",
        border_style="blue"
    ))
    console.print()
    
    # Display stats in columns
    console.print(Panel(stats_table, title="[bold cyan]📈 Statistics[/bold cyan]", border_style="cyan"))
    console.print()
    console.print(Panel(info_table, title="[bold green]ℹ️ Repository Info[/bold green]", border_style="green"))
    console.print()
    console.print(lang_panel)
    console.print()
    console.print(contrib_panel)
    console.print()
    
    # Repository link
    console.print(f"[dim]🔗 {data.get('html_url', '')}[/dim]")

def main():
    if len(sys.argv) != 2:
        console.print("[yellow]Usage: python dashboard.py owner/repo-name[/yellow]")
        console.print("[dim]Example: python dashboard.py microsoft/vscode[/dim]")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    if '/' not in repo_path:
        console.print("[red]❌ Invalid format. Use: owner/repo-name[/red]")
        sys.exit(1)
    
    owner, repo = repo_path.split('/', 1)
    display_dashboard(owner, repo)

if __name__ == "__main__":
    main()
