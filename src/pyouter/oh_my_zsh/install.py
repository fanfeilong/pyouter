import string
import os
import os.path
import re


def install(config, options):
    base = """#compdef

_pyouter() {
    compls=$(pyouter --tasks)

    completions=(${=compls})
    compadd -- $completions
}

compdef _pyouter pyouter

"""
    command = string.Template("""
_pipeline() {
    compls=$$(python $script --tasks)

    completions=($${=compls})
    compadd -- $$completions
}

compdef _pipeline $script

""")
    script_name = options.script if options.script else "main.py"
    home = os.getenv("HOME")
    plugin_name = "pyouter"
    plugin_dir = os.path.join(home, ".oh-my-zsh/plugins", plugin_name)
    plugin_path = os.path.join(plugin_dir, plugin_name + ".plugin.zsh")
    zshrc = os.path.join(home, ".zshrc")
    regex = re.compile(r"\nplugins=\(.*?\)")

    if not os.path.exists(plugin_dir):
        os.mkdir(plugin_dir)

    with open(zshrc, "r") as f:
        zshrc_content = f.read()

    m = regex.search(zshrc_content)
    if m is None:
        zshrc_content = zshrc_content + f"\nplugins=({plugin_name})\n"
    else:
        plugins_setting = m.group(0)
        if plugin_name not in plugins_setting:
            plugins_setting = plugins_setting[:-1] + f" {plugin_name}" + plugins_setting[-1]
            prev, post = regex.split(zshrc_content)
            zshrc_content = prev + plugins_setting + post

    if os.path.exists(plugin_path):
        with open(plugin_path) as f:
            plugin_content = f.read()
    else:
        plugin_content = ""

    if base not in plugin_content:
        plugin_content = base + plugin_content
    script = command.substitute(script=script_name)
    if script not in plugin_content:
        plugin_content += script

    with open(plugin_path, "w+") as f:
        f.write(plugin_content)

    with open(zshrc, "w+") as f:
        f.write(zshrc_content)
    print("success")
