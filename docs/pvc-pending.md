\# Runbook: PVC stuck in Pending



Symptoms: PersistentVolumeClaim shows Pending; pod cannot start.



Steps:

1\. Check PVC events: oc describe pvc <pvc> -n <namespace>

2\. Verify storage class exists: oc get storageclass

3\. Check if a default storage class is set.

4\. Confirm requested size and access mode (RWO, RWX) are supported.

5\. Check CSI driver pods are running.

6\. For WaitForFirstConsumer, the PVC binds only after a pod uses it.

