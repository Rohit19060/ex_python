import os

commands = ["deno upgrade",
            "flutter upgrade --force",
            "git update-git-for-windows",
            "heroku update",
            "npm i -g create-react-app firebase firebase-tools forever grunt-cli jshint mocha node nodemon npm npm-check-updates react-native-cli typescript vercel @vue/cli sass",
            "rustup update",
            "scoop update",
            "scoop update *",
            "yarn set version latest"]

for c in commands:
    os.system(c)
