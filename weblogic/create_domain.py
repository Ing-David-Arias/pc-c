readTemplate("/opt/oracle/middleware/wlserver/common/templates/wls/wls.jar")

cd("Servers/AdminServer")
set("Name", "AdminServer")
set("ListenAddress", "")
set("ListenPort", 7001)

cd("/")
cd("Security/base_domain/User/weblogic")
cmo.setPassword("Welcome1")

setOption("OverwriteDomain", "true")
writeDomain("/u01/oracle/user_projects/domains/base_domain")
closeTemplate()
exit()