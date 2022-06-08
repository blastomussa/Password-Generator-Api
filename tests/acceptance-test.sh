#!/bin/bash
set -x

CLUSTER_IP=$(kubectl get svc flask-service -o=jsonpath='{.spec.clusterIP}')
SVC_PORT=$(kubectl get svc flask-service -o=jsonpath='{.spec.ports[0].targetPort}')


status=`curl -o /dev/null -s -w "%{http_code}\n" ${CLUSTER_IP}:${SVC_PORT}`

if (test $status -ne 200);
echo "Error" 1>&2
fi
