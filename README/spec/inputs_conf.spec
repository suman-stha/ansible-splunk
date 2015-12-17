############################################
#
# Possible values for inputs_conf role
# 
# Follows Splunk inputs.conf.spec closely
#
############################################

splunk_inputs_conf:
  splunktcp: 
    port: <port>

  splunktcp_ssl: 
    port: <port>

  SSL:
    rootCA: <filepath>
    * Certificate authority list
    * Autogenerated file under $SPLUNK_HOME/etc/auth/cacert.pem

    serverCert: <filepath>
    * Full path to the server certificate.
    * Autogenerated file under $SPLUNK_HOME/etc/auth/server.pem

    password: <string>
    * Encrypted password