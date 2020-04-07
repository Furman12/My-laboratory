import sys
import json
def connector(output_path, *input_files):
    out_dict = dict()   
    for fname in input_files:
        with open(fname, 'r') as infile:
            out_dict[fname] = infile.read()
            
    json_dump = json.dumps(out_dict)
    
    with open(output_path, 'w', encoding='utf-8') as output_file:          
        output_file.write(json.dumps(json_dump,ensure_ascii=False, indent=4))
        
                    
if __name__=="__main__":
    print(connector(sys.argv[1],sys.argv[2]))
#connector('/Users/romafurman/Semester2/programing/L3_255909/data.json','/Users/romafurman/Semester2/programing/L3_255909/file1.txt', '/Users/romafurman/Semester2/programing/L3_255909/file2.txt')


