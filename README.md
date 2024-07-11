# Pyouter

Pyouter is a tasks router by  hierarchy and layered tasks, which may come from command line or http restful api

![pyouter](pyouter.gif)

## INSTALL

First, install pyouter

```shell
pip install pyouter
```

and then, you can install your shell completion support

```shell
pyouter install.ohmyzsh
```

or

```shell
pyouter install.bash
```

or

```shell
pyouter install.fish
```

Default script name is `main.py` 。Now it support bash, fish and zsh with oh-my-zsh .

## What's new

### 0.0.8

- add app.option support
- improve App(config=), support config patth

### 0.0.7

- add pyouter self completion of bash and fish

### 0.0.6

- fixed bug in fish completion install

### 0.0.5

- pass config if need

### 0.04

- custom parser

### 0.0.3

- support pyouter completion
- pyouter as entry points of package

### 0.0.2

- rename plugin to pyouter

### 0.0.1

- project init
- add pypi settings
- add installer
