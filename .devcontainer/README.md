# Python 3.12 Dev Container

This is a development container for Python 3.12 with the following features:

- A non-root user called `user` with password `user` and sudo access.
- Python 3.12.
- Updated pip.
- A virtual environment created in ~/venv.
- Terminals automatically have the venv activated.
- Zsh as the default shell.
- Oh My Zsh using the `robbyrussell` theme.
- Passthrough .ssh keys from the host ssh agent (both PC and Mac).
- VS Code extensions for Python and Jupyter notebooks.
- The working directory on the host is mapped to ~/dbg_sandbox.
- venv is the default Python environment.
- The following Python libraries are installed: pytest, flit, jupyter, ipykernel.

