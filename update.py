import platform
import subprocess

from tqdm import tqdm

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    except subprocess.CalledProcessError:
        print(f"No update available for {command}")

def update_dependencies():
    """
    Update various dependencies and tools.
    This function executes a series of commands to update different dependencies and tools.
    The commands include upgrading Deno, Flutter, Git for Windows, Rust, Scoop, NPM,
    Firebase, Forever, Grunt CLI, JSHint, Mocha, Node.js, Nodemon, npm-check-updates,
    React Native CLI, TypeScript, Vercel, Sass, Angular CLI, Vue TSC, Concurrently,
    PNPM, GitHub Copilot CLI, and the pip package manager for Python.
    """
    os_name = platform.system().lower()

    common_commands = [
        "deno upgrade",
        "flutter upgrade --force",
        "rustup update",
        "npm i -g vitest firebase firebase-tools node nodemon npm typescript vercel pnpm @githubnext/github-copilot-cli bun wrangler drizzle-kit drizzle-orm  @google/gemini-cli --force",
        # "pnpm add -g pnpm genkit-sli",
        # "composer global require laravel/installer",
        "gh extension upgrade gh-copilot",
    ]

    windows_commands = [
        "git update-git-for-windows",
        "scoop update",
        "scoop update *",
        "python.exe -m pip install --upgrade pip",
        "winget upgrade JanDeDobbeleer.OhMyPosh -s winget",
        "winget upgrade Cloudflare.cloudflared -s winget",
        "choco upgrade make -y",
    ]

    macos_commands = [
        "brew update",
        "brew upgrade",
        "pip3 install --upgrade pip",
        "brew upgrade oh-my-posh",
        "brew upgrade cloudflared",
    ]

    linux_commands = [
        "curl -f https://zed.dev/install.sh | sh",
        "sudo apt-get update",
        "sudo apt-get upgrade -y",
        "pip3 install --upgrade pip",
    ]

    commands_to_run = common_commands.copy()

    if os_name == "windows":
        commands_to_run.extend(windows_commands)
    elif os_name == "darwin":
        commands_to_run.extend(macos_commands)
    elif os_name == "linux":
        commands_to_run.extend(linux_commands)

    progress_bar = tqdm(commands_to_run, unit="command", colour="green")

    fixed_width = 20

    for command in progress_bar:
        command_description = (
            (command[:fixed_width] + "...")
            if len(command) > fixed_width
            else command.ljust(fixed_width)
        )
        progress_bar.set_description(f"Running: {command_description}")
        run_command(command)

if __name__ == "__main__":
    update_dependencies()
