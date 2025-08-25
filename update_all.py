import os
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
        "npm i -g firebase firebase-tools node nodemon npm typescript vercel pnpm @githubnext/github-copilot-cli bun wrangler --force",
        "pnpm add -g pnpm genkit-sli",
        "composer global require laravel/installer",
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


def update_project_dependencies():
    """
    Update project dependencies.
    This function executes a series of commands to update the dependencies of the current project.
    The commands include upgrading the dependencies of the project using the package manager of the project.
    """
    # Define project paths and their respective commands

    jsCommands = ["npx npm-check-updates -u", "bun i --save-text-lockfile"]
    flutterCommands = [
        "flutter pub upgrade --major-versions",
        "flutter pub upgrade --tighten",
        "flutter analyze",
        "flutter test",
    ]

    projects = [
        {
            "commands": jsCommands,
            "path": [
                "C:\\Users\\Rohit Jain\\Documents\\methicollection_admin",
                "C:\\Users\\Rohit Jain\\Documents\\methicollection",
                "D:\\Projects\\queue-box-desktop",
                "D:\\Projects\\kingtechnologies.dev\\kingtechnologies.dev",
                "D:\\Projects\\rohit19060.github.io",
                "D:\\Projects\\typing-friend\\typing-friend",
            ],
        },
        {
            "commands": flutterCommands,
            "path": [
                "D:\\Projects\\king_cache\\king_cache",
                "D:\\Projects\\line_up\\lineup",
                # "D:\\Projects\\kaushal\\kaushal",
                "D:\\Projects\\tech_book\\tech_book_mobile",
            ],
        },
    ]

    # Create a list of all commands with their project context for the progress bar
    all_commands = []
    for project in projects:
        for cmd in project["path"]:
            for command in project["commands"]:
                all_commands.append((cmd, command))
    # Create a progress bar
    progress_bar = tqdm(all_commands, unit="command", colour="blue")
    # Execute each command in its respective directory
    for project_path, command in progress_bar:
        # Get just the folder name for cleaner display
        folder_name = os.path.basename(project_path)
        progress_bar.set_description(f"[{folder_name}] Running: {command}")

        try:
            # Run the command in the appropriate directory
            process = subprocess.run(
                command,
                shell=True,
                check=True,
                text=True,
                encoding="utf-8",
                capture_output=True,
                cwd=project_path,  # Set the working directory for this command
            )
            print(f"\n[{folder_name}] Output from '{command}':")
            print(process.stdout)
        except subprocess.CalledProcessError as e:
            print(f"\n[{folder_name}] Error running '{command}': {e}")
            print(e.stderr)
        except FileNotFoundError:
            print(f"\n[{folder_name}] Directory not found: {project_path}")
        except UnicodeDecodeError as e:
            print(f"\n[{folder_name}] Error decoding output: {e}")
            print(e)
        except Exception as e:
            print(f"\n[{folder_name}] An error occurred: {e}")
            print(e)


if __name__ == "__main__":
    # update_dependencies()
    update_project_dependencies()
