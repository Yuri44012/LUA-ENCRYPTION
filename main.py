from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    obfuscated_script = ""
    if request.method == "POST":
        script = request.form["script"]
        with open("input.lua", "w") as f:
            f.write(script)

        # Call LuaSrcDiet obfuscator
        cmd = ["lua", "LuaSrcDiet.lua", "input.lua", "-o", "output.lua"]
        subprocess.run(cmd)

        if os.path.exists("output.lua"):
            with open("output.lua", "r") as f:
                obfuscated_script = f.read()

            os.remove("output.lua")
        os.remove("input.lua")

    return render_template("index.html", obfuscated_script=obfuscated_script)
