import string

def install(config, options):
    command = string.Template("""#!/usr/bin/env pyouter.bash
# please save this script into your pyouter.bash completion dir and restart 
# your base or source it use
# . script_name
# in MacOS with home brew, it is /usr/local/etc/bash_completion.d/

_pipeline_router()
{
   COMPREPLY=($(compgen -W "$$(pyouter --tasks)" "$${COMP_WORDS[1]}"))
}

complete -F _pipeline_router pyouter

# if you has used pyouter any old edition, maybe just use below source
_completion_router()
{
   COMPREPLY=($(compgen -W "$$(python $script --tasks)" "$${COMP_WORDS[1]}"))
}

complete -F _completion_router $script
""")
    script_name = options.script if options.script else "__main__.py"
    content = command.substitute(script=script_name)
    print(content)
