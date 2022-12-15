# Remove key from YAML

The only script in this repository at this time removes a specified key from a YAML file. A YAML file may consist of multiple YAML _documents_ that are separated by three dashes `---`. This script can handle such files as well as YAML files containing only a single document with no separators.

Consider the following YAML file:

```yaml
apiVersion: v1
kind: Namespace
status:
  one: 1
  two: 2
  three: 3
metadata:
  labels:
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/warn: privileged
  name: metallb-system

---

apiVersion: v1
kind: Namespace
status: complete
metadata:
  labels:
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/warn: privileged
  name: metallb-controller
```

If you want to remove the `status` key and all of its children from the this YAML, the output would look like this:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/warn: privileged
  name: metallb-system

---

apiVersion: v1
kind: Namespace
metadata:
  labels:
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/warn: privileged
  name: metallb-controller
```

To do this, simply execute the command

```bash
python yaml_remove_key.py KEY FILENAME
```

or 

```bash
python yaml_remove_key.py status sample.yaml
```

The script will send the output to the console, so you should redirect the output to a file.

```bash
python yaml_remove_key.py status sample.yaml > filtered.yaml
```
