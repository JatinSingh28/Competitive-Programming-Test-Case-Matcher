import os
import subprocess
import shutil
# import filecmp

base_path = "Test Cases"

cpp_source_file = "a.cpp"
cpp_executable = "program.exe"
compile_cmd = ["g++", cpp_source_file, "-o", cpp_executable]
try:
    subprocess.run(compile_cmd, check=True)
    print(f"Compilation successful. Executable '{cpp_executable}' created.")
except subprocess.CalledProcessError as e:
    print(f"Compilation failed: {e}")

folder = os.listdir(base_path)[0]
path = os.path.join(base_path, folder)

input_files = [f for f in os.listdir(path) if f.endswith(".in")]

shutil.rmtree('Output Files')
os.mkdir("Output Files")

cnt = 0
for file in input_files:
    input_path = os.path.join(path, file)
    output_file = file.replace(".in", ".out")
    input_file_path = os.path.join(path, output_file)
    output_file_path = os.path.join("Output Files", output_file)
    with open(output_file_path, 'w') as f:
        pass

    try:
        output = subprocess.check_output(
            [cpp_executable, "<", input_path], shell=True, text=True)
        with open(output_file_path, 'w') as f:
            f.write(output)
    except subprocess.CalledProcessError as e:
        print(f"Error running C++ executable for {input_path}: {e}")
        continue

    # print(output_file_path,os.path.join(path,output_file))
    # compare = filecmp.cmp(output_file_path,)
    # print(os.path.exists(os.path.join(path,output_file)))
    # if filecmp.cmp(output_file_path, os.path.join(path,output_file)):
    #     print(f"Files {file} is a match!")
    #     cnt += 1
    # else:
    #     print(f"Files {file} is not a match!")

    file1 = open(output_file_path, 'r')
    file2 = open(input_file_path, 'r')

    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
    
    f=1
    for i in range(len(file1_lines)):
        if file1_lines[i] != file2_lines[i]:
            print("Line " + str(i+1) + " doesn't match.")
            print("------------------------")
            print("File1: " + file1_lines[i])
            print("File2: " + file2_lines[i])
            f=0
            break
    if f:
        print(f"Files {file} is a match!")
        cnt+=1
    else:
        print(f"Files {file} is not a match!")
    file1.close()
    file2.close()

ans_folder = "Output Files"

total_testcases = len(os.listdir(ans_folder))
if cnt == total_testcases:
    print("Yayy All test cases passed!")
else:
    print(f"{total_testcases-cnt} test cases failed!")
