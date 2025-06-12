#!/bin/bash
set -e

# Jenkins env vars
TARGET_HOST="${TARGET_HOST}"
SSH_USER="${SSH_USER}"
SSH_PASS="${SSH_PASS}"

# Validación básica
if [[ -z "$TARGET_HOST" || -z "$SSH_USER" || -z "$SSH_PASS" ]]; then
  echo "Faltan variables: TARGET_HOST, SSH_USER, SSH_PASS"
  exit 1
fi

# Generar inventory.ini dinámicamente
cat > inventory.ini <<EOF
[target]
$TARGET_HOST ansible_user=$SSH_USER ansible_password=$SSH_PASS ansible_port=22 ansible_connection=ssh
EOF

# Ejecutar el playbook
ansible-playbook setup_nodo_base.yml