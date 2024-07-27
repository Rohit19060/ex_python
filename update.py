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
    The commands include upgrading Deno, Flutter, Git for Windows, Rust, Scoop, Yarn, NPM,
    Firebase, Forever, Grunt CLI, JSHint, Mocha, Node.js, Nodemon, npm-check-updates,
    React Native CLI, TypeScript, Vercel, Sass, Angular CLI, Vue TSC, Concurrently, Yarn,
    PNPM, GitHub Copilot CLI, and the pip package manager for Python.
    """
    os_name = platform.system().lower()

    common_commands = [
        "deno upgrade",
        "flutter upgrade --force",
        "rustup update",  # Update Rust for all channels
        "pnpm add -g pnpm",
        "yarn set version latest",
        "npm i -g firebase firebase-tools forever grunt-cli jshint mocha node nodemon npm npm-check-updates react-native-cli typescript vercel sass @angular/cli vue-tsc concurrently yarn pnpm @githubnext/github-copilot-cli --force",
        "composer global require laravel/installer",
    ]

    windows_commands = [
        "git update-git-for-windows",
        "scoop update",
        "scoop update *",
        "python.exe -m pip install --upgrade pip",
        "gh extension upgrade gh-copilot",
        "winget upgrade JanDeDobbeleer.OhMyPosh -s winget",
        "winget upgrade Cloudflare.cloudflared -s winget",
        "choco upgrade make -y",
    ]

    macos_commands = [
        "brew update",
        "brew upgrade",
        "pip3 install --upgrade pip",
        "gh extension upgrade gh-copilot",
        "brew upgrade oh-my-posh",
        "brew upgrade cloudflared",
    ]

    linux_commands = [
        "sudo apt-get update",
        "sudo apt-get upgrade -y",
        "pip3 install --upgrade pip",
        "gh extension upgrade gh-copilot",
        "curl -s https://bun.sh/install | bash",  # Bun installation/upgrade
    ]

    commands_to_run = common_commands.copy()

    if os_name == "windows":
        commands_to_run.extend(windows_commands)
    elif os_name == "darwin":  # macOS
        commands_to_run.extend(macos_commands)
    elif os_name == "linux":
        commands_to_run.extend(linux_commands)

    for command in tqdm(
        commands_to_run, desc="Updating dependencies", unit="command", colour="green"
    ):
        run_command(command)


if __name__ == "__main__":
    update_dependencies()
