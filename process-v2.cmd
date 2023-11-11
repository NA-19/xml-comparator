cmd /c yq3 "walk(if type == \"object\" then with_entries(select(.key |= match(\"^@\"))) | to_entries | sort_by(.key) | from_entries else . end)" input1.xml > input1-canonical.xml
cmd /c yq3 "walk(if type == \"object\" then with_entries(select(.key |= match(\"^@\"))) | to_entries | sort_by(.key) | from_entries else . end)" input2.xml > input2-canonical.xml
