import os

commands = ["deno upgrade",
            "flutter upgrade --force",
            "git update-git-for-windows",
            "rustup update",
            "scoop update",
            "scoop update *",
            "yarn set version latest",
            "npm i -g firebase firebase-tools forever grunt-cli jshint mocha node nodemon npm npm-check-updates react-native-cli typescript vercel sass @angular/cli vue-tsc concurrently yarn",
            ]

for c in commands:
    os.system(c)
