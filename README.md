#### Slicer (Nuclei Path Vulnerability Scanning)

```bash
katana -u alive_http_services.txt -ct 3m -ef js,png,css,jpeg,jpg,woff2 -c 50 -p 50 -rl 300 -d 5 -iqp -o katana.txt
python3 slicer.py katana.txt slicer; cat slicer*.txt > combined.txt
```
#### Expected Output
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
#### Nuclei Slicer Scanner
```
nuclei -l slicer1.txt -itags config,exposure -s medium,high,critical -rl 1000 -c 100 -stats -si 60 -o nuclei_path_results.txt
nuclei -l combined.txt -itags config,exposure -s medium,high,critical -rl 1000 -c 100 -stats -si 60 -o nuclei_path_results.txt
```
