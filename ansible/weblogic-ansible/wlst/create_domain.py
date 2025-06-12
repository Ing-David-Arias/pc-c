# create_domain.py

print('>>> Iniciando la creación del dominio...')

readTemplate("/u01/oracle/wlserver/common/templates/wls/wls.jar")
cd('Servers/AdminServer')
set('ListenAddress', 'localhost')
set('ListenPort', 7001)

cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('Welcome1')

setOption('OverwriteDomain', 'true')
writeDomain('/u01/oracle/user_projects/domains/base_domain')
closeTemplate()

print('>>> Dominio creado exitosamente')