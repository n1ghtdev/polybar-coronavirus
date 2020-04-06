# Polybar corona tracker module

[![sample screenshot](https://i.imgur.com/jvdMCrs.png)](https://i.imgur.com/jvdMCrs.png)

Polybar module which displays coronavirus cases/todayCases and
deaths/todayDeaths. Stats is fetching from
[NovelCOVID/API](https://github.com/NovelCOVID/API).

### Dependencies

- Python (>= 3.6)
- Python `requests` module

### Installation

1. Download corona.py

```
curl -O https://raw.githubusercontent.com/n1ghtdev/polybar-coronavirus/master/corona.py
```

2. Give execution permission to corona.py with `chmod +x corona.py`
3. Add module with type=custom/script to polybar config
4. Reload polybar

Example:

```ini
modules-left = corona

[module/corona]
type = custom/script
interval = 3600
exec = ~/.config/polybar/corona.py
```
