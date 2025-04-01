# Smart Compiler

This **Smart Compiler** uses AI models and traditional compiler techniques to enhance the performance scalability of **C** programs. By determining the optimal transformations for each section of code, it can profile, optimize, and output new versions of your applications.

---

## 1. Overview

- **Component Description**:  
  This compiler framework develops or uses existing AI models to decide what transformations to apply to a given C program. Its goal is to improve performance scalability by analyzing code sections and applying optimizations accordingly.

- **Diagrams**:  
  - [Diagram 1](https://drive.google.com/file/d/1S5gRxw_vizR1XnmbiZnAH1yZnkB8Ep0_/view?usp=drive_link)  
  - [Diagram 2](https://drive.google.com/file/d/1tgCcINlzBUe6A1PCNX6R_ftAnb9WidcA/view?usp=sharing)

---

## 2. Requirements

1. **Standard C libraries** in the runtime environment  
2. **Java Runtime Environment** (≥ 1.8)  
3. **gcc** (> 4.5.0, e.g. `gcc/11.2.0`)  
4. **anaconda/2023.03**  
5. **cuda/12.1.1**  
6. **papi/5.4.3**  
7. **Parot_jdk** or **jdk/17.0.9**  
8. **Cetus**  
9. **python3_11**  

**Input Pre-conditions**: All input programs must be **valid C** programs.

---

## 3. Installation

1. **Obtain Source**: Clone or download this repository.  
2. **Check Dependencies**: Ensure the above requirements (Java, gcc, Python, etc.) are installed and available in your environment.  
3. **Install or Configure**: If needed, install **Cetus** and any additional environment modules (e.g., `papi`, `cuda`) required for your target system.  
4. **Edit Environment Variables**: Update `.env` in the project’s root (see [Environment Variables](#5-environment-variables)).  
5. **Run the Compiler**: Execute `run_all.py` as described below.

---

## 4. Usage

### Changing LLM Prompts
If you want to modify the prompts used by AI/LLMs:

Go to "/current_folder/pcaot/prompts" and Edit these files to adjust how the models interpret or transform your source code.


### Component Run
1. **CSV Plan**: Create or edit `planning/experiments_plans_caviness_demo.csv` with the following **semicolon-separated** structure:


- **bench**: Name of the benchmark or test  
- **#trials**: Number of runs or trials  
- **DATASET**: Small, Medium, or Large  
- **parent_folder**: Folder where your target C program is located  
- **kernel_folder**: Folder containing kernels (if applicable)  
- **target_source_code**: Filename of the target C application  
- **binary_placeholder**: Directory where the compiled/optimized binary will be placed  
- **expected_bin_name**: Name for the output binary

2. **Run the Script**:
```bash
python src/run_all.py planning/experiments_plans_caviness_demo.csv
```

### Component Output

## Component Output
The output can be:
1. The optimized version of the target C application **or**  
2. Profiling information, depending on what the user wants to do.

The output is stored in: /currentPath/kernel_folder/Target_source_code/binary_place/expected_bin_name

The report is stored in: /currentPath/run_all_backup.log


## Environment Variables
The environment variables are located in:
You must modify the environment variables. For example:
```bash
OPENAI_API_URL=
OPENAI_API_KEY=
HugginFace_TOKEN=
HuggingFace_URL= 
HuggingFace_URL= 
PCAOT_DIR=
MONGO_USER=
MONGO_PASSWORD=
MONGO_URI=
MONGO_DB_NAME=
LOG_LEVEL=
EXECUTION_ENV='hpc' #or hpc
INVALIDATE_COMPILATION_CHECKPOINTS="true"
AOTS_CONFIG_FILE="/currentFile/config/caviness_demo_aots.json"

```

### Thank you for using Smart Compiler!
For further details, refer to the diagrams linked above, the .env configuration, or contact the project maintainers.









