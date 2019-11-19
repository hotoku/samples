cat <<EOF | awk '{print NR}'
1
2
3
EOF


cat <<EOF | awk 'NR!=$1{print NR; exit}'
2
3
EOF


cat <<EOF | awk 'NR!=$1{print NR; exit}'
1 a
3 b
EOF
