import string
import os.path

def install():
    command = string.Template("""#compdef

_pipeline() {
    compls=$$(python $script --tasks)

    completions=($${=compls})
    compadd -- $$completions
}

compdef _pipeline python actions.py
""")
    plugin_dir = "/Users/mars/.oh-my-zsh/plugins/tasks-router"
    plugin_path = os.path.join(plugin_dir, "tasks-router.plugin.zsh")
    if not os.path.exists(plugin_dir):
        os.mkdir(plugin_dir)

    with open(plugin_path, "w+") as f:
        f.write(command.substitute(script="main.py"))
    print("success")