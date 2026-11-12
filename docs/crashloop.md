\# Runbook: Pod in CrashLoopBackOff



Symptoms: Pod restarts again and again. Status shows CrashLoopBackOff.



Steps:

1\. Check pod events: oc describe pod <pod> -n <namespace>

2\. Check current logs: oc logs <pod> -n <namespace>

3\. Check previous container logs: oc logs <pod> --previous

4\. Common causes: wrong config or secret, missing env variable, OOMKilled (memory limit too low), failing liveness probe.

5\. If OOMKilled, increase memory limit in the deployment.

6\. If probe fails, check the probe path, port and initialDelaySeconds.

