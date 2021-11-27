import string
import os
import os.path


def install(config, options):
    base = """!/usr/bin/env fish
complete -c pyouter -f
complete -c pyouter -a "(python pyouter --tasks)"
    """
    command = string.Template("""
complete -c $script -f
complete -c $script -a "(python $script --tasks)"
""")
    script_name = options.script if options.script else "main.py"
    home = os.getenv("HOME")
    plugin_dir = os.path.join(home, ".config/fish/completions")
    plugin_path = os.path.join(plugin_dir, script_name + ".fish")

    if not os.path.exists(plugin_dir):
        os.mkdir(plugin_dir)

    content = ""
    if os.path.exists(plugin_path):
        with open(plugin_path) as f:
            content = f.read()

    if not content.startswith(base):
        content = base + content

    plugin = command.substitute(script=script_name)
    if plugin not in content:
        content += plugin

    with open(plugin_path, "w+") as f:
        f.write(content)

    print("success")
