# Script WLST para crear un dominio básico

import sys

admin_username = 'weblogic'
admin_password = 'Welcome1'
domain_name = 'mydomain'
domain_path = '/u01/oracle/user_projects/domains/' + domain_name

print('>>> Iniciando configuración de dominio WebLogic...')

readTemplate("/opt/oracle/middleware/wlserver/common/templates/wls/wls.jar")

cd('Servers/AdminServer')
set('ListenAddress', '')
set('ListenPort', 7001)

cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword(admin_password)

setOption('OverwriteDomain', 'true')
writeDomain(domain_path)
closeTemplate()

print('>>> Dominio creado en: ' + domain_path)
exit()