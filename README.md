# Polybar corona tracker module

[![sample screenshot](https://i.imgur.com/jvdMCrs.png)](https://i.imgur.com/jvdMCrs.png)

Polybar module which displays coronavirus cases/todayCases and
deaths/todayDeaths. Stats being fetched from
[NovelCOVID/API](https://github.com/NovelCOVID/API).

### Dependencies

- Python (>= 3.6)
- Python `requests` module

### Installation

1. Download corona.py
2. Add module as custom/script to polybar config

Example:

```ini
modules-left = corona

[module/corona]
type = custom/script
interval = 3600
exec = ~/.config/polybar/corona.py
```
