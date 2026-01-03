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

## 🛠 Future Plans

- More string helpers
- Number utilities
- Array utilities
- Validation helpers
- Unit tests
- Package publishing to npm / PyPI / Composer / RubyGems

---

## 📄 License

MIT License
