\# Runbook: Pod in ImagePullBackOff



Symptoms: Pod stuck in ImagePullBackOff or ErrImagePull.



Steps:

1\. Check events: oc describe pod <pod> -n <namespace>

2\. Verify image name and tag are correct.

3\. Check pull secret: oc get secret -n <namespace>

4\. Link secret to service account: oc secrets link default <secret> --for=pull

5\. Check if the registry is reachable from the node (proxy, firewall).

6\. For private registries, confirm credentials are not expired.

