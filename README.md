# PyLaunchAgent

- [PyLaunchAgent](#pylaunchagent)
  - [About](#about)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Configuration](#configuration)
    - [Running](#running)

## About

Install Python code to macOS LaunchAgents. This is project is meant for personal use; documentation and testing is missing.

## Installation

```sh
pip install git+https://github.com/leonardcser/pylaunchagent
```

## Usage

### Configuration

There are two options:

1. Use command line args
2. Use config file (`pylaunchagent.yaml` - recommended)

You can see the list of all command with:

```sh
pylaunchagent -h
```

### Running

There are 4 sub-commands available:

-   `install`
-   `uninstall`
-   `status`
-   `logs`

```sh
pylaunchagent <SUB-COMMAND> <OPTIONS>
```
