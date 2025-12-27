<div align="center">
<img src="https://github.com/sepandhaghighi/clox/raw/main/otherfiles/logo.png" width="450">
<h1>Clox: A Geeky Clock for Terminal Enthusiasts</h1>
<br/>
<a href="https://badge.fury.io/py/clox"><img src="https://badge.fury.io/py/clox.svg" alt="PyPI version"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
<a href="https://github.com/sepandhaghighi/clox"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/sepandhaghighi/clox"></a>
</div>			
				
## Overview	

<p align="justify">					
Clox is a terminal-based clock application designed for terminal enthusiasts who appreciate simplicity, elegance, and productivity within their command-line environment. Whether you're coding, monitoring tasks, or simply enjoying the terminal aesthetic, Clox brings a stylish and customizable time display to your workspace.
</p>

<table>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/clox"><img src="http://pepy.tech/badge/clox"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/clox"><img src="https://img.shields.io/github/stars/sepandhaghighi/clox.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">main</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/clox/actions/workflows/test.yml/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/clox/actions/workflows/test.yml/badge.svg?branch=dev"></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/clox"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/clox/badge" alt="CodeFactor"></a></td>
		<td align="center"><a href="https://app.codacy.com/gh/sepandhaghighi/clox/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/4cd4cd3b20b1474fb674823b1b417b76"></a></td>
	</tr>
</table>


## Installation		

### Source Code
- Download [Version 1.5](https://github.com/sepandhaghighi/clox/archive/v1.5.zip) or [Latest Source](https://github.com/sepandhaghighi/clox/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install clox==1.5`						


## Usage

ℹ️ You can use `clox` or `python -m clox` to run this program

### Version

```console
clox --version
```

### Info

```console
clox --info
```

### Basic

ℹ️ Press `Ctrl + C` to exit

```console
clox
```

### Face

```console
clox --face=3
```
* Use `--face=-1` for random mode
* [Faces List](https://github.com/sepandhaghighi/clox/blob/main/FACES.md): `clox --faces-list`


### Timezone

```console
clox --timezone="Etc/GMT+7"
```
* [Timezones List](https://github.com/sepandhaghighi/clox/blob/main/TIMEZONES.md): `clox --timezones-list`


### Manual Offset

ℹ️ The local and timezone offset both have default values of `0`

These arguments allow you to manually adjust the time by ±X hours. This is especially useful when daylight saving time (DST) is not correctly applied by the system or timezone database.

```console
clox --offset-local=1 --offset-timezone=-1
```

### Country

The `--country` argument allows you to specify a country using its **ISO 3166** code format

ℹ️ When the `--country` argument is provided, the `--timezone` argument will be ignored

ℹ️ If the specified country has multiple timezones, the first timezone will be selected automatically

```console
clox --country="DE"
```
* [Countries List](https://github.com/sepandhaghighi/clox/blob/main/COUNTRIES.md): `clox --countries-list`


### Vertical/Horizontal Shift

ℹ️ The vertical and horizontal shift both have default values of `0`

```console
clox --v-shift=20 --h-shift=30
```

### No Blink

Disable blinking mode

```console
clox --no-blink
```

### Once

Print current time once and exit immediately

```console
clox --once
```

### Hide Date

In this mode, the date will not be shown

```console
clox --hide-date
```

### Hide Timezone

In this mode, the timezone will not be shown

```console
clox --hide-timezone
```

### AM/PM Mode

In this mode, the clock will be displayed in 12-hour format

```console
clox --am-pm
```

### Vertical Mode

```console
clox --vertical
```

### Calendar Mode

In this mode, the calendar will be displayed

ℹ️ Valid choices: [`MONTH`, `YEAR`]

```console
clox --calendar=month --first-weekday="SUNDAY"
```

### Date System

ℹ️ Valid choices: [`GREGORIAN`, `JALALI`]

ℹ️ The default date system is `GREGORIAN`

```console
clox --date-system=jalali
```

### Date Format

ℹ️ Valid choices: [`ISO`, `US`, `US-SHORT`, `EU`, `EU-SHORT`, `DOT`, `DASH`, `YMD`, `DMY`, `MDY`, `FULL`]

ℹ️ The default date format is `FULL`

```console
clox --date-system=jalali --date-format=EU
```
* Date Formats List: `clox --date-formats-list`

### Color

⚠️ This mode may not be supported on all systems

ℹ️ Valid choices: [`BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`, `LIGHTBLACK`, `LIGHTRED`, `LIGHTGREEN`, `LIGHTYELLOW`, `LIGHTBLUE`, `LIGHTMAGENTA`, `LIGHTCYAN`, `LIGHTWHITE`]

ℹ️ The default color is `WHITE`

```console
clox --date-system=jalali --color="red"
```

### Background Color

⚠️ This mode may not be supported on all systems

ℹ️ Valid choices: [`BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`, `LIGHTBLACK`, `LIGHTRED`, `LIGHTGREEN`, `LIGHTYELLOW`, `LIGHTBLUE`, `LIGHTMAGENTA`, `LIGHTCYAN`, `LIGHTWHITE`]

ℹ️ The default background color is `BLACK`

```console
clox --date-system=jalali --color="red" --bg-color="blue"
```

### Intensity

⚠️ This mode may not be supported on all systems

ℹ️ Valid choices: [`NORMAL`, `BRIGHT`, `DIM`]

ℹ️ The default intensity is `NORMAL`

```console
clox --color="red" --intensity="bright"
```

## Screen Record

<div align="center">

<img src="https://github.com/sepandhaghighi/clox/raw/main/otherfiles/help.gif">

</div>

## Try Clox Online!

Clox can be used online in interactive Jupyter Notebooks via the Binder or Colab services! Try it out now! :

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sepandhaghighi/clox/main)

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sepandhaghighi/clox/blob/main)

- Open `notebook.ipynb`

## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template
 			

## Show Your Support
								
<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to Our Project</h3>	

<h4>Bitcoin</h4>
1KtNLEEeUbTEK9PdN6Ya3ZAKXaqoKUuxCy
<h4>Ethereum</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Litecoin</h4>
Ldnz5gMcEeV8BAdsyf8FstWDC6uyYR6pgZ
<h4>Doge</h4>
DDUnKpFQbBqLpFVZ9DfuVysBdr249HxVDh
<h4>Tron</h4>
TCZxzPZLcJHr2qR3uPUB1tXB6L3FDSSAx7
<h4>Ripple</h4>
rN7ZuRG7HDGHR5nof8nu5LrsbmSB61V1qq
<h4>Binance Coin</h4>
bnb1zglwcf0ac3d0s2f6ck5kgwvcru4tlctt4p5qef
<h4>Tether</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Dash</h4>
Xd3Yn2qZJ7VE8nbKw2fS98aLxR5M6WUU3s
<h4>Stellar</h4>		
GALPOLPISRHIYHLQER2TLJRGUSZH52RYDK6C3HIU4PSMNAV65Q36EGNL
<h4>Zilliqa</h4>
zil1knmz8zj88cf0exr2ry7nav9elehxfcgqu3c5e5
<h4>Coffeete</h4>
<a href="http://www.coffeete.ir/opensource">
<img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:260px;" />
</a>

