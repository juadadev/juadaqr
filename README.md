# juadaqr

> Generate QR codes from your terminal with a simple command

## Features

- Instantly generates QR codes from any URL
- Simple command line interface
- Fast and lightweight
- Clean, formatted output
- Easy one-command installation


## Installation

### Quick Installation (recommended)

```bash
curl -LsSf https://github.com/juadadev/juadaqr/releases/download/v0.3.0/install.sh | sh
```

## After Installation
> If the command is not recognized, add ~/.local/bin to your PATH:

**For bash/zsh:**
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**For fish**
```bash
fish_add_path ~/.local/bin
```

**Other option**
```bash
uv tool update-shell
```

## Verify installation
```bash
juadaqr --version
```

## Use
```bash
juadaqr <url>
```

## Example:
```bash
juadaqr https://github.com/juadadev
```
