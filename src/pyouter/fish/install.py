import string
import os
import os.path


def install(config, options):
    command = string.Template("""#!/usr/bin/env pyouter.fish

complete -c __main__.py -f
complete -c __main__.py -a "(python $script --tasks)"
""")
    script_name = options.script if options.script else "__main__.py"
    home = os.getenv("HOME")
    plugin_dir = os.path.join(home, ".config/pyouter.fish/completion")
    plugin_path = os.path.join(plugin_dir, script_name + ".pyouter.fish")

    if not os.path.exists(plugin_dir):
        os.mkdir(plugin_dir)

    with open(plugin_path, "w+") as f:
        f.write(command.substitute(script=script_name))

    print("success")
