#!bin/bash

riscv_files=$(ls /tests/benchmarks -a | grep  "\.riscv$")
for file in $riscv_files ; do
  echo "Executing ${file}..." > "/tests/results_riscv.txt"
  /mipt-mips/build/mipt-mips -b /tests/benchmarks/$file --isa riscv64 -d >> "/tests/results_riscv.txt"    
done

isa_files=$(ls /tests/benchmarks -a | grep  "[^\.dump]$")
for file in $isa_files ; do
  echo "Executing ${file}..." > "/tests/results_isa.txt"
  /mipt-mips/build/mipt-mips -b /tests/isa/$file --isa riscv64 -n 800 >> "/tests/results_isa.txt"     
done