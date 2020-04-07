import sys
import json
def connector(output_path: str, input_files: list):
    out_dict = dict()
    for fname in input_files:
        print(fname)
        with open(fname, 'r') as infile:
            out_dict[fname] = infile.read()
            
    json_dump = json.dumps(out_dict)
    
    with open(output_path, 'w', encoding='utf-8') as output_file:          
        output_file.write(json.dumps(json_dump,ensure_ascii=False, indent=4))
        
                    
if __name__ == "__main__":
    connector(sys.argv[1],sys.argv[2:])


# python3 zad_1,2.py arch.json t1.txt t2.txt 