""" Os is imported for executing commands in the terminal. """
import os


def update_dependencies():
    """
    Update various dependencies and tools.

    This function executes a series of commands to update different dependencies and tools.
    The commands include upgrading Deno, Flutter, Git for Windows, Rust, Scoop, Yarn, NPM,
    Firebase, Forever, Grunt CLI, JSHint, Mocha, Node.js, Nodemon, npm-check-updates,
    React Native CLI, TypeScript, Vercel, Sass, Angular CLI, Vue TSC, Concurrently, Yarn,
    PNPM, GitHub Copilot CLI, and the pip package manager for Python.

    Additionally, it also upgrades the OhMyPosh package using the Windows Package Manager (winget).

    Note: Make sure to run this script with appropriate permissions.

    """
    commands = [
        "deno upgrade",
        "flutter upgrade --force",
        "git update-git-for-windows",
        "rustup update",  # Update rust all channels
        "scoop update",
        "scoop update *",
        "yarn set version latest",
        "npm i -g firebase firebase-tools forever grunt-cli jshint mocha node nodemon npm npm-check-updates react-native-cli typescript vercel sass @angular/cli vue-tsc concurrently yarn pnpm @githubnext/github-copilot-cli --force",
        "python.exe -m pip install --upgrade pip",
        "pnpm add -g pnpm",
        "gh extension upgrade gh-copilot",
        "winget upgrade JanDeDobbeleer.OhMyPosh -s winget",
    ]

    for c in commands:
        os.system(c)


# Call the function to update dependencies
update_dependencies()
