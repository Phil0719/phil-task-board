#!/bin/bash
echo "===== Running todo.py ====="
python3 /app/.github/scripts/todo.py | tee /app/todo_output.txt

echo "===== Running unit tests ====="
python3 /app/.github/scripts/todo-test.py | tee /app/test_output.txt

echo "===== Updating index.html ====="
bash /app/.github/scripts/update_index.sh /app/todo_output.txt /app/test_output.txt

echo "===== Task board updated ====="
