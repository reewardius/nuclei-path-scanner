### 🔪 Slicer (Nuclei Path Vulnerability Scanning)

**Slicer** is a lightweight Python tool designed to extract unique URL paths at different depths from a list of URLs. When used alongside katana and nuclei, it provides an efficient way to focus vulnerability scans on meaningful endpoints, enhancing performance and results.

#### ⚡ 1. Crawl URLs with Katana

Use Katana to discover active HTTP services and extract potential URL paths.

```bash
katana -u alive_http_services.txt -ct 3m -ef js,png,css,jpeg,jpg,woff2 -c 50 -p 50 -rl 300 -d 5 -iqp -o katana.txt
```
#### 🧠 2. Slice URLs by Path Depth

Run the slicer.py script to categorize URLs by their path depth. It removes unnecessary static files and organizes paths into separate files.
```
python3 slicer.py katana.txt slicer; cat slicer*.txt > combined.txt
```
#### 🗂️ Output Example
```
✓ Extracted 923 unique paths at depth 1
→ Saved to: slicer1.txt
✓ Extracted 807 unique paths at depth 2
→ Saved to: slicer2.txt
✓ Extracted 717 unique paths at depth 3
→ Saved to: slicer3.txt
✓ Extracted 92 unique paths at depth 4
→ Saved to: slicer4.txt
```
#### 🔍 3. Scan with Nuclei

📍 The true power of this workflow lies in its granular control over vulnerability scanning. By slicing discovered URLs into groups based on path depth, you can:

- Prioritize scanning of shallow, more critical entry points first
- Focus efforts on deeper, potentially overlooked endpoints
- Run parallel scans for better efficiency and coverage

✅ Each output file (`slicer1.txt`, `slicer2.txt`, etc.) represents a distinct level of URL path depth, enabling you to run Nuclei with precision:
```
nuclei -l slicer1.txt -rl 1000 -c 100 -stats -si 60 -o nuclei_path1_results.txt
nuclei -l slicer2.txt -rl 1000 -c 100 -stats -si 60 -o nuclei_path2_results.txt
...
nuclei -l combined.txt -rl 1000 -c 100 -stats -si 60 -o nuclei_combined_results.txt
```
---
🧩 Script Details

This script `slicer.py`:

- Parses URLs from a file
- Extracts domain and path parts
- Categorizes them by depth
- Filters out overly long paths
- Outputs results in separate files
```bash
python3 slicer.py <input_file> <output_prefix> [-m MAX_LENGTH]
```
- `input_file`: File containing URLs
- `output_prefix`: Prefix for output files (e.g., slicer)
- `-m, --maxlen`: Optional, default is 20
