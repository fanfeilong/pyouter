import string
import os
import os.path
import re


def install(config, options):
    command = string.Template("""#compdef

_pipeline() {
    compls=$$(python $script --tasks)

    completions=($${=compls})
    compadd -- $$completions
}

compdef _pipeline $script
""")
    script_name = options.script if options.script else "main.py"
    home = os.getenv("HOME")
    plugin_name = "tasks-router"
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
        if "tasks-router" not in plugins_setting:
            plugins_setting = plugins_setting[:-1] + f" {plugin_name}" + plugins_setting[-1]
            prev, post = regex.split(zshrc_content)
            zshrc_content = prev + plugins_setting + post

    with open(plugin_path, "w+") as f:
        f.write(command.substitute(script=script_name))

    with open(zshrc, "w+") as f:
        f.write(zshrc_content)
    print("success")
