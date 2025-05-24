import sys
import argparse
from urllib.parse import urlparse, unquote

def extract_domain_and_paths(url, max_path_length=20):
    parsed_url = urlparse(url)
    domain = parsed_url.scheme + "://" + parsed_url.netloc

    raw_path = unquote(parsed_url.path).strip('/')
    if not raw_path or raw_path.strip() == '':
        return None

    path_parts = [part for part in raw_path.split('/') if part.strip()]
    
    # Проверяем, что длина пути не превышает максимальное значение
    path = '/' + '/'.join(path_parts)
    if len(path) > max_path_length:
        return None

    return domain, path_parts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract domains and paths from URLs.")
    parser.add_argument("input_file", help="File with list of URLs")
    parser.add_argument("output_file", help="Output file prefix")
    parser.add_argument("-m", "--maxlen", type=int, default=20, help="Max path length (default: 20)")

    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        urls = file.readlines()

    # Для каждой глубины создаём пустой set
    unique_paths = {}

    for url in urls:
        url = url.strip()
        if not url:
            continue

        result = extract_domain_and_paths(url, max_path_length=args.maxlen)
        if result:
            domain, path_parts = result
            depth = len(path_parts)
            
            if depth not in unique_paths:
                unique_paths[depth] = set()

            path = domain + '/' + '/'.join(path_parts)
            unique_paths[depth].add(path)

    # Записываем результаты в файлы для каждой глубины
    for depth, paths in unique_paths.items():
        output_path = f"{args.output_file}{depth}.txt"
        with open(output_path, "w") as out:
            for entry in sorted(paths):
                out.write(entry + "\n")
        
        print(f"✓ Extracted {len(paths)} unique paths at depth {depth}")
        print(f"→ Saved to: {output_path}")
