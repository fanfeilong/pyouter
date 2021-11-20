#!/usr/bin/env bash

_completion_router()
{
   COMPREPLY=($(compgen -W "$(python main.py --tasks)" "${COMP_WORDS[1]}"))
}

complete -F _completion_router main.py
