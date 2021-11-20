import string
import os
import os.path


def install(config, options):
    command = string.Template("""#!/usr/bin/env bash
# please save this script into your bash completion dir and restart 
# your base or source it use
# . script_name
# in MacOS with home brew, it is /usr/local/etc/bash_completion.d/

_completion_router()
{
   COMPREPLY=($(compgen -W "$$(python $script --tasks)" "$${COMP_WORDS[1]}"))
}

complete -F _completion_router $script
""")
    script_name = options.script if options.script else "main.py"
    content = command.substitute(script=script_name)
    print(content)
