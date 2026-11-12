\# Runbook: Route not working



Symptoms: Application URL gives 503 or does not open.



Steps:

1\. Check route: oc get route -n <namespace>

2\. Check service and endpoints: oc get svc,endpoints -n <namespace>

3\. If endpoints are empty, service selector does not match pod labels.

4\. Confirm pods are Running and Ready.

5\. Check target port in route matches service port.

6\. Check ingress controller pods: oc get pods -n openshift-ingress

7\. For TLS issues, verify certificate and termination type (edge, passthrough, reencrypt).

