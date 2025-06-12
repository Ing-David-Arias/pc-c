#!/bin/bash

VAULT_PASS="${VAULT_PASS:-vault123}"  # Puedes inyectar esto como variable en Jenkins

ansible-playbook playbook.yml --ask-vault-pass <<EOF
$VAULT_PASS
EOF