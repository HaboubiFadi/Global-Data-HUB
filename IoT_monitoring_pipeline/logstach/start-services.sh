#!/bin/bash

servcie metricbeat test config
service filebeat test config
#filebeat setup -e
service metricbeat start
 

service filebeat start
chmod 777 /usr/share/logstash/pipeline/logstash.conf
logstash -f /usr/share/logstash/pipeline/*.conf
