\# Runbook: Node in NotReady state



Symptoms: oc get nodes shows NotReady.



Steps:

1\. Check node details: oc describe node <node>

2\. Look at conditions: MemoryPressure, DiskPressure, PIDPressure.

3\. Check kubelet: oc adm node-logs <node> -u kubelet

4\. Debug the node: oc debug node/<node>, then chroot /host

5\. Check disk usage (df -h) and clean up if full.

6\. If needed, cordon and drain: oc adm cordon <node>, oc adm drain <node> --ignore-daemonsets --delete-emptydir-data

7\. Reboot the node and uncordon after it becomes Ready.

