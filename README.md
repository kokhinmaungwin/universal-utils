# Universal Utils

Multi-language utility library for everyday development.

Supports:
- JavaScript
- TypeScript
- Python
- PHP
- Ruby

---

## ✨ Features

- String capitalize
- Date formatting
- Debounce / Throttle helpers
- Clipboard copy helpers (where supported)
- Simple and lightweight

---

## 📂 Project Structure

- utils.ts  → TypeScript / JavaScript utilities
- utils.py  → Python utilities
- utils.php → PHP utilities
- utils.rb  → Ruby utilities

---

## 🚀 Usage Examples

### JavaScript / TypeScript
```js
import { capitalize, formatDate } from "./utils";

console.log(capitalize("hello")); // Hello
console.log(formatDate(new Date())); // 2026-01-03
```
### Python
```bash
from utils import capitalize, format_date
print(capitalize("hello"))
print(format_date(datetime.now()))
```
### PHP
```bash
require 'utils.php';
echo capitalize("hello");
```
### Ruby
```bash
require "./utils"
puts capitalize("hello")
```

---

## 💾 Installation

### JavaScript / TypeScript (via npm)

```bash
npm install @kokhinmaungwin/universal-utils-v2
```

### Python (via pip)

```bash
pip install universal-utils
```

### PHP (via Composer)

```bash
composer require kokhinmaungwin/universal-utils
```

### Ruby (via Gem)

```bash
gem install universal-utils
```

---

## 🚀 Usage Examples (with package imports)

### JavaScript / TypeScript
```js
import { capitalize, formatDate } from "@kokhinmaungwin/universal-utils-v2";

console.log(capitalize("hello")); // Hello
console.log(formatDate(new Date())); // 2026-01-03
```
### Python
```Py
from universal_utils import capitalize, format_date
print(capitalize("hello"))
print(format_date(datetime.now()))
```
### PHP
```Php
require 'vendor/autoload.php'; // Assuming installed via composer
echo capitalize("hello");
```
### Ruby
```Rb
require "universal-utils"
puts capitalize("hello")
```

---

## 🛠 Future Plans

- More string helpers
- Number utilities
- Array utilities
- Validation helpers
- Unit tests
- Package publishing to npm / PyPI / Composer / RubyGems

---

## 📅 Changelog

### v1.0.3 (2026-01-05)
- Fixed Rollup build config
- Added minified bundle
- Updated README and usage examples

---

## 📞 Contact / Support

If you encounter any issues or have questions, please open an issue on GitHub:
[https://github.com/kokhinmaungwin/universal-utils/issues](https://github.com/kokhinmaungwin/universal-utils/issues)

---

## 📄 License

MIT License
