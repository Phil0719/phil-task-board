#!/bin/bash
TASK_FILE=$1
TEST_FILE=$2
HTML_FILE=index.html

TODO=$(sed -n '/ToDo Tasks:/,/^$/p' "$TASK_FILE" | grep -v "ToDo Tasks:" | sed '/^$/d')
DONE=$(awk '/Done Tasks:/{found=1; next} found' "$TASK_FILE")
UNIT_TEST_RESULTS=$(cat "$TEST_FILE")

update_pre() {
  local id="$1"
  local content="$2"
  local file="$3"
  CONTENT="$content" perl -0pi -e 's|(<pre id="'"$id"'">).*?(</pre>)|$1$ENV{CONTENT}$2|s' "$file"
}

update_pre "pending" "$TODO" "$HTML_FILE"
update_pre "completed" "$DONE" "$HTML_FILE"
update_pre "unittest" "$UNIT_TEST_RESULTS" "$HTML_FILE"

git config --global user.name "github-actions"
git config --global user.email "github-actions@users.noreply.github.com"
git config --global --add safe.directory /app
git add "$HTML_FILE"
git commit -m "Update task board page for $GITHUB_USER" || echo "No changes to commit"
git push origin main
